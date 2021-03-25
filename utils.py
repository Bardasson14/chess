from string import ascii_lowercase
import tkinter as tk
from functools import partial

ALPHABETIC_COORDS = list(ascii_lowercase)[:8]

def convert_coord(originalRow, originalCol):
    row = 8 - originalRow
    col = ALPHABETIC_COORDS[originalCol]
    return str(row) + col

def get_piece_type(piece_name):
    return piece_name.split('_')[1]
