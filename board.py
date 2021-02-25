import tkinter as tk
from PIL import Image, ImageTk
from player import Player, COLORS

class GameBoard(tk.Frame):
    def __init__(self, parent, rows=8, columns=8, size=32, color1="grey", color2="blue"):
        '''size is the size of a square, in pixels'''
        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.pieces = {}
        self.squares = []
        global sprites
        sprites = []

        '''
        for i in range (8, 0,-1):
            file = []
            for j in range (len(ALPHABETIC_COORDS)):
                square = {
                    "coord": ALPHABETIC_COORDS[j] + str(i), #coord will be used to generate game log.
                    "currentPiece": None
                }
                file.append(square)
            self.squares.append(file)
        '''
        
        canvas_width = columns * size
        canvas_height = rows * size

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="black")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        # this binding will cause a refresh if the user interactively
        # changes the window size
        self.canvas.bind("<Configure>", self.refresh)

    def addPiece(self, name, imageDir, row=0, column=0):
        sprites.append(tk.PhotoImage(file = imageDir))
        self.canvas.create_image(0,0, image=sprites[len(sprites)-1], tags=(name, "piece"), anchor="c")
        self.placepiece(name, row, column)

    def placepiece(self, name, row, column):
        '''Place a piece at the given row/column'''
        self.pieces[name] = (row, column)
        x0 = (column * self.size) + int(self.size/2)
        y0 = (row * self.size) + int(self.size/2)
        self.canvas.coords(name, x0, y0)

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
        
        for name in self.pieces:
            self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
        
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")
    
    def positionPieces(self, player):
        startLine = 0
        endLine = 1
        colorName = COLORS[player.color]
        
        if (player.color != 0):
            startLine = 7
            endLine = 6
        
        self.addPiece(colorName + '_king', player.pieces[0].spriteDir, startLine, 3)
        print(0)
        self.addPiece(colorName + '_queen', player.pieces[1].spriteDir, startLine, 4)
        
        rooks = player.pieces[2:4]
        bishops = player.pieces[4:6]
        knights = player.pieces[6:8]
        pawns = player.pieces[8:16]

        for i in range (2):
            self.addPiece(colorName + '_rook_' + str(i), rooks[i].spriteDir, startLine, i*7)
            self.addPiece(colorName + '_bishop_' + str(i), bishops[i].spriteDir, startLine, 2 + 3*i)
            self.addPiece(colorName + '_knight_' + str(i), knights[i].spriteDir, startLine, 1 + 5*i)
        
        for i in range(8):
            self.addPiece(colorName + '_pawn_' + str(i), pawns[i].spriteDir, endLine, i)
        

    '''
    def positionSinglePiece(self, piece, ):
        global img #garbage collector
        colorName = COLORS[player.color]
        img = tk.PhotoImage(file=(player.pieces[0].spriteDir))
        self.addPiece(colorName + '_king', img, 0,3)
        img = tk.PhotoImage(file=(player.pieces[1].spriteDir))
        self.addPiece(colorName + '_queen', img, 0,2)
    '''