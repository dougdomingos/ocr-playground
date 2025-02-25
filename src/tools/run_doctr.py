from os import path
from plistlib import InvalidFileException
from sys import argv

from doctr.io import DocumentFile
from doctr.models import ocr_predictor


class TesseractRunner:
    def __init__(self, outdir: str):
        """Create a new TesseractRunner instance.

        Args:
            outdir (str): The directory in which the output files shall be created.
        """

        self._outdir = outdir
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
            raise InvalidFileException(
                "The provided file must be in one of the following formats: PDF, JPG, PNG"
            )

        extracted_text = self._extract_contents(file_path)
        self._write_output_to_file(extracted_text)

        if print_output:
            print(extracted_text)

    def _extract_contents(self, file_path: str):
        """_summary_

        Args:
            file_path (str): _description_

        Returns:
            _type_: _description_
        """

        document = None
        extracted_text = None

        if file_path.lower().endswith(".pdf"):
            document = DocumentFile.from_pdf(file_path)
        else:
            document = DocumentFile.from_images(file_path)

        extracted_text = self._predictor(document).render()

        return extracted_text

    def _save_output_to_file(extracted_contents: str) -> str:
        outfile_path = path.join(path.dirname(path.abspath(__file__)), "output.txt")

        with open(outfile_path, "w") as outfile:
            outfile.writelines(extracted_contents)

        return outfile_path
