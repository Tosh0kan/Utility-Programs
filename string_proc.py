import random
import argparse
import pyperclip
import datetime as dt

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
        err = str(err)
        print(f'The <{err}> character is not supported. Only unnacented letters, digits, punctuation, '
              'and the special characters \', \", #, $, %, &, ), (, *, /, +, -, are allowed.')
        quit()

def goddess_format(string: str) -> str:
    CAPITAL_PRONOUNS = {'you': 'You',
                        'you\'re': 'You\'re',
                        'your': 'Your',
                        'yours': 'Yours',
                        'yourself': 'Yourself'}
    str_list = string.split(' ')

    for n, e in enumerate(str_list):
        try:
            str_list[n] = CAPITAL_PRONOUNS[e]
        except KeyError:
            continue

    return ' '.join(str_list)

def snowflake_format(lid: int) -> dt.datetime:
    bin_id = format(lid, "#066b")[2:]
    d_epoch = int(bin_id[0:42], 2)
    u_epoch = d_epoch + 1420070400000

    return dt.datetime.fromtimestamp(u_epoch/1000)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-mt', '--meme-text', type=str, default=None,
                        help='Randomly capitalizes the letters of the string')
    parser.add_argument('-t', '--title', type=str, default=None,
                        help='Capitalizes the first letter of every word.')
    parser.add_argument('-fw', '--fullwidth', type=str, default=None,
                        help='Converts the text to its fullwidth version. '
                        'Supports letters, digits and SOME special characters')
    parser.add_argument('-goddess', '--goddess-format', type=str, default=None,
                        help='Capitalizes the appropriate pronouns')
    parser.add_argument('-s', '--snowflake-timestamp', type=int, default=None,
                        help='Formats snowflake IDs, like a Discord message ID to its timestamp.')

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
        pyperclip.copy(fullwidthed)
        print(f"Sent <{fullwidthed}> to clipboard!")
    elif args.goddess_format is not None:
        goddess_formatted = goddess_format(args.goddess_format)
        pyperclip.copy(goddess_formatted)
        print("Result sent to clipboard!")
    elif args.snowflake_timestamp is not None:
        timestamp = snowflake_format(args.snowflake_timestamp)
        pyperclip.copy(dt.datetime.strftime(timestamp, "%Y-%m-%d %H:%M:%S.%f"))
        print(timestamp)

if __name__ == '__main__':
    main()
