import re
import win32gui
import pynput
import pyautogui
import pyperclip
from time import sleep


def goddess_format() -> None:
    CAPITAL_PRONOUNS = {'you': 'You', 'you\'re': 'You\'re', 'your': 'Your',
                        'yours': 'Yours', 'yourself': 'Yourself', 'goddess': 'Goddess',
                        'her': 'Her', 'herself': 'Herself', 'she': 'She', 'min': 'Min',
                        'juu': 'Juu'
                        }

    print('into goddess_format function')
    title = win32gui.GetWindowText(win32gui.GetForegroundWindow())

    if 'Discord' in title:
        sleep(0.01)
        with pyautogui.hold('ctrl'):
            pyautogui.press('a')
            pyautogui.press('x')
        text = re.split(r'(\W)', pyperclip.paste())
        for n, e in enumerate(text):
            try:
                text[n] = CAPITAL_PRONOUNS[e]
            except KeyError:
                continue
        pyperclip.copy(''.join(text))
        with pyautogui.hold('ctrl'):
            pyautogui.press('v')

    else:
        pass

def on_press(key):
    canonical_key = listener.canonical(key)
    for hotkey in hotkeys:
        hotkey.press(canonical_key)

def on_release(key):
    canonical_key = listener.canonical(key)
    for hotkey in hotkeys:
        hotkey.release(canonical_key)

hotkeys = [
    pynput.keyboard.HotKey(pynput.keyboard.HotKey.parse('<ctrl>+<shift>+g'), goddess_format)
    ]

if __name__ == '__main__':
    with pynput.keyboard.Listener(on_press=on_press,
                                  on_release=on_release) as listener:
        listener.join()
