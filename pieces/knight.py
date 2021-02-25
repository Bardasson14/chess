from .piece import Piece

class Knight(Piece):
    
    def __init__(self, color):
        self.spriteDir = 'assets/img/' + color + 'Knight.png'
