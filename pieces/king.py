from .piece import Piece

class King(Piece):
    
    def __init__(self, color):
        self.spriteDir = 'assets/img/' + color + 'King.png'
