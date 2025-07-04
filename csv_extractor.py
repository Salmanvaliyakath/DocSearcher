import pandas as pd

class CSVExtractor():
    def extract_text(self, file_path: str) -> str:
        df = pd.read_csv(file_path)
        return df.to_string().replace('\n',' ')