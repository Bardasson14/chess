from .piece import Piece

class Queen(Piece):
    
    def __init__(self, color):
        self.spriteDir = 'assets/img/' + color + 'Queen.png'