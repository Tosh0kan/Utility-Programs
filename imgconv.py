import os
import asyncio
import argparse
import pillow_avif
from PIL import Image
from pathlib import Path
from datetime import datetime as dt

async def img_convert(path_outer: str, fmt: str) -> Image:
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
        start = dt.now()
        # tasks = (file_convert(e, 'png', batch=True) for e in file_list)
        await asyncio.gather(*(asyncio.to_thread(file_convert, e, 'png', batch=True) for e in file_list))
        print(f"Total time to convert: {dt.now() - start}")
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", help="Input file or folder path", default=os.getcwd())
    parser.add_argument("-f", help="Output file/files format")
    args = parser.parse_args()
    asyncio.run(img_convert(args.p, args.f))
if __name__ == "__main__":
    pillow_avif
    main()
