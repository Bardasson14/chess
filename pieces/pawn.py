from .piece import Piece
from game_rules import GameRules
from game_state import GameState

class Pawn(Piece):

    # add boundary checking functions
    
    def __init__(self, color, name):
        self.sprite_dir = 'assets/img/' + color + 'Pawn.png'
        self.name = name
        self.color=color
        super(Pawn,self).__init__(color,name)
        
    def get_possible_moves(self, coord, matrix):
        
        game_rules = GameRules()
        list_aux = game_rules.can_move(self.color, matrix, coord)

        if(list_aux):
            return list_aux
        
        self.possible_moves=[]
        self.mov_d(coord, matrix)
        self.mov_v(coord, matrix)
        if (GameState.possible_en_passant):
            self.check_en_passant(coord, matrix)
        return self.possible_moves

    def mov_v(self, coord, matrix): 
        ###print(first_move)
        if (self.color == 'white'):
            self.check_upper_edge(coord, matrix)
        else:
            self.check_lower_edge(coord, matrix)

    def mov_d(self, coord, matrix):
        ###print(first_move)
        if (self.color == 'white'):
            self.check_upper_left_edge(coord, matrix)
            self.check_upper_right_edge(coord, matrix)   
        else: 
            self.check_lower_left_edge(coord, matrix)
            self.check_lower_right_edge(coord, matrix)

    def check_en_passant(self, coord, matrix):
        if (coord[1]-1>=0 and (coord[0], coord[1]-1) == GameState.possible_en_passant):
            if matrix[coord]['piece'].color == 'white':
                self.possible_moves.append((coord[0]-1, coord[1]-1, 'mov'))
            else:
                self.possible_moves.append((coord[0]+1, coord[1]-1, 'mov'))
        elif (coord[1]+1<=7 and (coord[0], coord[1]+1) == GameState.possible_en_passant):
            if matrix[coord]['piece'].color =='white':
                self.possible_moves.append((coord[0]-1, coord[1]+1, 'mov'))
            else:
                self.possible_moves.append((coord[0]+1, coord[1]+1, 'mov'))
    def check_upper_edge(self, coord, matrix):
        if (coord[0]-1>=0):
            front_piece = matrix[(coord[0]-1,coord[1])]['piece'] 
            if (not front_piece):
                self.possible_moves.append((coord[0]-1,coord[1],'mov'))

        if not self.was_moved_before:
            i=0
            while(i<2):
                if(coord[0]-(i+1)>=0): # limite superior
                    front_piece = matrix[(coord[0]-(i+1),coord[1])]['piece']    # ⬆⬆⬆
                    if (not front_piece):
                        self.possible_moves.append((coord[0]-(i+1),coord[1],'mov'))
                        i+=1
                    else:
                        i=2
                else: 
                    i=2

    def check_lower_edge(self, coord, matrix):
        if (coord[0]+1<=7):
            bottom_piece = matrix[(coord[0]+1,coord[1])]['piece']
            if (not bottom_piece):
                self.possible_moves.append((coord[0]+1,coord[1],'mov'))

        if (not self.was_moved_before):
            i=0
            while(i<2):
                if(coord[0]+(i+1)<=7): #limite inferior
                    front_piece=matrix[(coord[0]+(i+1),coord[1])]['piece']#⬇⬇⬇
                    if (not front_piece):
                        self.possible_moves.append((coord[0]+(i+1),coord[1],'mov'))
                        i+=1
                    else:
                        i=2
                else:
                    i=2            
    
    def check_upper_right_edge(self, coord, matrix):
        if (coord[1]!=7 and coord[0]!=0):
            front_right_piece = matrix[(coord[0]-1,coord[1]+1)]['piece']
            if (front_right_piece and front_right_piece.color != self.color):
                self.possible_moves.append((coord[0]-1,coord[1]+1,'mov'))
        
    def check_upper_left_edge(self, coord, matrix):
        if (coord[1]!=0 and coord[0]!=0): 
            front_left_piece = matrix[(coord[0]-1,coord[1]-1)]['piece']
            if (front_left_piece and front_left_piece.color != self.color):
                self.possible_moves.append((coord[0]-1,coord[1]-1,'mov'))

    def check_lower_right_edge(self, coord, matrix):
        if (coord[1]!=7 and coord[0]!=7):
            bottom_right_piece = matrix[(coord[0]+1,coord[1]+1)]['piece']
            if (bottom_right_piece and bottom_right_piece.color != self.color):
                self.possible_moves.append((coord[0]+1,coord[1]+1,'mov'))

    def check_lower_left_edge(self, coord, matrix):
        if (coord[1]!=0 and coord[0]!=7):
            bottom_left_piece = matrix[(coord[0]+1,coord[1]-1)]['piece']
            if(bottom_left_piece and bottom_left_piece.color != self.color):
                self.possible_moves.append((coord[0]+1,coord[1]-1,'mov'))