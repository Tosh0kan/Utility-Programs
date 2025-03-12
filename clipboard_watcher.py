import pynput
import pyperclip
from time import sleep


def wrapper_proccer():
    def clipboard_proccer():
        current_value = pyperclip.paste()
        current_value = current_value.replace('\n','')
        current_value = current_value.replace('\r', '')
        pyperclip.copy(current_value)

    sleep(0.01)
    return clipboard_proccer()

def for_canonical(f):
    return lambda k: f(listener.canonical(k))
''
if __name__ == '__main__':
    hotkey = pynput.keyboard.HotKey(pynput.keyboard.HotKey.parse('<ctrl>+c'), wrapper_proccer)
    with pynput.keyboard.Listener(on_press=for_canonical(hotkey.press),
                                  on_release=for_canonical(hotkey.release)) as listener:
        listener.join()
