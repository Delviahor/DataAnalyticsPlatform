# Architecture – DataAnalyticsPlatform

## 1. Overview

DataAnalyticsPlatform is a data analytics platform developed in Python. Its purpose is to provide tools for data ingestion, inspection, cleaning, transformation, statistical analysis, and visualization of datasets.

The project uses a modular architecture that separates data processing, analytics, and visualization responsibilities.

The system is currently in **Stage 3: Analytics Engine and Visualization**.

## 2. Project Architecture

The application is organized into independent modules within the `app.data` package.

```markdown
DataAnalyticsPlatform/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   └── data/
│       ├── __init__.py
│       ├── ingestion.py
│       ├── inspection.py
│       ├── cleaning.py
│       ├── transformation.py
│       ├── analytics.py
│       └── visualization.py
│
├── datasets/
│   └── sales.csv
│
├── tests/
│   ├── test_ingestion.py
│   ├── test_inspection.py
│   ├── test_cleaning.py
│   ├── test_transformation.py
│   ├── test_analytics.py
│   ├── test_visualization.py
│   └── test_integration.py
│
├── .gitignore
├── README.md
├── pyproject.toml
└── requirements.txt
```

## 3. Main Components

### 3.1 Data Ingestion – `ingestion.py`

Responsible for loading datasets from CSV files.

Main functionality:

- `load_csv(file_path)`: loads a CSV file and returns a Pandas DataFrame.

### 3.2 Data Inspection – `inspection.py`

Provides structural and descriptive information about datasets.

Functions:

- `get_dataset_shape(df)`: retrieves the number of rows and columns.
- `get_data_types(df)`: identifies data types.
- `get_missing_values(df)`: identifies missing values.
- `get_duplicates(df)`: counts duplicate records.
- `get_descriptive_statistics(df)`: generates descriptive statistics.

### 3.3 Data Cleaning – `cleaning.py`

Provides operations to improve data quality.

Functions:

- `remove_duplicates(df)`: removes duplicate records.
- `handle_missing_values(df, column, value)`: replaces missing values in a column.

Operations work on DataFrame copies to preserve the original dataset.

### 3.4 Data Transformation – `transformation.py`

Allows datasets to be modified and enriched.

Functions:

- `convert_date_column(df, column)`: converts a column to a date and time format.
- `create_calculated_column(df, new_column, column_a, column_b, operation)`: generates a new column using arithmetic operations.

Available operations:

- Multiplication.
- Addition.
- Subtraction.
- Division.

### 3.5 Analytics Engine – `analytics.py`

Implements statistical and analytical operations.

Functions:

- `calculate_correlation(df, column1, column2, method)`: calculates the correlation between two variables.
- `aggregate_data(df, group_by_column, target_column, operation)`: groups and aggregates data.
- `calculate_frequency(df, column)`: calculates the frequency of values.
- `calculate_variance(df, column, ddof)`: calculates variance.
- `calculate_skewness(df, column)`: calculates skewness.
- `calculate_kurtosis(df, column)`: calculates kurtosis.
- `calculate_iqr(df, column)`: calculates the interquartile range.

Available correlation methods:

- Pearson.
- Spearman.
- Kendall.

The functions include validation for non-existent columns, incompatible data types, and invalid parameters.

### 3.6 Visualization – `visualization.py`

Responsible for generating graphical representations using Plotly Express.

Functions:

- `create_histogram(df, column, title, nbins)`: generates histograms.
- `create_bar_chart(df, x_column, y_column, title)`: generates bar charts.
- `create_scatter_plot(df, x_column, y_column, title)`: generates scatter plots.
- `create_line_chart(df, x_column, y_column, title)`: generates line charts.
- `create_box_plot(df, y_column, x_column, title)`: generates box plots.

The functions validate datasets, columns, and the required data types.

## 4. Data Processing Workflow

The main processing workflow follows this sequence:

```yaml
CSV File
    |
    v
Data Ingestion
    |
    v
Data Inspection
    |
    v
Data Cleaning
    |
    v
Data Transformation
    |
    v
Statistical Analysis
    |
    v
Visualization
```

Each module has a specific responsibility and receives the data required to perform its operations.

Pandas DataFrames serve as the data exchange structure between components.

## 5. Technologies Used

| Technology  | Purpose                                       |
| ----------- | --------------------------------------------- |
| Python 3.14 | Primary programming language                  |
| Pandas      | Data manipulation and analysis                |
| NumPy       | Numerical operations                          |
| SciPy       | Support for statistical operations            |
| Plotly      | Data visualization                            |
| Pytest      | Automated testing                             |
| pytest-cov  | Test coverage measurement                     |
| Ruff        | Static analysis and code style enforcement    |
| Git         | Version control                               |
| GitHub      | Repository hosting                            |

## 6. Design Principles

The project follows these principles:

- **Modularity:** each module has clearly defined responsibilities.
- **Separation of concerns:** ingestion, cleaning, transformation, analysis, and visualization are implemented independently.
- **Reusability:** functions can be used across different components.
- **Validation:** operations validate their inputs to reduce errors.
- **Data preservation:** cleaning and transformation operations work on copies whenever appropriate.
- **Testability:** components can be tested individually and through integration tests.

## 7. Architectural Evolution

The following features are part of the future development roadmap and are not considered implemented in the current architecture:

- **Stage 4:** Web application using FastAPI and Streamlit, user management, dataset uploads, and analysis history.
- **Stage 5:** Integration of Machine Learning algorithms using Scikit-learn.
- **Stage 6:** Containerization, deployment, security, and monitoring.
- **Stage 7:** Advanced artificial intelligence features and AI-assisted data interpretation.

The architecture may evolve as these components are introduced while maintaining separation of concerns.