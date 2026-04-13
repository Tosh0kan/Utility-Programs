import re
import argparse
import pyperclip

input_txt = "彼は 政界[せいかい]なのに 有名人[ゆうめいじん]と<b>親[した]しい。</b>"

def plain2ruby(term_list: str):
    def reg_htmler(plain_chunk: str) -> str:
        return '<span class="term">' + plain_chunk + '</span>'

    def furiganed_htmler(furiganed_chunk: str) -> str:
        hrtmled_furigana = furiganed_chunk.replace('[', '<rt>').replace(']', '</rt>')
        return '<span class="term"><ruby>' + hrtmled_furigana + '</ruby></span>'

    def bolded_htmler(bolded_chunk: str) -> str:
        return '<span class="term"><b>' + bolded_chunk + '</b></span>'

    split_txt = [e for e in re.split(r'\s+|(\w+\[\w+\])|(\w+)|(<b>.*</b>)', term_list) if e != '' and e is not None]
    htmled_list = []
    for e in split_txt:
        if '[' in e:
            htmled_list.append(furiganed_htmler(e))
        elif '<b>' in e:
            htmled_list.append(bolded_htmler(e))
        else:
            htmled_list.append(reg_htmler(e))
    return '\n'.join(htmled_list)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('text', type=str, help='plain text')
    args = parser.parse_args()

    pyperclip.copy(plain2ruby(args.text))
    print('The converted text was successfuly copied to the clipboard.')
