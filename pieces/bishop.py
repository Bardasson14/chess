from .piece import Piece

class Bishop(Piece):
    
    def __init__(self, color):
        self.spriteDir = 'assets/img/' + color + 'Bishop.png'
