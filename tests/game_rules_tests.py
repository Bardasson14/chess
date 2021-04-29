import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../src')
from game_rules import *
from pieces.king import King
from pieces.pawn import Pawn

class GameRulesTest(unittest.TestCase):

    def test_king_checked(self):
        matrix = self.initialize_empty_grid()
        matrix[(1,1)]['piece'] = Pawn('white', 'white_pawn_1')
        matrix[(0,0)]['piece'] = King('black', 'black_king')
        self.assertTrue(check_all(matrix, (0,0), 'black'))

    @classmethod
    def initialize_empty_grid(self):
        squares = {}

        for i in range(8):
            for j in range(8):
                square_info = {'piece': None, 'coord':(i, j), 'selected':None, 'gamerule':None}
                squares[(i,j)] = square_info

        return squares

    