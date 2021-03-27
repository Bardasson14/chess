import tkinter as tk
from PIL import Image, ImageTk
from player import Player, COLORS
from utils import *
from game_state import GameState
import pieces
from pieces.special_moves import *

class Board(tk.Frame):

    def __init__(self, parent, rows=8, columns=8, size=32, color1="grey", color2="blue"):
        
        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.squares = {} #this dict will be populated with the board grid using tuple(row, col) as key
        global sprites
        sprites = []
        self.lock = False # indica se existe alguma peca selecionada no tabuleiro
        self.selsquare = [] # guarda as variaveis dos quadrados que indicam os possiveis movimentos
        global special_moves
        special_moves = SpecialMoves()

        for i in range(8):
            for j in range(8):
                newSquareInfo = {'piece': None, 'coord':(i, j),'selected':None} #each entry in self.squares has a piece and a coordinate
                self.squares[(i,j)] = newSquareInfo

        canvas_width = columns * size
        canvas_height = rows * size

        #print(self.squares)

        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="black")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)
        self.canvas.bind("<Configure>", self.refresh)
        self.canvas.bind("<Button-1>", self.clickEventHandler)

    def addPiece(self, piece, row=0, column=0):
        sprites.append(tk.PhotoImage(file = piece.spriteDir))
        piece.spriteID = len(sprites)-1 #saves the sprite position in global sprites array
        self.canvas.create_image(row, column, image=sprites[piece.spriteID], tags=(piece.name, "piece_name"), anchor="c")
        self.placePiece(piece, row, column)

    def placePiece(self, piece, row, column):
        print(row, column)
        print(piece.name, "entrou")
        self.squares[(row, column)]['piece'] = piece
        print(self.squares[(row, column)]['piece'])
        x0 = (column * self.size) + int(self.size/2)
        y0 = (row * self.size) + int(self.size/2)
       # print(self.squares[(row, column)])
        self.canvas.coords(piece.name, x0, y0)

    def refresh(self, event):
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
        
        for item in self.squares.items(): #iterates through the self.squares dict, attributing key to item[0] and value to item[1]
            
            if item[1]['piece']: #if statement is only true if square isn't empty
                piece = item[1]['piece']
                self.placePiece(piece, item[0][0], item[0][1])
        
        # puts piece over the square
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
    
    def addSquare(self,piece,coord): # trava a movimentacao no tabuleiro 
        piece.selected = True        # e encaminha os possiveis movimentos para o desenho 
        self.lock = True
        vec = piece.getPossibleMoves(coord,self.squares)
        if(not(vec)):# se nao tem movimentos libera a selecao de outras pecas
            piece.selected = False
            self.lock = False
        self.drawSquare(vec,coord)
        
    def drawSquare(self,vec,coord): # desenha os possiveis movimentos na tela
        for i in range (len(vec)):
            self.squares[(vec[i][0],vec[i][1])]['selected']=coord
            x1 = (vec[i][0] * self.size)
            y1 = (vec[i][1] * self.size)
            x2 = x1 + self.size
            y2 = y1 + self.size
            self.selsquare.append(self.canvas.create_rectangle(y1, x1, y2, x2, width=2,outline="red", tags="square"))

    def clearSquare(self,piece,selected=[]): # libera da tela e do dicionarios os possiveis movimentos e destrava o tabuleiro
        piece.selected = False
        self.lock = False
        for i in range(len(self.selsquare)):# libera da tela os quadrados referentes aos possiveis movimentos 
            self.canvas.delete(self.selsquare[i])
        for i in range(len(selected)): # libera do dicionario as referencias a peca selecionada                     
            self.squares[selected[i]]['selected']=None
        self.selsquare = []
        
    def pieceCapture(self, coord):
        capturedPiece = self.squares[coord]['piece']
        if capturedPiece:
            self.canvas.delete(capturedPiece.name)
        
    def movePiece(self, piece, ref, coord): 
        selected = piece.getPossibleMoves(self.squares[ref]['coord'],self.squares)
        piece.wasMovedBefore = True
        self.clearSquare(piece,selected)
        self.pieceCapture(coord)
        
        self.placePiece(self.squares[ref]['piece'],coord[0],coord[1]) # move a peca                    
        self.squares[ref]['piece'] = None

    def clickEventHandler(self, event): # encaminha funcoes dependendo do click do mouse
        for row in range(self.rows):
            for col in range(self.columns):
                if(self.clickIsValid(row, col, event)):  # tratamento do click mouse
                    piece = self.squares[(col,row)]['piece']
                    ref = self.squares[(col,row)]['selected']
                    if piece:    # clicou na peca
                        if(not(self.lock) and not(piece.selected)):
                            self.addSquare(piece,(col,row))
                        elif(self.lock and piece.selected):
                            self.clearSquare(piece)
                    if ref:  # clicou no quadrado vermelho
                        piece = self.squares[ref]['piece']

                        if(piece and piece.selected):
                              
                            if (get_piece_type(piece.name)=='pawn'):
                                if (abs(row-ref[1])==1) and not self.squares[(col, row)]['piece']:
                                    print(special_moves.selected_piece)
                                    special_moves.en_passant(self, piece, row, col, ref)
   
                            if not GameState.first_move and GameState.possible_en_passant == piece:
                                GameState.possible_en_passant = None

                            else:
                                GameState.first_move = False
                                if (get_piece_type(piece.name) == 'pawn' and (abs(col-ref[0]) == 2)):
                                    GameState.possible_en_passant = piece                                        
                            
                            self.movePiece(piece,ref,(col,row))

                            if (get_piece_type(piece.name)=='pawn' and col in [0,7]):
                                print("ocupa a casa no momento: ", piece.name)
                                print(special_moves.selected_piece)
                                print(row, col)
                                print('certo:', self.squares[(col, row)]['piece'])
                                print('errado:', self.squares[(row, col)]['piece'])
                                special_moves.pawn_promotion(self, piece, col, row, sprites)
                            
    def clickIsValid(self, row, col, event):
        return (row*self.size<event.x<=(row+1)*self.size) and (col*self.size<event.y<=(col+1)*self.size)    