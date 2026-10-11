"""Tests for the rental service."""

import pytest

from rental_service import RentalService
from vehicles.bike import Bike
from vehicles.car import Car


def make_service() -> RentalService:
    return RentalService((Car("CAR-001", 45.0), Bike("BIKE-001", 20.0)))


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
