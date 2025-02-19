from PIL import Image
from pytesseract import image_to_string
from pdf2image import convert_from_path
from os import path
from sys import argv


def convert_pdf_to_images(file_path: str):
    image_list = None

    if path.isfile(file_path):
        image_list = convert_from_path(file_path)

    return image_list


def extract_text_from_image(img_path: str):
    file_content = None

    if path.isfile(img_path):
        file_content = image_to_string(Image.open(img_path))

    return file_content


def write_output_to_file(content: str):
    outfile_path = path.join(path.dirname(path.abspath(__file__)), 'output.txt')
    
    with open(outfile_path, 'w') as outfile:
        outfile.write(content)


if __name__ == '__main__':
    file_path = argv[1]
    file_pages = convert_pdf_to_images(file_path)

    for page in file_pages:
        print(image_to_string(page))
