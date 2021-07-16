import os
import os.path
import requests
from loader import get_file_name
HEADERS = {
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        'AppleWebKit/537.36 (KHTML, like Gecko)'
        'Chrome/91.0.4472.101 Safari/537.36'
}

def download_web_link(dir_to_download, url, domain_name, ext='html'):
    if url.startswith(domain_name):
        response = requests.get(url, headers=HEADERS)
        # !  # download the body of response by chunk, not immediately
        response.raise_for_status()
        file_name = get_file_name(url, ext)
        file_path = os.path.join(dir_to_download, file_name)
        with open(file_path, 'wb') as file:
            file.write(response.content)
    print(file_path)

download_web_link('tmp_data', 'https://linzi-vsem.ru/karnavalnye/linzy-sharingan/', 'https://linzi-vsem.ru')