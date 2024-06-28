import os
import asyncio
import argparse
import pillow_avif
from PIL import Image
from pathlib import Path
from datetime import datetime as dt


async def img_convert(path_outer: str, fmt: str, async_flag: bool = False) -> Image:
    def file_convert(path_inner: str, fmt: str, batch: bool = False, count: int = 0) -> Image:
        if not batch:
            with Image.open(r"{}".format(path_inner)).convert("RGB") as icon:
                icon.save(r"{}.{}".format(path_inner.split('.')[0], fmt), format=f"{fmt.upper()}")
        elif batch:
            converted_folder = (path_inner.replace(os.path.basename(path_inner), '')) + 'converted'
            img_name = os.path.basename(path_inner).split('.')[0]
            with Image.open(r"{}".format(path_inner)).convert("RGB") as icon:
                icon.save(r"{}.{}".format(converted_folder  + '\\' + img_name, fmt), format=f"{fmt.upper()}")
                print(f"Saved file {count}/{len(file_list)}")


    if Path(path_outer).is_file():
        file_convert(path_outer, fmt)

    elif Path(path_outer).is_dir():
        if async_flag:
            dir_ls = os.listdir(path_outer)
            file_list = [path_outer + '\\' + e for e in dir_ls]

            try:
                os.mkdir(path_outer + '\\' + 'converted')
            except FileExistsError:
                pass
            start = dt.now()
            await asyncio.gather(*(asyncio.to_thread(file_convert, e, fmt, batch=True, count=i)
                                for i, e in enumerate(file_list, start=1)))
            print(f"Total time to convert: {dt.now() - start}")

        elif not async_flag:
            print("Boost mode is off. With it on, it's faster but very CPU intesive. "
                  "Activate it by adding the -b or --boost option. To learn more, pass -h or --help.")
            dir_ls = os.listdir(path_outer)
            file_list = [path_outer + '\\' + e for e in dir_ls]

            try:
                os.mkdir(path_outer + '\\' + 'converted')
            except FileExistsError:
                pass
            start = dt.now()
            for i, e in enumerate(file_list, start=1):
                file_convert(e, fmt, batch=True, count=i)

            print(f"Total time to convert: {dt.now() - start}.")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="Input file or folder path with serveral images to convert.",
                        default=os.getcwd())
    parser.add_argument("-f", "--format", help="Output file/files format")
    parser.add_argument("-b", "--boost", help="Enables asynchronous execution when given a folder path."
                        "Extremely fast but extremely CPU intensive. Default is OFF.",
                        default=False, action="store_true")
    args = parser.parse_args()
    asyncio.run(img_convert(args.path, args.format, args.boost))
if __name__ == "__main__":
    pillow_avif
    main()
