# Testing – DataAnalyticsPlatform

## 1. Purpose

This document describes the testing strategy used to verify the functionality, reliability, and integration of DataAnalyticsPlatform components.

The project uses Pytest as its automated testing framework and pytest-cov to measure code coverage.

## 2. Testing Environment

| Component         | Version         |
| ----------------- | --------------- |
| Operating System  | Windows (win64) |
| Python            | 3.14.10         |
| Pytest            | 9.2.0           |
| pytest-cov        | 7.1.0           |

Tests are executed within the `.venv` virtual environment.

## 3. Test Organization

Test files are located in the `tests/` directory.

```text
tests/
│
├── test_ingestion.py
├── test_inspection.py
├── test_cleaning.py
├── test_transformation.py
├── test_analytics.py
├── test_visualization.py
└── test_integration.py
```

Each file contains tests related to a specific module.

### 3.1 Unit Tests

Unit tests verify the individual behavior of functions.

The following aspects are validated:

**Data Ingestion**

- Successful loading of CSV files.

**Data Inspection**

- Dataset dimensions.
- Data types.
- Identification of missing values.
- Duplicate detection.
- Descriptive statistics.

**Data Cleaning**

- Removal of duplicate records.
- Replacement of missing values.
- Preservation of the original DataFrame.

**Data Transformation**

- Date column conversion.
- Creation of calculated columns.
- Available arithmetic operations.
- Handling of unsupported operations.
- Preservation of the original DataFrame.

**Analytics**

- Pearson, Spearman, and Kendall correlation.
- Aggregations.
- Frequencies.
- Sample and population variance.
- Skewness.
- Kurtosis.
- Interquartile range.

**Visualization**

- Histogram generation.
- Bar charts.
- Scatter plots.
- Line charts.
- Box plots.
- Column validation.
- Datetime type column validation.
- Handling of empty DataFrames.
- Validate numeric columns.

### 3.2 Integration Tests

The `test_integration.py` file verifies interactions between modules through a data processing workflow.

The validated sequence is:

1. CSV file loading.
2. Dataset inspection.
3. Record cleaning.
4. Column transformation.
5. Execution of analytical operations.
6. Visualization generation.

The tests verify that data produced by one component can be correctly used by the next.

## 4. Running the Tests

To run all tests:

```bash
python -m pytest -v
```

To run tests for a specific module:

```bash
python -m pytest tests/test_analytics.py -v
```

To run integration tests:

```bash
python -m pytest tests/test_integration.py -v
```

To measure code coverage:

```bash
python -m pytest --cov=app --cov-branch --cov-report=term-missing
```

## 5. Validation Results

The latest recorded execution of the unit and integration test suite produced the following results:

| Metric              | Result        |
| ------------------- | ------------- |
| Collected tests     | 78            |
| Passed tests        | 78            |
| Failed tests        | 0             |
| Execution time      | 2.17 seconds  |

**Status:** All collected tests passed.

### 5.1 Code Coverage

The previous coverage review reported:

- Overall coverage: 90%.
- 100% statement coverage across the functional data processing, analytics, and visualization modules.
- 100% branch coverage across those modules.
- `main.py`: 0% coverage.

`main.py` was not included as a primary coverage target because its current purpose is to serve as the application entry point and demonstrate the processing workflow.

The decision was to prioritize coverage of functional components and avoid artificially increasing the overall percentage through low-value tests.

**Note:** The 90% figure corresponds to a previously recorded coverage review. It does not necessarily represent a measurement obtained during the latest execution of 78 tests.

## 6. Quality Criteria

The following criteria are used to evaluate the components:

- Functions must produce the expected results.
- Invalid inputs must be handled through the appropriate validation mechanisms.
- Edge cases must be covered by unit tests.
- Operations expected to preserve original data must not modify it.
- Modules must function correctly within the integrated workflow.
- Automated tests must complete without errors.

## 7. Stage 3 Validation Status

| Activity                        | Status     |
| ------------------------------- | ---------- |
| Unit testing                    | Passed     |
| Edge case review                | Completed  |
| Coverage review                 | Completed  |
| Integration testing             | Passed     |
| Main workflow validation        | Passed     |

Stage 3 has achieved satisfactory technical validation based on the recorded results.

## 8. Test Maintenance

Each new feature must include unit tests to validate its behavior.

Whenever existing components are modified, the corresponding tests must be executed to detect potential regressions.

Integration tests must be updated whenever the processing workflow or interfaces between modules change.

Code coverage must be reviewed periodically, prioritizing the identification of unvalidated behavior over artificially increasing the coverage percentage.