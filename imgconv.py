import os
import argparse
import pillow_avif
from pprint import pp
from PIL import Image
from pathlib import Path
from datetime import datetime as dt

def img_convert(path_outer: str, fmt: str) -> Image:
    def file_convert(path_inner: str, fmt: str, batch: bool = False) -> Image:
        if not batch:
            icon = Image.open(r"{}".format(path_inner)).convert("RGB")
            icon.save(r"{}.{}".format(path_inner.split('.')[0], fmt), format=f"{fmt.upper()}")
        elif batch:
            converted_folder = '\\'.join(path_inner.split('\\')[0:-1]) + '\\converted'
            img_name = path_inner.split('\\')[-1].split('.')[0]
            icon = Image.open(r"{}".format(path_inner)).convert("RGB")
            icon.save(r"{}.{}".format(converted_folder  + '\\' + img_name, fmt), format=f"{fmt.upper()}")

    if Path(path_outer).is_file():
        file_convert(path_outer, fmt)

    elif Path(path_outer).is_dir():
        dir_ls = os.listdir(path_outer)
        file_list = [path_outer + '\\' + e for e in dir_ls]
        try:
            os.mkdir(path_outer + '\\' + 'converted')
        except FileExistsError:
            pass
        total_files = len(file_list)
        file_no = 1
        start = dt.now()
        for e in file_list:
            file_convert(e, 'png', batch=True)
            print(f"Saved file {file_no}/{total_files}")
            file_no += 1
        print(f"Total time to convert: {dt.now() - start}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", help="Input file or folder path", default=os.getcwd())
    parser.add_argument("-f", help="Output file/files format")
    args = parser.parse_args()
    img_convert(args.p, args.f)


if __name__ == "__main__":
    pillow_avif
    main()
