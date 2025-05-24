import os
import json

def line_rip(dir_path) -> None:
    def json_rip() -> dict:
        dir_walk = os.walk(dir_path)
        pages = {}
        for root, dirs, files in dir_walk:
            for file in files:
                if 'json' in file:
                    with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                        data = json.loads(f.read())
                    all_lines = [n['lines'] for n in data['blocks']]
                    procced_lines = []
                    for line in all_lines:
                        if len(line) == 1:
                            procced_lines.append(line[0])
                        else:
                            for n in range(len(line)):
                                procced_lines.append(line[n])
                    pages.setdefault(file.split('.')[0], procced_lines)
                else:
                    pass
        return pages

    def txt_save(pages: dict) -> None:
        final_txt = ''
        for key, value in pages.items():
            final_txt += key + '\n'
            for n in value:
                final_txt += n + '\n'
            final_txt += '\n\n\n'

        with open(dir_path + r'\speech_extracted.txt', 'w', encoding='utf-8') as f:
            f.write(final_txt)

    txt_save(json_rip())


line_rip(r"D:\Scanlation\水星の魔女\_ocr\c1")
