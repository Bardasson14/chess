
import tkinter as tk
from PIL import Image, ImageTk
from player import Player, COLORS
from utils import *
from game_state import GameState
import pieces
from pieces.special_moves import *
from game_rules import *
from timer import *
import random

'''
encontrar um loop e chamar
inicia ai(cor da ia , squares inicial da board, board atualizada)
if GameState.turn(ai.color):
    ai.board=board
    ai.move()
    GameState.switch()
'''

class Ai:
    def __init__(self,color,matrix,board,sprites,sp):
        self.color=color
        self.squares = {}#possiveis pecas para movimentacao ia
        self.rangex=None#intervalo linha
        self.rangey=(0,8)#intervalo coluna
        self.rowpiece=None#linha da peca escolhida no dicionario de ia pelo random 
        self.colpiece=None#coluna da peca escolhida no dicionario de ia pelo random
        self.board=board
        self.contpieces=16
        self.sprites=sprites
        self.special_moves = sp
        self.populate_grid(matrix)
    
    def populate_grid(self,matrix):
        if(self.color=='white'):#define o intervalo linha dependendo da cor escolhida para ia
            self.rangex=(6,8) 
        else:
            self.rangex=(0,2)
        for i in range(self.rangex[0],self.rangex[1]):#define um dicionario com base no tabuleiro
            for j in range(8):
                square_info = {'piece': matrix[(i,j)]['piece'], 'coord':matrix[(i,j)]['coord'],'selected':matrix[(i,j)]['selected'],'gamerule':matrix[(i,j)]['gamerule']}
                self.squares[(i,j)] = square_info
                self.board.squares[(i,j)]['aicoord']=(i,j)

    def random(self):#escolha da peca pela ia
        self.rowpiece=random.randrange(self.rangex[0],self.rangex[1])
        self.colpiece=random.randrange(self.rangey[0],self.rangey[1])

    def update(self,coord):
        self.squares[(coord[0],coord[1])]['piece']=None
        self.squares[(coord[0],coord[1])]['mov']=None
        self.contpieces-=1
        #print('cont='+str(self.contpieces))

    def mov_ai_piece(self,piece,row,col,mov,capture):
        if(capture):#se ia capturou uma peca
            self.board.capture_piece((row,col))
        if (not piece.was_moved_before):
            piece.was_moved_before = True
        if(get_piece_type(piece.name)=='pawn'):
            pcoord=self.squares[self.rowpiece,self.colpiece]['coord']
            if (abs(pcoord[0]-row) == 2 and ((col < 7 and self.board.squares[(row, col+1)]['piece']) or (col>0 and self.board.squares[(row, col-1)]['piece']))):
                GameState.possible_en_passant = (row,col)   
            if (abs(pcoord[1]-col) == 1) and not self.board.squares[(row, col)]['piece']:
                self.special_moves.en_passant(self.board)
        self.board.place_piece(piece,row,col)#move a peca
        self.board.squares[self.squares[(self.rowpiece,self.colpiece)]['coord']]['piece']=None#apaga posicao anterior
        self.board.squares[(row,col)]['aicoord']=(self.rowpiece,self.colpiece)
        self.squares[(self.rowpiece,self.colpiece)]['coord']=(row,col)#atualiza dicionario da ia
        if(mov!='mov'):#faz o roque
            self.special_moves.mov_roque(self.board,mov,(row,col))
        if(get_piece_type(piece.name)=='pawn' and row in [0,7]):
            self.special_moves.ai_pawn_promotion(self.board, piece, row, col, self.sprites, self.board.state.players[select_player(piece.color)])
            self.squares[(self.rowpiece,self.colpiece)]['piece']=self.board.squares[(row,col)]['piece']
        if (get_piece_type(piece.name)=='king'):
            if (piece.color == 'white'):
                GameState.whitecoord = (row, col)
            else:
                GameState.blackcoord = (row, col)
        
            

    


    def ai_move(self):# o jogo entra em loop quando as peças restantes nãos tiverem mais movimentos 
        continua=True
        while(continua and self.contpieces>0):
            self.random()
            piece=self.squares[(self.rowpiece,self.colpiece)]['piece']
            if piece is not None :#se ia escolheu uma peca valida para o loop
                vec = piece.get_possible_moves(self.squares[(self.rowpiece,self.colpiece)]['coord'],self.board.squares)
                list_aux = []
                if(piece.color == 'white'):
                    list_aux = check_all(self.board.squares, GameState.whitecoord, piece.color)
                else:
                    list_aux = check_all(self.board.squares, GameState.blackcoord, piece.color)
                if(list_aux):
                    vec = list(set(vec) & set(list_aux))
                    aux = 0
                    for i in range(8):
                        aux = 0
                        for j in range(8):
                            piece_aux = self.board.squares[(i,j)]['piece']
                            if(piece_aux is not None and piece.color != piece_aux.color):
                                aux = 2
                            if(piece_aux is not None and piece.color == piece_aux.color):
                                vec_aux = list(set(piece_aux.get_possible_moves((i,j), self.board.squares)) & set(list_aux))
                                if(vec_aux or (get_piece_type(piece_aux.name) == 'king' and piece_aux.get_possible_moves((i,j), self.board.squares))):
                                    aux = 1
                                    # print(piece_aux.get_possible_moves(i,j), self.board.squares)
                                    break
                        if(aux == 1):
                            break
                    if(aux == 0 or aux == 2):
                        stri = "Xeque-Mate"
                        tk.messagebox.showinfo("Xeque-Mate", stri)
                        self.board.clear()
                        self.board.black.pack()
                else:
                    aux = 0
                    for i in range(1,8):
                        aux = 0
                        for j in range(1,8):
                            piece_aux = self.board.squares[(i,j)]['piece']
                            if(piece_aux is not None and piece.color != piece_aux.color):
                                aux = 2
                            if(piece_aux is not None and piece.color == piece_aux.color):
                                vec_aux = piece_aux.get_possible_moves((i,j), self.board.squares)
                                if(vec_aux):
                                    aux = 1
                                    break
                        if(aux == 1):
                            break
                    if(aux == 0 or aux == 2):
                        stri = "Afogamento"
                        tk.messagebox.showinfo("Empate por afogamento", stri)
                        self.board.clear()
                print("piece",piece.__dict__)
                print("piece aux",piece_aux.__dict__)
                if(get_piece_type(piece.name) == 'king'):
                    vec = piece.possible_moves
                    print("POSSIBLE MOVES KING",vec)
                ai_possible_moves = vec #pega um vetor de possiveis movimentos da peca escolhida
                if(ai_possible_moves):#se o vetor nao e vazio vai movimentar
                    intervalo=random.randrange(0,len(ai_possible_moves))#qual movimento vai fazer
                    next_row=ai_possible_moves[intervalo][0]#linha que vai mover
                    next_col=ai_possible_moves[intervalo][1]#coluna que vai mover
                    mov=ai_possible_moves[intervalo][2]#se eh roque
                    capture=self.board.squares[(next_row,next_col)]['piece']
                    self.mov_ai_piece(piece,next_row,next_col,mov,capture)
                    continua=False
                    print("next row", next_row)
                    print("next col", next_col)