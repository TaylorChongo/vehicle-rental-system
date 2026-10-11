# Sprint 2 Retrospective

## What went well

- The Sprint 1 separation between CLI and service logic made new commands small
  and easy to test.
- Tests were added alongside each new business rule, including invalid input and
  log output.
- Logging makes successful operations and rejected operations visible without
  exposing customer data.

## What could be improved

- Fleet and rental state are now stored in `data/fleet.json`, but the JSON
  storage format will need migration if the domain model changes.
- The CLI converts rental-day input directly with `int`, so malformed input is
  handled as an error but could receive a more specific prompt.
- CI runs tests but does not yet publish coverage or package a release artifact.

## Lessons learned and next improvements

1. Introduce a dedicated input-validation layer for clearer CLI feedback.
2. Add coverage reporting and a release workflow once the prototype's behavior
   is stable.
3. Consider replacing the JSON file with a database if concurrent users need to
   manage the fleet.
