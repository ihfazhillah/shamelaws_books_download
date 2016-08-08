#-*- coding:utf-8 -*-
import requests
import csv
from bs4 import BeautifulSoup
from requests.compat import urljoin


def find_bok_link(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'lxml')
    bok_img = soup.select('div > a > img[src*="files/img/front/bok.png"]')
    bok_url = bok_img[0].parent['href']
    return urljoin(url, bok_url)


def find_books_in_page(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'lxml')
    books_in_page = soup.select('td.regular-book > a')
    return [x for x in books_in_page if x.text]

def find_next_page(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.content, 'lxml')
    next_page = soup.find('a', text='التالي')
    return next_page['href']

def build_urls(url, from_page, to_page):
    urls = [urljoin(url, 'page-%s' %(x)) for x in range(from_page, to_page + 1)]
    return urls

def get_all_bok_link(url, fpath, from_page=1, to_page=3):
    """Dapatkan semua bok file dari url yang diberikan, dan simpan ke
    file dengan fpath path , from page default 1, to_page default 3"""

    urls = build_urls(url, from_page, to_page)
    with open(fpath, 'w') as f:
        books_url_writer = csv.writer(f, delimiter=',', quotechar='|')
        books_url_writer.writerow(['3nwan', 'url'])
        for url in urls:
            for x in find_books_in_page(url):
                books_url_writer.writerow([x.text, urljoin(url, x['href'])])
            # books = [(urljoin(url, x['href']), x.text)
            #          for x in find_books_in_page(url)]
            # books_url += books




# print(find_bok_link("http://shamela.ws/index.php/book/17874"))
# print(find_books_in_page("http://shamela.ws/index.php/tag/%D9%83%D8%AA%D8%A8+%D8%A3%D8%AF%D8%AE%D9%84%D9%87%D8%A7+%D9%85%D9%88%D9%82%D8%B9+%D8%A7%D9%84%D8%B4%D8%A7%D9%85%D9%84%D8%A9"))
# print(urljoin('http://shamela.ws', find_next_page('http://shamela.ws/rep.php/search/last/page-1')))
# build_urls('http://shamela.ws/rep.php/search/last', 3, 52)
# print(get_all_bok_file('http://shamela.ws/rep.php/search/last/', 'coba'))
