from .piece import Piece

class Rook(Piece):
    
    def __init__(self, color):
        self.spriteDir = 'assets/img/' + color + 'Rook.png'