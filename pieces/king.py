from .piece import Piece

class King(Piece):
    
    def __init__(self, color, name):
        self.spriteDir = 'assets/img/' + color + 'King.png'
        self.name = name
        super(King,self).__init__(color,name)

    def getPossibleMoves(self, coord, matrix):
        self.possibleMoves=[]
        super().movD(1,coord,matrix,3,False)
        super().movH(1,coord,matrix)
        super().movV(1,coord,matrix,3)
        return self.possibleMoves