"""Tests for the rental service."""

import pytest

from rental_service import RentalService
from vehicles.bike import Bike
from vehicles.car import Car


def make_service(storage_path: str | None = None) -> RentalService:
    return RentalService(
        (Car("CAR-001", 45.0), Bike("BIKE-001", 20.0)),
        storage_path=storage_path,
    )


def test_list_vehicles_returns_all_vehicles_in_identifier_order() -> None:
    service = make_service()

    vehicles = service.list_vehicles()

    assert [vehicle.vehicle_id for vehicle in vehicles] == ["BIKE-001", "CAR-001"]
    assert all(vehicle.is_available for vehicle in vehicles)


def test_rent_vehicle_marks_vehicle_as_unavailable() -> None:
    service = make_service()

    rented_vehicle = service.rent_vehicle("CAR-001")

    assert rented_vehicle.vehicle_id == "CAR-001"
    assert rented_vehicle.is_available is False


def test_renting_an_already_rented_vehicle_fails() -> None:
    service = make_service()
    service.rent_vehicle("CAR-001")

    with pytest.raises(ValueError, match="already rented"):
        service.rent_vehicle("CAR-001")


def test_renting_an_unknown_vehicle_fails() -> None:
    service = make_service()

    with pytest.raises(ValueError, match="was not found"):
        service.rent_vehicle("UNKNOWN")


def test_duplicate_vehicle_ids_are_rejected() -> None:
    service = make_service()

    with pytest.raises(ValueError, match="already exists"):
        service.add_vehicle(Car("CAR-001", 50.0))


def test_return_vehicle_marks_vehicle_as_available() -> None:
    service = make_service()
    service.rent_vehicle("CAR-001")

    returned_vehicle = service.return_vehicle("CAR-001")

    assert returned_vehicle.vehicle_id == "CAR-001"
    assert returned_vehicle.is_available is True


def test_returning_an_available_vehicle_fails() -> None:
    service = make_service()

    with pytest.raises(ValueError, match="already available"):
        service.return_vehicle("CAR-001")


def test_calculate_cost_uses_daily_rate_and_rental_days() -> None:
    service = make_service()

    cost = service.calculate_cost("CAR-001", 3)

    assert cost == 135.0


@pytest.mark.parametrize("rental_days", [0, -1, True, 1.5])
def test_calculate_cost_requires_positive_whole_days(rental_days: object) -> None:
    service = make_service()

    with pytest.raises(ValueError, match="positive whole number"):
        service.calculate_cost("CAR-001", rental_days)  # type: ignore[arg-type]


def test_successful_actions_are_logged(caplog: pytest.LogCaptureFixture) -> None:
    service = make_service()

    with caplog.at_level("INFO"):
        service.rent_vehicle("CAR-001")
        service.return_vehicle("CAR-001")

    assert "Vehicle 'CAR-001' rented successfully." in caplog.text
    assert "Vehicle 'CAR-001' returned successfully." in caplog.text


def test_invalid_action_is_logged(caplog: pytest.LogCaptureFixture) -> None:
    service = make_service()

    with caplog.at_level("WARNING"), pytest.raises(ValueError):
        service.rent_vehicle("UNKNOWN")

    assert "Vehicle lookup failed: 'UNKNOWN' was not found." in caplog.text


def test_fleet_state_is_loaded_after_service_restart(tmp_path) -> None:
    storage_path = str(tmp_path / "fleet.json")
    first_service = make_service(storage_path)

    first_service.rent_vehicle("CAR-001")
    restarted_service = RentalService(storage_path=storage_path)

    assert restarted_service.list_vehicles()[1].is_available is False


def test_returned_state_is_saved_for_next_restart(tmp_path) -> None:
    storage_path = str(tmp_path / "fleet.json")
    service = make_service(storage_path)
    service.rent_vehicle("CAR-001")
    service.return_vehicle("CAR-001")

    restarted_service = RentalService(storage_path=storage_path)

    assert restarted_service.list_vehicles()[1].is_available is True
