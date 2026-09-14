import json
import argparse
import pyautogui
from time import sleep
from pyperclip import copy

def load_json(path: str) -> list:
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def text_transfer(text: str) -> None:
    copy(text)
    sleep(0.25)
    pyautogui.hotkey('ctrl', 'v')

def input_auto(content: dict[str, str], idx) -> None:
    if idx == 0:
        sleep(0.1)
        text_transfer(content['word'])

        sleep(0.1)
        for i in range(2):
            pyautogui.press('tab')
            sleep(0.1)

        sleep(0.1)
        text_transfer(content['word_meaning'])

        sleep(0.1)
        pyautogui.press('tab')

        sleep(0.1)
        pyautogui.hotkey('ctrl', 'shift', 'x')

        sleep(0.1)
        text_transfer(content['word_furigana'])

        sleep(0.1)
        for i in range(2):
            pyautogui.press('tab')
            sleep(0.1)
        pyautogui.hotkey('ctrl', 'shift', 'x')

        sleep(0.1)
        text_transfer(content['sentence'])

        sleep(0.1)
        for i in range(2):
            pyautogui.press('tab')
            sleep(0.1)
        text_transfer(content['sentence_meaning'])

        sleep(0.1)
        pyautogui.press('tab')

        sleep(0.1)
        pyautogui.hotkey('ctrl', 'shift', 'x')

        sleep(0.1)
        text_transfer(content['sentence_furigana'])

        pyautogui.hotkey('ctrl', 'enter')

    else:
        sleep(0.1)
        text_transfer(content['word'])

        sleep(0.1)
        for i in range(2):
            pyautogui.press('tab')
            sleep(0.1)

        sleep(0.1)
        text_transfer(content['word_meaning'])

        sleep(0.1)
        for i in range(2):
            pyautogui.press('tab')
            sleep(0.1)

        sleep(0.1)
        text_transfer(content['word_furigana'])

        sleep(0.1)
        for i in range(3):
            pyautogui.press('tab')
            sleep(0.1)

        sleep(0.1)
        text_transfer(content['sentence'])

        sleep(0.1)
        for i in range(2):
            pyautogui.press('tab')
            sleep(0.1)
        text_transfer(content['sentence_meaning'])

        sleep(0.1)
        for i in range(2):
            pyautogui.press('tab')
            sleep(0.1)

        sleep(0.1)
        text_transfer(content['sentence_furigana'])

        pyautogui.hotkey('ctrl', 'enter')
def countdown() -> None:
    elapsed = 0.0
    duration = 5
    while duration > elapsed:
        remaining = duration - elapsed
        print(f"\r{remaining:.1f}", end='', flush=True)
        sleep(0.1)
        elapsed += 0.1
    print("\rStart!")

if __name__ == '__main__':
    empty_dict = {'word': '','word_meaning': '',
                  'word_furigana': '', 'sentence': '',
                  'sentence_meaning': '', 'sentence_furigana': ''}

    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str)
    args = parser.parse_args()

    cards2b = load_json(args.path)
    countdown()
    for word in cards2b:
        for key, term in zip(empty_dict.keys(), word):
            empty_dict[key] = term

        input_auto(empty_dict, cards2b.index(word))
