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
                if(piece and (piece.color != current_king.color)) :
                    print(piece.color)
                    print(get_piece_type(piece.name))
                    print(string_mode.split('_')[0])

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
        #print(coord)
        #print(x,y)
    
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
        p_moves = self.append_moves(color, matrix, coord)
        if(len(p_moves) > 0 and p_moves[0] == 0):
            p_moves.pop(0)
            list_aux = self.verify_squares_bottom(color, matrix, coord)
            if(len(list_aux) > 0):
                p_moves.extend(list_aux)
            else:
                p_moves = []
        elif(len(p_moves) > 0 and p_moves[0] == 1):
            p_moves.pop(0)
            list_aux = self.verify_squares_top(color, matrix, coord)
            if(len(list_aux) > 0):
                p_moves.extend(list_aux)
            else:
                p_moves = []
        elif(len(p_moves) > 0 and p_moves[0] == 2):
            p_moves.pop(0)
            list_aux = self.verify_squares_right(color, matrix, coord)
            if(len(list_aux) > 0):
                p_moves.extend(list_aux)
            else:
                p_moves = []
        elif(len(p_moves) > 0 and p_moves[0] == 3):
            p_moves.pop(0)
            list_aux = self.verify_squares_left(color, matrix, coord)
            if(len(list_aux) > 0):
                p_moves.extend(list_aux)
            else:
                p_moves = []               
        return p_moves    
        
    def append_moves(self, color, matrix, coord):
        aux = []
        aux.extend(self.king_left(color, matrix, coord))
        aux.extend(self.king_right(color, matrix, coord))
        aux.extend(self.king_top(color, matrix, coord))
        aux.extend(self.king_bottom(color, matrix, coord))
        return aux

    def king_top(self, color, matrix, coord):
        moves = []
        aux = False
        for i in range(1,8):
            if(coord[0]-i < 0):
                break
            else:
                piece = matrix[(coord[0]-i, coord[1])]['piece']
                if(piece and piece.color == color):
                    if(get_piece_type(piece.name) in ['king']):
                        aux = True
                        break
                    else:
                        break
                elif(not(piece)):
                    moves.append((coord[0]-i,coord[1], 'mov'))
                else:
                    break
        if(aux):
            moves.insert(0, 0)
            return moves
        else:
            moves = []
            return moves

    def king_bottom(self, color, matrix, coord):
        moves = []
        aux = False
        for i in range(1,8):
            if(coord[0]+i > 7):
                break
            else:
                piece = matrix[(coord[0]+i, coord[1])]['piece']
                if(piece and piece.color == color):
                    if(get_piece_type(piece.name) in ['king']):
                        aux = True
                        break
                    else:
                        break
                elif(not(piece)):
                    moves.append((coord[0]+i,coord[1], 'mov'))
                else:
                    break
        if(aux):
            moves.insert(0, 1)
            return moves
        else:
            moves = []
            return moves
        
    def king_left(self, color, matrix, coord):
        moves = []
        aux = False
        for i in range(1,8):
            if(coord[1]-i < 0):
                break
            else:
                piece = matrix[(coord[0], coord[1]-i)]['piece']
                if(piece and piece.color == color):
                    if(get_piece_type(piece.name) in ['king']):
                        aux = True
                        break
                    else:
                        break
                elif(not(piece)):
                    moves.append((coord[0],coord[1]-i, 'mov'))
                else:
                    break
        if(aux):
            moves.insert(0, 2)
            return moves
        else:
            moves = []
            return moves
    
    def king_right(self, color, matrix, coord):
        moves = []
        aux = False
        for i in range(1,8):
            if(coord[1]+i > 7):
                break
            else:
                piece = matrix[(coord[0], coord[1]+i)]['piece']
                if(piece and piece.color == color):
                    if(get_piece_type(piece.name) in ['king']):
                        aux = True
                        break
                    else:
                        break
                elif(not(piece)):
                    moves.append((coord[0],coord[1]+i, 'mov'))
                else:
                    break
        if(aux):
            moves.insert(0, 3)
            return moves
        else:
            moves = []
            return moves
    
    def verify_squares_bottom(self, color, matrix, coord):
        moves = []
        aux = False
        for i in range(1,8):
            if(coord[0]+i > 7):
                break
            else:
                piece = matrix[(coord[0]+i, coord[1])]['piece']
                if(not(piece)):
                    moves.append((coord[0]+i,coord[1], 'mov'))
                elif(piece and piece.color != color and (get_piece_type(piece.name) in ['rook', 'queen'])):
                    aux = True
                    moves.append((coord[0]+i,coord[1], 'mov'))
                    break
                else: 
                    break
        if(aux):
            return moves
        else:
            moves = []
            return moves

    def verify_squares_top(self, color, matrix, coord):
        moves = []
        aux = False
        for i in range(1,8):
            if(coord[0]-i < 0):
                break
            else:
                piece = matrix[(coord[0]-i, coord[1])]['piece']
                if(not(piece)):
                    moves.append((coord[0]-i,coord[1], 'mov'))
                elif(piece and piece.color and (get_piece_type(piece.name) in ['rook', 'queen'])):
                    aux = True
                    moves.append((coord[0]-i,coord[1], 'mov'))
                    break
                else: 
                    break
        if(aux):
            return moves
        else:
            moves = []
            return moves

    def verify_squares_right(self, color, matrix, coord):
        moves = []
        aux = False
        for i in range(1,8):
            if(coord[1]+i > 7):
                break
            else:
                piece = matrix[(coord[0], coord[1]+i)]['piece']
                if(not(piece)):
                    moves.append((coord[0],coord[1]+i, 'mov'))
                elif(piece and piece.color and (get_piece_type(piece.name) in ['rook', 'queen'])):
                    aux = True
                    moves.append((coord[0],coord[1]+i, 'mov'))
                    break
                else: 
                    break
        if(aux):
            return moves
        else:
            moves = []
            return moves

    def verify_squares_left(self, color, matrix, coord):
        moves = []
        aux = False
        for i in range(1,8):
            if(coord[1]-i < 0):
                break
            else:
                piece = matrix[(coord[0], coord[1]-i)]['piece']
                if(not(piece)):
                    moves.append((coord[0],coord[1]-i, 'mov'))
                elif(piece and piece.color and (get_piece_type(piece.name) in ['rook', 'queen'])):
                    aux = True
                    moves.append((coord[0],coord[1]-i, 'mov'))
                    break
                else: 
                    break
        if(aux):
            return moves
        else:
            moves = []
            return moves