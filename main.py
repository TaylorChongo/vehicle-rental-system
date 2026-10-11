"""Entry point for the vehicle rental system."""

import logging
from pathlib import Path

from rental_service import RentalService
from vehicles.bike import Bike
from vehicles.car import Car
from vehicles.truck import Truck


def create_default_service() -> RentalService:
    """Create the sample fleet used by the CLI."""
    return RentalService(
        (
            Car("CAR-001", 45.0),
            Truck("TRUCK-001", 75.0),
            Bike("BIKE-001", 20.0),
        ),
        storage_path=Path(__file__).parent / "data" / "fleet.json",
    )


def display_vehicles(service: RentalService) -> None:
    """Display all vehicles in the fleet."""
    vehicles = service.list_vehicles()
    if not vehicles:
        print("No vehicles are currently available.")
        return

    for vehicle in vehicles:
        availability = "Available" if vehicle.is_available else "Rented"
        print(
            f"{vehicle.vehicle_id} | {vehicle.vehicle_type} | "
            f"${vehicle.daily_rate:.2f}/day | {availability}"
        )


def run_cli(service: RentalService) -> None:
    """Run the interactive rental menu."""
    while True:
        print("\nVehicle Rental System")
        print("1. View vehicles")
        print("2. Rent a vehicle")
        print("3. Return a vehicle")
        print("4. Calculate rental cost")
        print("5. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            display_vehicles(service)
        elif choice == "2":
            vehicle_id = input("Enter vehicle ID: ").strip()
            try:
                vehicle = service.rent_vehicle(vehicle_id)
            except ValueError as error:
                print(f"Error: {error}")
            else:
                print(f"{vehicle.vehicle_id} has been rented successfully.")
        elif choice == "3":
            vehicle_id = input("Enter vehicle ID: ").strip()
            try:
                vehicle = service.return_vehicle(vehicle_id)
            except ValueError as error:
                print(f"Error: {error}")
            else:
                print(f"{vehicle.vehicle_id} has been returned successfully.")
        elif choice == "4":
            vehicle_id = input("Enter vehicle ID: ").strip()
            days_text = input("Enter rental days: ").strip()
            try:
                rental_days = int(days_text)
                cost = service.calculate_cost(vehicle_id, rental_days)
            except ValueError as error:
                print(f"Error: {error}")
            else:
                print(f"Rental cost: ${cost:.2f}")
        elif choice == "5":
            print("Goodbye!")
            return
        else:
            print("Invalid option. Please choose 1, 2, 3, 4, or 5.")


def main() -> None:
    """Run the vehicle rental system."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    run_cli(create_default_service())


if __name__ == "__main__":
    main()
