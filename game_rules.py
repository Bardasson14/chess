from utils import INVERTED_DIRECTIONS, DIRECTIONS, get_piece_type, piece_in
from game_state import GameState
from time import time
from game_state import GameState

def check_all(matrix, coord, color):
    return regular_checks(matrix, coord, color) or diagonal_checks(matrix, coord, color)

def regular_checks(matrix, coord, color):
    return vertical_check(matrix, coord, 'lower', color) or vertical_check(matrix, coord, 'up', color) or horizontal_check(matrix, coord, 'left', color) or horizontal_check(matrix, coord, 'right', color)    

def diagonal_checks(matrix, coord, color):
    string_modes = ['upper_left', 'upper_right', 'lower_left', 'lower_right']
    for mode in string_modes:
        if diagonal_check(matrix, coord, mode, color) or knight_check(matrix, coord, mode, color):
            return True
    return False

def vertical_check(matrix, coord, string_mode, color): 
    # string_mode = 'up' or 'lower'
    mode = {'lower': 1, 'up': -1} 
    ###print(string_mode)
    if(color == 'white'):
        current_king = matrix[GameState.whitecoord]['piece']
    else:
        current_king = matrix[GameState.blackcoord]['piece']
    list_aux = []
    for i in range(1,8):
        if (check_vertical_boundaries(coord, string_mode, i)):
            piece = matrix[(coord[0]+(mode[string_mode])*i, coord[1])]['piece']
            list_aux.append((coord[0]+(mode[string_mode])*i, coord[1], 'mov')) #lista para fazer a interseção com o possible_moves caso o rei esteja em xeque
            if (piece and piece.color != current_king.color):
                if(get_piece_type(piece.name) in ['rook', 'queen']):
                    return list_aux
                else:
                    break
            elif(piece is not None):
                break
    return False

def check_vertical_boundaries(coord, string_mode, i):
    if string_mode == 'up':
        return (coord[0] - i) >= 0
    return (coord[0] + i) <= 7

def horizontal_check(matrix, coord, string_mode, color):
    # string_mode = 'left' or 'right'
    mode = {'left': -1, 'right':1}
    if(color == 'white'):
        current_king = matrix[GameState.whitecoord]['piece']
    else:
        current_king = matrix[GameState.blackcoord]['piece']
    list_aux = []
    for i in range(1,8):
        if (check_horizontal_boundaries(coord, string_mode, i)):
            piece = matrix[(coord[0],coord[1]+mode[string_mode]*i)]['piece']
            list_aux.append((coord[0],coord[1]+mode[string_mode]*i, 'mov'))
            if ((piece and piece.color != current_king.color)): 
                if(get_piece_type(piece.name) in ['rook', 'queen']):
                    return list_aux
                else:
                    break
            elif(piece is not None):
                break
    return False
    
def check_horizontal_boundaries(coord, string_mode, i):
    if string_mode == 'left':
        return (coord[1] - i) >= 0
    return (coord[1] + i) <= 7


def diagonal_check(matrix, coord, string_mode, color):
    # string_mode = 'upper_left', 'lower_left', 'upper_right', 'lower_right'
    mode = {'upper_left': (-1,-1), 'lower_left': (1, -1), 'upper_right': (-1, 1), 'lower_right': (1,1)}
    selected_mode = mode[string_mode]
    if(color == 'white'):
        current_king = matrix[GameState.whitecoord]['piece']
    else:
        current_king = matrix[GameState.blackcoord]['piece']
    list_aux = []
    for i in range(1,8):

        if (check_diagonal_boundaries(coord, string_mode, i)):
            coord_piece = (coord[0] + selected_mode[0]*i, coord[1] + selected_mode[1]*i)
            piece = matrix[coord_piece]['piece']
            diff = (abs(coord_piece[0] - coord[0]),abs(coord_piece[1] - coord[1]))
            list_aux.append((coord[0] + selected_mode[0]*i, coord[1] + selected_mode[1]*i, 'mov'))
            if(piece and (piece.color != current_king.color)):
                if (get_piece_type(piece.name) in ['bishop', 'queen']) or (get_piece_type(piece.name) == 'pawn' and ((piece.color == 'white' and string_mode.split('_')[0] == 'lower' and (diff[0] < 2 and diff[1] < 2)) or (piece.color=='black' and string_mode.split('_')[0] == 'upper' and (diff[0] < 2 and diff[1] < 2)))):
                    return list_aux
                else:
                    break

            elif(piece is not None):
                break
    return False

def check_diagonal_boundaries(coord, string_mode, i):
    if string_mode == 'upper_left':
        return coord[0]-i >= 0 and coord[1]-i >= 0
    elif string_mode == 'upper_right':
        return coord[0]-i >= 0 and coord[1]+i <= 7 
    elif string_mode == 'lower_left':
        return coord[0]+i <= 7 and coord[1]-i >= 0
    return coord[0]+i <= 7 and coord[1]+i <= 7

def knight_check(matrix, coord, string_mode, color):
    mode = {'upper_left': (-2, -1), 'upper_right': (-2, 1), 'lower_left': (2,-1), 'lower_right': (2,1)}
    reverse_mode = {'upper_left': (-2, -1), 'upper_right': (2, -1), 'lower_left': (-2,1), 'lower_right': (2,1)}
    x = mode[string_mode][0]
    y = mode[string_mode][1]
    reverse_x = reverse_mode[string_mode][0]
    reverse_y = reverse_mode[string_mode][1]
    if(color == 'white'):
        current_king = matrix[GameState.whitecoord]['piece']
    else:
        current_king = matrix[GameState.blackcoord]['piece']
    list_aux = []
    if (check_knight_boundaries(coord, string_mode)[0]):
        piece = matrix[(coord[0]+x, coord[1]+y)]['piece']
        list_aux.append((coord[0]+x, coord[1]+y, 'mov'))
        if ((piece and piece.color != current_king.color) and (get_piece_type(piece.name)=='knight')):
            print(list_aux)
            return list_aux

    if (check_knight_boundaries(coord, string_mode)[1]):
        piece = matrix[(coord[0]+reverse_y, coord[1]+reverse_x)]['piece']
        list_aux.append((coord[0]+reverse_y, coord[1]+reverse_x, 'mov'))
        if ((piece and piece.color != current_king.color) and (get_piece_type(piece.name)=='knight')):
            print(list_aux)
            return list_aux

        return False

