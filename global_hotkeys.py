import os
import re
import win32gui
import pynput
import pyautogui
import pyperclip
from time import sleep
from datetime import datetime as dt


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

def wrapper_proccer():
    def clipboard_proccer():
        if pyperclip.paste() != '':
            current_value = pyperclip.paste()
            current_value = current_value.replace('\n', '').replace('\r', '').replace(' ', '')
            pyperclip.copy(current_value)
        else:
            pass

    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('c')
    sleep(0.2)
    with pyautogui.hold('ctrl'):
        sleep(0.2)
        pyautogui.press('c')
    print('working')
    sleep(0.2)
    return clipboard_proccer()

def quit_process():
    return quit()

def restart_lcore():
    start = dt.now()
    print("into restart_lcore")
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('r')
    sleep(0.2)
    print("before killing process")
    os.system('taskkill /f /im lcore.exe')
    sleep(0.2)
    print("before starting process")
    os.startfile(r"C:\Program Files\Logitech Gaming Software\LCore.exe")
    sleep(2)
    while True:
        print("into loop")
        pc_img = pyautogui.locateCenterOnScreen('logitech_computer.png', confidence=0.9)
        if pc_img is not None:
            break
    x, y = pc_img
    print("before click")
    pyautogui.click(x, y)
    print(dt.now() - start)

if __name__ == '__main__':
    with pynput.keyboard.GlobalHotKeys({'<ctrl>+<shift>+g': goddess_format,
                                        '<ctrl>+<shift>+c': wrapper_proccer,
                                        '<ctrl>+<shift>+q': quit_process,
                                        '<ctrl>+<alt>+<shift>+r': restart_lcore
                                        }) as listener:
        listener.join()
