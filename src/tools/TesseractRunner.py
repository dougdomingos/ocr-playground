from os import path
from sys import argv

from pdf2image import convert_from_path
from PIL import Image
from pytesseract import image_to_string

from utils.runtime_telemetry import measure_time


class TesseractRunner:
    def __init__(self):
        """Create a new TesseractRunner."""
        pass

    def process_file(self, file_path: str, print_output=True):
        """Given a PDF or image file, extracts its contents with the OCR tool.

        Args:
            file_path (str): The path to the target file (must be in one of the following formats: PDF, JPG, PNG).
            print_output (bool, optional): Determines if the contents should be displayed after the extraction. Defaults to True.

        Raises:
            InvalidFileException: Thrown if the provided file does not match the specified formats.
        """

        if not path.isfile(file_path):
            raise ValueError(
                "The provided file must be in one of the following formats: PDF, JPG, PNG"
            )

        extracted_text = self._extract_contents(file_path)

        if print_output:
            print(extracted_text)

    @measure_time(ocr_engine="Tesseract")
    def _extract_contents(self, file_path: str):
        """Extracts all text from the provided file.

        Args:
            file_path (str): The path to the target file,

        Returns:
            str: The text content detected within the file.
        """

        pages = []
        extracted_texts = []

        if file_path.lower().endswith(".pdf"):
            pages = convert_from_path(file_path)
        else:
            pages.append(Image.open(file_path))

        for page in pages:
            extracted_texts.append(image_to_string(page))

        return "".join(extracted_texts)


if __name__ == "__main__":
    ocr_runner = TesseractRunner()
    file_path = argv[1]
    ocr_runner.process_file(file_path)
