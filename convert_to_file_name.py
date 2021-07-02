import re
from pathlib import Path
from pathlib import PurePosixPath
import os.path


def convert_to_file_name(path):
    if path.startswith('http'):
        _, path = re.split('://', path)
    return re.sub(r'[\W_]', '-', path)

# EXTENSION = {'html', 'jpeg', 'jpg', 'png', 'gif', 'svg', 'webp'}

# def convert_to_file_name(path):
#     if path.startswith('http'):
#         _, path = re.split('://', path)
#     suff = PurePosixPath(path).suffix
#     if suff in EXTENSION:
#         name = re.sub(r'[\W_]', '-', path) + suff
#     else:
#         name = re.sub(r'[\W_]', '-', path)
#     # ! разбивает путь на пару (root, ext), где ext начинается с точки
#     # ! и содержит не более одной точки
#     # >>  ru.hexlet.io/courses.html
#     # >> ru.hexlet.io/courses
#     # ! re.sub возвращает новую строку, полученную в результате замены
#     # ! по шаблону. Использовал регулярные выражения,
#     # ! https://proglib.io/p/regex-for-beginners/
#     return name
# >> ru-hexlet-io-courses or ru-hexlet-io-courses.html

# path = "/w/load.php?lang=en&amp;modules=ext.cite.styles%7Cext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cext.wikimediaBadges%7Cskins.vector.styles.legacy%7Cwikibase.client.init&amp;only=styles&amp;skin=vector"
path = 'https://linzi-vsem.ru/karnavalnye/linzy-sharingan/'
p = convert_to_file_name(path)
print(p)