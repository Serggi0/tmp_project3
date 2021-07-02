from convert_to_file_name import convert_to_file_name

def add_extension(path, ext):
    file_name = convert_to_file_name(path) + '.' + ext
    print(file_name)
    return file_name

path = "/w/load.php?lang=en&amp;modules=ext.cite.styles%7Cext.uls.interlanguage%7Cext.visualEditor.desktopArticleTarget.noscript%7Cext.wikimediaBadges%7Cskins.vector.styles.legacy%7Cwikibase.client.init&amp;only=styles&amp;skin=vector"
# path = 'https://linzi-vsem.ru/karnavalnye/linzy-sharingan/'

add_extension(path, 'html')