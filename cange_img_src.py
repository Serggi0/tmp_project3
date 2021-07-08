import os
import os.path
from pathlib import PurePosixPath
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse


HEADERS = {
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        'AppleWebKit/537.36 (KHTML, like Gecko)'
        'Chrome/91.0.4472.101 Safari/537.36'
}

EXTENSION_IMG = {'.html', '.jpeg', '.jpg', '.png', '.gif', '.svg', '.webp'}


def change_img_src(file_path, domain_name):
    file = open(file_path, 'r')
    html = file.read()
    soup = BeautifulSoup(html, "html.parser")
    file.close
    list_tags_img_src = []
    list_tags_new_img_src = []
    tags_img = soup.find_all('img', src=True)
    for tag in tags_img:
        img_src = tag.get('src')
        suff = PurePosixPath(img_src).suffix
        if suff in EXTENSION_IMG:
            if domain_name in img_src:
                tag['src'] = '0000'
            elif urlparse(domain_name).netloc in img_src:
                tag['src'] = urljoin(domain_name, img_src)
            
            img_src_new = tag['src']
            list_tags_img_src.append(img_src_new)
            tag['src'] = '!!!!!_download_web_link'
            list_tags_new_img_src.append(tag['src'])
    print(list_tags_img_src)
    print(list_tags_new_img_src)
    print(soup.prettify(formatter='html5'))

file_path = 'fixtures/web_page.html'
domain_name = 'http://vospitatel.com.ua'
change_img_src(file_path, domain_name)