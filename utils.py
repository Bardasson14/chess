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

def get_canvas_keys(canvas):
    listbox_key = '!listbox'
    label_key = '!label'
    button_key = '!button'
    i = 1

    while listbox_key not in canvas:
        i+=1
        listbox_key = "!listbox{}".format(i)
        
    if (i!=1):
        label_key = "!label{}".format(i)
        button_key = "!button{}".format(i)

    return [listbox_key, label_key, button_key]

def piece_in(piece, arr):
    for element in arr:
        if piece.name in element:
            return True
    return False