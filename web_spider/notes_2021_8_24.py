#**************************   Web Spider of python3  ********************************
#**************************   Date 2021.8.24         ********************************
#**************************   learnning URL          ********************************
#  https://mp.weixin.qq.com/s?__biz=MzIxODg1OTk1MA==&mid=2247484915&idx=1&sn=204b7b62d7411cda53623fa69a56aa91&scene=19#wechat_redirect
# 微信公众号：  Jack Cui



'''
网络爬虫的第一步就是根据 URL ，获取网页的 HTML 信息。在 Python3 中，可以使用 urllib.request 和 requests 进行网页爬取。
urllib 库是 Python 内置的，无需我们额外安装，只要安装了 Python 就可以使用这个库。
requests 库是第三方库，需要我们自己安装。
requests 库强大好用，后续文章的实例，也都是以此为基础进行讲解。requests 库的 github 地址：

https://github.com/requests/requests

1、requests 安装
在 cmd 中，使用如下指令安装 requests ：

pip install requests

或者：

easy_install requests

2、用法
官方教程地址：   http://docs.python-requests.org/zh_CN/latest/user/quickstart.html
'''


"""# -*- coding:UTF-8 -*-
import requests

if __name__ == '__main__':
    target = "http://fanyi.baidu.com/"
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    print(req.text)"""

#  2、爬虫其实很简单，可以大致分为三个步骤：

#     A、发起请求：我们需要先明确如何发起 HTTP 请求，获取到数据。
#     B、解析数据：获取到的数据乱七八糟的，我们需要提取出我们想要的数据。
#     C、保存数据：将我们想要的数据，保存下载。

#  发起请求，我们就用 requests 就行，上篇文章已经介绍过。

#  解析数据工具有很多，比如xpath、Beautiful Soup、正则表达式等。本文就用一个简单的经典小工具，Beautiful Soup来解析数据。

#  保存数据，就是常规的文本保存。

#  3、Beautiful Soup库  的安装

'''
简单来说，Beautiful Soup 是 Python 的一个第三方库，主要帮助我们解析网页数据。
在使用这个工具前，我们需要先安装，在 cmd 中，使用 pip 或 easy_install 安装即可。
'''
#      pip install beautifulsoup4
# 或者
#      easy_install beautifulsoup4
'''安装好后，我们还需要安装 lxml，这是解析 HTML 需要用到的依赖'''
#   pip install lxml

'''
Beautiful Soup 的使用方法也很简单，可以看下我在 CSDN 的讲解或者官方教程学习，详细的使用方法：
我的 Beautiful Soup 讲解：

https://blog.csdn.net/c406495762/article/details/71158264

官方中文教程：

https://beautifulsoup.readthedocs.io/zh_CN/latest/
'''





    

import requests
#  import time
#  from tqdm import tqdm
from bs4 import BeautifulSoup
"""
def get_content(target):
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'lxml')
    texts = bf.find('div', id='content')
    content = texts.text.strip().split('\xa0'*4)
    return content
"""
if __name__ == '__main__':
    server = 'https://www.imiaobige.com/'
    book_name = '西游，开局观音姐姐要和我打扑克.txt'
    target = 'https://www.imiaobige.com/read/293121/'
    req = requests.get(url = target)
    req.encoding = 'utf-8'
    html = req.text
    chapter_bs = BeautifulSoup(html, 'lxml')
    chapters = chapter_bs.find('div', id='readerlists')
    chapters = chapters.find_all('a')
    for chapter in tqdm(chapters):
        print(chapter)
        """
        chapter_name = chapter.string
        url = server + chapter.get('href')
        content = get_content(url)
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')
            """



