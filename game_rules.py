from utils import get_piece_type, piece_in
from game_state import GameState

class GameRules:

    def check_all(self, matrix, coord):
        return self.regular_checks(matrix, coord) or self.diagonal_checks(matrix, coord)

    def regular_checks(self, matrix, coord):
        return self.vertical_check(matrix, coord, 'lower') or self.vertical_check(matrix, coord, 'up') or self.horizontal_check(matrix, coord, 'left') or self.horizontal_check(matrix, coord, 'right')    

    def diagonal_checks(self, matrix, coord):
        string_modes = ['upper_left', 'lower_left', 'upper_right', 'lower_right']
        for mode in string_modes:
            if self.diagonal_check(matrix, coord, mode) or self.knight_check(matrix, coord, mode):
                return True
        return False 

    def vertical_check(self, matrix, coord, string_mode): 
        # string_mode = 'up' or 'lower'
        mode = {'lower': -1, 'up':1} 

        cur_piece = matrix[coord]['piece']
        for i in range(1,8):
            if (coord[0] - i >= 0):
                piece = matrix[(coord[0]+mode[string_mode]*i, coord[1])]['piece']
                if (piece and piece.color != cur_piece.color) and (get_piece_type(piece) in ['rook', 'queen']):
                    return True
                elif(piece and piece.color == cur_piece.color):
                    break
        return False

    def horizontal_check(self, matrix, coord, string_mode):
        # string_mode = 'left' or 'right'
        mode = {'left': -1, 'right':1}
        cur_piece = matrix[coord]['piece']

        for i in range(1,8):
            if (coord[0] + i <= 7):
                piece = matrix[(coord[0],coord[1]+mode[string_mode]*i)]['piece']
                if ((piece and piece.color != cur_piece.color) and (get_piece_type(piece) in ['rook', 'queen'])):
                    return True
                elif(piece and piece.color == cur_piece.color):
                    break
        return False

    def diagonal_check(self, matrix, coord, string_mode):
        # string_mode = 'upper_left', 'lower_left', 'upper_right', 'lower_right'
        mode = {'upper_left': (-1,-1), 'lower_left': (1, -1), 'upper_right': (-1, 1), 'lower_right': (1,1)}
        selected_mode = mode[string_mode]
        cur_piece = matrix[coord]['piece']
        print(selected_mode)
        print(coord)
        for i in range(1,8):
            if (self.check_diagonal_boundaries(coord, string_mode, i)):
                piece = matrix[(coord[0] + selected_mode[0]*i, coord[1] + selected_mode[1]*i)]['piece']
                if((piece and piece.color != cur_piece.color) and (get_piece_type(piece) in ['bishop', 'queen'])):
                    return True
                elif((piece and piece.color == cur_piece.color)):
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
        mode = {'upper_left': (-2, -1), 'lower_left': (2, -1), 'upper_right': (-2, 1), 'lower_right': (2,1)}
        x = mode[string_mode][0]
        y = mode[string_mode][1]
        cur_piece = matrix[coord]['piece']
        # print(x,y)
    
        if (self.check_knight_boundaries(coord, string_mode)[0]):
            piece = matrix[(coord[0]+x, coord[1]+y)]['piece']
            if((piece and piece.color != cur_piece.color) and (get_piece_type(piece)=='knight')):
                return True

        if (self.check_knight_boundaries(coord, string_mode)[1]):
            piece = matrix[(coord[0]+y, coord[1]+x)]['piece']
            if((piece and piece.color != cur_piece.color) and (get_piece_type(piece)=='knight')):
                return True

        return False

    def check_knight_boundaries(self, coord, string_mode):
        if string_mode == 'upper_right':
            return [coord[0]-2 >= 0 and coord[1]+1 <= 7, coord[1]+2 <=7 and coord[0]-1 >=0]
        elif string_mode == 'upper_left':
            return [coord[0]-2 >= 0 and coord[1]-1 >= 0, coord[1]-2 >=0 and coord[0]-1 >=0]
        elif string_mode == 'lower_left':
            return [coord[0]+2 <= 7 and coord[1]-1 >=0, coord[0]+1 <= 7 and coord[1]-2 >=0]
        return [coord[0]+2 <= 7 and coord[1]+1 <=7, coord[0]+1 <= 7 and coord[1]+2 <= 7]
