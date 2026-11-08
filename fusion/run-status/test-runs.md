# Test Runs

A test run is a selection of scenarios and their tasks (with datasets). Each scenario selected when a new test run is created gets a `run_status` document.

## test_runs collection
Lists all test runs.

## Run execution id (RX)
Each execution of a run has an id in the form `<run number>X<execution index>`.

Example: `5X12` is execution 12 of run 5.

In a task's `job.json` the id also carries the scenario id: `<run>X<execution>S<scenario_idx>`, e.g. `28X190S24142` ([job-json.md](job-json.md)).

## To document
- Fields of `test_runs` (sample documents to come)
- How an `RX` links to `run_status` documents
