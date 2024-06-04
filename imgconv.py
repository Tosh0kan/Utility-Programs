import os
import argparse
import pillow_avif
from pprint import pp
from PIL import Image
from pathlib import Path

def img_convert(path_outer: str, fmt: str) -> Image:
    def file_convert(path_inner: str, fmt: str) -> Image:
        icon = Image.open(r"{}".format(path_inner)).convert("RGB")
        icon.save(r"{}.{}".format(path_inner.split('.')[0], fmt), format=f"{fmt.upper()}")

    print(path_outer)
    if Path(path_outer).is_file():
        file_convert(path_outer, fmt)

    elif Path(path_outer).is_dir():
        dir_ls = os.listdir(path_outer)
        file_list = [path_outer + '\\' + e for e in dir_ls]
        pp(file_list)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", help="Input file or folder path", default=os.getcwd())
    parser.add_argument("-f", help="Output file/files format")
    args = parser.parse_args()
    img_convert(args.p, args.f)


if __name__ == "__main__":
    pillow_avif
    main()
