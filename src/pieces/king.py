from .piece import Piece
from game_rules import *

class King(Piece):
    
    def __init__(self, color, name):
        self.sprite_dir = 'assets/img/' + color + 'King.png'
        self.name = name
        super(King,self).__init__(color,name)

    def little_roque(self, coord, matrix):
        if(not(self.was_moved_before)):
            for i in range(1,4):
                if (coord[1] + i <= 7):
                    piece = matrix[(coord[0],coord[1]+i)]['piece']
                    if (piece and piece.color==self.color):
                        if((coord[1] + i)==7 and (piece.name=='white_rook_2'or piece.name=='black_rook_2') and not (piece.was_moved_before)):
                            self.possible_moves.append((coord[0], coord[1]+i-1, 'lr'))
                        else:
                            ###print(piece.name)
                            break

    def big_roque(self, coord, matrix):
        if(not(self.was_moved_before)):    
            for i in range(1,5):
                if (coord[1] - i >= 0):
                    piece = matrix[(coord[0], coord[1]-i)]['piece']
                    if (piece and piece.color==self.color):
                        if((coord[1] - i)==0 and (piece.name=='white_rook_1' or piece.name=='black_rook_1') and not (piece.was_moved_before)):
                            self.possible_moves.append((coord[0], coord[1]-i+2, 'br'))
                        else:
                            ###print(piece.name)
                            break
                            
    def roque(self,coord,matrix):
        if(not(check_all(matrix,coord,self.color))):#xeque do rei
            if(not(check_all(matrix,(coord[0],coord[1]+1),self.color)and check_all(matrix,(coord[0],coord[1]+2),self.color))):#xeque do lr
                self.little_roque(coord,matrix)
            if(not(check_all(matrix,(coord[0],coord[1]-1),self.color)and check_all(matrix,(coord[0],coord[1]-2),self.color))):#xeque do br
                self.big_roque(coord,matrix)
                
    def get_possible_moves(self, coord, matrix):

        list_aux = can_move(self.color, matrix, coord)

        if(list_aux):
            return list_aux
            
        self.possible_moves=[]
        self.mov_d(coord, matrix)
        self.mov_v(coord, matrix)
        self.mov_h(coord, matrix)

        if(not(self.was_moved_before)):
            self.roque(coord,matrix)
        return self.possible_moves

    def mov_h(self, coord, matrix):
        self.check_right_edge(coord, matrix)
        self.check_left_edge(coord, matrix)
        
    def mov_d(self, coord, matrix):
        self.check_upper_right_edge(coord, matrix)
        self.check_upper_left_edge(coord, matrix)
        self.check_lower_right_edge(coord, matrix)
        self.check_lower_left_edge(coord, matrix)
    
    def mov_v(self, coord, matrix): 
        self.check_upper_edge(coord, matrix)
        self.check_lower_edge(coord, matrix)

    def check_upper_edge(self, coord, matrix):
        if (coord[0]-1>=0): 
            piece = matrix[(coord[0]-1,coord[1])]['piece']
            if ((piece and piece.color!=self.color) or (not piece)):
                self.possible_moves.append((coord[0]-1,coord[1],'mov'))
    
    def check_lower_edge(self, coord, matrix):
        if (coord[0]+1<=7): #limite inferior
            b = matrix[(coord[0]+1,coord[1])]['piece']    #⬇⬇⬇
            if (b and b.color!=self.color or (not b)):
                self.possible_moves.append((coord[0]+1,coord[1],'mov'))
                self.possible_moves.append((coord[0]+1,coord[1],'mov'))
    
    def check_right_edge(self, coord, matrix):
        if(coord[1]+1<=7):  
            right_piece = matrix[(coord[0],coord[1]+1)]['piece']
            if (right_piece and (right_piece.color != self.color)):
                self.possible_moves.append((coord[0],coord[1]+1,'mov'))
            elif not right_piece:
                self.possible_moves.append((coord[0],coord[1]+1,'mov'))

    def check_left_edge(self, coord, matrix):
        if(coord[1]-1>=0):
            left_piece = matrix[(coord[0],coord[1]-1)]['piece'] 
            if (left_piece and left_piece.color!=self.color or (not left_piece)):
                self.possible_moves.append((coord[0],coord[1]-1,'mov'))
    
    def check_upper_right_edge(self, coord, matrix):
        if(coord[1]!=7 and coord[0]!=0):
            front_right_piece = matrix[(coord[0]-1,coord[1]+1)]['piece']
            if ((front_right_piece and front_right_piece.color!=self.color) or (not front_right_piece)):
                self.possible_moves.append((coord[0]-1,coord[1]+1,'mov'))

    def check_upper_left_edge(self, coord, matrix):
        if(coord[1]!=0 and coord[0]!=0):
            front_left_piece = matrix[(coord[0]-1,coord[1]-1)]['piece']
            if((front_left_piece and front_left_piece.color!=self.color) or (not front_left_piece)) :
                self.possible_moves.append((coord[0]-1,coord[1]-1,'mov'))

    def check_lower_right_edge(self, coord, matrix):
        if(coord[1]!=7 and coord[0]!=7):
            bottom_right_piece = matrix[(coord[0]+1,coord[1]+1)]['piece']
            if(bottom_right_piece and bottom_right_piece.color!=self.color or (not bottom_right_piece)):
                self.possible_moves.append((coord[0]+1,coord[1]+1,'mov'))

    def check_lower_left_edge(self, coord, matrix):
        if(coord[1]!=0 and coord[0]!=7):
            bottom_left_piece = matrix[(coord[0]+1,coord[1]-1)]['piece']
            if((bottom_left_piece and bottom_left_piece.color!=self.color) or (not bottom_left_piece)):
                self.possible_moves.append((coord[0]+1,coord[1]-1,'mov'))
