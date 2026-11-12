import pandas as pd
import pytest

from app.data.analytics import (
    calculate_correlation,
    aggregate_data,
    calculate_frequency
)

def create_test_dataframe():
    return pd.DataFrame({
        "product": ["Laptop", "Mouse", "Keyboard", "Laptop"],
        "quantity": [2, 5, 3, 2],
        "unit_price": [850.0, 15.5, 45.0, 850.0],
        "region": ["North", "South", None, "North"]
    })

def test_calculate_correlation():
    
    df = create_test_dataframe()

    result = calculate_correlation(df, "quantity", "unit_price")
    assert isinstance(result, float)
    assert result == pytest.approx(-0.8309, abs = 0.01)  # Adjust the expected value based on actual correlation

def test_aggregate_data():
    df = create_test_dataframe()

    result = aggregate_data(df, "product", "quantity", "sum")

    assert isinstance(result, pd.DataFrame)
    assert "product" in result.columns
    assert "quantity" in result.columns

    laptop_quantity = result.loc[
        result["product"] == "Laptop", "quantity"
    ].iloc[0]

    assert laptop_quantity == 4

def test_aggregate_data_invalid_operation():
    df = create_test_dataframe()

    with pytest.raises(
        ValueError,
        match="Unsupported operation: lambda"
    ):
        aggregate_data(df, "product", "quantity", "lambda")

def test_calculate_frequency():
    df = create_test_dataframe()

    result = calculate_frequency(df, "product")
    
    assert isinstance(result, pd.Series)
    assert result["Laptop"] == 2
    assert result["Mouse"] == 1
    assert result["Keyboard"] == 1

def test_calculate_frequency_includes_missing():
    df = create_test_dataframe()
    
    result = calculate_frequency(df, "region")
    
    assert isinstance(result, pd.Series)
    assert result["North"] == 2
    assert result["South"] == 1
    assert result[result.index.isna()].iloc[0] == 1