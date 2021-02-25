from string import ascii_lowercase

ALPHABETIC_COORDS = list(ascii_lowercase)[:8]

def convertCoord(originalRow, originalCol):
    row = 8 - originalRow
    col = ALPHABETIC_COORDS[originalCol]
    return str(row) + col