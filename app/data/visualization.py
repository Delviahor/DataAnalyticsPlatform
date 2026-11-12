import pandas as pd
import plotly.express as px

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

def _validate_dataframe(df:pd.DataFrame) -> None:
    """
    Validate that the dataframe is not empty.
    """
    if df.empty:
        raise ValueError("DataFrame cannot be empty")

def _validate_numeric_columns(df:pd.DataFrame, columns: list[str]) -> None:
    """
    Validate that the specified columns are numeric.
    """
    non_numeric_columns = []

    for column in columns:
        if not pd.api.types.is_numeric_dtype(df[column]):
            non_numeric_columns.append(column)

    if non_numeric_columns:
        raise ValueError(
            f"Columns must be numeric: {non_numeric_columns}"
        )

def _validate_datetime_columns(
    df: pd.DataFrame,
    columns: list[str]
) -> None:
    """
    Validate that the specified columns are datetime.
    """
    non_datetime_columns = []

    for column in columns:
        if not pd.api.types.is_datetime64_any_dtype(df[column]):
            non_datetime_columns.append(column)

    if non_datetime_columns:
        raise ValueError(
            f"Columns must be datetime: {non_datetime_columns}"
        )

def create_histogram(
    df: pd.DataFrame,
    column: str,
    title: str = "Data Distribution",
    nbins: int = 10
    ):

    if not isinstance(nbins, int) or isinstance(nbins, bool) or nbins <= 0:
        raise ValueError("nbins must be a positive integer")
    
    _validate_dataframe(df)
    _validate_columns(df, [column])
    _validate_numeric_columns(df, [column])
    
    """
    Create an histogram to visualize the distribution of a numerical column
    """

    fig = px.histogram(
        df,
        x=column,
        nbins=nbins,
        title=title
    )

    return fig

def create_bar_chart(
        df: pd.DataFrame,
        x_column: str,
        y_column: str,
        title: str = "Category comparison"
    ):
    """
    Create a bar chart to compare values between categories
    """
    _validate_dataframe(df)
    _validate_columns(df, [x_column, y_column])
    _validate_numeric_columns(df, [y_column])

    fig=px.bar(
        df,
        x=x_column,
        y=y_column,
        title=title
    )
    
    return fig

def create_scatter_plot(
    df: pd.DataFrame,
    x_column: str,
    y_column: str,
    title: str = "variable relationship"
    ):

    """
    create a scatter plot to visualize the relationship between two variables
    """
    _validate_dataframe(df)
    _validate_columns(df, [x_column, y_column])
    _validate_numeric_columns(df, [x_column, y_column])
    fig = px.scatter(
        df,
        x= x_column,
        y=y_column,
        title=title
    )

    return fig

def create_line_chart(
    df: pd.DataFrame,
    x_column: str,
    y_column: str,
    title: str = "Trend Over Time"
):
    """
    Create a line chart to visualize trends over time.
    """
    _validate_dataframe(df)
    _validate_columns(df, [x_column, y_column])
    _validate_numeric_columns(df, [y_column])

    if not pd.api.types.is_numeric_dtype(df[x_column]):
        _validate_datetime_columns(df, [x_column])

    fig = px.line(
        df,
        x=x_column,
        y=y_column,
        title=title
    )

    return fig

def create_box_plot(
    df: pd.DataFrame,
    y_column: str,
    x_column: str = None,
    title: str = "Data Distribution"
):
    """
    Create a box plot to visualize statistical distribution.
    """
    columns = [y_column] if x_column is None else [x_column, y_column]
    _validate_dataframe(df)
    _validate_columns(df, columns)
    _validate_numeric_columns(df, [y_column])
    
    fig = px.box(
        df,
        x=x_column,
        y=y_column,
        title=title
    )

    return fig

