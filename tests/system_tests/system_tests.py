import tkinter as tk
import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../../src')

from board import Board

class SystemTest(unittest.TestCase):

    # Testa se o reset do jogo no modo IA cria o objeto necessário
    def test_board_reset(self):
        board = Board(tk.Toplevel())
        board.clear()
        board.mode("black")
        self.assertNotEqual(board.ai, None)