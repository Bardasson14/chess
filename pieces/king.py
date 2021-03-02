from .piece import Piece

class King(Piece):
    
    def __init__(self, color, name):
        self.spriteDir = 'assets/img/' + color + 'King.png'
        self.name = name
        super(King,self).__init__(color,name)