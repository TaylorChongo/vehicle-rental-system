# Sprint 2 Review

## Sprint goal

Complete the rental lifecycle, show rental costs, and make important application
events observable through logs.

## Delivered backlog items

### US-03: Return a vehicle

Delivered. The CLI can return a rented vehicle. The service rejects returning a
vehicle that is already available and reports unknown identifiers clearly.

### US-04: Calculate rental cost

Delivered. The service calculates cost using the vehicle's daily rate and a
positive whole-number rental duration. Invalid durations are rejected.

### US-06: Logging

Delivered. Successful rentals and returns are logged at INFO level. Unknown
vehicles and invalid rental actions are logged at WARNING level.

## Demonstration

Run:

```powershell
poetry run python main.py
```

The demonstrated flow is:

1. Select `2` and rent `CAR-001`.
2. Select `4`, enter `CAR-001`, and enter `3` days.
3. Confirm the displayed cost is `$135.00`.
4. Select `3` and return `CAR-001`.
5. Select `1` to confirm that `CAR-001` is available again.
6. Select `5` to exit.

## Testing and DevOps evidence

- The test suite now contains 14 tests covering the full rental lifecycle,
  cost validation, and logging.
- `poetry run pytest -q` passes.
- The CI workflow continues to run the complete test suite on pushes and pull
  requests.

## Outcome

The Sprint 1 retrospective improvements were applied: the system now supports a
complete rent/return cycle, validates user-facing rental durations, and exposes
important operations through logs.
