import tkinter as tk
from board import GameBoard

def main():
    root = tk.Tk()
    board = GameBoard(root)
    board.pack(side="top", fill="both", expand="true")
    root.geometry('900x600')
    root.resizable(width=0, height=0)
    root.mainloop()

main()