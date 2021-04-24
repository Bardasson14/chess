import tkinter as tk
import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../src')

from board import Board
from timer import Countdown
from pieces.pawn import Pawn


class GUITest(unittest.TestCase):

    def test_add_piece(self):
        board = Board(tk.Tk())
        pawn = Pawn('white', 'white_pawn_x')
        previous_dir = pawn.sprite_dir
        pawn.sprite_dir = os.path.dirname(os.path.realpath(__file__)) + '/../src/' + previous_dir
        board.add_piece(pawn)
        self.assertIsNotNone(board.canvas.find_withtag(pawn.name))

    def test_capture_piece(self):
        pass

    def test_click_is_valid(self):
        pass

    def test_populate_grid(self):
        board = Board(tk.Tk())
        board.populate_grid()
        self.assertNotEqual(board.squares, {})

    def test_start_timer(self):
        root = tk.Tk()
        test_timer = Countdown(tk.LabelFrame(root, text="test", height = 0, width = 0))
        test_timer.pack()
        test_timer.start_timer()
        self.assertTrue(test_timer.timer_on)

    def test_stop_timer(self):
        root = tk.Tk()
        test_timer = Countdown(tk.LabelFrame(root, text="test", height = 0, width = 0))
        test_timer.pack()
        test_timer.start_timer()
        test_timer.stop_timer()
        self.assertFalse(test_timer.timer_on)