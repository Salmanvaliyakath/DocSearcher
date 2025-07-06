import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

class ImageExtractor():
    """
    Extracts text from an image file using Tesseract OCR.

    Args:
        file_path (str): Path to the image file (.png).

    Returns:
        str: Extracted text from the image.
    """
    def extract_text(self, file_path: str) -> str:
        image = Image.open(file_path)
        return pytesseract.image_to_string(image)