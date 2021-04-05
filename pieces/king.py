from .piece import Piece
from game_state import GameState

class King(Piece):
    
    def __init__(self, color, name):
        self.sprite_dir = 'assets/img/' + color + 'King.png'
        self.name = name
        super(King,self).__init__(color,name)

    def kingCheck(self, coord, matrix):
        if(self.topCheck(coord, matrix)):
            return 1
        elif(self.bottomCheck(coord, matrix)):
            return 1
        elif(self.rightCheck(coord, matrix)):
            return 1
        elif(self.letfCheck(coord, matrix)):
            return 1
        elif(self.topleftCheck(coord, matrix)):
            return 1
        elif(self.toprightCheck(coord, matrix)):
            return 1
        elif(self.bottomleftCheck(coord, matrix)):
            return 1
        elif(self.bottomrightCheck(coord, matrix)):
            return 1
        elif(self.ulCheck(coord, matrix)):
            return 1
        elif(self.urCheck(coord, matrix)):
            return 1
        elif(self.lrCheck(coord, matrix)):
            return 1
        elif(self.llCheck(coord, matrix)):
            return 1
        else:
            return 0

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
    
    def little_roque(self, coord, matrix):
        if(not(self.was_moved_before)):
            for i in range(1,4):
                if (coord[1] + i <= 7):
                    piece = matrix[(coord[0],coord[1]+i)]['piece']
                    if (piece and piece.color==self.color):
                        if((coord[1] + i)==7 and (piece.name=='white_rook_2'or piece.name=='black_rook_2') and not (piece.was_moved_before)):
                            self.possible_moves.append((coord[0], coord[1]+i-1, 'lr'))
                        else:
                            #print(piece.name)
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
                            #print(piece.name)
                            break

    def roque(self,coord,matrix):
        self.big_roque(coord,matrix)
        self.little_roque(coord,matrix)
        
    def get_possible_moves(self, coord, matrix):
        self.possible_moves=[]
        self.kingPosition(matrix)
        self.mov_d(coord, matrix)
        self.mov_v(coord, matrix)
        self.mov_h(coord, matrix)
        self.roque(coord,matrix)
        self.kingPosition(matrix)
        print(self.possible_moves)
        return self.possible_moves

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
            if(self.kingCheck((coord[0]-1,coord[1]), matrix)):
                return 1 
            else:
                piece = matrix[(coord[0]-1,coord[1])]['piece']
                if ((piece and piece.color!=self.color) or (not piece)):
                    self.possible_moves.append((coord[0]-1,coord[1],'mov'))
                return 0 
    
    def check_lower_edge(self, coord, matrix):
        if (coord[0]+1<=7): #limite inferior
            if(self.kingCheck((coord[0]+1,coord[1]), matrix)):
                return 1 
            else:
                b = matrix[(coord[0]+1,coord[1])]['piece']    #⬇⬇⬇
                if (b and b.color!=self.color or (not b)):
                    self.possible_moves.append((coord[0]+1,coord[1],'mov'))
                return 0
    
    def check_right_edge(self, coord, matrix):
        if(coord[1]+1<=7): 
            if(self.kingCheck((coord[0],coord[1]+1), matrix)):
                return 1 
            else:
                right_piece = matrix[(coord[0],coord[1]+1)]['piece']
                if (right_piece and (right_piece.color != self.color)):
                    self.possible_moves.append((coord[0],coord[1]+1,'mov'))
                elif not right_piece:
                    self.possible_moves.append((coord[0],coord[1]+1,'mov'))
                return 0

    def check_left_edge(self, coord, matrix):
        if(coord[1]-1>=0):
            if(self.kingCheck((coord[0],coord[1]-1), matrix)):
                return 1 
            else:
                left_piece = matrix[(coord[0],coord[1]-1)]['piece'] 
                if (left_piece and left_piece.color!=self.color or (not left_piece)):
                    self.possible_moves.append((coord[0],coord[1]-1,'mov'))
                return 0

    def check_upper_right_edge(self, coord, matrix):
        if(coord[1]!=7 and coord[0]!=0):
            if(self.kingCheck((coord[0]-1,coord[1]+1), matrix)):
                return 1 
            else:
                front_right_piece = matrix[(coord[0]-1,coord[1]+1)]['piece']
                if ((front_right_piece and front_right_piece.color!=self.color) or (not front_right_piece)):
                    self.possible_moves.append((coord[0]-1,coord[1]+1,'mov'))
                return 0

    def check_upper_left_edge(self, coord, matrix):
        if(coord[1]!=0 and coord[0]!=0):
            if(self.kingCheck((coord[0]-1,coord[1]-1), matrix)):
                return 1 
            else:
                front_left_piece = matrix[(coord[0]-1,coord[1]-1)]['piece']
                if((front_left_piece and front_left_piece.color!=self.color) or (not front_left_piece)) :
                    self.possible_moves.append((coord[0]-1,coord[1]-1,'mov'))
                return 0

    def check_lower_right_edge(self, coord, matrix):
        if(coord[1]!=7 and coord[0]!=7):
            if(self.kingCheck((coord[0]+1,coord[1]+1), matrix)):
                return 1 
            else:
                bottom_right_piece = matrix[(coord[0]+1,coord[1]+1)]['piece']
                if(bottom_right_piece and bottom_right_piece.color!=self.color or (not bottom_right_piece)):
                    self.possible_moves.append((coord[0]+1,coord[1]+1,'mov'))
                return 0

    def check_lower_left_edge(self, coord, matrix):
        if(coord[1]!=0 and coord[0]!=7):
            if(self.kingCheck((coord[0]+1,coord[1]-1), matrix)):
                return 1 
            else:
                bottom_left_piece = matrix[(coord[0]+1,coord[1]-1)]['piece']
                if((bottom_left_piece and bottom_left_piece.color!=self.color) or (not bottom_left_piece)):
                    self.possible_moves.append((coord[0]+1,coord[1]-1,'mov'))
                return 0