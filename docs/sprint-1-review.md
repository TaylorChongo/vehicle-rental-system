# Sprint 1 Review

## Sprint goal

Deliver the first usable CLI flow for viewing vehicles and renting an available
vehicle.

## Delivered backlog items

### US-01: View vehicles

Delivered. The CLI displays each vehicle's identifier, type, daily rate, and
availability. The default fleet includes a car, truck, and bike.

### US-02: Rent a vehicle

Delivered. A user can rent an available vehicle by identifier. The system marks
the vehicle as rented and rejects unknown or already-rented identifiers with
clear error messages.

## Demonstration

Run:

```powershell
poetry run python main.py
```

The demonstrated flow is:

1. Select `1` to view the default fleet.
2. Select `2` and enter `CAR-001`.
3. Select `1` again to confirm that `CAR-001` is marked `Rented`.
4. Select `3` to exit.

## Testing and DevOps evidence

- Five unit tests cover listing, successful rentals, duplicate IDs, unknown IDs,
  and attempts to rent an already-rented vehicle.
- `poetry run pytest -q` passes with `5 passed`.
- The CI workflow at `.github/workflows/ci.yml` runs the test suite on pushes and
  pull requests.

## Outcome

The sprint goal was met. The project has a working first increment with the
business rules separated from the CLI, making the next sprint easier to extend.
