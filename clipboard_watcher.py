import pyperclip
import pynput


def clipboard_proccer():
    print('into proccer')
    current_value = pyperclip.paste()
    current_value = current_value.replace('\n','')
    current_value = current_value.replace('\r', '')
    pyperclip.copy(current_value)
    print('out of proccer')

def for_canonical(f):
    return lambda k: f(l.canonical(k))

if __name__ == '__main__':
    hotkey = pynput.keyboard.HotKey(pynput.keyboard.HotKey.parse('<ctrl>+c'), clipboard_proccer)
    with pynput.keyboard.Listener(on_press=for_canonical(hotkey.press), on_release=for_canonical(hotkey.release)) as l:
        l.join()
