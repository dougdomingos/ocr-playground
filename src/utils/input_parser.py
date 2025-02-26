from argparse import ArgumentParser, Namespace


def get_cli_arguments() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="file", help="File to be processed")
    parser.add_argument("--ocr-engine", dest="ocr_engine", help="OCR Engine")
    arguments = parser.parse_args()

    return arguments
