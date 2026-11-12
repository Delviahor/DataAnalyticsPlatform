import pandas as pd

from app.data.inspection import (
    get_dataset_shape,
    get_data_types,
    get_missing_values,
    get_duplicates,
    get_descriptive_statistics
)

def create_test_dataframe():
    return pd.DataFrame({
        "product": ["Laptop", "Mouse", "Keyboard", "Laptop"],
        "quantity": [2, 5, 3, 2],
        "unit_price": [850.0, 15.5, 45.0, 850.0],
        "region": ["North", "South", None, "North"]
    })

def test_get_dataset_shape():
    df = create_test_dataframe()

    result = get_dataset_shape(df)

    assert result == {
        "rows": 4,
        "columns": 4
    }

def test_get_data_types():
    df = create_test_dataframe()

    result = get_data_types(df)

    assert pd.api.types.is_string_dtype(result["product"])
    assert result["quantity"] == "int64"
    assert result["unit_price"] == "float64"


def test_get_missing_values():
    df = create_test_dataframe()

    result = get_missing_values(df)

    assert result.loc["region", "missing_count"] == 1
    assert result.loc["region", "missing_percentage"] == 25.0


def test_get_duplicates():
    df = create_test_dataframe()

    result = get_duplicates(df)

    assert result == 1


def test_get_descriptive_statistics():
    df = create_test_dataframe()

    result = get_descriptive_statistics(df)

    assert isinstance(result, pd.DataFrame)
    assert "quantity" in result.columns
    assert result.loc["mean", "quantity"] == 3.0
    assert result.loc["max", "quantity"] == 5
