from os import path
from sys import argv

from doctr.io import DocumentFile
from doctr.models import ocr_predictor

def process_file(file_path: str) -> dict:
    document = None
    extracted_text = None
    predictor = ocr_predictor(pretrained=True)

    if not path.isfile(file_path):
        return None

    elif file_path.lower().endswith(".pdf"):
        document = DocumentFile.from_pdf(file_path)

    else:
        document = DocumentFile.from_images(file_path)

    extracted_text = predictor(document).render()

    return extracted_text


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
