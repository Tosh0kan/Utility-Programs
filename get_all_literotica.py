import httpx
import asyncio
import argparse
from bs4 import BeautifulSoup as bs


class Arrays:
    forbidden_characters = (
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


async def scrape_and_proc():
    base_url = input("What's the story link? ")

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0'}
    timeout = 5

    req = httpx.get(base_url, headers=headers, timeout=timeout)
    active_page = bs(req.text, 'lxml')
    story_title = active_page.find_all('li', class_='h_aW')[2].text
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

    pages_texts = [bs(page.text, 'lxml').find('div', class_='panel article aa_eQ').prettify() for page in reqs]
    text_body = ''.join(pages_texts)

    return text_body, story_title

def title_legality(story_title: str):
    char_list = list(story_title)
    forbidden_indexes = []
    for e in char_list:
        if e in Arrays.forbidden_characters:
            forbidden_indexes.append(char_list.index(e))
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


def save_2_file(body, story_title: str):
    # folder_path = input("Folder path: ")
    with open(f'D:/01 Libraries/Documents/Igor Martinez/{story_title}.html', 'w', encoding='utf-8') as f:
        f.write(body)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='URL of the story\'s first page.', type=str)
    parser.add_argument('path', help='Folder path to save the file.', type=str)
    

if __name__ == '__main__':
    body, title = asyncio.run(scrape_and_proc())
    title = title_legality(title)
    save_2_file(body, title)
