import pandas as pd


def _validate_columns(
    df: pd.DataFrame,
    columns: list[str]
    ) -> None:
        """
        Validate that the DataFrame contains the required columns.
        """
        missing_columns = [
            column for column in columns
            if column not in df.columns
        ]
    
        if missing_columns:
            raise ValueError(
                f"Columns not found in DataFrame: {missing_columns}"
            )

def _validate_numeric_columns(
        df:pd.DataFrame,
        columns: list[str]) -> None:
    """
    Validate that the specified columns are numeric and not boolean.
    """
    non_numeric_columns = []

    for column in columns:
        if (
            not pd.api.types.is_numeric_dtype(df[column])
            or pd.api.types.is_bool_dtype(df[column])
        ):
            non_numeric_columns.append(column)
    if non_numeric_columns:
        raise ValueError(
            f"Columns must be numeric: {non_numeric_columns}"
        )
    
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
    _validate_columns(df, [column1, column2])
    _validate_numeric_columns(df, [column1, column2])
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

def calculate_variance(
    df: pd.DataFrame,
    column: str,
    ddof: int = 1) ->float:

    _validate_columns(df, columns=[column])
    _validate_numeric_columns(df, columns=[column])

    if (
    not isinstance(ddof, int)
    or isinstance(ddof, bool)
    or ddof < 0
):
        raise ValueError("ddof must be a non-negative integer")
    
    return float(df[column].var(ddof=ddof))

def calculate_skewness(
    df: pd.DataFrame,
    column: str
) -> float:
    """
    Calculate the skewness of a numerical column.
    """
    _validate_columns(df, [column])
    _validate_numeric_columns(df, [column])

    return float(df[column].skew())

def calculate_kurtosis(
    df: pd.DataFrame,
    column: str
) -> float:
    """
    Calculate the Fisher kurtosis of a numerical column.
    """
    _validate_columns(df, [column])
    _validate_numeric_columns(df, [column])

    return float(df[column].kurt())

def calculate_iqr(
    df: pd.DataFrame,
    column: str
) -> float:
    """
    Calculate the interquartile range of a numerical column.
    """
    _validate_columns(df, [column])
    _validate_numeric_columns(df, [column])

    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)

    return float(q3 - q1)