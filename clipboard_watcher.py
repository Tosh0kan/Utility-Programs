import pyperclip


def clipboard_proccer():
    last_value = ''
    while True:
        if pyperclip.paste() != '' and '\n' in pyperclip.paste():
            current_value = pyperclip.paste()
            if last_value != current_value:
                current_value = current_value.replace('\n','')
                current_value = current_value.replace('\r', '')
                pyperclip.copy(current_value)
                last_value = current_value
            else:
                pass
        else:
            pass

if __name__ == '__main__':
    clipboard_proccer()
