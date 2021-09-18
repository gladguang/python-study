import requests
import time
from tqdm import tqdm
from bs4 import BeautifulSoup

wangzhan = input('请输入网址:')
shuming = input('请输入书名：')
muluulr = input('请输入书名ulr：')


def get_content(target):
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'lxml')
    texts = bf.find('div', id='content')
    content = texts.text.strip().split('\xa0'*4)
    return content

if __name__ == '__main__':
    server = wangzhan
    book_name = shuming + '.txt'
    target = muluulr
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    chapter_bs = BeautifulSoup(html, 'lxml')
    chapters = chapter_bs.find('div', id='readerlists')
    chapters = chapters.find_all('a')
    for chapter in tqdm(chapters):
        chapter_name = chapter.string
        url = server + chapter.get('href')
        content = get_content(url)
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')