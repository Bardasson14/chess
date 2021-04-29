import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../src')

from board import Board
from pieces.bishop import Bishop
from pieces.king import King
from pieces.knight import Knight
from pieces.pawn import Pawn
from pieces.queen import Queen
from pieces.rook import Rook


# Os testes são realizados considerando tabuleiros vazios

class PieceTest(unittest.TestCase):

    def test_bishop_get_possible_moves(self):
        matrix = PieceTest.initialize_empty_grid()
        bishop = Bishop('white', 'white_bishop_1')
        positions = [(0,0), (0,7), (3,4), (7,0), (7,7)]
        expectations = {
            (0,0): [(i,i,'mov') for i in range(1,8)],
            (0,7): [(i,7-i,'mov') for i in range(1,8)], 
            (3,4): [(2, 3, 'mov'), (1, 2, 'mov'), (0, 1, 'mov'), (2, 5, 'mov'), (1, 6, 'mov'), (0, 7, 'mov'), (4, 3, 'mov'), (5, 2, 'mov'), (6, 1, 'mov'), (7, 0, 'mov'), (4, 5, 'mov'), (5, 6, 'mov'), (6, 7, 'mov')], 
            (7,0): [(i,7-i,'mov') for i in range(0,7)], 
            (7,7): [(i,i,'mov') for i in range(0,7)],
        }

        for pos in positions:
            possible_moves = bishop.get_possible_moves(pos, matrix)
            self.assertCountEqual(possible_moves, expectations[pos])

    def test_king_get_possible_moves(self):
        matrix = PieceTest.initialize_empty_grid()
        king = King('white', 'white_king')
        positions = [(0,0), (0,7), (3,4), (7,0), (7,7)]
        expectations = {
            (0,0): [(1, 1, 'mov'), (1, 0, 'mov'), (1, 0, 'mov'), (0, 1, 'mov')],
            (0,7): [(1, 6, 'mov'), (1, 7, 'mov'), (1, 7, 'mov'), (0, 6, 'mov')],
            (3,4): [(2, 5, 'mov'), (2, 3, 'mov'), (4, 5, 'mov'), (4, 3, 'mov'), (2, 4, 'mov'), (4, 4, 'mov'), (4, 4, 'mov'), (3, 5, 'mov'), (3, 3, 'mov')],
            (7,0): [(6, 1, 'mov'), (6, 0, 'mov'), (7, 1, 'mov')],
            (7,7): [(6, 6, 'mov'), (6, 7, 'mov'), (7, 6, 'mov')]
        }

        for pos in positions:
            possible_moves = king.get_possible_moves(pos, matrix)
            self.assertCountEqual(possible_moves, expectations[pos])

    def test_knight_get_possible_moves(self):
        matrix = PieceTest.initialize_empty_grid()
        knight = Knight('white', 'white_knight_1')
        positions = [(0,0), (0,7), (3,4), (7,0), (7,7)]
        expectations = {
            (0,0): [(2, 1, 'mov'), (1, 2, 'mov')],
            (0,7): [(2, 6, 'mov'), (1, 5, 'mov')],
            (3,4): [(1, 3, 'mov'), (2, 2, 'mov'), (1, 5, 'mov'), (2, 6, 'mov'), (5, 3, 'mov'), (4, 2, 'mov'), (5, 5, 'mov'), (4, 6, 'mov')],
            (7,0): [(5, 1, 'mov'), (6, 2, 'mov')],
            (7,7): [(5, 6, 'mov'), (6, 5, 'mov')]
        }

        for pos in positions:
            possible_moves = knight.get_possible_moves(pos, matrix)
            self.assertCountEqual(possible_moves, expectations[pos])

    def test_pawn_get_possible_moves(self):
        matrix = PieceTest.initialize_empty_grid()
        pawn = Pawn('black', 'black_pawn_1')
        positions = [(1,0), (1,7), (6,0), (6,7)]
        expectations = {
            (1, 0): [(2, 0, 'mov'), (3, 0, 'mov')],
            (1, 7): [(2, 7, 'mov'), (3, 7, 'mov')],
            (6, 0): [(7, 0, 'mov')],
            (6, 7): [(7, 7, 'mov')]
        }
        
        for pos in positions:
            possible_moves = pawn.get_possible_moves(pos, matrix)
            self.assertCountEqual(list(set(possible_moves)), expectations[pos])

    def test_queen_get_possible_moves(self):
        matrix = PieceTest.initialize_empty_grid()
        queen = Queen('black', 'black_queen')
        positions = [(0,0), (0,7), (3,4), (7,0), (7,7)]

        expectations = {
            (0,0): [(0, 1, 'mov'), (0, 2, 'mov'), (0, 3, 'mov'), (0, 4, 'mov'), (0, 5, 'mov'), (0, 6, 'mov'), (0, 7, 'mov'), (1, 0, 'mov'), (2, 0, 'mov'), (3, 0, 'mov'), (4, 0, 'mov'), (5, 0, 'mov'), (6, 0, 'mov'), (7, 0, 'mov'), (1, 1, 'mov'), (2, 2, 'mov'), (3, 3, 'mov'), (4, 4, 'mov'), (5, 5, 'mov'), (6, 6, 'mov'), (7, 7, 'mov')],
            (0,7): [(0, 6, 'mov'), (0, 5, 'mov'), (0, 4, 'mov'), (0, 3, 'mov'), (0, 2, 'mov'), (0, 1, 'mov'), (0, 0, 'mov'), (1, 7, 'mov'), (2, 7, 'mov'), (3, 7, 'mov'), (4, 7, 'mov'), (5, 7, 'mov'), (6, 7, 'mov'), (7, 7, 'mov'), (1, 6, 'mov'), (2, 5, 'mov'), (3, 4, 'mov'), (4, 3, 'mov'), (5, 2, 'mov'), (6, 1, 'mov'), (7, 0, 'mov')],
            (3,4): [(3, 3, 'mov'), (3, 2, 'mov'), (3, 1, 'mov'), (3, 0, 'mov'), (3, 5, 'mov'), (3, 6, 'mov'), (3, 7, 'mov'), (2, 4, 'mov'), (1, 4, 'mov'), (0, 4, 'mov'), (4, 4, 'mov'), (5, 4, 'mov'), (6, 4, 'mov'), (7, 4, 'mov'), (2, 3, 'mov'), (1, 2, 'mov'), (0, 1, 'mov'), (2, 5, 'mov'), (1, 6, 'mov'), (0, 7, 'mov'), (4, 3, 'mov'), (5, 2, 'mov'), (6, 1, 'mov'), (7, 0, 'mov'), (4, 5, 'mov'), (5, 6, 'mov'), (6, 7, 'mov')],
            (7,0): [(7, 1, 'mov'), (7, 2, 'mov'), (7, 3, 'mov'), (7, 4, 'mov'), (7, 5, 'mov'), (7, 6, 'mov'), (7, 7, 'mov'), (6, 0, 'mov'), (5, 0, 'mov'), (4, 0, 'mov'), (3, 0, 'mov'), (2, 0, 'mov'), (1, 0, 'mov'), (0, 0, 'mov'), (6, 1, 'mov'), (5, 2, 'mov'), (4, 3, 'mov'), (3, 4, 'mov'), (2, 5, 'mov'), (1, 6, 'mov'), (0, 7, 'mov')],
            (7,7): [(7, 6, 'mov'), (7, 5, 'mov'), (7, 4, 'mov'), (7, 3, 'mov'), (7, 2, 'mov'), (7, 1, 'mov'), (7, 0, 'mov'), (6, 7, 'mov'), (5, 7, 'mov'), (4, 7, 'mov'), (3, 7, 'mov'), (2, 7, 'mov'), (1, 7, 'mov'), (0, 7, 'mov'), (6, 6, 'mov'), (5, 5, 'mov'), (4, 4, 'mov'), (3, 3, 'mov'), (2, 2, 'mov'), (1, 1, 'mov'), (0, 0, 'mov')]
        }

        for pos in positions:
            possible_moves = queen.get_possible_moves(pos, matrix)
            self.assertCountEqual(possible_moves, expectations[pos])

    def test_rook_get_possible_moves(self):
        matrix = PieceTest.initialize_empty_grid()
        rook = Rook('black', 'black_rook_1')
        positions = [(0,0), (0,7), (3,4), (7,0), (7,7)]

        expectations = {
            (0,0): [(0, 1, 'mov'), (0, 2, 'mov'), (0, 3, 'mov'), (0, 4, 'mov'), (0, 5, 'mov'), (0, 6, 'mov'), (0, 7, 'mov'), (1, 0, 'mov'), (2, 0, 'mov'), (3, 0, 'mov'), (4, 0, 'mov'), (5, 0, 'mov'), (6, 0, 'mov'), (7, 0, 'mov')],
            (0,7): [(0, 6, 'mov'), (0, 5, 'mov'), (0, 4, 'mov'), (0, 3, 'mov'), (0, 2, 'mov'), (0, 1, 'mov'), (0, 0, 'mov'), (1, 7, 'mov'), (2, 7, 'mov'), (3, 7, 'mov'), (4, 7, 'mov'), (5, 7, 'mov'), (6, 7, 'mov'), (7, 7, 'mov')], 
            (3,4): [(3, 3, 'mov'), (3, 2, 'mov'), (3, 1, 'mov'), (3, 0, 'mov'), (3, 5, 'mov'), (3, 6, 'mov'), (3, 7, 'mov'), (2, 4, 'mov'), (1, 4, 'mov'), (0, 4, 'mov'), (4, 4, 'mov'), (5, 4, 'mov'), (6, 4, 'mov'), (7, 4, 'mov')], 
            (7,0): [(7, 1, 'mov'), (7, 2, 'mov'), (7, 3, 'mov'), (7, 4, 'mov'), (7, 5, 'mov'), (7, 6, 'mov'), (7, 7, 'mov'), (6, 0, 'mov'), (5, 0, 'mov'), (4, 0, 'mov'), (3, 0, 'mov'), (2, 0, 'mov'), (1, 0, 'mov'), (0, 0, 'mov')], 
            (7,7): [(7, 6, 'mov'), (7, 5, 'mov'), (7, 4, 'mov'), (7, 3, 'mov'), (7, 2, 'mov'), (7, 1, 'mov'), (7, 0, 'mov'), (6, 7, 'mov'), (5, 7, 'mov'), (4, 7, 'mov'), (3, 7, 'mov'), (2, 7, 'mov'), (1, 7, 'mov'), (0, 7, 'mov')]
        }

        for pos in positions:
            possible_moves = rook.get_possible_moves(pos, matrix)
            self.assertCountEqual(possible_moves, expectations[pos])

    @classmethod
    def initialize_empty_grid(self):
        squares = {}

        for i in range(8):
            for j in range(8):
                square_info = {'piece': None, 'coord':(i, j), 'selected':None, 'gamerule':None}
                squares[(i,j)] = square_info

        return squares