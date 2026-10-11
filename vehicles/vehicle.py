"""Base vehicle model."""

from dataclasses import dataclass


@dataclass
class Vehicle:
    """Represent a vehicle available for rental."""

    vehicle_id: str
    daily_rate: float
    is_available: bool = True

    @property
    def vehicle_type(self) -> str:
        """Return the display name for this vehicle's type."""
        return self.__class__.__name__
