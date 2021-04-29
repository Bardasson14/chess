import tkinter as tk
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
    board = Board(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    create_menu(root, board)
    #recebendo a cor da iaroot.after(500, add_letter)
    
    root.geometry('1000x600')
    root.resizable(width=0, height=0)
    root.mainloop()


def msg():
    stri = "Feito alegremente por:\n\n Felipe Esser \n Pedro Henrique \n Vitor Bardasson \n Victor Brandão"
    tk.messagebox.showinfo("About", stri)

def callback(url):
    webbrowser.open_new(url)
        
def create_menu(root, board):
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
    menubar.add_cascade(label="Help", menu=help_menu, underline=0)
    help_menu.add_command(label='Rules', command = lambda: callback("https://www.chess.com/pt-BR/como-jogar-xadrez") )
    help_menu.add_command(label='About...', command = lambda: msg())
    sub_menu.add_command(label='Versus', command = lambda: [root.after(500, board.clear(), board.mode(""))])
    color.add_command(label='Black', command = lambda: [root.after(500, board.clear(), board.mode("black"))])
    color.add_command(label='White', command = lambda: [root.after(500, board.clear(), board.mode("white"))])

main()