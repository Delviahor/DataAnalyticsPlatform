import pandas as pd
import pytest

from scipy.stats import (
    skew as scipy_skew,
    kurtosis as scipy_kurtosis
)

from app.data.analytics import (
    calculate_correlation,
    aggregate_data,
    calculate_frequency,
    calculate_variance,
    calculate_skewness,
    calculate_kurtosis,
    calculate_iqr
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

def test_calculate_variance_missing_columns():
    df = create_test_dataframe()

    with pytest.raises(
        ValueError,
        match="Columns not found in DataFrame"
    ):
        calculate_variance(df, "nonexistent_column")

def test_calculate_variance_boolean_column():
    df = pd.DataFrame({
        "active": [True, False, True]
    })

    with pytest.raises(
        ValueError,
        match="Columns must be numeric"
    ):
        calculate_variance(df, "active")

@pytest.mark.parametrize(
    "ddof",
    [-1, 1.5, "1", True]
)

def test_calculate_variance_invalid_ddof(ddof):
    df = create_test_dataframe()

    with pytest.raises(
        ValueError,
        match="ddof must be a non-negative integer"
    ):
        calculate_variance(df, "quantity", ddof=ddof)

def test_calculate_variance_null_values():
    df = pd.DataFrame({
        "quantity": [10, 20, None, 30, 40]
    })

    result = calculate_variance(df, "quantity")

    expected = pd.Series([10, 20, 30, 40]).var(ddof=1)

    assert result == pytest.approx(expected)

def test_calculate_variance_constant_values():
    df = pd.DataFrame({
        "quantity": [5, 5, 5, 5]
    })

    result = calculate_variance(df, "quantity")

    assert result == 0.0

def test_calculate_variance_sample():
    df = pd.DataFrame({
        "quantity": [2, 4, 6, 8]
    })

    result = calculate_variance(df, "quantity")

    assert result == pytest.approx(6.6666666667)

def test_calculate_variance_population():
    df = pd.DataFrame({
        "quantity": [2, 4, 6, 8]
    })

    result = calculate_variance(
        df,
        "quantity",
        ddof=0
    )

    assert result == pytest.approx(5.0)

def test_calculate_variance_insufficient_observations():
    df = pd.DataFrame({
    "quantity": [10, None]
})
    result = calculate_variance(
        df,
        "quantity"
    )
    assert pd.isna(result)

def test_calculate_correlation_missing_columns():
    df = create_test_dataframe()

    with pytest.raises(
        ValueError,
        match="Columns not found in DataFrame"
    ):
        calculate_correlation(
            df,
            "quantity",
            "nonexistent"
        )

def test_calculate_correlation_non_numeric_columns():
    df = create_test_dataframe()

    with pytest.raises(
        ValueError,
        match="Columns must be numeric"
    ):
        calculate_correlation(
            df,
            "quantity",
            "region"
        )

def test_calculate_correlation_constant_column():
    df = pd.DataFrame({
        "quantity": [5, 5, 5, 5],
        "price": [10, 20, 30, 40]
    })

    result = calculate_correlation(
        df,
        "quantity",
        "price"
    )

    assert pd.isna(result)

def test_calculate_correlation_null_values():
    df = pd.DataFrame({
        "quantity": [2, 4, None, 8, 10],
        "price": [10, 20, 30, 40, 50]
    })

    result = calculate_correlation(
        df,
        "quantity",
        "price"
    )

    expected = pd.Series(
        [2, 4, 8, 10]
    ).corr(
        pd.Series([10, 20, 40, 50])
    )

    assert result == pytest.approx(expected)

@pytest.mark.parametrize(
    "method",
    ["pearson", "spearman", "kendall"]
)
def test_calculate_correlation_methods(method):
    df = pd.DataFrame({
        "quantity": [1, 2, 3, 4],
        "price": [10, 20, 30, 40]
    })

    result = calculate_correlation(
        df,
        "quantity",
        "price",
        method=method
    )

    assert result == pytest.approx(1.0)

def test_calculate_skewness():
    df = pd.DataFrame({
        "values": [1, 2, 2, 3, 9]
    })

    result = calculate_skewness(df, "values")

    expected = scipy_skew(
        df["values"],
        bias=False
    )

    assert result == pytest.approx(expected)


def test_calculate_skewness_missing_column():
    df = pd.DataFrame({
        "values": [1, 2, 3, 4]
    })

    with pytest.raises(
        ValueError,
        match="Columns not found in DataFrame"
    ):
        calculate_skewness(df, "nonexistent")


def test_calculate_skewness_non_numeric_column():
    df = pd.DataFrame({
        "category": ["A", "B", "C"]
    })

    with pytest.raises(
        ValueError,
        match="Columns must be numeric"
    ):
        calculate_skewness(df, "category")


def test_calculate_skewness_null_values():
    df = pd.DataFrame({
        "values": [1, 2, None, 3, 9]
    })

    result = calculate_skewness(df, "values")

    expected = scipy_skew(
        df["values"].dropna(),
        bias=False
    )

    assert result == pytest.approx(expected)


def test_calculate_skewness_constant_values():
    df = pd.DataFrame({
        "values": [5, 5, 5, 5]
    })

    result = calculate_skewness(df, "values")

    assert pd.isna(result)

def test_calculate_kurtosis():
    df = pd.DataFrame({
        "values": [1, 2, 2, 3, 9]
    })

    result = calculate_kurtosis(df, "values")

    expected = scipy_kurtosis(
        df["values"],
        bias=False
    )

    assert result == pytest.approx(expected)


def test_calculate_kurtosis_missing_column():
    df = pd.DataFrame({
        "values": [1, 2, 3, 4]
    })

    with pytest.raises(
        ValueError,
        match="Columns not found in DataFrame"
    ):
        calculate_kurtosis(df, "nonexistent")


def test_calculate_kurtosis_non_numeric_column():
    df = pd.DataFrame({
        "category": ["A", "B", "C"]
    })

    with pytest.raises(
        ValueError,
        match="Columns must be numeric"
    ):
        calculate_kurtosis(df, "category")


def test_calculate_kurtosis_null_values():
    df = pd.DataFrame({
        "values": [1, 2, None, 3, 9]
    })

    result = calculate_kurtosis(df, "values")

    expected = scipy_kurtosis(
        df["values"].dropna(),
        bias=False
    )

    assert result == pytest.approx(expected)


def test_calculate_kurtosis_constant_values():
    df = pd.DataFrame({
        "values": [5, 5, 5, 5]
    })

    result = calculate_kurtosis(df, "values")

    assert pd.isna(result)

def test_calculate_iqr():
    df = pd.DataFrame({
        "values": [1, 2, 3, 4, 5, 6, 7, 8]
    })

    result = calculate_iqr(df, "values")

    expected = 6.25 - 2.75

    assert result == pytest.approx(expected)


def test_calculate_iqr_missing_column():
    df = pd.DataFrame({
        "values": [1, 2, 3, 4]
    })

    with pytest.raises(
        ValueError,
        match="Columns not found in DataFrame"
    ):
        calculate_iqr(df, "nonexistent")


def test_calculate_iqr_non_numeric_column():
    df = pd.DataFrame({
        "category": ["A", "B", "C"]
    })

    with pytest.raises(
        ValueError,
        match="Columns must be numeric"
    ):
        calculate_iqr(df, "category")


def test_calculate_iqr_null_values():
    df = pd.DataFrame({
        "values": [1, 2, None, 4, 5, 6, 7, 8]
    })

    result = calculate_iqr(df, "values")

    expected = (
        df["values"].dropna().quantile(0.75)
        - df["values"].dropna().quantile(0.25)
    )

    assert result == pytest.approx(expected)


def test_calculate_iqr_constant_values():
    df = pd.DataFrame({
        "values": [5, 5, 5, 5]
    })

    result = calculate_iqr(df, "values")

    assert result == 0.0