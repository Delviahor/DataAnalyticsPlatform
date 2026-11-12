import pandas as pd

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows from the DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame from which duplicates will be removed.

    Returns:
    pd.DataFrame: A DataFrame with duplicate rows removed.
    """
    return df.drop_duplicates().copy()

def handle_missing_values(
    df: pd.DataFrame,
    column: str,
    value
) -> pd.DataFrame:
    """
    Fill missing values in a specified column.

    Parameters:
    df (pd.DataFrame): Input DataFrame.
    column (str): Column where missing values will be handled.
    value: Value used to replace missing entries.

    Returns:
    pd.DataFrame: DataFrame with missing values handled.
    """
    cleaned_df = df.copy()
    cleaned_df[column] = cleaned_df[column].fillna(value)

    return cleaned_df