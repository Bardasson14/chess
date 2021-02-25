import tkinter as tk
from PIL import Image, ImageTk
from board import GameBoard, COLORS
from player import Player

def main():
    root = tk.Tk()
    player = Player(0)
    board = GameBoard(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    board.positionPieces(player)

    #img = tk.PhotoImage(file=(player.pieces[0].spriteDir))
    #board.addpiece(COLORS[player.color] + '_king', img, 1, 3)
    root.geometry('1000x600')
    root.resizable(width=0, height=0)
    root.mainloop()

main()