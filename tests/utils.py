import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../src')

from utils import *


class UtilsTest(unittest.TestCase):

    def test_get_piece_type(self):
        piece_name = 'white_bishop_1'
        self.assertEqual(get_piece_type(piece_name), 'bishop')

    def test_get_canvas_keys(self):
        canvas_keys = ['!listbox2', '!label2', '!button2']
        self.assertEqual(get_canvas_keys(canvas_keys), canvas_keys)