# Test Runs

A test run is a selection of scenarios and their tasks (with datasets). Each scenario selected when a new test run is created gets a `run_status` document.

## test_runs collection
Lists all test runs.

## Run execution id (RX)
Each execution of a run has an id in the form `<run number>X<execution index>`.

Example: `5X12` is execution 12 of run 5.

## To document
- Fields of `test_runs` (sample documents to come)
- How an `RX` links to `run_status` documents
