import tkinter as tk
from timer import *
from tkinter import Menu
from PIL import Image, ImageTk
from board import *
from player import Player
from game_state import GameState
import pieces
from tkinter import messagebox
import webbrowser

def main():
    root = tk.Tk()
    root.title("chess")
    
    menubar = Menu(root)
    root.config(menu=menubar)
    gameMenu = Menu(menubar)

    gameMenu = Menu(menubar, tearoff=False)
    sub_menu = Menu(gameMenu, tearoff=0)
    color = Menu(sub_menu, tearoff=0)
    gameMenu.add_cascade(label='Mode', menu = sub_menu)    
    sub_menu.add_cascade(label='IA', menu = color)
    gameMenu.add_separator()
    gameMenu.add_command(label='Exit', command = root.destroy)
    menubar.add_cascade(label="Game", menu = gameMenu, underline=1)         
    help_menu = Menu(menubar, tearoff=0)
    
    def msg():
        stri = "Feito alegremente por:\n\n Felipe Esser \n Pedro Henrique \n Vitor Bardasson \n Victor Brandão"
        tk.messagebox.showinfo("About", stri, parent= root)
    
    def callback(url):
        webbrowser.open_new(url)

    menubar.add_cascade(label="Help", menu=help_menu, underline=0)
    help_menu.add_command(label='Rules', command = lambda: callback("https://www.chess.com/pt-BR/como-jogar-xadrez") )
    help_menu.add_command(label='About...', command = lambda: msg())
    
    board = Board(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    GameState(board, [Player(0), Player(1)])
    #recebendo a cor da ia
    sub_menu.add_command(label='Versus', command = lambda: [reset(root, "")])
    color.add_command(label='Black', command = lambda: reset(root, "black"))
    color.add_command(label='White', command = lambda: reset(root, "white"))

    root.geometry('1000x600')
    root.resizable(width=0, height=0)
    root.mainloop()

def reset(root, cor):
    tag_name = '!board'
    i = 2
    while tag_name not in root.children:
        tag_name = "!board{}".format(i)
    board = root.children[tag_name]
    board.destroy()
    board = Board(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    GameState(board, [Player(0), Player(1)])
    board.mode(cor)
    i += 1

main()