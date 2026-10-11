"""Business rules for managing the vehicle fleet."""

import json
import logging
from collections.abc import Iterable
from pathlib import Path

from vehicles.bike import Bike
from vehicles.car import Car
from vehicles.truck import Truck
from vehicles.vehicle import Vehicle


logger = logging.getLogger(__name__)
VEHICLE_TYPES = {"Bike": Bike, "Car": Car, "Truck": Truck}


class RentalService:
    """Manage vehicles and their rental availability."""

    def __init__(
        self,
        vehicles: Iterable[Vehicle] = (),
        storage_path: str | Path | None = None,
    ) -> None:
        self._storage_path = Path(storage_path) if storage_path is not None else None
        self._vehicles: dict[str, Vehicle] = {}
        if self._storage_path is not None and self._storage_path.exists():
            self._load()
        else:
            for vehicle in vehicles:
                self._add_vehicle(vehicle)
            self._save()

    def add_vehicle(self, vehicle: Vehicle) -> None:
        """Add a vehicle to the fleet."""
        if vehicle.vehicle_id in self._vehicles:
            raise ValueError(f"Vehicle '{vehicle.vehicle_id}' already exists.")
        self._vehicles[vehicle.vehicle_id] = vehicle
        self._save()

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
        self._save()
        logger.info("Vehicle '%s' rented successfully.", vehicle_id)
        return vehicle

    def return_vehicle(self, vehicle_id: str) -> Vehicle:
        """Return a rented vehicle by identifier."""
        vehicle = self._get_vehicle_or_log(vehicle_id)
        if vehicle.is_available:
            logger.warning("Return rejected: vehicle '%s' is already available.", vehicle_id)
            raise ValueError(f"Vehicle '{vehicle_id}' is already available.")
        vehicle.is_available = True
        self._save()
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

    def _add_vehicle(self, vehicle: Vehicle) -> None:
        if vehicle.vehicle_id in self._vehicles:
            raise ValueError(f"Vehicle '{vehicle.vehicle_id}' already exists.")
        self._vehicles[vehicle.vehicle_id] = vehicle

    def _load(self) -> None:
        assert self._storage_path is not None
        try:
            records = json.loads(self._storage_path.read_text(encoding="utf-8"))
            if not isinstance(records, list):
                raise ValueError("Fleet data must be a JSON list.")
            for record in records:
                if not isinstance(record, dict):
                    raise ValueError("Each fleet record must be a JSON object.")
                vehicle_type = record["vehicle_type"]
                vehicle_class = VEHICLE_TYPES[vehicle_type]
                vehicle = vehicle_class(
                    vehicle_id=record["vehicle_id"],
                    daily_rate=record["daily_rate"],
                    is_available=record["is_available"],
                )
                self._add_vehicle(vehicle)
        except (KeyError, TypeError, ValueError, json.JSONDecodeError) as error:
            raise ValueError(
                f"Could not load fleet data from '{self._storage_path}'."
            ) from error

    def _save(self) -> None:
        if self._storage_path is None:
            return
        self._storage_path.parent.mkdir(parents=True, exist_ok=True)
        records = [
            {
                "vehicle_id": vehicle.vehicle_id,
                "vehicle_type": vehicle.vehicle_type,
                "daily_rate": vehicle.daily_rate,
                "is_available": vehicle.is_available,
            }
            for vehicle in self.list_vehicles()
        ]
        self._storage_path.write_text(
            json.dumps(records, indent=2) + "\n",
            encoding="utf-8",
        )
