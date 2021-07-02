from urllib.parse import urlparse

# o = urlparse('//upload.wikimedia.org')


# # def get_web_text(url, ext='html', path='page_loader/tmp'):  # use response.text
# #     response = requests.get(url, headers=HEADERS)
# #     response.raise_for_status()
# #     page_name = convert_path_name(url) + '.' + ext
# #     file_path = os.path.join(path, page_name)
# #     domain_name = urlparse(url).scheme + "://" + urlparse(url).netloc
# #     with open(file_path, 'w') as file:
# #         file.write(response.text)
# #     return file_path, domain_name

# print(o.netloc)

def netlock_(url):
    domain_name = urlparse(url).netloc
    print(domain_name)

url = 'https://en.wikipedia.org/wiki/Correction_fluid'
# url = 'www.en.wikipedia.org/wiki/Correction_fluid'
netlock_(url)