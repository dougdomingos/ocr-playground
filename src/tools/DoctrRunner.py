from os import path
from sys import argv

from doctr.io import DocumentFile
from doctr.models import ocr_predictor

from utils.file_handler import save_output_to_file
from utils.runtime_telemetry import measure_time


class DoctrRunner:
    def __init__(self):
        """Create a new DoctrRunner instance."""

        self._predictor = ocr_predictor(pretrained=True)

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
        
        save_output_to_file(file_path, extracted_text)

    @measure_time(ocr_engine="DocTR")
    def _extract_contents(self, file_path: str):
        """Extracts all text from the provided file.

        Args:
            file_path (str): The path to the target file,

        Returns:
            str: The text content detected within the file.
        """

        document = None
        extracted_text = None

        if file_path.lower().endswith(".pdf"):
            document = DocumentFile.from_pdf(file_path)
        else:
            document = DocumentFile.from_images(file_path)

        extracted_text = self._predictor(document).render()

        return extracted_text


if __name__ == "__main__":
    ocr_runner = DoctrRunner()
    file_path = argv[1]
    ocr_runner.process_file(file_path, print_output=True)
