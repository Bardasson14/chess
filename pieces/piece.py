import sys
sys.path.append('/utils.py')
import utils

class Piece:

    def __init__(self, spriteDir, color):
        self.spriteDir = spriteDir
        self.color = color
        self.possibleMoves = []

    def getPossibleMoves(self, currentPosition):
        pass

