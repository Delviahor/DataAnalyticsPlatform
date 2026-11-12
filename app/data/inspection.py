
import pandas as pd


def get_dataset_shape(df: pd.DataFrame) -> dict:
    """
    Return the number of rows and columns.
    """

    rows, columns = df.shape

    return {
        "rows": rows,
        "columns": columns
    }


def get_data_types(df: pd.DataFrame) -> pd.Series:
    """
    Return the data type of each column.
    """

    return df.dtypes


def get_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return the number and percentage of missing values per column.
    """

    missing_count = df.isnull().sum()

    missing_percentage = (missing_count / len(df)) * 100

    return pd.DataFrame({
        "missing_count": missing_count,
        "missing_percentage": missing_percentage
    })


def get_duplicates(df: pd.DataFrame) -> int:
    """
    Return the number of duplicated rows.
    """

    return int(df.duplicated().sum())


def get_descriptive_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return descriptive statistics for numerical and categorical columns.
    """

    return df.describe(include="all")
