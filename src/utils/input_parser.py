from argparse import ArgumentParser, Namespace, BooleanOptionalAction


def get_cli_arguments() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="file", help="File to be processed")
    parser.add_argument("-d", "--dir", dest="dir", help="Directory to be processed")
    parser.add_argument("--ocr-engine", dest="ocr_engine", help="OCR Engine")
    parser.add_argument(
        "-p",
        "--print",
        dest="print_output",
        help="Display extracted text",
        action=BooleanOptionalAction,
    )
    
    return parser.parse_args()

