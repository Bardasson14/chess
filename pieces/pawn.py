from .piece import Piece

class Pawn(Piece):
    
    def __init__(self, color):
        self.spriteDir = 'assets/img/' + color + 'Pawn.png'