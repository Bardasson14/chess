import tkinter as tk
import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../src')

from timer import Countdown
from board import Board
from pieces.pawn import Pawn
from game_state import *


class GUITest(unittest.TestCase):

    def test_click_is_valid(self):
        pass

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