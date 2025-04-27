import pynput
import pyperclip
from time import sleep


def wrapper_proccer():
    def clipboard_proccer():
        if pyperclip.paste() != '':
            current_value = pyperclip.paste()
            current_value = current_value.replace('\n', '')
            current_value = current_value.replace('\r', '')
            pyperclip.copy(current_value)
        else:
            pass

    sleep(0.01)
    return clipboard_proccer()

def quit_process():
    return quit()

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
        pynput.keyboard.HotKey(pynput.keyboard.HotKey.parse('<ctrl>+c'), wrapper_proccer),
        pynput.keyboard.HotKey(pynput.keyboard.HotKey.parse('<ctrl>+q'), quit_process),
        ]
    with pynput.keyboard.Listener(on_press=on_press,
                                  on_release=on_release) as listener:
        listener.join()
