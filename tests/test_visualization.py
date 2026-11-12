import pandas as pd
import plotly.graph_objects as go
import pytest

from app.data.ingestion import load_csv
from app.data.transformation import convert_date_column
from app.data.visualization import(
    create_histogram,
    create_bar_chart,
    create_scatter_plot,
    create_line_chart,
    create_box_plot
)


def create_test_dataframe():
    return load_csv("datasets/sales.csv")

def test_create_histogram():
    df = create_test_dataframe()

    result = create_histogram(df, "unit_price")
    
        
    assert isinstance(result, go.Figure)
    assert result.data[0].type == "histogram"

    assert list(result.data[0].x)==df["unit_price"].tolist()
    
def test_create_bar_chart():
    df = create_test_dataframe()

    result = create_bar_chart(df, "product", "quantity")

    assert isinstance(result, go.Figure)
    assert result.data[0].type == "bar"  

    assert list(result.data[0].x) == df["product"].tolist()
    assert list(result.data[0].y) == df["quantity"].tolist()

def test_create_scatter_plot():
    df = create_test_dataframe()

    result = create_scatter_plot(df, "quantity", "unit_price")

    assert isinstance(result, go.Figure)
    assert result.data[0].type == "scatter"

    assert list(result.data[0].x) == df["quantity"].tolist()
    assert list(result.data[0].y) == df["unit_price"].tolist()

def test_create_line_chart():
    df = create_test_dataframe()

    df = convert_date_column(df, "date")

    result = create_line_chart(
        df,
        "date",
        "quantity"
    )

    assert isinstance(result, go.Figure)
    assert result.data[0].type == "scatter"
    assert result.data[0].mode == "lines"

def test_create_box_plot():
    df = create_test_dataframe()

    result = create_box_plot(
        df,
        y_column="unit_price"
    )

    assert isinstance(result, go.Figure)
    assert result.data[0].type == "box"

def test_create_histogram_invalid_column():
    df = create_test_dataframe()

    with pytest.raises(
        ValueError,
        match="Columns not found in DataFrame"
    ):
        create_histogram(df, "profit")

def test_create_bar_chart_invalid_column():
    df = create_test_dataframe()

    with pytest.raises(
        ValueError,
        match="Columns not found in DataFrame"
    ):
        create_bar_chart(df, "product", "profit")

def test_create_scatter_plot_invalid_column():
    df = create_test_dataframe()

    with pytest.raises(
        ValueError,
        match="Columns not found in DataFrame"
    ):
        create_scatter_plot(df, "profit", "unit_price")

def test_create_line_chart_invalid_column():
    df = create_test_dataframe()

    with pytest.raises(
        ValueError,
        match="Columns not found in DataFrame"
    ):
        create_line_chart(df, "date", "profit")

def test_create_box_plot_invalid_column():
    df = create_test_dataframe()

    with pytest.raises(
        ValueError,
        match="Columns not found in DataFrame"
    ):
        create_box_plot(df, y_column="profit")

def test_create_histogram_empty_dataframe():
    df = pd.DataFrame(columns=["unit_price"])

    with pytest.raises(
        ValueError,
        match="DataFrame cannot be empty"
    ):
        create_histogram(df, "unit_price")

def test_create_bar_chart_empty_dataframe():
    df = pd.DataFrame(columns=["product", "quantity"])

    with pytest.raises(
            ValueError,
            match="DataFrame cannot be empty"
        ):
        create_bar_chart(df, "product", "quantity")

def test_create_scatter_plot_empty_dataframe():
    df = pd.DataFrame(columns=["quantity", "unit_price"])
    
    with pytest.raises(
            ValueError,
            match="DataFrame cannot be empty"
        ):
        create_scatter_plot(df, "quantity", "unit_price")

def test_create_line_chart_empty_dataframe():
    df = pd.DataFrame(columns=["date", "quantity"])

    with pytest.raises(
            ValueError,
            match="DataFrame cannot be empty"
        ):
        create_line_chart(df, "date", "quantity")

def test_create_box_plot_empty_dataframe():
    df = pd.DataFrame(columns=["unit_price"])

    with pytest.raises(
            ValueError,
            match="DataFrame cannot be empty"
        ):
        create_box_plot(df, y_column="unit_price")

def test_create_histogram_non_numeric_column():
    df = create_test_dataframe()

    with pytest.raises(
        ValueError,
        match="Columns must be numeric"
    ):
        create_histogram(df, "product")

def test_create_bar_chart_non_numeric_y_column():
    df = create_test_dataframe()

    with pytest.raises(
        ValueError,
        match="Columns must be numeric"
    ):
        create_bar_chart(df, "product", "region")

def test_create_scatter_plot_non_numeric_x_column():
    df = create_test_dataframe()

    with pytest.raises(
        ValueError,
        match="Columns must be numeric"
    ):
        create_scatter_plot(df, "product", "quantity")

def test_create_scatter_plot_non_numeric_y_column():
    df = create_test_dataframe()

    with pytest.raises(
        ValueError,
        match="Columns must be numeric"
    ):
        create_scatter_plot(df, "quantity", "product")

def test_create_box_plot_non_numeric_y_column():
    df = create_test_dataframe()

    with pytest.raises(
        ValueError,
        match="Columns must be numeric"
    ):
        create_box_plot(df, "product")

def test_create_line_chart_non_numeric_x_column():
    df = create_test_dataframe()

    with pytest.raises(
        ValueError,
        match="Columns must be datetime"
    ):
        create_line_chart(df, "product", "quantity")

def test_create_bar_chart_categorical_x_column():
    df = create_test_dataframe()

    result = create_bar_chart(
        df,
        "product",
        "quantity"
    )

    assert isinstance(result, go.Figure)

def test_create_line_chart_numeric_x_column():
    df = create_test_dataframe()

    result = create_line_chart(
        df,
        "quantity",
        "unit_price"
    )

    assert isinstance(result, go.Figure)

def test_create_histogram_invalid_nbins():
    df = create_test_dataframe()

    with pytest.raises(
        ValueError,
        match="nbins must be a positive integer"
    ):
        create_histogram(df, "quantity", nbins=0)