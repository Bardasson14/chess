from .piece import Piece

class King(Piece):
    
    def __init__(self):
        super.spriteDir = 'assets/img/' + super.color + 'King.png'

    def getPossibleMoves(self, coord, matrix):
        pass