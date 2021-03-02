from .piece import Piece

class Queen(Piece):
    
    def __init__(self, color, name):
        self.spriteDir = 'assets/img/' + color + 'Queen.png'
        self.name = name
        super(Queen,self).__init__(color,name)