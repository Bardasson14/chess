class Piece:

    def __init__(self, color, name):
        self.wasMovedBefore = False
        self.possibleMoves = []
        self.spriteID = None
        self.name = name

    def getPossibleMoves(self, coord, matrix):
        pass

