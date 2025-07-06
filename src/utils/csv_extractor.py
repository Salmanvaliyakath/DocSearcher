import pandas as pd

class CSVExtractor():
    """
    Converts CSV content to a single string.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        str: Flattened string representation of the CSV.
    """

    def extract_text(self, file_path: str) -> str:
        df = pd.read_csv(file_path)
        return df.to_string().replace('\n',' ')