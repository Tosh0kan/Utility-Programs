import os
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
                        'soo': 'Soo', 'jin': 'Jin', "soojin": "SooJin",
                        'her': 'Her', 'hers': 'Hers', 'herself': 'Herself',
                        'she': 'She',
                        }

    title = win32gui.GetWindowText(win32gui.GetForegroundWindow())

    if 'Discord' in title:
        sleep(0.1)
        loop_cnt = 0
        while True:
            loop_cnt += 1
            if loop_cnt == 3:
                print('Failed to find file logo')
                break
            web_logo = pyautogui.locateOnScreen('icons_web.png', confidence=0.7)
            if web_logo is not None:
                x, y, w, h = web_logo
                break
            app_logo = pyautogui.locateOnScreen('icons_app.png', confidence=0.7)
            if app_logo is not None:
                x, y, w, h = app_logo
                break
        print('before move')
        pyautogui.moveTo(x - 100, y + 20)
        sleep(0.2)
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('shift')
        sleep(0.1)
        print('hotkey start')
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
        print('in not discord')
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
    print("into restart_lcore")
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('shift')
    pyautogui.keyUp('r')
    sleep(0.2)
    os.system('taskkill /f /im lcore.exe')
    sleep(0.2)
    os.startfile(r"C:\Program Files\Logitech Gaming Software\LCore.exe")
    sleep(2)
    while True:
        pc_img = pyautogui.locateCenterOnScreen('logitech_computer.png', confidence=0.9)
        if pc_img is not None:
            break
    x, y = pc_img
    print("before click")
    pyautogui.click(x, y)
    with pyautogui.hold('ctrl'):
        pyautogui.press('f4')

if __name__ == '__main__':
    with pynput.keyboard.GlobalHotKeys({'<ctrl>+<shift>+g': goddess_format,
                                        '<ctrl>+<shift>+c': wrapper_proccer,
                                        '<ctrl>+<shift>+q': quit_process,
                                        '<ctrl>+<alt>+<shift>+r': restart_lcore
                                        }) as listener:
        listener.join()
