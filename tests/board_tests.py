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

    def test_add_piece(self): # Teste de Integração entre a interface e o módulo Board
        board = Board(tk.Toplevel())
        pawn = Pawn('white', 'white_pawn_x')
        BoardTest.fix_sprite_dir(pawn)
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
        
        self.assertEqual((), board.canvas.find_withtag(p2.name)) # o nome de p2 foi removido do canvas

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

    @classmethod 
    def fix_sprite_dir(self, pawn):
        previous_dir = pawn.sprite_dir
        pawn.sprite_dir = os.path.dirname(os.path.realpath(__file__)) + '/../src/' + previous_dir
        
        
