import pandas as pd

def calculate_correlation(
    df: pd.DataFrame,
    column1: str,
    column2: str,
    method: str = "pearson") -> float:
    """
    Calculate the Pearson correlation coefficient between two columns in a DataFrame.

    Parameters:
    dataframe (pd.DataFrame): The input DataFrame containing the data.
    column1 (str): The name of the first column.
    column2 (str): The name of the second column.

    Returns:
    float: The Pearson correlation coefficient between the two columns.
    """
    return float(
        df[column1].corr(df[column2], method=method)
    )

def aggregate_data(
    df: pd.DataFrame,
    group_by_column: str,
    target_column: str,
    operation: str
) -> pd.DataFrame:
    """
    Aggregate data by a specified column and operation.
    """

    operations = {
        "sum": "sum",
        "mean": "mean",
        "median": "median",
        "min": "min",
        "max": "max",
        "count": "count"
    }

    if operation not in operations:
        raise ValueError(f"Unsupported operation: {operation}")

    result = (
        df.groupby(group_by_column)[target_column]
        .agg(operations[operation])
        .reset_index()
    )

    return result

def calculate_frequency(
    df: pd.DataFrame,
    column: str) -> pd.Series:
    """
    Calculate the frequency of unique values in a specified column of a DataFrame.

    Parameters:
    dataframe (pd.DataFrame): The input DataFrame containing the data.
    column (str): The name of the column for which to calculate frequencies.

    Returns:
    pd.Series: A Series containing the frequency of each unique value in the specified column.
    """
    return df[column].value_counts(dropna=False)