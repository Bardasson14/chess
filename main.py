import tkinter as tk
from PIL import Image, ImageTk
from board import GameBoard, COLORS
from player import Player

def main():
    root = tk.Tk()
    p1 = Player(0)
    p2 = Player(1)
    board = GameBoard(root)
    board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
    board.positionPieces(p1)
    board.positionPieces(p2)

    #print(player)

    #img = tk.PhotoImage(file=(player.pieces[0].spriteDir))
    #board.addpiece(COLORS[player.color] + '_king', img, 1, 3)

    #print(board.__dict__)
    #board.update()
    root.geometry('1000x600')
    root.resizable(width=0, height=0)
    root.mainloop()
    
main()
