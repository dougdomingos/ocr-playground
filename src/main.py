from os import listdir, path

from tools.DoctrRunner import DoctrRunner
from tools.TesseractRunner import TesseractRunner
from utils.input_parser import get_cli_arguments

args = get_cli_arguments()
engines = {"tesseract": TesseractRunner(), "doctr": DoctrRunner()}

if not args.ocr_engine:
    raise ValueError("No OCR engine was provided!")

if args.dir:
    files = [path.join(args.dir, f) for f in listdir(args.dir)]

    for file in files:
        print(f'File "{path.basename(file)}"', end=": ")
        engines[args.ocr_engine].process_file(file, print_output=args.print_output)

else:
    engines[args.ocr_engine].process_file(args.file, print_output=args.print_output)
