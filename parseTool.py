# How file works

# parse the data (potentially do this through pandas):
# put coordinates in one array, put Unicode characters in another array
# iterate through the length of either array, and place the Unicode character at the corresponding coordinates (both will have same index position)

# create a "board", where the width is the highest x-coordinate found in the Doc
# height will be the highest y-coordinate found

import pandas as pd

coords = []
chars = []


def parseDoc(url):
    print(url)
    fileContent = pd.read_html(url, encoding='utf-8')
    print(fileContent)
    return 1

print(parseDoc('https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'))


print('hi')

