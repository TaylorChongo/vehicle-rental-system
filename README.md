# Vehicle Rental System

A command-line vehicle rental system built with Python and Poetry.

## Run the application

```powershell
poetry install
poetry run python main.py
```

The application stores the fleet and rental availability in
`data/fleet.json`. The file is created automatically on the first run, and
changes made by renting or returning a vehicle are saved before the program
continues.

For example, rent `CAR-001`, exit the application, and run it again. The car
will still be shown as rented.

## Run the tests

```powershell
poetry run pytest
```
