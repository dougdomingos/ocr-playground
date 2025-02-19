from PIL import Image
from pytesseract import image_to_string
from os import path
from sys import argv

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
    img_path = argv[1]
    file_content = extract_text_from_image(img_path)

    if file_content == None:
        print('Unable to read image ', img_path)
    else:
        write_output_to_file(file_content)
        print('Text contents written to output file.')
