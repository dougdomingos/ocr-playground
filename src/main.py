from os import listdir, path
from typing import Dict

from extractors.abstract_extractor import AbstractExtractor
from extractors.doctr import DocTrExtractor
from extractors.tesseract import TesseractExtractor
from utils.input_parser import get_cli_arguments

args = get_cli_arguments()
engines: Dict[str, AbstractExtractor] = {
    "tesseract": TesseractExtractor(),
    "doctr": DocTrExtractor(),
}

if not args.ocr_engine:
    raise ValueError("No OCR engine was provided!")

if args.dir:
    files = [path.join(args.dir, f) for f in listdir(args.dir)]

    for file in files:
        print(f'File "{path.basename(file)}"', end=": ")
        engines[args.ocr_engine].run_extractor(file, print_output=args.print_output)

else:
    engines[args.ocr_engine].run_extractor(args.file, print_output=args.print_output)
