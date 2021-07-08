import os.path
import re
from pathlib import PurePosixPath
from bs4 import BeautifulSoup
from collections import defaultdict
from urllib.parse import urljoin, urlparse



HEADERS = {
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        'AppleWebKit/537.36 (KHTML, like Gecko)'
        'Chrome/91.0.4472.101 Safari/537.36'
}

EXTENSION_IMG = {'.html', '.jpeg', '.jpg', '.png', '.gif', '.svg', '.webp'}


def convert_path_name(path):
    if path.startswith('http'):
        _, path = re.split('://', path)
    return re.sub(r'[\W_]', '-', path)


def convert_relativ_link(path, domain_name):
    if domain_name not in path:
        if path.startswith('//', 0, 2) is False:
            return urljoin(domain_name, path)
        else:
            path = path
    return path


def change_img_src(file_path, domain_name, new_html_path='fixtures/new_web_page.html'):
    dict_all = {}
    list_all = []
    file = open(file_path, 'r')
    html = file.read()
    soup = BeautifulSoup(html, "html.parser")
    file.close
    tags_img = soup.find_all('img', src=True)
    tags_script = soup.find_all('script', src=True)
    for tag in tags_img:
        img_src_old = tag['src']
        list_all.append(img_src_old)
    for tag in tags_script:
        script_src_old = tag['src']
        list_all.append(script_src_old)
    print(list_all)
    print()

    for i in list_all:
        dict_all[i] = convert_relativ_link(i, domain_name)
    print(dict_all)

    for tag in tags_img:
        if tag['src'] in dict_all.keys():
            tag['src'] = dict_all[tag['src']]

    for tag in tags_script:
        if tag['src'] in dict_all.keys():
            tag['src'] = dict_all[tag['src']]

        # dict_all[img_src_old] = 'IMG'
        # tag['src'] = '!!!!!_download_web_link'
    # print(list_tags_img_src)
    # print(list_tags_new_img_src)
    # new_html = soup.prettify(formatter='html5')
    print(soup.prettify(formatter='html5'))
    # with open(new_html_path, 'w') as file:
    #     file.write(new_html)
    # return new_html_path


file_path = 'fixtures/web_page.html'
domain_name = 'http://vospitatel.com.ua'
change_img_src(file_path, domain_name)


        # img_src = tag.get('src')
        # suff = PurePosixPath(img_src).suffix
        # if suff in EXTENSION_IMG:
        #     if domain_name in img_src:
        #         tag['src'] = '0000'
        #     elif urlparse(domain_name).netloc in img_src:
        #         tag['src'] = urljoin(domain_name, img_src)
            
        #     img_src_new = tag['src']
        #     list_tags_img_src.append(img_src_new)