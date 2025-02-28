import re
from os import path
from typing import Iterable


def save_output_to_file(file_path: str, content: str | Iterable[str]):
    outfile_name = re.sub(r"\.(pdf|jpg|jpeg|png)", ".txt", path.basename(file_path))
    outfile_abspath = path.join(get_results_dir(file_path), outfile_name)

    with open(outfile_abspath, 'w') as outfile:
        outfile.writelines(content)


def get_results_dir(file_path: str) -> str:
    results_dir = path.abspath(__file__).replace("/src/utils/file_handler.py", "/results")

    if "digitalized" in file_path:
        results_dir = path.join(results_dir, "digitalized")
    else:
        results_dir = path.join(results_dir, "textual")

    return results_dir
