import tkinter as tk
from tkinter import Menu
from PIL import Image, ImageTk
from board import *
from player import Player
from game_state import GameState

class Game:
    
    def __init__(self):
        self.state = GameState()
        self.root = tk.Tk()
        self.root.title("chess")
        menubar = Menu(self.root)
        
        self.root.config(menu=menubar)
        gameMenu = Menu(menubar)
        
        gameMenu = Menu(menubar, tearoff=False)
        sub_menu = Menu(gameMenu, tearoff=0)
        sub_menu.add_command(label='Versus')
        sub_menu.add_command(label='IA')
        gameMenu.add_cascade(label='Mode', menu = sub_menu)
        
        gameMenu.add_separator()
        
        gameMenu.add_command(label='Exit', command = self.root.destroy)
        menubar.add_cascade(label="Game", menu = gameMenu, underline=1)     
        
        help_menu = Menu(menubar, tearoff=0)

        help_menu.add_command(label='Rules')
        help_menu.add_command(label='About...')
        menubar.add_cascade(label="Help", menu=help_menu, underline=0)
        
        self.player1 = Player(0)
        self.player2 = Player(1)
        self.board = Board(self.root)
        self.board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
        self.board.positionPieces(self.player1)
        self.board.positionPieces(self.player2)   
        #for sq in board.squares.values():
        #    print(sq)
        self.root.geometry('1000x600')
        self.root.resizable(width=0, height=0)
        self.root.mainloop()