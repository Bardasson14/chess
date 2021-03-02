import tkinter as tk
from PIL import Image, ImageTk
from board import Board, COLORS
from player import Player
from utils import convertCoord

def main():
    root = tk.Tk()
    p1 = Player(0)
    p2 = Player(1)
    board = Board(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    board.positionPieces(p1)
    board.positionPieces(p2)   
    for sq in board.squares.values():
        print(sq)
    root.geometry('1000x600')
    root.resizable(width=0, height=0)
    root.mainloop()
    
main()
