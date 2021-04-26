import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + '/../src')
from game_state import *

class GameStateTest(unittest.TestCase):

    def test_turn(self):
        state = GameState(None, None)
        GameState.switch()
        self.assertEqual(state.player, 'black')