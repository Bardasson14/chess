import tkinter as tk
import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../src')

from pieces.special_moves import *
from pieces.pawn import Pawn
from game_state import *
from board import Board


class SpecialMovesTest(unittest.TestCase):

    def test_en_passant(self):

        board = Board(tk.Toplevel())
        pawn = Pawn('white', 'white_pawn_x')
        previous_dir = pawn.sprite_dir
        pawn.sprite_dir = os.path.dirname(os.path.realpath(__file__)) + '/../src/' + previous_dir
        # print(pawn.__dict__)
        board.add_piece(pawn, 3, 4)
        GameState.possible_en_passant = (3,4)
        special_moves = SpecialMoves()
        special_moves.en_passant(board) 
        self.assertIsNone(board.squares[(3,4)]['piece'])
