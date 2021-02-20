class King (Piece):
    
    def __init__(self):
        super.spriteDir = 'assets/img/' + super.color + 'Rook.png'

    def getPossibleMoves(self, coord, matrix):
        pass