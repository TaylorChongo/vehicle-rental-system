# Sprint 1 Retrospective

## What went well

- Separating `RentalService` from the CLI made the rental rules straightforward
  to test.
- Small domain objects for cars, trucks, and bikes allowed the first CLI flow to
  support multiple vehicle types without duplicating rental logic.
- Running tests through Poetry exposed an import-path issue early, which was
  fixed in project configuration instead of relying on a local shell setting.
- The first CI workflow is defined before Sprint 2, so future changes can be
  checked automatically.

## What could be improved

- The CLI currently uses a hard-coded sample fleet, so vehicle data is lost when
  the application exits.
- The first sprint did not include return functionality, which limits the
  usefulness of a complete rental cycle.
- User input validation is basic and should be made more explicit as more
  commands are added.

## Improvements for Sprint 2

1. Add a return-vehicle flow and tests for returning rented and available
   vehicles.
2. Add rental-cost calculation with validation for positive rental durations.
3. Add application logging for successful and invalid operations.
4. Keep business rules in `RentalService` and add tests before extending the
   CLI.
