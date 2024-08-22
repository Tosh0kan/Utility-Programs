import os
import httpx
import asyncio
import argparse
from bs4 import BeautifulSoup as bs


async def scrape_and_proc(url: str, path: str, custom_title: str = None,
                          prefix: str = None, suffix: str = None,
                          title_add: list[str] = None) -> None:

    def title_legality(story_title: str) -> str:
        FORBIDDEN_CHARACTERS = (
        '/',
        '|',
        '\\',
        ':',
        '*',
        '?',
        '"',
        '<',
        '>',
        )
        char_list = list(story_title)
        forbidden_indexes = []
        for n, e in enumerate(char_list):
            if e in FORBIDDEN_CHARACTERS:
                forbidden_indexes.append(n)
                continue

            else:
                continue

        if len(forbidden_indexes) == 0:
            return ''.join(char_list)

        for e in forbidden_indexes:
            if char_list[e] == ':':
                char_list[e] = '-'

            else:
                char_list[e] = ' NaN '

        return ''.join(char_list)

    def string_insertion(og_title: str, prefix: str = None, suffix: str = None,
                            custom_title: str = None, title_add: list[str] = None) -> str:
        if custom_title is not None:
            og_title = custom_title
        elif prefix is not None and suffix is not None:
            og_title = prefix + ' ' + og_title + ' ' + suffix
        elif prefix is not None:
            og_title = prefix + ' ' + og_title
        elif suffix is not None:
            og_title = og_title + ' ' + suffix
        elif title_add is not None:
            global usage_info
            sub_chars = ["{", "}"]
            padding_chars = ("<", "^", ">")
            if len(title_add) < 3:
                raise Exception("There's not engough parameters or too many for title addition."
                                "\nThere are exaclty three, they must be in this order, and of these types:"
                                f"{usage_info}")
            elif len(title_add) == 3:
                if title_add[1] not in padding_chars:
                    raise Exception("Invalid alignment option. Valid alignment options are:"
                                    "\n\t\t<: Left aglignment. Inserts space to the left of the inserted text."
                                    "\n\t\t^: Center Alignment. Inserts space to the left and right"
                                    "\t\tof the inserted text."
                                    "\n\t\t>: Right alignment. Inserts space to the right of the inserted text.")
                else:
                    if title_add[0].isdigit():
                        idx_pos = title_add[0]
                    else:
                        if len(title_add[0]) == 1:
                            idx_pos = og_title.index(title_add[0])
                        else:
                            idx_pos = og_title.index(title_add[0]) + len(title_add[0])

                    alignment = title_add[1]
                    to_insert = title_add[2]

            if alignment == '^':
                form_syntax = list(f":{alignment}{len(to_insert)+2}")
                for e in reversed(form_syntax):
                    sub_chars.insert(1, e)
            else:
                form_syntax = list(f":{alignment}{len(to_insert)+1}")
                for e in reversed(form_syntax):
                    sub_chars.insert(1, e)

            story_title_list = list(og_title)

            for e in reversed(sub_chars):
                story_title_list.insert(int(idx_pos), e)

            story_title = ''.join(story_title_list).format(to_insert)
            return story_title
        else:
            return og_title


    base_url = url

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'}
    timeout = 5

    req = httpx.get(base_url, headers=headers, timeout=timeout)
    active_page = bs(req.text, 'lxml')
    story_title = active_page.find_all('li', class_='h_aW')[2].text
    story_title = title_legality(story_title)

    page_no = active_page.find_all('a', class_='l_bJ')[-1].text

    all_urls = []
    for n in range(1, int(page_no) + 1):
        if n == 1:
            all_urls.append(base_url)

        else:
            all_urls.append(base_url + '?page=' + str(n))

    async with httpx.AsyncClient() as client:
        tasks = (client.get(url, headers=headers, timeout=timeout) for url in all_urls)
        reqs = await asyncio.gather(*tasks)

    pages_texts = [bs(page.text, 'lxml').find('div', class_='aa_ht').prettify() for page in reqs]
    text_body = ''.join(pages_texts)

    story_title = string_insertion(story_title, prefix=prefix, suffix=suffix,
                                   custom_title=custom_title, title_add=title_add)

    with open(rf'{path}/{story_title}.html', 'w', encoding='utf-8') as f:
        f.write(text_body)



def main() -> None:
    usage_info = """
    \n
    [[index|string to seek][<|^|>][string]]
    \n
    \t\t Index or String: The index at which the text will be inserted. First character of the text is index 0.
    \t\tEverything originally at that index and after will be moved to the right.
    \t\tAlternatively, you can input a string, after which the text to be inserted
    \t\twill be placed. This is case sensitive.
    \n
    \t\t<: Left aglignment. Inserts space to the right of the inserted text.
    \t\t^: Center Alignment. Inserts space both to the left and right of the inserted text.
    \t\t>: Right alignment. Inserts space to the right of the inserted text.
    \n
    \t\tString: The text you wish to place.
    \n
    \t\tWARNING: All parameters must be INDIVIDUALLY enclosed in double quotation marks.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='URL of the story\'s first page.', type=str)
    parser.add_argument('path', help='Folder path to save the file.', type=str,
                        default=os.getcwd())
    parser.add_argument('-t', '--custom-title', help='Custom title for the story.', type=str)
    parser.add_argument('-p', '--prefix', help='Adds something to the beggining of the title.'
                        'Auto inputs space after.', type=str)
    parser.add_argument('-s', '--suffix', help='Adds something to the end of the title.'
                        'Auto inputs space before.', type=str)
    parser.add_argument('-ta', '--title-addition', nargs='+', type=int|str and str,
                        help=f"{usage_info}")

    args = parser.parse_args()
    asyncio.run(scrape_and_proc(args.url, args.path, args.custom_title, args.prefix,
                                args.suffix, args.title_addition))

if __name__ == '__main__':
    main()
