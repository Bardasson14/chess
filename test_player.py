import unittest
from player import Player
from utils import get_piece_type


class PlayerTest(unittest.TestCase):

    def test_piece_list(self):
        player = Player(1)

        piece_dict = {
            'bishop': 2,
            'king': 1,
            'knight': 2,
            'pawn': 8,
            'queen': 1,
            'rook': 2
        }

        for p in piece_dict.keys():
            piece_list = self.filter_piece_list(p, player.pieces)
            self.assertEqual(len(piece_list), piece_dict[p])
            

    @classmethod 
    def filter_piece_list(self, piece_name, piece_list):
        piece = list(filter(lambda x: get_piece_type(x.name) == piece_name, piece_list))
        return piece