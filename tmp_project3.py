import requests
import pytest
# import tempfile
# from PIL import Image, ImageChops
from bs4 import BeautifulSoup
HEADERS = {
    'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        'AppleWebKit/537.36 (KHTML, like Gecko)'
        'Chrome/91.0.4472.101 Safari/537.36'
}

# url = 'http://vospitatel.com.ua/images/l/lopuh.jpg'


# def download_web_img(url):
#     response = requests.get(url, headers=HEADERS)
#     response.raise_for_status()
#     with open('img_web.jpg', 'wb') as file:
#         file.write(response.content)
#     return file

# def diff_img(img1, img2):
#     img1 = Image.open(img1)
#     img2 = Image.open(img2)
#     differences = ImageChops.difference(img1, img2)
#     if differences.getbbox():
#         print ('there are differences between the images')
#     print('ok!')

# # download_web_img(url)
# # img1 = 'img_web.jpg'
# # img2 = '../page_loader/data/vospitatel-com-ua-zaniatia-rastenia_files/vospitatel-com-ua-images-l.jpg'
# # diff_img(img1, img2)

# '''
# https://webtort.ru/%D0%BA%D0%B0%D0%BA-%D0%BD%D0%B0%D0%B9%D1%82%D0%B8-%D0%BE%D1%82%D0%BB%D0%B8%D1%87%D0%B8%D1%8F-%D0%BD%D0%B0-%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B0%D1%85-%D1%81-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89/
# '''


# def count_web_link(path):
#     tags_src = []
#     with open(path) as my_string:
#         soup = BeautifulSoup(my_string, "html.parser")
#         tags_img = soup.find_all('img', src=True)
#         for tag in tags_img:
#             src = tag.get('src')
#             if is_extension(src):
#                 tags_src.append(src)
#     return len(tags_src)

# path = 'tests/fixtures/web_page.html'
# count_web_link(path)

# @pytest.mark.parametrize(
#     'path, domain_name',
#     [
#         ('../page_loader/data/vospitatel-com-ua-zaniatia-rastenia_files/vospitatel-com-ua-zaniatia-rastenia.html', 'http://vospitatel.com.ua')
#     ]
# )
# def test_count_web_link(path, domain_name):
#     tags_src = []
#     soup = BeautifulSoup(path, "html.parser")
#     tags_img = soup.find_all('img', src=True)
#     for tag in tags_img:
#         src = tag.get('src')
#         if domain_name in src:
#             tags_src.append(src)
#     print('tags_src >>>> ', tags_src)


@pytest.mark.parametrize(
    'url',
    [
        ('http://oldmuzzle.ru/flora/taraxacum-officinale.html')
    ]
)
def test_page_loader(tmp_path, url):
    d = tmp_path / "sub"
    d.mkdir()
    file_temp = d / "tmp.html"
    content_text = requests.get(url, headers=HEADERS).text
    file_temp.write_text(content_text)
    soup1 = BeautifulSoup(file_temp.read_text(), "html.parser")
    soup2 = BeautifulSoup(content_text, "html.parser")
    assert soup1 == soup2
    # assert file_temp.read_text() == content_text


#     new_html = change_src(dir_temp, file_temp, domain_name)

#     with open(new_html) as fp:
#         string1 = fp.read()

#     with open(path_page_loader) as file:
#         string2 = file.read()

#     assert string1 == string2

# p = 'tests/fixtures/web_page.html'
# url = 'http://vospitatel.com.ua/zaniatia/rastenia/lopuh.html'
# domain_name = 'http://vospitatel.com.ua'


# tst_page_loader(p, url, domain_name)


# def get_text(url):
#     return requests.get(url, headers=HEADERS).text


  content_text = requests.get(url, headers=HEADERS).text
    file_temp.write_text(content_text)
    soup2 = BeautifulSoup(content_text, 'html.parser')
    with open(file_temp) as fp:
        soup1 = BeautifulSoup(fp, 'html.parser')
    assert soup1 == soup2
