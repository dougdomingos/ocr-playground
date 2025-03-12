from pdf2image import convert_from_path
from PIL import Image
from pytesseract import image_to_string

from tools.abstract_extractor import AbstractExtractor
from utils.runtime_telemetry import measure_time


class TesseractExtractor(AbstractExtractor):
    def run_extractor(self, file_path, print_output=True):
        self._process_file(file_path, "tesseract", print_output)

    def _setup_runner(self):
        pass

    @measure_time(ocr_engine="Tesseract")
    def _extract_contents(self, file_path: str) -> str:
        pages = []
        extracted_texts = []

        if file_path.lower().endswith(".pdf"):
            pages = convert_from_path(file_path)
        else:
            pages.append(Image.open(file_path))

        for page in pages:
            extracted_texts.append(image_to_string(page))

        return "".join(extracted_texts)
