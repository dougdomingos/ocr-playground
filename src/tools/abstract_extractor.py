from abc import ABC, abstractmethod
from os import path

from utils.file_handler import save_output_to_file


class AbstractExtractor(ABC):
    """
    This class serves as a default implementation for extraction tools
    """

    def __init__(self):
        """
        Create a new runner class. It applies the specified procedures within
        the instance's "__setup_runner()" method.
        """
        self._setup_runner()

    def _process_file(self, file_path: str, engine_name: str, print_output=True):
        """Given a valid file, extracts its text contents using the OCR tool.

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

        save_output_to_file(file_path, extracted_text, engine_name)

    def _setup_runner(self):
        """
        Configures the extractor with its necessary parameters. This method is intended to be overriden by extractors that
        require specific configurations beforehand.
        """
        pass

    @abstractmethod
    def run_extractor(self, file_path: str, print_output=False):
        """Apply the extractor algorithm to a given file."""
        pass

    @abstractmethod
    def _extract_contents(self, file_path: str) -> str:
        """
        Extracts all detected text content from the provided file.

        Args:
            file_path (str): The path to the target file

        Returns:
            str: The text content detected within the file
        """
        pass
