class Knight (Piece):
    
    def __init__(self):
        super.spriteDir = 'assets/img/' + super.color + 'Knight.png'

    def getPossibleMoves(self, coord, matrix):
        pass