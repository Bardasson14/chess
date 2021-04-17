from string import ascii_lowercase
import tkinter as tk
from functools import partial

ALPHABETIC_COORDS = list(ascii_lowercase)[:8]
DIRECTIONS = ['bottom', 'top', 'right', 'left', 'upper_right', 'upper_left', 'lower_right', 'lower_left']

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

def possible_directions(piece):
    piece_type = get_piece_type(piece.name)
    directions = {
        'black_queen': DIRECTIONS, 
        'white_queen': DIRECTIONS,
        'white_pawn': [d for d in DIRECTIONS if (d.split('_')[0]=='upper') or d=='top'],
        'black_pawn': [d for d in DIRECTIONS if (d.split('_')[0]=='lower') or d=='bottom'],
        'white_bishop': [d for d in DIRECTIONS if len(d.split('_'))>1],
        'black_bishop': [d for d in DIRECTIONS if len(d.split('_'))>1],
        'white_rook': [d for d in DIRECTIONS if len(d.split('_'))==1],
        'black_rook': [d for d in DIRECTIONS if len(d.split('_'))==1],
        'black_king': DIRECTIONS,
        'white_king': DIRECTIONS
    }
    return directions[piece.color + '_' + piece_type]

    