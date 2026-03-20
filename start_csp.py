import os
import sys
import ctypes
import pyautogui
import win32gui
import pyperclip
from time import sleep

def is_admin() -> bool:
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

def run_as_adm() -> bool:
    script = sys.argv[0]
    params = ' '.join([f'"{x}"' for x in sys.argv])

    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f'"{script}" {params}', None, 1)
        return True
    except Exception as e:
        print(f"Failed to elevate privileges: {e}")
        return False

def win_enum_handler(hwnd, top_windows: list):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

def start_csp() -> None:
    os.startfile(r"C:\Program Files\CELSYS\CLIP STUDIO 1.5\CLIP STUDIO PAINT\CLIPStudioPaint.exe")

    print('start!')

    pyperclip.copy('lai2 zi4 bbs.itzmx.com mian3 fei4 fen1 xiang3 fa1 xian4 fan4 mai4 tui4 kuan3 ju3 bao4 cha4 ping2 '+
                   'bbs.itzmx.com Always Free')

    sleep(0.5)
    top_windows: list = []
    win32gui.EnumWindows(win_enum_handler, top_windows)
    for i in  top_windows:
        if "application requires" in i[1].lower():
            print(i)
            win32gui.ShowWindow(i[0], 5)
            win32gui.SetForegroundWindow(i[0])
            break

    sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')
    sleep(0.5)
    pyautogui.press('enter')

if __name__ == '__main__':
    if is_admin():
        start_csp()
    else:
        print("Requesting administrator privileges...")
        if run_as_adm():
            print("Please check the new window for the elevated process.")
        else:
            print("Failed to get admin rights. The script will exit.")
