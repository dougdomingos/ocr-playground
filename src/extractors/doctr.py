from doctr.io import DocumentFile
from doctr.models import ocr_predictor

from extractors.abstract_extractor import AbstractExtractor
from utils.runtime_telemetry import measure_time


class DocTrExtractor(AbstractExtractor):
    def run_extractor(self, file_path, print_output=True):
        self._process_file(file_path, "doctr", print_output)

    def _setup_runner(self):
        self._predictor = ocr_predictor(pretrained=True)

    @measure_time(ocr_engine="DocTR")
    def _extract_contents(self, file_path: str) -> str:
        document = None
        extracted_text = None

        if file_path.lower().endswith(".pdf"):
            document = DocumentFile.from_pdf(file_path)
        else:
            document = DocumentFile.from_images(file_path)

        extracted_text = self._predictor(document).render()

        return extracted_text
