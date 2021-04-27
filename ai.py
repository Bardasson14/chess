
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
    GameState.troca()
'''
class Ai:
    def __init__(self,color,matrix,board):
        self.color=color
        self.squares = {}#possiveis pecas para movimentacao ia
        self.rangex=None#intervalo linha
        self.rangey=(0,8)#intervalo coluna
        self.rowpiece=None#linha da peca escolhida no dicionario de ia pelo random 
        self.colpiece=None#coluna da peca escolhida no dicionario de ia pelo random
        self.board=board
        self.contpieces=16
        global special_moves
        special_moves = SpecialMoves()
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
                print(square_info)

    def aleatorio(self):#escolha da peca pela ia
        self.rowpiece=random.randrange(self.rangex[0],self.rangex[1])
        self.colpiece=random.randrange(self.rangey[0],self.rangey[1])

    def update(self,coord):
        self.squares[(coord[0],coord[1])]['piece']=None
        self.squares[(coord[0],coord[1])]['mov']=None
        self.contpieces-=1
        print('cont='+str(self.contpieces))

    def movAiPiece(self,piece,row,col,mov,capture):
        if(capture):#se ia capturou uma peca
            self.board.capture_piece((row,col))
        self.board.place_piece(piece,row,col)#move a peca
        self.board.squares[self.squares[(self.rowpiece,self.colpiece)]['coord']]['piece']=None#apaga posicao anterior
        self.board.squares[(row,col)]['aicoord']=(self.rowpiece,self.colpiece)
        self.squares[(self.rowpiece,self.colpiece)]['coord']=(row,col)#atualiza dicionario da ia
        if(mov!='mov'):#faz o roque
            special_moves.movRoque(self.board,mov,(row,col))

    def aiMove(self):# o jogo entra em loop quando as peças restantes nãos tiverem mais movimentos 
        continua=True
        while(continua and self.contpieces>0):
            self.aleatorio()
            piece=self.squares[(self.rowpiece,self.colpiece)]['piece']
            if piece :#se ia escolheu uma peca valida para o loop
                print(piece.name)
                ai_possible_moves=piece.get_possible_moves(self.squares[(self.rowpiece,self.colpiece)]['coord'],self.board.squares)#pega um vetor de possiveis movimentos da peca escolhida
                if(ai_possible_moves):#se o vetor nao e vazio vai movimentar
                    intervalo=random.randrange(0,len(ai_possible_moves))#qual movimento vai fazer
                    next_row=ai_possible_moves[intervalo][0]#linha que vai mover
                    next_col=ai_possible_moves[intervalo][1]#coluna que vai mover
                    mov=ai_possible_moves[intervalo][2]#se eh roque
                    capture=self.board.squares[(next_row,next_col)]['piece']
                    self.movAiPiece(piece,next_row,next_col,mov,capture)
                    continua=False