import pandas as pd

def convert_date_column(
    df: pd.DataFrame,
    column: str
) -> pd.DataFrame:
    """
    Convert a specified DataFrame column to datetime.

    Parameters:
    df (pd.DataFrame): Input DataFrame.
    column (str): Name of the column to convert.

    Returns:
    pd.DataFrame: DataFrame with the specified column converted to datetime.
    """
    transformed_df = df.copy()
    transformed_df[column] = pd.to_datetime(transformed_df[column])

    return transformed_df


def create_calculated_column(
    df: pd.DataFrame,
    new_column: str,
    column_a: str,
    column_b: str,
    operation: str = "multiply"
) -> pd.DataFrame:
    """
    Create a new column using an arithmetic operation
    between two existing columns.

    Parameters:
    df (pd.DataFrame): Input DataFrame.
    new_column (str): Name of the new column.
    column_a (str): First source column.
    column_b (str): Second source column.
    operation (str): Arithmetic operation to perform.

    Returns:
    pd.DataFrame: DataFrame with the calculated column.
    """
    transformed_df = df.copy()

    operations = {
        "multiply": lambda a, b: a * b,
        "add": lambda a, b: a + b,
        "subtract": lambda a, b: a - b,
        "divide": lambda a, b: a / b
    }

    if operation not in operations:
        raise ValueError(f"Unsupported operation: {operation}")

    transformed_df[new_column] = operations[operation](
        transformed_df[column_a],
        transformed_df[column_b]
    )

    return transformed_df

