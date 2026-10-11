# Vehicle Rental System

A command-line vehicle rental system built with Python and Poetry. The project
was developed as a two-sprint Agile and DevOps assessment prototype.

## Product vision

Provide a simple rental application that allows a customer or rental clerk to
view vehicles, rent an available vehicle, return a rented vehicle, and
calculate rental costs while preventing invalid rental actions.

## Features

- View cars, trucks, and bikes in the fleet.
- Display each vehicle's type, identifier, daily rate, and availability.
- Rent an available vehicle.
- Return a rented vehicle.
- Calculate rental cost from a vehicle's daily rate and rental duration.
- Reject duplicate, unknown, already-rented, and already-available vehicles.
- Validate rental duration as a positive whole number.
- Log successful and invalid operations.
- Persist fleet and availability state in a JSON file.

## Requirements

- Python 3.10 or newer
- Poetry 2.x

## Installation

Clone the repository, move into the project directory, and install the
dependencies:

```powershell
git clone https://github.com/TaylorChongo/vehicle-rental-system.git
cd vehicle-rental-system
poetry install
```

Poetry uses the project-local `.venv` environment configured in
`poetry.toml`.

## Run the application

```powershell
poetry run python main.py
```

The CLI provides the following menu:

```text
1. View vehicles
2. Rent a vehicle
3. Return a vehicle
4. Calculate rental cost
5. Exit
```

The default fleet contains:

| ID | Type | Daily rate |
|---|---|---:|
| `CAR-001` | Car | `$45.00` |
| `TRUCK-001` | Truck | `$75.00` |
| `BIKE-001` | Bike | `$20.00` |

## Persistent state

The application stores fleet data in `data/fleet.json`. The file is created
automatically on the first run. Rental and return operations save the updated
availability immediately, so state is restored when the application starts
again.

The runtime JSON file is intentionally ignored by Git because it contains
machine-specific application state. The `data/.gitkeep` file keeps the data
directory in the repository. A fresh checkout receives the default fleet when
the application is first started.

## Project structure

```text
vehicle-rental-system/
├── .github/
│   └── workflows/
│       └── ci.yml
├── data/
│   └── .gitkeep
├── docs/
│   ├── assessment-plan.md
│   ├── sprint-1-review.md
│   ├── sprint-1-retrospective.md
│   ├── sprint-2-review.md
│   └── sprint-2-retrospective.md
├── tests/
│   └── test_rental_service.py
├── vehicles/
│   ├── __init__.py
│   ├── bike.py
│   ├── car.py
│   ├── truck.py
│   └── vehicle.py
├── main.py
├── rental_service.py
├── poetry.lock
├── poetry.toml
├── pyproject.toml
└── README.md
```

### Main components

- `vehicles/` contains the base `Vehicle` class and the `Car`, `Truck`, and
  `Bike` specializations.
- `rental_service.py` contains fleet management, rental rules, cost
  calculation, persistence, and logging.
- `main.py` contains the CLI and the default fleet configuration.
- `tests/` contains automated tests for business rules and persistence.
- `.github/workflows/ci.yml` defines the GitHub Actions pipeline.

## Testing

Run the complete test suite with:

```powershell
poetry run pytest -q
```

The suite covers:

- Fleet listing and ordering
- Successful and invalid rentals
- Successful and invalid returns
- Rental-cost calculation and input validation
- Duplicate and unknown vehicle IDs
- Successful and invalid-operation logging
- State restoration after restarting the rental service

## Continuous integration

The GitHub Actions workflow runs on every push and pull request. It:

1. Checks out the repository.
2. Sets up Python 3.14.
3. Installs Poetry.
4. Installs project dependencies.
5. Runs the test suite.

Workflow file: `.github/workflows/ci.yml`

Successful workflow run:
[Vehicle Rental System CI](https://github.com/TaylorChongo/vehicle-rental-system/actions)

## Agile assessment evidence

The `docs/` directory contains:

- Product vision, backlog, estimates, acceptance criteria, and Definition of
  Done in `assessment-plan.md`
- Sprint 1 review and retrospective
- Sprint 2 review and retrospective

The Git history demonstrates incremental delivery across setup, Sprint 1,
continuous integration, Sprint 2, and persistence:

```powershell
git log --oneline
```

## Useful commands

```powershell
# Install dependencies
poetry install

# Run the CLI
poetry run python main.py

# Run tests
poetry run pytest -q

# Validate Poetry configuration
poetry check

# See the Poetry environment path
poetry env info --path
```