def check_knight_boundaries(coord, string_mode):
    ###print('knight', string_mode)
    if string_mode == 'upper_left':
        return [coord[0]-2 >= 0 and coord[1]-1 >= 0, coord[1]-2 >=0 and coord[0]-1 >=0]
    elif string_mode == 'upper_right':
        return [coord[0]-2 >= 0 and coord[1]+1 <= 7, coord[1]+2 <=7 and coord[0]-1 >=0 and coord[0]<7]
    elif string_mode == 'lower_left':
        return [coord[0]+2 <= 7 and coord[1]-1 >=0, coord[0]+1 <= 7 and coord[1]-2 >=0]
    return [coord[0]+2 <= 7 and coord[1]+1 <=7, coord[0]+1 <= 7 and coord[1]+2 <= 7]

def can_move(color, matrix, coord):

    limited_moves = append_moves(color, matrix, coord)
    
    if (limited_moves):
        selected_dir = DIRECTIONS[limited_moves.pop(0)]
        
        list_aux = verify_squares(color, matrix, coord, selected_dir)
        if (list_aux):
            return limited_moves + list_aux

    return []

def append_moves(color, matrix, coord):
    #dirs = possible_directions(matrix[coord]['piece']) 
    aux = []
    
    for direction in DIRECTIONS:
        aux += king_check(matrix, coord, direction, color)
    
    return aux
    
def king_check(matrix, coord, string_mode, color):
    mode = {'left': (0, -1), 'top': (-1,0), 'right': (0,1), 'bottom': (1,0), 'upper_right': (-1,1), 'upper_left': (-1,-1), 'lower_right': (1,1), 'lower_left':(1,-1)} # talvez seja necessário trocar
    selected_mode = mode[string_mode]
    coord_aux = (coord[0]+selected_mode[0], coord[1]+selected_mode[1])
    moves = []
    aux = False

    for i in range(1,8):
        if(king_check_boundaries(coord, string_mode, i)):
            return []
        else:
            piece = matrix[(coord[0]+selected_mode[0]*i , coord[1]+selected_mode[1]*i )]['piece']
            
            if(piece and piece.color == color):
                if(get_piece_type(piece.name) == 'king'):
                    print(moves)
                    moves.insert(0, INVERTED_DIRECTIONS.index(string_mode))
                    return moves
                return []
            elif not piece:
                moves.append((coord[0]+selected_mode[0]*i, coord[1]+selected_mode[1]*i, 'mov'))

    return []


def king_check_boundaries(coord, string_mode, i):
    boundaries = {'left': coord[1]-i < 0, 'top': coord[0]-i < 0, 'right': coord[1]+i > 7, 'bottom': coord[0]+i > 7, 'upper_right': coord[0]-i < 0 or coord[1]+i > 7, 'upper_left': coord[0]-i < 0 or coord[1]-i < 0, 'lower_right': coord[0]+i > 7 or coord[1]+i > 7, 'lower_left': coord[0]+i > 7 or coord[1]-i < 0}
    return boundaries[string_mode]

def verify_squares(color, matrix, coord, string_mode):
    mode = {'left': (0, -1), 'top': (-1,0), 'right':(0,1), 'bottom':(1,0), 'upper_right': (-1,1), 'upper_left': (-1,-1), 'lower_right': (1,1), 'lower_left':(1,-1)}
    selected_mode = mode[string_mode]
    # coord_aux = (coord[0]+selected_mode[0], coord[1]+selected_mode[1])
    moves = []
    # aux = False
    piece_list = ['rook', 'queen'] if len(string_mode.split('_')) == 1 else ['bishop', 'queen']
    
    for i in range(1,8):
        if(king_check_boundaries(coord, string_mode, i)):
            return []
        else:
            piece = matrix[coord[0] + iterate_board(i, string_mode)[0], coord[1] + iterate_board(i, string_mode)[1]]['piece']
            
            if not piece:
                moves.append((coord[0] + iterate_board(i, string_mode)[0], coord[1] + iterate_board(i, string_mode)[1], 'mov'))

            elif (piece and (get_piece_type(piece.name) in piece_list)):
                
                if (piece.color == color):
                    return 
                    
                moves.append((coord[0] + iterate_board(i, string_mode)[0], coord[1] + iterate_board(i, string_mode)[1], 'mov'))
                return moves

            # elif(piece and piece.color != color):
            #     moves.append((coord[0] + iterate_board(i, string_mode)[0], coord[1] + iterate_board(i, string_mode)[1], 'mov'))
            #     print(moves)
            #     return moves
            
            elif(piece):
                return

    return []

def iterate_board (i, string_mode):
    mode = {'left': (0, -i), 'top': (-i,0), 'right':(0,i), 'bottom':(i,0), 'upper_right': (-i,i), 'upper_left': (-i,-i), 'lower_right': (i,i), 'lower_left':(i,-i)}
    #print("iterate_board: ", mode[string_mode])
    return mode[string_mode]