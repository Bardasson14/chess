from utils import get_piece_type, piece_in
from game_state import GameState
from time import time

class GameRules:

    def check_all(self, matrix, coord):
        return self.regular_checks(matrix, coord) or self.diagonal_checks(matrix, coord)

    def regular_checks(self, matrix, coord):
        return self.vertical_check(matrix, coord, 'lower') or self.vertical_check(matrix, coord, 'up') or self.horizontal_check(matrix, coord, 'left') or self.horizontal_check(matrix, coord, 'right')    

    def diagonal_checks(self, matrix, coord):
        string_modes = ['upper_left', 'upper_right', 'lower_left', 'lower_right']
        for mode in string_modes:
            if self.diagonal_check(matrix, coord, mode) or self.knight_check(matrix, coord, mode):
                return True
        return False

    def vertical_check(self, matrix, coord, string_mode): 
        # string_mode = 'up' or 'lower'
        mode = {'lower': 1, 'up': -1} 
        ##print(string_mode)

        current_king = matrix[coord]['piece']
        for i in range(1,8):
            if (self.check_vertical_boundaries(coord, string_mode, i)):
                piece = matrix[(coord[0]+(mode[string_mode])*i, coord[1])]['piece']
                if (piece and piece.color != current_king.color) and (get_piece_type(piece.name) in ['rook', 'queen']):
                    return True
                elif (piece and piece.color == current_king.color):
                    break
        return False

    def check_vertical_boundaries(self, coord, string_mode, i):
        if string_mode == 'up':
            return (coord[0] - i) >= 0
        return (coord[0] + i) <= 7

    def horizontal_check(self, matrix, coord, string_mode):
        # string_mode = 'left' or 'right'
        mode = {'left': -1, 'right':1}
        current_king = matrix[coord]['piece']

        for i in range(1,8):
            if (self.check_horizontal_boundaries(coord, string_mode, i)):
                piece = matrix[(coord[0],coord[1]+mode[string_mode]*i)]['piece']
                if ((piece and piece.color != current_king.color) and (get_piece_type(piece.name) in ['rook', 'queen'])):
                    return True
                elif(piece and piece.color == current_king.color):
                    break
        return False
        
    def check_horizontal_boundaries(self, coord, string_mode, i):
        if string_mode == 'left':
            return (coord[1] - i) >= 0
        return (coord[1] + i) <= 7


    def diagonal_check(self, matrix, coord, string_mode):
        # string_mode = 'upper_left', 'lower_left', 'upper_right', 'lower_right'
        mode = {'upper_left': (-1,-1), 'lower_left': (1, -1), 'upper_right': (-1, 1), 'lower_right': (1,1)}
        selected_mode = mode[string_mode]
        current_king = matrix[coord]['piece']
        for i in range(1,8):

            if (self.check_diagonal_boundaries(coord, string_mode, i)):
                piece = matrix[(coord[0] + selected_mode[0]*i, coord[1] + selected_mode[1]*i)]['piece']
                

                if(piece and (piece.color != current_king.color)) :
                    print(piece.color)
                    print(get_piece_type(piece.name))
                    print(string_mode.split('_')[0])

                    if (get_piece_type(piece.name) in ['bishop', 'queen']) or (get_piece_type(piece.name) == 'pawn' and ((piece.color == 'white' and string_mode.split('_')[0] == 'lower') or (piece.color=='black' and string_mode.split('_')[0] == 'upper'))):
                        return True
                    
                    elif((piece and piece.color == current_king.color)):
                        break
        return False

    def check_diagonal_boundaries(self, coord, string_mode, i):
        if string_mode == 'upper_left':
            return coord[0]-i >= 0 and coord[1]-i >= 0
        elif string_mode == 'upper_right':
            return coord[0]-i >= 0 and coord[1]+i <= 7 
        elif string_mode == 'lower_left':
            return coord[0]+i <= 7 and coord[1]-i >= 0
        return coord[0]+i <= 7 and coord[1]+i <= 7

    def knight_check(self, matrix, coord, string_mode):
        mode = {'upper_left': (-2, -1), 'upper_right': (-2, 1), 'lower_left': (2,-1), 'lower_right': (2,1)}
        reverse_mode = {'upper_left': (-2, -1), 'upper_right': (2, -1), 'lower_left': (-2,1), 'lower_right': (2,1)}
        x = mode[string_mode][0]
        y = mode[string_mode][1]
        reverse_x = reverse_mode[string_mode][0]
        reverse_y = reverse_mode[string_mode][1]
        current_king = matrix[coord]['piece']
        ##print(coord)
        # ##print(x,y)
    
        if (self.check_knight_boundaries(coord, string_mode)[0]):
            piece = matrix[(coord[0]+x, coord[1]+y)]['piece']
            if ((piece and piece.color != current_king.color) and (get_piece_type(piece.name)=='knight')):
                return True

        if (self.check_knight_boundaries(coord, string_mode)[1]):
            piece = matrix[(coord[0]+reverse_y, coord[1]+reverse_x)]['piece']
            if ((piece and piece.color != current_king.color) and (get_piece_type(piece.name)=='knight')):
                return True

        return False

    def check_knight_boundaries(self, coord, string_mode):
        ##print('knight', string_mode)
        if string_mode == 'upper_left':
            return [coord[0]-2 >= 0 and coord[1]-1 >= 0, coord[1]-2 >=0 and coord[0]-1 >=0]
        elif string_mode == 'upper_right':
            return [coord[0]-2 >= 0 and coord[1]+1 <= 7, coord[1]+2 <=7 and coord[0]-1 >=0 and coord[0]<7]
        elif string_mode == 'lower_left':
            return [coord[0]+2 <= 7 and coord[1]-1 >=0, coord[0]+1 <= 7 and coord[1]-2 >=0]
        return [coord[0]+2 <= 7 and coord[1]+1 <=7, coord[0]+1 <= 7 and coord[1]+2 <= 7]
    