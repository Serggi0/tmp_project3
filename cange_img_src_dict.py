import os.path
import re
from pathlib import PurePosixPath
from sys import path
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


def convert_url_with_domain_name(url, domain_name):
    if url.startswith(domain_name):
        _, url = re.split('://', url)
        return re.sub(r'[\W_]', '-', url)
    else:
        return url


def convert_relativ_link(link, domain_name):
    if link.startswith('//', 0, 2):
        return link
    else:
        return urljoin(domain_name, link)


def change_tags(dir_to_download, file_path, domain_name):
    dict_all = {}
    list_all = []
    with open(file_path) as f:
        data = f.read()
        soup = BeautifulSoup(data, "html.parser")

    tags_img = soup.find_all('img', src=True)
    tags_script = soup.find_all('script', src=True)
    tags_link = soup.find_all('link', href=True)

    for tag in tags_img:
        img_src = tag['src']
        list_all.append(img_src)
    for tag in tags_script:
        script_src = tag['src']
        list_all.append(script_src)
    for tag in tags_link:
        link_href = tag['href']
        list_all.append(link_href)

    for i in list_all:
        dict_all[i] = convert_relativ_link(i, domain_name)

    for k, v in dict_all.items():
        dict_all[k] = download_web_link(dir_to_download, v)
        
        # convert_url_with_domain_name(v, domain_name)

    # print(dict_all)

    for tag in tags_img:
        if tag['src'] in dict_all.keys():
            tag['src'] = dict_all[tag['src']]

    for tag in tags_script:
        if tag['src'] in dict_all.keys():
            tag['src'] = dict_all[tag['src']]
    
    for tag in tags_link:
        if tag['href'] in dict_all.keys():
            tag['href'] = dict_all[tag['href']]

    # print(soup.prettify(formatter='html5'))
    new_html = soup.prettify(formatter='html5')
    with open(file_path, 'w') as file:
        file.write(new_html)
    return file_path




file_path = 'fixtures/web_page.html'
domain_name = 'http://vospitatel.com.ua'
# change_img_src(file_path, domain_name)
# change_tags(file_path, domain_name)
link = './vospitatel.com.ua/assets/application.css'
print(convert_relativ_link(link, domain_name))


        # img_src = tag.get('src')
        # suff = PurePosixPath(img_src).suffix
        # if suff in EXTENSION_IMG:
        #     if domain_name in img_src:
        #         tag['src'] = '0000'
        #     elif urlparse(domain_name).netloc in img_src:
        #         tag['src'] = urljoin(domain_name, img_src)
            
        #     img_src_new = tag['src']
        #     list_tags_img_src.append(img_src_new)\