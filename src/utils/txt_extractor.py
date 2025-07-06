
class TXTExtractor():
    """
    Extracts and returns the text from a .txt file.

    Args:
        file_path (str): Path to the .txt file.

    Returns:
        str: Text content of the file.
    """
    def extract_text(self, file_path: str) -> str:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()