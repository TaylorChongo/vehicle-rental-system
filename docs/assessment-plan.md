# Vehicle Rental System Assessment Plan

## Product vision

Provide a simple command-line vehicle rental system that allows a customer or rental
clerk to view vehicles, rent an available vehicle, and return it while preventing
invalid rental actions.

The prototype will demonstrate incremental Agile delivery and DevOps practices through
automated tests, continuous integration, logging, and clear sprint documentation.

## Product backlog

| ID | User story | Priority | Estimate |
|---|---|---:|---:|
| US-01 | As a rental clerk, I want to see all vehicles and their availability so that I can help customers choose a vehicle. | Must | 3 |
| US-02 | As a customer, I want to rent an available vehicle so that I can use it. | Must | 5 |
| US-03 | As a customer, I want to return a rented vehicle so that it becomes available again. | Must | 3 |
| US-04 | As a customer, I want to know the rental cost so that I understand what I will pay. | Should | 5 |
| US-05 | As a rental clerk, I want to add different vehicle types so that the fleet can grow. | Should | 3 |
| US-06 | As an operator, I want important actions and errors logged so that I can monitor the application. | Should | 2 |

Estimates use Fibonacci story points: 1, 2, 3, 5, 8.

## Acceptance criteria

### US-01: View vehicles

- The CLI displays each vehicle's identifier, type, and availability.
- The list includes cars, trucks, and bikes.
- An empty fleet is handled without an unhandled exception.

### US-02: Rent a vehicle

- A customer can rent an available vehicle using its identifier.
- A rented vehicle cannot be rented again.
- An unknown identifier produces a clear error message.

### US-03: Return a vehicle

- A customer can return a rented vehicle using its identifier.
- A vehicle that is already available cannot be returned as a new rental.
- An unknown identifier produces a clear error message.

### US-04: Calculate rental cost

- The system calculates cost from the vehicle's daily rate and rental duration.
- A rental duration must be a positive whole number.
- The CLI displays the calculated cost clearly.

### US-05: Add vehicles

- The system accepts a vehicle identifier, type, and daily rate.
- Vehicle identifiers must be unique.
- Unsupported vehicle types and invalid rates produce clear errors.

### US-06: Logging

- Successful rentals and returns are logged.
- Invalid operations are logged at an appropriate level.
- Logs do not expose unnecessary customer data.

## Definition of Done

A backlog item is done when:

- Its acceptance criteria are implemented.
- Relevant unit or integration tests pass.
- The code follows the project's Python style and type-safety expectations.
- The feature works through the CLI where applicable.
- CI runs the tests successfully.
- The change is committed with a descriptive Git message.
- The sprint review documents the delivered behavior.

## Sprint 1 plan

### Sprint goal

Deliver the first usable CLI flow for viewing vehicles and renting an available vehicle.

### Selected stories

- US-01: View vehicles — 3 points
- US-02: Rent a vehicle — 5 points

### Sprint 1 work sequence

1. Implement the base vehicle model and vehicle types.
2. Implement the rental service for listing and renting vehicles.
3. Add CLI commands for viewing and renting.
4. Add unit tests for availability and rental rules.
5. Add the initial CI workflow.
6. Demonstrate the working flow and record the sprint review.
7. Record the retrospective and identify improvements for Sprint 2.

## Sprint 2 plan

Sprint 2 will be finalized after the Sprint 1 retrospective. The initial candidates are:

- US-03: Return a vehicle — 3 points
- US-04: Calculate rental cost — 5 points
- US-06: Add logging — 2 points

