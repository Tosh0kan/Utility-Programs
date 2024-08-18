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

    if custom_title is not None:
        story_title = custom_title
    else:
        pass

    if prefix is not None:
        story_title = prefix + ' ' + story_title
    elif suffix is not None:
        story_title = story_title + ' ' + suffix
    elif prefix is not None and suffix is not None:
        story_title = prefix + ' ' + story_title + ' ' + suffix
    elif title_add is not None:
        sub_chars = ["}", "{"]
        story_title_list = list(story_title)

        for e in sub_chars:
            story_title_list.insert(int(title_add[0]), e)

        procced_title_add = ''.join(story_title_list)
        story_title = procced_title_add.format(' ' + title_add[1] + ' ')
    else:
        pass

    with open(rf'{path}/{story_title}.html', 'w', encoding='utf-8') as f:
        f.write(text_body)



def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='URL of the story\'s first page.', type=str)
    parser.add_argument('path', help='Folder path to save the file.', type=str)
    parser.add_argument('-t', '--custom-title', help='Custom title for the story.', type=str)
    parser.add_argument('-p', '--prefix', help='Adds something to the beggining of the title.'
                        'Auto inputs space after.', type=str)
    parser.add_argument('-s', '--suffix', help='Adds something to the end of the title.'
                        'Auto inputs space before.', type=str)
    parser.add_argument('-ta', '--title-add', nargs='+', type=int and str,
                        help="Add a string to the title at a specific position. "
                        "The character at that position originally will be moved to the right.")

    args = parser.parse_args()
    asyncio.run(scrape_and_proc(args.url, args.path, args.custom_title, args.prefix,
                                args.suffix, args.title_add))

if __name__ == '__main__':
    main()
