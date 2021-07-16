import os
import os.path
import requests
import re
from pathlib import PurePosixPath, Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from loader import *

def get_web_content(url, ext='html', path='tmp_data'):
    # use response.content
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    # dir_path = create_dir_from_web(path, url)
    page_name = get_file_name(url, ext)

    file_path = os.path.join(path, page_name)
    # domain_name = urlparse(url).scheme + "://" + urlparse(url).netloc
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print('get_web_content(url, ext="html", path) -> ', file_path)
    print()
    return file_path

url = 'https://httpbin.org'
get_web_content(url, ext='html', path='tmp_data')