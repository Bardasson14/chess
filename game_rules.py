from utils import DIRECTIONS, get_piece_type, piece_in, possible_directions
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
                elif (piece):
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
                elif (piece):
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
                if(piece and (piece.color != current_king.color)):
                    
                    if (get_piece_type(piece.name) in ['bishop', 'queen']) or (get_piece_type(piece.name) == 'pawn' and ((piece.color == 'white' and string_mode.split('_')[0] == 'lower') or (piece.color=='black' and string_mode.split('_')[0] == 'upper'))):
                        return True

                elif(piece):
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
    
    def can_move(self, color, matrix, coord):

        possible_moves = self.append_moves(color, matrix, coord) # ok
        print("possible_moves", possible_moves)
        
        if (possible_moves):
            selected_dir = DIRECTIONS[possible_moves.pop(0)]
            list_aux = self.verify_squares(color, matrix, coord, selected_dir)
            print("Verificacao: ", list_aux)
            if (list_aux):
                return possible_moves + list_aux

        return []

    def append_moves(self, color, matrix, coord):
        dirs = possible_directions(matrix[coord]['piece']) 
        aux = []
        
        for direction in ['left', 'right', 'bottom', 'top']:
            aux += self.king_check(matrix, coord, direction, color)
        
        return aux
        
    def king_check(self, matrix, coord, string_mode, color):
        mode = {'left': (0, -1), 'top': (-1,0), 'right': (0,1), 'bottom': (1,0), 'upper_right': (-1,1), 'upper_left': (-1,-1), 'lower_right': (1,1), 'lower_left':(1,-1)} # talvez seja necessário trocar
        selected_mode = mode[string_mode]
        coord_aux = (coord[0]+selected_mode[0], coord[1]+selected_mode[1])
        moves = []
        aux = False

        for i in range(1,8):
            if(self.king_check_boundaries(coord, string_mode, i)):
                break
            else:
                piece = matrix[coord_aux]['piece']
                
                if(piece and piece.color == color):
                    if(get_piece_type(piece.name) == 'king'):
                        aux = True
                    break
                
                elif not piece:
                    moves.append((coord_aux[0], coord_aux[1], 'mov'))
                else:
                    break

        if(aux):
            # print(string_mode)
            # print(DIRECTIONS.index(string_mode))
            moves.insert(0, DIRECTIONS.index(string_mode))
            return moves

        return []
    

    def king_check_boundaries(self, coord, string_mode, i): # feita
        boundaries = {'left': coord[1]-i < 0, 'top': coord[0]-i < 0, 'right': coord[1]+i > 7, 'bottom': coord[0]+i > 7, 'upper_right': coord[0]-i < 0 or coord[1]+i > 7, 'upper_left': coord[0]-i < 0 or coord[1]-i < 0, 'lower_right': coord[0]+i > 7 or coord[1]+i > 7, 'lower_left': coord[0]+i > 7 or coord[1]-i < 0}
        return boundaries[string_mode]

    def verify_squares(self, color, matrix, coord, string_mode): # ok
        mode = {'left': (0, -1), 'top': (-1,0), 'right':(0,1), 'bottom':(1,0), 'upper_right': (-1,1), 'upper_left': (-1,-1), 'lower_right': (1,1), 'lower_left':(1,-1)}
        selected_mode = mode[string_mode]
        coord_aux = (coord[0]+selected_mode[0], coord[1]+selected_mode[1])
        moves = []
        aux = False
        piece_list = ['rook', 'queen'] if len(string_mode.split('_')) == 1 else ['bishop', 'queen']
        
        for i in range(1,8):
            if(self.king_check_boundaries(coord, string_mode, i)):
                break
            else:
                piece = matrix[coord_aux]['piece']
                if not piece:
                    moves.append((coord_aux[0], coord_aux[1],'mov'))
                elif(piece and piece.color != color and (get_piece_type(piece.name) in piece_list)):
                    aux = True
                    moves.append((coord_aux[0], coord_aux[1], 'mov'))
                    break
                else: 
                    break
        if(aux):
            return moves

        return []