import os
import pyperclip
import pyautogui
from time import sleep


def start_csp() -> None:
    os.startfile(r"C:\Program Files\CELSYS\CLIP STUDIO 1.5\CLIP STUDIO PAINT\CLIPStudioPaint.exe")

    pyperclip.copy('lai2 zi4 bbs.itzmx.com mian3 fei4 fen1 xiang3 fa1 xian4 fan4 mai4 cha4 ping2 ju3 bao4 tui4 kuan3 '+
                   'bbs.itzmx.com Always Free')
    sleep(1)
    pyautogui.hotkey('ctrl', 'v')
    sleep(0.55)
    pyautogui.press('enter')

if __name__ == '__main__':
    start_csp()
