from .piece import Piece

class Pawn(Piece):
    
    def __init__(self, color, name):
        self.spriteDir = 'assets/img/' + color + 'Pawn.png'
        self.name = name