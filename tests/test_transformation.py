import pandas as pd

from app.data.transformation import (
    convert_date_column, 
    create_calculated_column)

def create_test_dataframe():
    return pd.DataFrame({
        "date": ["2026-01-05", "2026-01-06", "2026-01-07"],
        "quantity": [2, 5, 3],
        "unit_price": [850.0, 15.5, 45.0]
    })


def test_convert_date_column():
    df = create_test_dataframe()

    result = convert_date_column(df, "date")

    assert pd.api.types.is_datetime64_any_dtype(result["date"])
    assert result.loc[0, "date"] == pd.Timestamp("2026-01-05")


def test_convert_date_column_preserves_original():
    df = create_test_dataframe()
    original_df = df.copy(deep=True)

    convert_date_column(df, "date")

    pd.testing.assert_frame_equal(df, original_df)


def test_create_calculated_column():
    df = create_test_dataframe()

    result = create_calculated_column(
        df,
        "total",
        "quantity",
        "unit_price"
    )

    assert "total" in result.columns
    assert result.loc[0, "total"] == 1700.0
    assert result.loc[1, "total"] == 77.5
    assert result.loc[2, "total"] == 135.0


def test_create_calculated_column_preserves_original():
    df = create_test_dataframe()
    original_df = df.copy(deep=True)

    create_calculated_column(
        df,
        "total",
        "quantity",
        "unit_price"
    )

    pd.testing.assert_frame_equal(df, original_df)