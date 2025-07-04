from .txt_extractor import TXTExtractor
from .pdf_extractor import PDFExtractor
from .csv_extractor import CSVExtractor
from .image_extractor import ImageExtractor


def get_extractor(file_path: str):
    if file_path.endswith(".txt"):
        return TXTExtractor()
    elif file_path.endswith(".pdf"):
        return PDFExtractor()
    elif file_path.endswith(".csv"):
        return CSVExtractor()
    elif file_path.endswith(".png"):
        return ImageExtractor()
    return None