import tkinter as tk
import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../src')
from board import Board
from pieces.pawn import Pawn

class BoardTest(unittest.TestCase):
    
    def test_populate_grid(self):
        board = Board(tk.Tk())
        board.populate_grid()
        self.assertNotEqual(board.squares, {})

    def test_add_piece(self): # Teste de Integração entre a interface e o módulo Board
        board = Board(tk.Tk())
        pawn = Pawn('white', 'white_pawn_x')
        previous_dir = pawn.sprite_dir
        pawn.sprite_dir = os.path.dirname(os.path.realpath(__file__)) + '/../src/' + previous_dir
        board.add_piece(pawn)
        self.assertIsNotNone(board.canvas.find_withtag(pawn.name))

    def test_capture_piece(self):
        board = Board(tk.Tk())
        p1 = Pawn('white', 'white_pawn_xxx')
        p2 = Pawn('black', 'black_pawn_xxx')
        board.squares[(2,2)]['piece'] = p1
        board.squares[(1,1)]['piece'] = p2

        if (1,1) in p2.get_possible_moves((2,2), board.squares):
            board.capture_piece((1,1)) # p2 captura p1
        
        self.assertEqual((), board.canvas.find_withtag(p2.name)) # o nome de p2 foi removido do canvas