from .piece import Piece

class Rook(Piece):
    
    def __init__(self, color, name):
        self.spriteDir = 'assets/img/' + color + 'Rook.png'
        self.name = name
        super(Rook,self).__init__(color,name)