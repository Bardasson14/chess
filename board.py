import tkinter as tk
from PIL import Image, ImageTk
from player import Player, COLORS
from utils import convertCoord

class Board(tk.Frame):

    def __init__(self, parent, rows=8, columns=8, size=32, color1="grey", color2="blue"):
        '''size is the size of a square, in pixels'''
        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        #self.pieces = {}
        self.squares = {}
        global sprites
        sprites = []

        for i in range(8):
            for j in range(8):
                newSquareInfo = {'piece': None, 'coord': convertCoord(i, j)}
                self.squares[(i,j)] = newSquareInfo

        canvas_width = columns * size
        canvas_height = rows * size

        print(self.squares)

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="black")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)

    def addPiece(self, piece, row=0, column=0):
        sprites.append(tk.PhotoImage(file = piece.spriteDir))
        piece.spriteID = len(sprites)-1
        print(row, column)
        print(piece.name)
        self.canvas.create_image(0,0, image=sprites[piece.spriteID], tags=(piece.name, "piece_name"), anchor="c")
        print(self.canvas.__dict__)
        self.placePiece(piece, row, column)

    def placePiece(self, piece, row, column):
        self.squares[(row, column)]['piece'] = piece
        x0 = (column * self.size) + int(self.size/2)
        y0 = (row * self.size) + int(self.size/2)
        print(self.squares[(row, column)])
        self.canvas.coords(piece.name, x0, y0)

    def refresh(self, event):
        '''Redraw the board, possibly in response to window being resized'''
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
        
        for item in self.squares.items():

            if item[1]['piece'] != None:
                piece = item[1]['piece']
                self.placePiece(piece, item[0][0], item[0][1])
        
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")
    
    def positionPieces(self, player):
        
        firstLine = 0
        secondLine = 1
        
        if (player.color != 0):
            firstLine = 7
            secondLine = 6
        
        self.addPiece(player.pieces[0], firstLine, 3)
        self.addPiece(player.pieces[1], firstLine, 4)
        
        rooks = player.pieces[2:4]
        bishops = player.pieces[4:6]
        knights = player.pieces[6:8]
        pawns = player.pieces[8:16]

        for i in range (2):
            self.addPiece(rooks[i], firstLine, i*7)
            self.addPiece(bishops[i], firstLine, 2 + 3*i)
            self.addPiece(knights[i], firstLine, 1 + 5*i)
        
        for i in range(8):
            self.addPiece(pawns[i], secondLine, i)