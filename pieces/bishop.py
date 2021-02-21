from .piece import Piece

class Bishop(Piece):
    
    def __init__(self):
        super.spriteDir = 'assets/img/' + super.color + 'Bishop.png'

    '''
    def getPossibleMoves(self, coord, matrix):
        #returns an array of coords
        possibleMoves = [] # filled squares are added as well
        currentRow, currentCol = convertCoord(coord)

        for i in range(9):
            for j in range(9):
                if ((abs(i-currentRow) == abs(j-currentCol)) > 0):
                    possibleMoves.append(matrix[i][j].coord) 

        return possibleMoves
        '''
