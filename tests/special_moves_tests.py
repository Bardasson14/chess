import tkinter as tk
import unittest
from unittest.mock import Mock
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../src')

from pieces.special_moves import *
from pieces.pawn import Pawn
from game_state import *
from board import Board
from helpers import *


class SpecialMovesTest(unittest.TestCase):

    def test_en_passant(self):
        board = Board(tk.Toplevel())
        special_moves = SpecialMoves()
        pawn = Pawn('white', 'white_pawn_x')
        board[(3,4)]['piece'] = pawn
        GameState.possible_en_passant = (3,4)
        special_moves.en_passant(board) 
        self.assertIsNone(board.squares[(3,4)]['piece'])
