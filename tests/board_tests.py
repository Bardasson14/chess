import tkinter as tk
import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../src')
from board import Board
from pieces.pawn import Pawn
from pieces.bishop import Bishop
from pieces.king import King
from game_state import *

class BoardTest(unittest.TestCase):
    
    def test_populate_grid(self):
        board = Board(tk.Tk())
        board.populate_grid()
        self.assertNotEqual(board.squares, {})

    
    def test_board_lock(self):
        board = Board(tk.Toplevel())
        b = Bishop('white', 'white_bishop_1')
        board.handle_board_lock(b, 0, 0)
        self.assertTrue(board.lock)
        b.selected = True
        board.lock = True
        board.handle_board_lock(b, 0, 0)
        self.assertFalse(board.lock)

    '''
    def test_handle_piece_movimentation(self):
        board = Board(tk.Toplevel())
        k = King('black', 'black_king')
        BoardTest.fix_sprite_dir(k)
        board.add_piece(k, 0, 4)
        k.selected = True
        board.handle_piece_movimentation(k, 0, 4, (0,3))
        self.assertEqual(GameState.blackcoord, (0, 3))  
    '''
