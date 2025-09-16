import pynput
import pyperclip
import argparse
from time import sleep


def wrapper_proccer():
    def clipboard_proccer():
        if args.averager:
            freq_check = False

            s = pyperclip.paste()
            chrs = ([chr(e) for e in range(0x3041, 0x3097)] +
                    [chr(e) for e in range(0x30a1, 0x30fb)] +
                    [chr(e) for e in range(0x4e00, 0x9fb0)])

            matches = {True: 0, False: 0}
            for e in s:
                if e in chrs:
                    matches[True] += 1
                else:
                    matches[False] += 1
            if matches[True] >= (len(s) / 5) * 4:
                freq_check = True
            else:
                pass

            if freq_check:
                if pyperclip.paste() != '':
                    current_value = pyperclip.paste()
                    current_value = current_value.replace('\n', '').replace('\r', '').replace(' ', '')
                    pyperclip.copy(current_value)
                else:
                    pass
            else:
                if pyperclip.paste() != '':
                    current_value = pyperclip.paste()
                    current_value = current_value.replace('\n', '').replace('\r', '')
                    pyperclip.copy(current_value)
                else:
                    pass

        else:
            if pyperclip.paste() != '':
                current_value = pyperclip.paste()
                current_value = current_value.replace('\n', '').replace('\r', '').replace(' ', '')
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
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--averager', action='store_true')
    args = parser.parse_args()

    hotkeys = [
        pynput.keyboard.HotKey(pynput.keyboard.HotKey.parse('<ctrl>+c'), wrapper_proccer),
        pynput.keyboard.HotKey(pynput.keyboard.HotKey.parse('<ctrl>+q'), quit_process),
        ]
    with pynput.keyboard.Listener(on_press=on_press,
                                  on_release=on_release) as listener:
        listener.join()
