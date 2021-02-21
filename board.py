import tkinter as tk
from PIL import ImageTk,Image

from utils import ALPHABETIC_COORDS
from pieces import bishop as bishopModule, king as kingModule, knight as knightModule, pawn as pawnModule, queen as queenModule, rook as rookModule

class GameBoard(tk.Frame):
    def __init__(self, parent, rows=8, columns=8, size=32, color1="white", color2="black"):
        #size is the size of a square, in pixels
        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.squares = []

        for i in range (8, 0,-1):
            file = []
            for j in range (len(ALPHABETIC_COORDS)):
                square = {
                    "coord": ALPHABETIC_COORDS[j] + str(i), #coord will be used to generate game log.
                    "currentPiece": None
                }
                file.append(square)
            self.squares.append(file)

        canvas_width = columns * size
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height)
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)

        
    def refresh(self, event):
        #Redraw the board, possibly in response to window being resized
        xsize = int((event.width-1) / self.columns)
        ysize = int((event.height-1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
                color = self.color1 if color == self.color2 else self.color2
        self.canvas.tag_lower("square")