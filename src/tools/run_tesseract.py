from os import path
from sys import argv

from pdf2image import convert_from_path
from PIL import Image
from pytesseract import image_to_string


def process_file(file_path: str) -> dict:
    pages = []
    extracted_texts = []

    if not path.isfile(file_path):
        return None

    elif file_path.lower().endswith(".pdf"):
        pages = convert_from_path(file_path)

    else:
        pages.append(Image.open(file_path))

    for page in pages:
        extracted_texts.append(image_to_string(page))

    return extracted_texts


def write_output_to_file(extracted_contents: list) -> str:
    outfile_path = path.join(path.dirname(path.abspath(__file__)), "output.txt")

    with open(outfile_path, "w") as outfile:
        outfile.writelines(extracted_contents)

    return outfile_path


if __name__ == "__main__":
    file_path = argv[1]
    extracted_text = process_file(file_path)
    outfile_path = write_output_to_file(extracted_text)
    print(f"Contents from {argv[1]} extracted to {outfile_path}")
