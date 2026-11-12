import pandas as pd
from plotly.graph_objects import Figure

from app.data.ingestion import load_csv

from app.data.inspection import (
    get_dataset_shape,
    get_data_types,
    get_missing_values,
    get_duplicates,
    get_descriptive_statistics
)

from app.data.cleaning import(
    remove_duplicates,
    handle_missing_values
)

from app.data.transformation import(
    convert_date_column,
    create_calculated_column
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

from app.data.visualization import (
    create_histogram,
    create_bar_chart,
    create_scatter_plot,
    create_line_chart,
    create_box_plot
)

def test_ingestion_and_inspection_integration():
    # Ingestion
    df = load_csv("datasets/sales.csv")

    # Verify ingestion output
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

    # Inspection
    shape = get_dataset_shape(df)
    data_types = get_data_types(df)
    missing_values = get_missing_values(df)
    duplicates = get_duplicates(df)
    descriptive_statistics = get_descriptive_statistics(df)

    # Verify inspection outputs
    assert shape["rows"] == df.shape[0]
    assert shape["columns"] == df.shape[1]
    
    assert not data_types.empty
    assert missing_values is not None
    assert duplicates >= 0
    assert not descriptive_statistics.empty

    # Cleaning
    cleaned_df = remove_duplicates(df)

    assert isinstance(cleaned_df, pd.DataFrame)
    assert not cleaned_df.duplicated().any()

    # Handle missing values
    column_with_missing = missing_values[missing_values > 0].index

    if len(column_with_missing) > 0:
        column = column_with_missing[0]

        cleaned_df = handle_missing_values(
            cleaned_df,
            column,
            value="Unknown"
        )

        assert cleaned_df[column].isna().sum() == 0

        # Transformation: convert date column
    transformed_df = convert_date_column(
        cleaned_df,
        "date"
    )

    assert pd.api.types.is_datetime64_any_dtype(
        transformed_df["date"]
    )

    # Transformation: create calculated column
    transformed_df = create_calculated_column(
        transformed_df,
        "total",
        "quantity",
        "unit_price",
        operation="multiply"
    )

    assert "total" in transformed_df.columns

    assert (
        transformed_df["total"]
        == transformed_df["quantity"] * transformed_df["unit_price"]
    ).all()

    # Analytics: correlation
    correlation = calculate_correlation(
        transformed_df,
        "quantity",
        "unit_price"
    )

    assert isinstance(correlation, float)
    assert -1 <= correlation <= 1

    # Analytics: aggregation
    regional_sales = aggregate_data(
        transformed_df,
        "region",
        "total",
        "sum"
    )

    assert "region" in regional_sales.columns
    assert "total" in regional_sales.columns
    assert regional_sales["total"].sum() == transformed_df["total"].sum()

    # Analytics: frequency
    product_frequency = calculate_frequency(
        transformed_df,
        "product"
    )

    assert product_frequency.sum() == len(transformed_df)

    # Analytics: variance
    variance = calculate_variance(
        transformed_df,
        "total"
    )

    assert variance >= 0

    # Analytics: skewness
    skewness = calculate_skewness(
        transformed_df,
        "total"
    )

    assert isinstance(skewness, float)

    # Analytics: kurtosis
    kurtosis = calculate_kurtosis(
        transformed_df,
        "total"
    )

    assert isinstance(kurtosis, float)

    # Analytics: interquartile range
    iqr = calculate_iqr(
        transformed_df,
        "total"
    )

    assert iqr >= 0

        # Visualization: histogram
    histogram = create_histogram(
        transformed_df,
        "total"
    )

    assert isinstance(histogram, Figure)
    assert len(histogram.data) > 0
    assert len(histogram.data[0].x) == len(transformed_df)

    # Visualization: bar chart
    bar_chart = create_bar_chart(
        regional_sales,
        "region",
        "total"
    )

    assert isinstance(bar_chart, Figure)
    assert len(bar_chart.data) > 0

    # Visualization: scatter plot
    scatter = create_scatter_plot(
        transformed_df,
        "quantity",
        "unit_price"
    )

    assert isinstance(scatter, Figure)
    assert len(scatter.data[0].x) == len(transformed_df)
    assert len(scatter.data[0].y) == len(transformed_df)

    # Visualization: line chart
    line_chart = create_line_chart(
        transformed_df,
        "date",
        "total"
    )

    assert isinstance(line_chart, Figure)
    assert len(line_chart.data) > 0

    # Visualization: box plot
    box_plot = create_box_plot(
        transformed_df,
        "total",
        x_column="category"
    )

    assert isinstance(box_plot, Figure)
    assert len(box_plot.data) > 0