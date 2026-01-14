import os
import sys
import ctypes
import pyautogui
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

def start_csp() -> None:
    os.startfile(r"C:\Program Files\CELSYS\CLIP STUDIO 1.5\CLIP STUDIO PAINT\CLIPStudioPaint.exe")

    print('start')
    print('text copied')
    sleep(2)
    pyautogui.write('lai2 zi4 bbs.itzmx.com mian3 fei4 fen1 xiang3 fa1 xian4 fan4 mai4 cha4 ping2 ju3 bao4 tui4 kuan3 '+
                   'bbs.itzmx.com Always Free')
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
