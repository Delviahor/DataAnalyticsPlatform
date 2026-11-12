from app.data.ingestion import load_csv

def test_load_csv():
    result = load_csv("datasets/sales.csv")
    
    assert result is not None, "The result should not be None"
    assert len(result) == 10, "row count should be 10"
    assert len(result.columns) ==7, "column count should be 7"