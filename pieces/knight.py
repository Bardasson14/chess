from .piece import Piece

class Knight(Piece):
    
    def __init__(self, color, name):
        self.spriteDir = 'assets/img/' + color + 'Knight.png'
        self.name = name
        super(Knight,self).__init__(color,name)