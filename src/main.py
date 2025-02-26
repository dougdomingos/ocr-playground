from utils.input_parser import get_cli_arguments
from tools.DoctrRunner import DoctrRunner
from tools.TesseractRunner import TesseractRunner

tesseract = TesseractRunner()
doctr = DoctrRunner()
args = get_cli_arguments()

match args.ocr_engine:
    case "tesseract":
        tesseract.process_file(args.file, print_output=True)
    case "doctr":
        doctr.process_file(args.file, print_output=True)
    case _:
        print("Invalid OCR engine provided")