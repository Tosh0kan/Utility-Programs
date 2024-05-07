import argparse
import pillow_avif
from PIL import Image

def img_convert(i_file: str, fmt: str) -> Image:
    icon = Image.open(r"{}".format(i_file)).convert("RGB")

    icon.save(r"{}.{}".format(i_file.split('.')[0], fmt), format=f"{fmt.upper()}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", help="Input file path")
    parser.add_argument("-f", help="Output file format")
    args = parser.parse_args()
    img_convert(args.i, args.f)


if __name__ == "__main__":
    pillow_avif
    main()
