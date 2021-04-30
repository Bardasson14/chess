import tkinter as tk
from PIL import Image, ImageTk
from player import Player, COLORS
from utils import *
from game_state import GameState
import pieces
from pieces.special_moves import *
from game_rules import *
from timer import *
from ai import *


class Board(tk.Frame):

    def __init__(self, parent, rows=8, columns=8, size=32, color1="light steel blue", color2="steel blue"):
        
        self.rows = rows
        self.columns = columns
        self.size = size
        self.color1 = color1
        self.color2 = color2
        self.squares = {}
        global sprites
        sprites = []
        self.lock = False
        self.selsquare = []
        global special_moves
        special_moves = SpecialMoves()
        self.populate_grid()
        canvas_width = columns * size
        canvas_height = rows * size
        tk.Frame.__init__(self, parent)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                                width=canvas_width, height=canvas_height, background="black")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)
        self.canvas.bind("<Configure>", self.refresh)
        self.canvas.bind("<Button-1>", self.click_event_handler)
        self.contadorPosPieces = 0
        self.state = GameState(self, [Player(0), Player(1)])
        
        global timerp1
        global timerp2

        LabelC1 = tk.LabelFrame(self, text="player2", height = 100, width = 150)
        LabelC1.pack()
        LabelC1.place(x = 600, y= 5)
        timerp2  = Countdown(LabelC1)
        timerp2.pack(padx = 30, pady = 10)
        
        LabelC2 = tk.LabelFrame(self, text="player1", height = 100, width = 150)
        LabelC2.pack()
        LabelC2.place(x = 600, y= 450)
        timerp1  = Countdown(LabelC2)
        timerp1.pack(padx = 30, pady = 10)
        timerp1.start_timer()

        self.ai=None



    def populate_grid(self):

        for i in range(8):
            for j in range(8):
                square_info = {'piece': None, 'coord':(i, j),'selected':None,'gamerule':None,'aicoord':None}
                self.squares[(i,j)] = square_info

    def add_piece(self, piece, row=0, column=0):
        sprites.append(tk.PhotoImage(file = piece.sprite_dir))
        piece.sprite_ID = len(sprites)-1 #saves the sprite position in global sprites array
        self.canvas.create_image(row, column, image=sprites[piece.sprite_ID], tags=(piece.name, "piece_name"), anchor="c")
        self.place_piece(piece, row, column)

    def place_piece(self, piece, row, column):
        self.contadorPosPieces += 1
        self.squares[(row, column)]['piece'] = piece
        x0 = (column * self.size) + int(self.size/2)
        y0 = (row * self.size) + int(self.size/2)
       # ####print(self.squares[(row, column)])
        self.canvas.coords(piece.name, x0, y0)

        if(GameState.first_move and piece.color == "white" and self.contadorPosPieces == 65):
            timerp1.start_timer()
            timerp2.stop_timer()
        elif(self.contadorPosPieces >64):
            if(piece.color == "white"):
                timerp2.start_timer()
                timerp1.stop_timer()
            else:
                timerp2.stop_timer()
                timerp1.start_timer()

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
                self.place_piece(piece, item[0][0], item[0][1])
        
        # puts piece over the square
        self.canvas.tag_raise("piece")
        self.canvas.tag_lower("square")
    
    def mode(self, str): 
        self.ai = Ai(str,self.squares,self,sprites,special_moves)
        if (GameState.turn(self.ai.color)):
            self.ai.board=self
            self.ai.ai_move()
            GameState.switch()


    def clear(self):
        pieces_1 = self.state.players[0].pieces
        pieces_2 = self.state.players[1].pieces
        GameState.player = 'white'
        for i in range (len(pieces_1)):
            self.canvas.delete(pieces_1[i].name)
            self.canvas.delete(pieces_2[i].name)
        timerp1.restart()
        timerp1.seconds_left += 15
        timerp2.restart()
        timerp2.seconds_left += 15
        self.squares = {}
        self.populate_grid()
        self.state = GameState(self, [Player(0), Player(1)])
        timerp1.start_timer()
        timerp2.stop_timer()
        self.ai = None
        self.mode("")
        GameState.blackcoord = (0,4)
        GameState.whitecoord = (7,4)
    
    def position_pieces(self, player):
        
        first_line = 0
        second_line = 1
        
        if (player.color != 0):
            first_line = 7
            second_line = 6
        
        self.add_piece(player.pieces[0], first_line, 4)
        self.add_piece(player.pieces[1], first_line, 3)
        rooks = player.pieces[2:4]
        bishops = player.pieces[4:6]
        knights = player.pieces[6:8]
        pawns = player.pieces[8:16]

        for i in range (2):
            self.add_piece(rooks[i], first_line, i*7)
            self.add_piece(bishops[i], first_line, 2 + 3*i)
            self.add_piece(knights[i], first_line, 1 + 5*i)
        
        for i in range(8):
            self.add_piece(pawns[i], second_line, i)
            
    def add_square(self, piece, coord): # trava a movimentacao no tabuleiro 
        piece.selected = True        # e encaminha os possiveis movimentos para o desenho 
        self.lock = True
        vec = piece.get_possible_moves(coord,self.squares)
        list_aux = []
        if(piece.color == 'white'):
            list_aux = check_all(self.squares, GameState.whitecoord, piece.color)
        else:
            list_aux = check_all(self.squares, GameState.blackcoord, piece.color)
        if(list_aux):
            vec = list(set(vec) & set(list_aux))
            aux = 0
            for i in range(8):
                aux = 0
                for j in range(8):
                    piece_aux = self.squares[(i,j)]['piece']
                    if(piece_aux is not None and piece.color != piece_aux.color):
                        aux = 2
                    if(piece_aux is not None and piece.color == piece_aux.color):
                        vec_aux = list(set(piece_aux.get_possible_moves((i,j), self.squares)) & set(list_aux))
                        if(vec_aux or (get_piece_type(piece_aux.name) == 'king' and piece_aux.get_possible_moves((i,j), self.squares))):
                            # print("TO NÂO")
                            aux = 1
                            break
                if(aux == 1):
                    break
            if(aux == 0 or aux == 2):
                stri = "Xeque-Mate"
                tk.messagebox.showinfo("Xeque-Mate", stri)
                self.clear()
        else:
            aux = 0
            for i in range(1,8):
                aux = 0
                for j in range(1,8):
                    piece_aux = self.squares[(i,j)]['piece']
                    if(piece_aux is not None and piece.color != piece_aux.color):
                        aux = 2
                    if(piece_aux is not None and piece.color == piece_aux.color):
                        vec_aux = piece_aux.get_possible_moves((i,j), self.squares)
                        if(vec_aux):
                            aux = 1
                            break
                if(aux == 1):
                    break
            if(aux == 0 or aux == 2):
                stri = "Afogamento"
                tk.messagebox.showinfo("Empate por afogamento", stri)
                self.clear()
        if(get_piece_type(piece.name) == 'king'):
            vec = piece.get_possible_moves(coord, self.squares)
        if(not(vec)):# se nao tem movimentos libera a selecao de outras pecas
            piece.selected = False
            self.lock = False
        self.draw_square(vec,coord)
        
    def draw_square(self, vec, coord): # desenha os possiveis movimentos na tela
        for i in range (len(vec)):
            self.squares[(vec[i][0],vec[i][1])]['selected']=coord
            self.squares[(vec[i][0],vec[i][1])]['gamerule']=vec[i][2]
            x1 = (vec[i][0] * self.size)
            y1 = (vec[i][1] * self.size)
            x2 = x1 + self.size*0.8
            y2 = y1 + self.size*0.8
            if(vec[i][2]=='mov'):
                self.selsquare.append(self.canvas.create_oval(y1+self.size*0.2, x1+self.size*0.2, y2, x2,outline="",fill="black",stipple="gray50", tags="square"))
            else:
                self.selsquare.append(self.canvas.create_oval(y1+self.size*0.2, x1+self.size*0.2, y2, x2,outline="",fill="green",stipple="gray50", tags="square"))

    def clear_square(self,piece,selected): # libera da tela e do dicionarios os possiveis movimentos e destrava o tabuleiro
        piece.selected = False
        self.lock = False
        for i in range(len(self.selsquare)):# libera da tela os quadrados referentes aos possiveis movimentos 
            self.canvas.delete(self.selsquare[i])
        for i in range(len(selected)): # libera do dicionario as referencias a peca selecionada                     
            self.squares[(selected[i][0], selected[i][1])]['selected']=None
        self.selsquare = []
        
    def capture_piece(self, coord):
        capturedPiece = self.squares[coord]['piece']
        if capturedPiece:
            aicoord=self.squares[coord]['aicoord']

            if aicoord:
                self.squares[coord]['aicoord']=None
                self.ai.update(aicoord)
            self.canvas.delete(capturedPiece.name)
        
    def move_piece(self, piece, ref, coord): 
        
        selected = piece.get_possible_moves(self.squares[ref]['coord'],self.squares)
        color = piece.color
        if (not piece.was_moved_before):

            if (get_piece_type(piece.name) == "pawn"):
                if (abs(ref[0]-coord[0]) == 2 and ((coord[1] < 7 and self.squares[(coord[0], coord[1]+1)]['piece']) or (coord[1]>0 and self.squares[(coord[0], coord[1]-1)]['piece']))):
                    GameState.possible_en_passant = coord   

            piece.was_moved_before = True

        self.clear_square(piece,selected)
        self.capture_piece(coord)
        self.place_piece(self.squares[ref]['piece'],coord[0],coord[1]) # move a peca                    
        self.squares[ref]['piece'] = None

        if(color == 'white'):
            timerp2.start_timer()
            timerp1.stop_timer()
        else:
            timerp2.stop_timer()
            timerp1.start_timer()
    
    def click_event_handler(self, event): # encaminha funcoes dependendo do click do mouse
        for row in range(self.rows):
            for col in range(self.columns):
                if(self.click_is_valid(row, col, event)):  # tratamento do click mouse
                    piece = self.squares[(col,row)]['piece'] # guarda se o quadrado clicado eh uma peca
                    
                    if(piece):
                        color = piece.color
                        
                    ref = self.squares[(col,row)]['selected']
                    gr = self.squares[(col,row)]['gamerule']
                    
                    if piece and GameState.turn(color):    # clicou na peca
                        self.handle_board_lock(piece, row, col)
                        
                    if ref:  # clicou no quadrado vermelho
                        piece = self.squares[ref]['piece']    
                        self.handle_piece_movimentation(piece, col, row, ref)
                        GameState.switch() # troca a cor do turno
                        
                        if(gr!='mov'):
                            special_moves.movRoque(self,gr,(col,row))
                        if (self.ai and GameState.turn(self.ai.color)):
                            self.ai.special_moves=special_moves
                            self.ai.board=self
                            self.ai.ai_move()
                            GameState.switch()

    def click_is_valid(self, row, col, event):
        return (row*self.size<event.x<=(row+1)*self.size) and (col*self.size<event.y<=(col+1)*self.size)    

    def handle_board_lock(self, piece, row, col):
        if(not(self.lock) and not(piece.selected)):
            self.add_square(piece,(col,row))
        elif(self.lock and piece.selected):
            self.clear_square(piece, piece.get_possible_moves(self.squares[(col,row)]['coord'],self.squares))
                        
    def handle_piece_movimentation(self, piece, row, col, ref):

        if(piece is not None and piece.selected):
            if (get_piece_type(piece.name)=='pawn'):
                if (abs(col-ref[1])==1) and not self.squares[(row, col)]['piece']:
                    special_moves.en_passant(self)
                else:
                    GameState.possible_en_passant = None

            GameState.first_move = False                        
            self.move_piece(piece,ref,(row,col))

            if (get_piece_type(piece.name)=='pawn' and row in [0,7]):
                self.lock=True
                special_moves.pawn_promotion(self, piece, row, col, sprites)
                
            elif (get_piece_type(piece.name)=='king'):      
                if (piece.color == 'white'):
                    GameState.whitecoord = (row, col)
                else:
                    GameState.blackcoord = (row, col)

    def reset_timer(self): # consertar
        timerp1.restart()
        timerp2.restart()

    def click_is_valid(self, row, col, event):
        return (row*self.size<event.x<=(row+1)*self.size) and (col*self.size<event.y<=(col+1)*self.size)    
