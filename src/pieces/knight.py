from .piece import Piece
from game_rules import can_move
import os

class Knight(Piece):
    
    def __init__(self, color, name):
        self.sprite_dir = color + "Knight.png"
        self.name = name
        super(Knight,self).__init__(color,name)

    def get_possible_moves(self, coord, matrix):

        
        list_aux = can_move(self.color, matrix, coord)
        
        self.possibleMoves=[]
        self.mov_ul(coord,matrix)
        self.mov_ur(coord,matrix)
        self.mov_ll(coord,matrix)
        self.mov_lr(coord,matrix)

        if(list_aux):
            return [move for move in list_aux if move in self.possible_moves]
        
        return self.possibleMoves

    def mov_ul(self, coord, matrix):
        if (coord[0]-2 >= 0 and coord[1]-1 >= 0):
            piece = matrix[(coord[0]-2,coord[1]-1)]['piece']
            if (not piece):
                self.possibleMoves.append((coord[0]-2,coord[1]-1,'mov'))
            elif(piece is not None and piece.color != self.color):
                self.possibleMoves.append((coord[0]-2,coord[1]-1,'mov'))
        
        if (coord[1]-2 >=0 and coord[0]-1 >=0):
            piece = matrix[(coord[0]-1,coord[1]-2)]['piece']
            if (not piece):
                self.possibleMoves.append((coord[0]-1,coord[1]-2,'mov'))
            elif(piece is not None and piece.color != self.color):
                self.possibleMoves.append((coord[0]-1,coord[1]-2,'mov'))

    def mov_ur(self, coord, matrix):
        if (coord[0]-2 >= 0 and coord[1]+1 <= 7):
            piece = matrix[(coord[0]-2,coord[1]+1)]['piece']
            if (not piece):
                self.possibleMoves.append((coord[0]-2,coord[1]+1,'mov'))
            elif(piece is not None and piece.color != self.color):
                self.possibleMoves.append((coord[0]-2,coord[1]+1,'mov'))
          
        if (coord[1]+2 <=7 and coord[0]-1 >=0):
            piece = matrix[(coord[0]-1,coord[1]+2)]['piece']
            if (not piece):
                self.possibleMoves.append((coord[0]-1,coord[1]+2,'mov'))
            elif(piece is not None and piece.color != self.color):
                self.possibleMoves.append((coord[0]-1,coord[1]+2,'mov'))

    def mov_ll(self, coord, matrix):
        if (coord[0]+2 <= 7 and coord[1]-1 >=0):
            piece = matrix[(coord[0]+2,coord[1]-1)]['piece']
            if (not piece):
                self.possibleMoves.append((coord[0]+2,coord[1]-1,'mov'))
            elif(piece is not None and piece.color != self.color):
                self.possibleMoves.append((coord[0]+2,coord[1]-1,'mov'))
        
        if (coord[0]+1 <= 7 and coord[1]-2 >=0):
            piece = matrix[(coord[0]+1,coord[1]-2)]['piece']
            if (not piece):
                self.possibleMoves.append((coord[0]+1,coord[1]-2,'mov'))
            elif(piece is not None and piece.color != self.color):
                self.possibleMoves.append((coord[0]+1,coord[1]-2,'mov'))

    def mov_lr(self, coord, matrix):
        if (coord[0]+2 <= 7 and coord[1]+1 <=7):
            piece = matrix[(coord[0]+2,coord[1]+1)]['piece']
            if (not piece):
                self.possibleMoves.append((coord[0]+2,coord[1]+1,'mov'))
            elif(piece is not None and piece.color != self.color):
                self.possibleMoves.append((coord[0]+2,coord[1]+1,'mov'))          
        
        if (coord[0]+1 <= 7 and coord[1]+2 <= 7):
            piece = matrix[(coord[0]+1,coord[1]+2)]['piece']
            if (not piece):
                self.possibleMoves.append((coord[0]+1,coord[1]+2,'mov'))
            elif(piece is not None and piece.color != self.color):
                self.possibleMoves.append((coord[0]+1,coord[1]+2,'mov'))