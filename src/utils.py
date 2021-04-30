from string import ascii_lowercase
import tkinter as tk
from functools import partial

ALPHABETIC_COORDS = list(ascii_lowercase)[:8]
DIRECTIONS = ['bottom', 'top', 'right', 'left', 'upper_right', 'upper_left', 'lower_right', 'lower_left']
INVERTED_DIRECTIONS = ['top', 'bottom', 'left', 'right', 'lower_left', 'lower_right', 'upper_left', 'upper_right']

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

def select_player(color):
    if color == 'white':
        return 0
    return 1