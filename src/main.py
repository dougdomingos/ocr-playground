from utils.input_parser import get_cli_arguments
from tools.DoctrRunner import DoctrRunner
from tools.TesseractRunner import TesseractRunner

tesseract = TesseractRunner()
doctr = DoctrRunner()
args = get_cli_arguments()

match args.ocr_engine:
    case "tesseract":
        tesseract.process_file(args.file, print_output=args.print_output)
    case "doctr":
        doctr.process_file(args.file, print_output=args.print_output)
    case "all":
        tesseract.process_file(args.file, print_output=args.print_output)
        doctr.process_file(args.file, print_output=args.print_output)        
    case _:
        print("Invalid OCR engine provided")