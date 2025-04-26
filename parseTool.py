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
    fileContent = pd.read_html(url, encoding='utf-8', header=0)

    for index, row in fileContent[0].iterrows():
        coords.append([row[0], row[2]])
        chars.append(row[1])

    # find boundaries of the grid:
    bigX = max(point[0] for point in coords)
    bigY = max(point[1] for point in coords)

    grid = generateGrid()
    print('coords:', coords, ' chars:', chars)    


    print('Here are items 3-5', fileContent[0].iloc[2:5])
    return 'done'


def handleRow(row):
    print('handeling')


def generateGrid(bigX, bigY):
    print('x-bound:', bigX, 'y-bound:', bigY)
    # create grid here
    return grid

print(parseDoc('https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub'))



