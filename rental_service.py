"""Business rules for managing the vehicle fleet."""

from collections.abc import Iterable

from vehicles.vehicle import Vehicle


class RentalService:
    """Manage vehicles and their rental availability."""

    def __init__(self, vehicles: Iterable[Vehicle] = ()) -> None:
        self._vehicles: dict[str, Vehicle] = {}
        for vehicle in vehicles:
            self.add_vehicle(vehicle)

    def add_vehicle(self, vehicle: Vehicle) -> None:
        """Add a vehicle to the fleet."""
        if vehicle.vehicle_id in self._vehicles:
            raise ValueError(f"Vehicle '{vehicle.vehicle_id}' already exists.")
        self._vehicles[vehicle.vehicle_id] = vehicle

    def list_vehicles(self) -> list[Vehicle]:
        """Return all vehicles ordered by their identifier."""
        return sorted(self._vehicles.values(), key=lambda vehicle: vehicle.vehicle_id)

    def rent_vehicle(self, vehicle_id: str) -> Vehicle:
        """Rent an available vehicle by identifier."""
        vehicle = self._get_vehicle(vehicle_id)
        if not vehicle.is_available:
            raise ValueError(f"Vehicle '{vehicle_id}' is already rented.")
        vehicle.is_available = False
        return vehicle

    def _get_vehicle(self, vehicle_id: str) -> Vehicle:
        try:
            return self._vehicles[vehicle_id]
        except KeyError as error:
            raise ValueError(f"Vehicle '{vehicle_id}' was not found.") from error
