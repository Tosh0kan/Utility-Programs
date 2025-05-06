import re
import win32gui
import pynput
import pyautogui
import pyperclip
from time import sleep


def goddess_format() -> None:
    CAPITAL_PRONOUNS = {'you': 'You', 'you\'re': 'You\'re', 'your': 'Your',
                        'yours': 'Yours', 'yourself': 'Yourself', 'goddess': 'Goddess',
                        'min': 'Min', 'juu': 'Juu', 'minjuu': 'MinJuu',
                        'soo': 'Soo', 'jin': 'Jin', "soojin": "SooJin"
                        }

    title = win32gui.GetWindowText(win32gui.GetForegroundWindow())

    if 'Discord' in title:
        sleep(0.1)
        file_logo = pyautogui.locateOnScreen('icons.png', confidence=0.9)
        x, y, w, h = file_logo
        while True:
            pyautogui.moveTo(x - 50, y + 20)
            break
        sleep(0.2)
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('shift')
        sleep(0.1)
        with pyautogui.hold('ctrl'):
            pyautogui.press('a')
            sleep(0.1)
            pyautogui.press('x')
        sleep(0.2)
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

if __name__ == '__main__':
    with pynput.keyboard.GlobalHotKeys({'<ctrl>+<shift>+g': goddess_format
                                        }) as listener:
        listener.join()
