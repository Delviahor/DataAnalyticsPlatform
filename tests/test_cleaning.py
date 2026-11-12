import pandas as pd

from app.data.cleaning import (
    remove_duplicates,
    handle_missing_values
)


def create_test_dataframe():
    return pd.DataFrame({
        "product": ["Laptop", "Mouse", "Keyboard", "Laptop"],
        "quantity": [2, 5, 3, 2],
        "unit_price": [850.0, 15.5, 45.0, 850.0],
        "region": ["North", "South", None, "North"]
    })


def test_remove_duplicates():
    df = create_test_dataframe()

    result = remove_duplicates(df)

    assert len(result) == 3
    assert result.duplicated().sum() == 0


def test_remove_duplicates_preserves_original():
    df = create_test_dataframe()
    original_df = df.copy(deep=True)

    remove_duplicates(df)

    pd.testing.assert_frame_equal(df, original_df)


def test_handle_missing_values():
    df = create_test_dataframe()

    result = handle_missing_values(df, "region", "Unknown")

    assert result["region"].isnull().sum() == 0
    assert result.loc[2, "region"] == "Unknown"


def test_handle_missing_values_preserves_original():
    df = create_test_dataframe()
    original_df = df.copy(deep=True)

    handle_missing_values(df, "region", "Unknown")

    pd.testing.assert_frame_equal(df, original_df)
