import tkinter as tk
import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../src/')
from board import Board
from pieces.pawn import Pawn


class BoardTest(unittest.TestCase):

    # Testes de Integração entre a interface e o módulo Board
    def test_add_piece(self): 
        board = Board(tk.Toplevel())
        pawn = Pawn('white', 'white_pawn_x')
        board.add_piece(pawn)
        self.assertIsNotNone(board.canvas.find_withtag(pawn.name))

    def test_capture_piece(self):
        board = Board(tk.Toplevel())
        p1 = Pawn('white', 'white_pawn_xxx')
        p2 = Pawn('black', 'black_pawn_xxx')
        board.squares[(2,2)]['piece'] = p1
        board.squares[(1,1)]['piece'] = p2

        if (1,1) in p2.get_possible_moves((2,2), board.squares):
            board.capture_piece((1,1)) # p2 captura p1
        
        self.assertEqual((), board.canvas.find_withtag(p2.name))