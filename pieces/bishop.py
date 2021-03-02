from .piece import Piece

class Bishop(Piece):
    
    def __init__(self, color, name):
        self.spriteDir = 'assets/img/' + color + 'Bishop.png'
        self.name = name
        super(Bishop,self).__init__(color,name)