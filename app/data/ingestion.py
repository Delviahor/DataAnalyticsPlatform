import pandas as pd

def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load data from a CSV file and return it as a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file to be loaded.


    Returns:
    pd.DataFrame: A DataFrame containing the ingested data.
    """

    return pd.read_csv(file_path)  # Return the loaded DataFrame or an empty DataFrame in case of error