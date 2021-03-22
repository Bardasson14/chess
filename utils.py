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

def pawn_promotion_menu(root):
    pieces = ['Bispo', 'Cavalo', 'Peão', 'Rei', 'Rainha', 'Torre']
    listbox = tk.Listbox(root, selectmode = 'single', width = 7, height=6)
    listbox.pack(expand = True, fill = "both")
    to_be_destroyed = [listbox]
    label = tk.Label(root, text = "Selecione a peça na qual o peão se transformará")
    label.pack()
    for piece in pieces:
        listbox.insert(listbox.size(), piece)
    submit = tk.Button(master = root, text = "Escolher", command = lambda: set_piece(root)) # check submit partial
    submit.pack()
    
def set_piece(root):
    index = root.children['!listbox'].curselection()[0]
    pieces = ['bishop', 'knight', 'pawn', 'king', 'queen', 'rook']
    root.children['!listbox'].destroy()
    root.children['!label'].destroy()
    root.children['!button'].destroy()
    #Transformar peça
    