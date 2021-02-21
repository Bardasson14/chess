import tkinter as tk
from PIL import Image, ImageTk
from board import GameBoard

def main():
    root = tk.Tk()
    board = GameBoard(root)
    board.pack(side="top", fill="both", expand="true")
    can = tk.Canvas(board)
    img  = ImageTk.PhotoImage(Image.open('assets/img/blackBishop.png'))
    can.pack()
    can.create_image((0,0),image=img)
    print(board.squares)
    root.geometry('900x600')
    root.resizable(width=0, height=0)
    root.mainloop()

main()