import re
import argparse
import pyperclip

input_txt = "彼は 政界[せいかい]なのに 有名人[ゆうめいじん]と<b>親[した]しい。</b>"

def plain2ruby(term_list: str):
    def reg_htmler(plain_chunk: str) -> str:
        return '<span class="term">' + plain_chunk + '</span>'

    def furiganed_htmler(furiganed_chunk: str) -> str:
        htmled_furigana = furiganed_chunk.replace('[', '<rt>').replace(']', '</rt>')
        return '<span class="term"><ruby>' + htmled_furigana + '</ruby></span>'

    def bolded_htmler(bolded_chunk: str) -> str:
        if '[' not in bolded_chunk:
            return '<span class="term">' + bolded_chunk + '</span>'
        else:
            htmled_furigana = bolded_chunk.replace('[', '<rt>').replace(']', '</rt>')
            htmled_furigana = htmled_furigana.replace('<b>', '').replace('</b>', '')
            return '<span class="term"><b><ruby>' + htmled_furigana + '</ruby></b></span>'

    split_txt = [e for e in re.split(r'\s+|(\w+\[\w+\])|(\w+)|(<b>.*</b>)', term_list) if e != '' and e is not None]
    htmled_list = []
    for e in split_txt:
        if '[' in e and '<b>' not in e:
            htmled_list.append(furiganed_htmler(e))
        elif '<b>' in e:
            htmled_list.append(bolded_htmler(e))
        else:
            htmled_list.append(reg_htmler(e))
    return '\n'.join(htmled_list)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('text', type=str, help='plain text', nargs='*')
    parser.add_argument('-l', '--loop', action='store_true')
    args = parser.parse_args()

    if args.loop:
        while True:
            pln_txt = input("Enter plain text: ")
            if pln_txt == 'q':
                break
            else:
                pyperclip.copy(plain2ruby(pln_txt))
                print('The converted text was successfuly copied to the clipboard.')
    else:
        pyperclip.copy(plain2ruby(args.text))
        print('The converted text was successfuly copied to the clipboard.')
