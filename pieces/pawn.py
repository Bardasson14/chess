from .piece import Piece
from game_state import GameState

class Pawn(Piece):

    # add boundary checking functions
    
    def __init__(self, color, name):
        self.sprite_dir = 'assets/img/' + color + 'Pawn.png'
        self.name = name
        self.color=color
        super(Pawn,self).__init__(color,name)

    def kingCheck(self, coord, matrix):
        if(self.h_Check(coord, matrix) or self.v_Check(coord, matrix) or self.d_Check(coord, matrix) or self.l_Check(coord, matrix)):
            return 1
        else:
            return 0
    
    def h_Check(self, coord, matrix):
        return self.letfCheck(coord, matrix) or self.rightCheck(coord, matrix)
    
    def v_Check(self, coord, matrix):
        return self.topCheck(coord, matrix) or self.bottomCheck(coord, matrix)

    def d_Check(self, coord, matrix):
        return self.topleftCheck(coord, matrix) or self.toprightCheck(coord, matrix) or self.bottomleftCheck(coord, matrix) or self.bottomrightCheck(coord, matrix)
    
    def l_Check(self, coord, matrix):
        return self.ulCheck(coord, matrix) or self.urCheck(coord, matrix) or self.lrCheck(coord, matrix) or self.llCheck(coord, matrix)

    def get_possible_moves(self, coord, matrix):
        self.possible_moves=[]
        self.kingPosition(matrix)
        if(self.color == 'white'):
            if(self.kingCheck(GameState.whitecoord, matrix) == 1):
                print("O rei está em xeque")
            else:
                self.mov_d(coord, matrix)
                self.mov_v(coord, matrix)
            if (GameState.possible_en_passant):
                self.check_en_passant(coord, matrix)
        else:
            if(self.kingCheck(GameState.blackcoord, matrix)):
                print("O rei está em xeque")
            else:
                self.mov_d(coord, matrix)
                self.mov_v(coord, matrix)
            if (GameState.possible_en_passant):
                self.check_en_passant(coord, matrix)
        return self.possible_moves

    def kingPosition(self, matrix):
        for i in range(8):
            for j in range(8):
                piece = matrix[(i, j)]['piece']
                if(self.color == 'white' and piece):
                    if(piece.name == 'white_king'):
                        GameState.whitecoord = (i,j)
                if(self.color == 'black' and piece):
                    if(piece.name == 'black_king'):
                        GameState.blackcoord = (i,j)

    def topCheck(self, coord, matrix):#checa se o rei está em xeque por cima
        for i in range(1,8):
            if (coord[0] - i >= 0):
                piece = matrix[(coord[0]-i,coord[1])]['piece']
                if((piece and piece.color != self.color) and (piece.name == 'black_queen' or piece.name == 'black_rook_2' or piece.name == 'black_rook_1')):
                    return 1
                elif((piece and piece.color != self.color) and (piece.name == 'white_queen' or piece.name == 'white_rook_2' or piece.name == 'white_rook_1')):
                    return 1
                elif((piece and piece.color == self.color)):
                    break
        return 0
    
    def bottomCheck(self, coord, matrix):#checha se o rei está em xeque por baixo
        for i in range(1,8):
            if (coord[0] + i <= 7):
                piece = matrix[(coord[0]+i,coord[1])]['piece']
                # print("\n"+piece.name+"\n")
                if((piece and piece.color != self.color) and (piece.name == 'black_queen' or piece.name == 'black_rook_2' or piece.name == 'black_rook_1')):
                    return 1
                elif((piece and piece.color != self.color) and (piece.name == 'white_queen' or piece.name == 'white_rook_2' or piece.name == 'white_rook_1')):
                    return 1
                elif((piece and piece.color == self.color)):
                    break
        return 0

    def rightCheck(self, coord, matrix):#checa se o rei está em xeque pela direita
        for i in range(1,8): 
            if (coord[1] + i <= 7):
                piece = matrix[(coord[0],coord[1]+i)]['piece']
                if((piece and piece.color != self.color) and (piece.name == 'black_queen' or piece.name == 'black_rook_2' or piece.name == 'black_rook_1')):
                    return 1
                elif((piece and piece.color != self.color) and (piece.name == 'white_queen' or piece.name == 'white_rook_2' or piece.name == 'white_rook_1')):
                    return 1
                elif((piece and piece.color == self.color)):
                    break
        return 0
    
    def letfCheck(self, coord, matrix):#checa se o rei está em xeque pela esquerda
        for i in range(1,8):
            if (coord[1] - i >= 0):
                piece = matrix[(coord[0],coord[1]-i)]['piece']
                if((piece and piece.color != self.color) and (piece.name == 'black_queen' or piece.name == 'black_rook_2' or piece.name == 'black_rook_1')):
                    return 1
                elif((piece and piece.color != self.color) and (piece.name == 'white_queen' or piece.name == 'white_rook_2' or piece.name == 'white_rook_1')):
                    return 1
                elif((piece and piece.color == self.color)):
                    break
        return 0
    
    def topleftCheck(self, coord, matrix):
        for i in range(1,8):
            if (coord[0]-i >= 0 and coord[1]-i >= 0):
                piece = matrix[(coord[0]-i,coord[1]-i)]['piece']
                if((piece and piece.color != self.color) and (piece.name == 'black_queen' or piece.name == 'black_bishop_2' or piece.name == 'black_bishop_1')):
                    return 1
                elif((piece and piece.color != self.color) and (piece.name == 'white_queen' or piece.name == 'white_bishop_2' or piece.name == 'white_bishop_1')):
                    return 1
                elif((piece and piece.color == self.color)):
                    break
        return 0
    
    def toprightCheck(self, coord, matrix):
        for i in range(1,8):
            if (coord[0]-i >= 0 and coord[1]+i <= 7):
                piece = matrix[(coord[0]-i,coord[1]+i)]['piece']
                if((piece and piece.color != self.color) and (piece.name == 'black_queen' or piece.name == 'black_bishop_2' or piece.name == 'black_bishop_1')):
                    return 1
                elif((piece and piece.color != self.color) and (piece.name == 'white_queen' or piece.name == 'white_bishop_2' or piece.name == 'white_bishop_1')):
                    return 1
                elif((piece and piece.color == self.color)):
                    break
    
    def bottomleftCheck(self, coord, matrix):
        for i in range(1,8):
            if (coord[0]+i <= 7 and coord[1]-i >= 0):
                piece = matrix[(coord[0]+i,coord[1]-i)]['piece']
                if((piece and piece.color != self.color) and (piece.name == 'black_queen' or piece.name == 'black_bishop_2' or piece.name == 'black_bishop_1')):
                    return 1
                elif((piece and piece.color != self.color) and (piece.name == 'white_queen' or piece.name == 'white_bishop_2' or piece.name == 'white_bishop_1')):
                    return 1
                elif((piece and piece.color == self.color)):
                    break

    def bottomrightCheck(self, coord, matrix):
        for i in range(1,8):
            if (coord[0]+i <= 7 and coord[1]+i <= 7):
                piece = matrix[(coord[0]+i,coord[1]+i)]['piece']
                if((piece and piece.color != self.color) and (piece.name == 'black_queen' or piece.name == 'black_bishop_2' or piece.name == 'black_bishop_1')):
                    return 1
                elif((piece and piece.color != self.color) and (piece.name == 'white_queen' or piece.name == 'white_bishop_2' or piece.name == 'white_bishop_1')):
                    return 1
                elif((piece and piece.color == self.color)):
                    break
    
    def ulCheck(self, coord, matrix):
        if (coord[0]-2 >= 0 and coord[1]-1 >= 0):
            piece = matrix[(coord[0]-2,coord[1]-1)]['piece']
            if((piece and piece.color != self.color) and (piece.name == 'black_knight_2' or piece.name == 'black_knight_1')):
                return 1
            elif((piece and piece.color != self.color) and (piece.name == 'white_knight_2' or piece.name == 'white_knight_1')):
                return 1

        if (coord[1]-2 >=0 and coord[0]-1 >=0):
            piece = matrix[(coord[0]-1,coord[1]-2)]['piece']
            if((piece and piece.color != self.color) and (piece.name == 'black_knight_2' or piece.name == 'black_knight_1')):
                return 1
            elif((piece and piece.color != self.color) and (piece.name == 'white_knight_2' or piece.name == 'white_knight_1')):
                return 1
        return 0
    
    def urCheck(self, coord, matrix):
        if (coord[0]-2 >= 0 and coord[1]+1 <= 7):
            piece = matrix[(coord[0]-2,coord[1]+1)]['piece']
            if((piece and piece.color != self.color) and (piece.name == 'black_knight_2' or piece.name == 'black_knight_1')):
                return 1
            elif((piece and piece.color != self.color) and (piece.name == 'white_knight_2' or piece.name == 'white_knight_1')):
                return 1
        if (coord[1]+2 <=7 and coord[0]-1 >=0):
            piece = matrix[(coord[0]-1,coord[1]+2)]['piece']
            if((piece and piece.color != self.color) and (piece.name == 'black_knight_2' or piece.name == 'black_knight_1')):
                return 1
            elif((piece and piece.color != self.color) and (piece.name == 'white_knight_2' or piece.name == 'white_knight_1')):
                return 1
        return 0

    def llCheck(self, coord, matrix):
        if (coord[0]+2 <= 7 and coord[1]-1 >=0):
            piece = matrix[(coord[0]+2,coord[1]-1)]['piece']
            if((piece and piece.color != self.color) and (piece.name == 'black_bishop_2' or piece.name == 'black_bishop_1')):
                return 1
            elif((piece and piece.color != self.color) and (piece.name == 'white_bishop_2' or piece.name == 'white_bishop_1')):
                return 1
        if (coord[0]+1 <= 7 and coord[1]-2 >=0):
            piece = matrix[(coord[0]+1,coord[1]-2)]['piece']
            if((piece and piece.color != self.color) and (piece.name == 'black_bishop_2' or piece.name == 'black_bishop_1')):
                return 1
            elif((piece and piece.color != self.color) and (piece.name == 'white_bishop_2' or piece.name == 'white_bishop_1')):
                return 1
        return 0
    
    def lrCheck(self, coord, matrix):
        if (coord[0]+2 <= 7 and coord[1]+1 <=7):
            piece = matrix[(coord[0]+2,coord[1]+1)]['piece']
            if((piece and piece.color != self.color) and (piece.name == 'black_bishop_2' or piece.name == 'black_bishop_1')):
                return 1
            elif((piece and piece.color != self.color) and (piece.name == 'white_bishop_2' or piece.name == 'white_bishop_1')):
                return 1
        if (coord[0]+1 <= 7 and coord[1]+2 <= 7):
            piece = matrix[(coord[0]+1,coord[1]+2)]['piece']
            if((piece and piece.color != self.color) and (piece.name == 'black_bishop_2' or piece.name == 'black_bishop_1')):
                return 1
            elif((piece and piece.color != self.color) and (piece.name == 'white_bishop_2' or piece.name == 'white_bishop_1')):
                return 1
        return 0

    def mov_v(self, coord, matrix): 
        #print(first_move)
        if (self.color == 'white'):
            self.check_upper_edge(coord, matrix)
        else:
            self.check_lower_edge(coord, matrix)

    def mov_d(self, coord, matrix):
        #print(first_move)
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
