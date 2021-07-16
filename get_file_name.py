import os
import os.path
import requests
import re
from pathlib import PurePosixPath, Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from loader import *

def get_file_name(path, ext):
    if is_extension(path):
        part, suff = os.path.splitext(path)
        if suff == 'html':
            print('suff ', suff)
            name = convert_path_name(part) + suff
            print('name0', name)
        else:
            name = convert_path_name(path) + '.html'
            print('name1', name)
    else:
        name = convert_path_name(path) + '.' + ext
        print('name2' , name)
    print('get_file_name(path, ext="html") ->', name)
    print()
    return name

path = 'https://httpbin.co'
ext = 'html'
get_file_name(path, ext)