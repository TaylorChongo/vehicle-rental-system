"""Business rules for managing the vehicle fleet."""

import logging
from collections.abc import Iterable

from vehicles.vehicle import Vehicle


logger = logging.getLogger(__name__)


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
        vehicle = self._get_vehicle_or_log(vehicle_id)
        if not vehicle.is_available:
            logger.warning("Rent rejected: vehicle '%s' is already rented.", vehicle_id)
            raise ValueError(f"Vehicle '{vehicle_id}' is already rented.")
        vehicle.is_available = False
        logger.info("Vehicle '%s' rented successfully.", vehicle_id)
        return vehicle

    def return_vehicle(self, vehicle_id: str) -> Vehicle:
        """Return a rented vehicle by identifier."""
        vehicle = self._get_vehicle_or_log(vehicle_id)
        if vehicle.is_available:
            logger.warning("Return rejected: vehicle '%s' is already available.", vehicle_id)
            raise ValueError(f"Vehicle '{vehicle_id}' is already available.")
        vehicle.is_available = True
        logger.info("Vehicle '%s' returned successfully.", vehicle_id)
        return vehicle

    def calculate_cost(self, vehicle_id: str, rental_days: int) -> float:
        """Calculate the rental cost for a positive number of whole days."""
        vehicle = self._get_vehicle_or_log(vehicle_id)
        if isinstance(rental_days, bool) or not isinstance(rental_days, int):
            logger.warning("Cost rejected: rental days must be a positive whole number.")
            raise ValueError("Rental days must be a positive whole number.")
        if rental_days <= 0:
            logger.warning("Cost rejected: rental days must be positive.")
            raise ValueError("Rental days must be a positive whole number.")
        return vehicle.daily_rate * rental_days

    def _get_vehicle_or_log(self, vehicle_id: str) -> Vehicle:
        try:
            return self._vehicles[vehicle_id]
        except KeyError as error:
            logger.warning("Vehicle lookup failed: '%s' was not found.", vehicle_id)
            raise ValueError(f"Vehicle '{vehicle_id}' was not found.") from error
