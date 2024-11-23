import os
import json
import asyncio
import argparse
import pillow_avif
from PIL import Image
from pathlib import Path
import datetime as dt
from shutil import rmtree


async def img_convert(path_outer: str, fmt: str, async_flag: bool = False,
                      debug_flag:bool = False, debug_info: str = '') -> Image:
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
            start = dt.datetime.now()
            await asyncio.gather(*(asyncio.to_thread(file_convert, e, fmt, batch=True, count=i)
                                for i, e in enumerate(file_list, start=1)))
            total_time = dt.datetime.now() - start
            print(f"Total time to convert: {total_time}")

            if debug_flag:
                rmtree(path_outer + '\\' + 'converted')
                with open("async_benchmarks.json", "r+", encoding="utf-8") as f:
                    benchmarks = json.load(f)
                    benchmarks.setdefault(debug_info, []).append(round(total_time.total_seconds(), 2))
                    f.seek(0)
                    f.truncate(0)
                    f.write(json.dumps(benchmarks, indent=4))
            else:
                pass

        elif not async_flag:
            print("Boost mode is off. With it on, it's faster but very CPU intesive. "
                  "Activate it by adding the -b or --boost option. To learn more, pass -h or --help.")
            dir_ls = os.listdir(path_outer)
            file_list = [path_outer + '\\' + e for e in dir_ls]

            try:
                os.mkdir(path_outer + '\\' + 'converted')
            except FileExistsError:
                pass
            start = dt.datetime.now()
            for i, e in enumerate(file_list, start=1):
                file_convert(e, fmt, batch=True, count=i)

            total_time = dt.datetime.now() - start
            print(f"Total time to convert: {total_time}")

            if debug_flag:
                rmtree(path_outer + '\\' + 'converted')
                with open("async_benchmarks.json", "r+", encoding="utf-8") as f:
                    benchmarks = json.load(f)
                    benchmarks.setdefault(debug_info, []).append(round(total_time.total_seconds(), 2))
                    f.seek(0)
                    f.truncate(0)
                    f.write(json.dumps(benchmarks, indent=4))
            else:
                pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Input file or folder path with serveral images to convert.",
                        default=os.getcwd())
    parser.add_argument("format", help="Output file/files format")
    parser.add_argument("-b", "--boost", help="Enables asynchronous execution when given a folder path."
                        "Extremely fast but extremely CPU intensive. Default is OFF.",
                        default=False, action="store_true")
    parser.add_argument("-d", "--debug",
                        help="Debug mode. Deletes the converted folder at the end of the process.",
                        default=False, action="store_true")
    parser.add_argument("-i", "--info", help="Extra info passed during debug.")
    args = parser.parse_args()
    asyncio.run(img_convert(args.path, args.format, async_flag = args.boost,
                            debug_flag=args.debug,debug_info=args.info))
if __name__ == "__main__":
    pillow_avif
    main()
