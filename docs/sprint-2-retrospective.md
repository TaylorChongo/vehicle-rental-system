# Sprint 2 Retrospective

## What went well

- The Sprint 1 separation between CLI and service logic made new commands small
  and easy to test.
- Tests were added alongside each new business rule, including invalid input and
  log output.
- Logging makes successful operations and rejected operations visible without
  exposing customer data.

## What could be improved

- The fleet is still stored only in memory, so changes are lost when the CLI
  exits.
- The CLI converts rental-day input directly with `int`, so malformed input is
  handled as an error but could receive a more specific prompt.
- CI runs tests but does not yet publish coverage or package a release artifact.

## Lessons learned and next improvements

1. Persist fleet and rental state in a file or database.
2. Introduce a dedicated input-validation layer for clearer CLI feedback.
3. Add coverage reporting and a release workflow once the prototype's behavior
   is stable.
