import re
import pynput
import pyperclip
# from time import sleep


def goddess_format() -> None:
    CAPITAL_PRONOUNS = {'you': 'You', 'you\'re': 'You\'re', 'your': 'Your',
                        'yours': 'Yours', 'yourself': 'Yourself', 'goddess': 'Goddess',
                        'her': 'Her', 'herself': 'Herself', 'she': 'She', 'min': 'Min',
                        'juu': 'Juu'
                        }

    text = re.split(r'(\W)', pyperclip.paste())
    for n, e in enumerate(text):
        try:
            text[n] = CAPITAL_PRONOUNS[e]
        except KeyError:
            continue

    pyperclip.copy(''.join(text))

def on_press(key):
    canonical_key = listener.canonical(key)
    for hotkey in hotkeys:
        hotkey.press(canonical_key)

def on_release(key):
    canonical_key = listener.canonical(key)
    for hotkey in hotkeys:
        hotkey.release(canonical_key)

if __name__ == '__main__':
    hotkeys = [
        pynput.keyboard.HotKey(pynput.keyboard.HotKey.parse('<ctrl>+<shift>+g'), goddess_format)
        ]

    with pynput.keyboard.Listener(on_press=on_press,
                                  on_release=on_release) as listener:
        listener.join()
