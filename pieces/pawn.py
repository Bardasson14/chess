from .piece import Piece

class Pawn(Piece):
    
    def __init__(self, color, name):
        self.spriteDir = 'assets/img/' + color + 'Pawn.png'
        self.name = name
        self.color=color
        super(Pawn,self).__init__(color,name)
    
    def getPossibleMoves(self, coord, matrix):
        self.possibleMoves=[]
        if(self.color=='white'):
            if(self.wasMovedBefore):
                super().movD(1,coord,matrix,1,True)
                super().movV(1,coord,matrix,1)
            else:
                super().movD(1,coord,matrix,1,True)
                super().movV(2,coord,matrix,1)
        else:
            if(self.wasMovedBefore):
                super().movD(1,coord,matrix,2,True)
                super().movV(1,coord,matrix,2)
            else:
                super().movD(1,coord,matrix,2,True)
                super().movV(2,coord,matrix,2)
        return self.possibleMoves