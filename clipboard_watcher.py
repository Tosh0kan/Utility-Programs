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

def for_canonical(key):
    return lambda k: key(listener.canonical(k))

if __name__ == '__main__':
    with pynput.keyboard.GlobalHotKeys({'<ctrl>+c': wrapper_proccer,
                                        '<ctrl>+q': quit_process}) as listener:
        listener.join()
