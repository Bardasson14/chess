from string import ascii_lowercase

ALPHABETIC_COORDS = list(ascii_lowercase)[:8]

def convertCoord(coord):
    #returns respective row and col in matrix
    row = coord[1]
    col = ALPHABETIC_COORDS.index(coord[0])
    return row, col

def squareStatus(coord, matrix):
    # 0 -> Empty
    # 1 -> Filled
    row, col = convertCoord(coord)
    return (0 if not matrix[row][col].currentPiece else 1)