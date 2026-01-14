import os
import psutil
import random
import argparse
import pyperclip
import pyautogui
import datetime as dt
from time import sleep
from pathlib import Path
from base64 import (b64decode,
                    b64encode)

def meme_string(string: str) -> str:
    split_str = [e for e in string]

    cnt = 0
    for e in split_str:
        flip = random.choice(range(2))
        if flip == 0:
            split_str[cnt] = e.lower()
            cnt += 1
        else:
            split_str[cnt] = e.upper()
            cnt += 1
    return ''.join(split_str)

def fullwidth(string: str) -> str|None:
    split_str = [e for e in string]

    ascii_chr = [e for e in range(32, 127)]
    fullwidth_chr = [e for e in range(0xff01, 0xff5e+1)]
    fullwidth_chr.insert(0, 0x3000)
    ascii_to_fullwidth_table = {chr(x): chr(y) for x, y in zip(ascii_chr, fullwidth_chr)}

    try:
        cnt = 0
        for e in split_str:
            split_str[cnt] = ascii_to_fullwidth_table[e]
            cnt += 1
        return ''.join(split_str)
    except KeyError as err:
        print(f'The <{err}> character is not supported. Only unnacented letters, digits, punctuation, '
              'and the special characters \', \", #, $, %, &, ), (, *, /, +, -, are allowed.')
        quit()

def snowflake_format(lid: int) -> str:
    bin_id = format(lid, "#066b")[2:]
    d_epoch = int(bin_id[0:42], 2)
    u_epoch = d_epoch + 1420070400000
    dt_epoch =  dt.datetime.fromtimestamp(u_epoch/1000)
    dt_str = dt.datetime.strftime(dt_epoch, "%Y-%m-%d %H:%M:%S.%f")

    to_proc = list(dt_str.split('.')[1])
    while to_proc[-1] == '0':
        to_proc.pop(-1)
    joined_to_proc = ''.join(to_proc)
    dt_str = dt_str.split('.')[0] + '.' + joined_to_proc

    return dt_str

def b64(txt: str, decode: bool = True):
    if decode:
        return b64decode(txt)
    else:
        return b64encode(txt.encode('utf-8'))

def md_quote() -> str:
    unproc_str = pyperclip.paste()
    unproc_str_list = unproc_str.split('\r\n\r\n')
    procced_str_list = ['> ' + e for e in unproc_str_list]
    procced_str = '\r\n\r\n'.join(procced_str_list)
    return procced_str

def add_wows_location() -> None:
    def img_rec_clicker(img_path: str) -> list[int]:
        while True:
            img_coords = pyautogui.locateCenterOnScreen(img_path, confidence=0.9)
            if img_coords is not None:
                break

        return [img_coords[0], img_coords[1]]


    wows_bins = "E:/Games/World_of_Warships/bin"

    wows_curr_ver_exe = Path(wows_bins + f'/{max(os.listdir(wows_bins))}' + '/bin64' + '/WorldOfWarships64.exe')

    os.startfile(r"C:/Program Files/Logitech Gaming Software/LCore.exe")
    ### Finds the hotkey icon and clicks
    sleep(0.55)
    ic_x, ic_y = img_rec_clicker('hotkeys_icon.png')
    pyautogui.click(ic_x, ic_y)

    ### Finds the wows icon and double clicks it
    sleep(0.55)
    wows_x, wows_y = img_rec_clicker('wows_icon.png')
    pyautogui.doubleClick(wows_x, wows_y)

    ##Finds the add button and clicks it
    sleep(0.55)
    add_x, add_y = img_rec_clicker('plus_minus_icon.png')
    pyautogui.click(add_x-15, add_y)

    pyperclip.copy(str(wows_curr_ver_exe))
    sleep(0.55)
    pyautogui.hotkey('ctrl', 'v')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(0.5)
    pyautogui.hotkey('alt', 'f4')

def demerit_calc(x:int, y:int) -> float:
    return (x * 0.25) + (y * 0.2)

def reset_lcore() -> None:
    PROCNAME = "LCore.exe"
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            proc.kill()

    os.startfile(r"C:/Program Files/Logitech Gaming Software/LCore.exe")
    sleep(2)
    pyautogui.click(1655, 368)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-mt', '--meme-text', type=str, default=None,
                        help='Randomly capitalizes the letters of the string')
    parser.add_argument('-t', '--title', type=str, default=None,
                        help='Capitalizes the first letter of every word.')
    parser.add_argument('-fw', '--fullwidth', type=str, default=None,
                        help='Converts the text to its fullwidth version. '
                        'Supports letters, digits and SOME special characters')
    parser.add_argument('-s', '--snowflake-timestamp', type=int, default=None,
                        help='Formats snowflake IDs, like a Discord message ID to its timestamp.')
    parser.add_argument('-b64d', "--base64-decode", type=str, default=None)
    parser.add_argument('-b64e', "--base64-encode", type=str, default=None)
    parser.add_argument('-mdq', "--markdown-quote", action='store_true', default=None,
                        help='Converts the text to a markdown quote.')
    parser.add_argument('-wows', "--add-wows-location", action='store_true', default=None,
                        help='Adds the World of Warships location to the clipboard.')
    parser.add_argument('-r', '--review-math', default=None, help='Calculates total demerits.')
    parser.add_argument('-rl', '--reset-lcore', action='store_true', default=None,
                        help='Resets Logitech Gaming Utility.')

    args = parser.parse_args()
    if args.meme_text is not None:
        meme_text = meme_string(args.meme_text)
        pyperclip.copy(meme_text)
        print(f"Sent <{meme_text}> to clipboard!")
    elif args.title is not None:
        titled = args.title.title()
        pyperclip.copy(titled)
        print(f"Sent <{titled}> to clipboard!")
    elif args.fullwidth is not None:
        fullwidthed = fullwidth(args.fullwidth)
        if fullwidthed is None:
            quit()
        pyperclip.copy(fullwidthed)
        print(f"Sent <{fullwidthed}> to clipboard!")
    elif args.snowflake_timestamp is not None:
        timestamp = snowflake_format(args.snowflake_timestamp)
        pyperclip.copy(timestamp)
        print(timestamp)
    elif args.base64_decode is not None:
        decoded_text = b64(args.base64_decode).decode('utf-8')
        pyperclip.copy(decoded_text)
        print(decoded_text)
    elif args.base64_encode is not None:
        encoded_text = b64(args.base64_encode, decode=False).decode('utf-8')
        pyperclip.copy(encoded_text)
        print(encoded_text)
    elif args.markdown_quote is not None:
        mdq = md_quote()
        pyperclip.copy(mdq)
        print("Procced text sent to clipboard!")
    elif args.add_wows_location is not None:
        add_wows_location()
    elif args.review_math is not None:
        print(demerit_calc(int(args.review_math.split()[0]), int(args.review_math.split()[1])))
    elif args.reset_lcore is not None:
        reset_lcore()

if __name__ == '__main__':
    main()
