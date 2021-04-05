from .piece import Piece
from game_state import GameState

class Bishop(Piece):
    
    def __init__(self, color, name):
        self.sprite_dir = 'assets/img/' + color + 'Bishop.png'
        self.name = name
        super(Bishop,self).__init__(color,name)

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

    def get_possible_moves(self, coord, matrix):
        self.possible_moves = []
        self.kingPosition(matrix)
        if(self.color == 'white'):
            if(self.kingCheck(GameState.whitecoord, matrix) == 1):
                print("O rei está em xeque")
            else:
                self.mov_d(coord,matrix)
        else:
            if(self.kingCheck(GameState.blackcoord, matrix)):
                print("O rei está em xeque")
            else:
                self.mov_d(coord,matrix)
        return self.possible_moves

    def kingPosition(self, matrix):
        for i in range(1,8):
            for j in range(1,8):
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

    def mov_d(self, coord, matrix):
        self.check_upper_left(coord, matrix)
        self.check_upper_right(coord, matrix)
        self.check_lower_left(coord, matrix)
        self.check_lower_right(coord, matrix)

    def check_upper_left(self, coord, matrix):
        for i in range(1,8):
            if (coord[0]-i >= 0 and coord[1]-i >= 0):
                piece = matrix[(coord[0]-i, coord[1]-i)]['piece']
                if (not piece):
                    self.possible_moves.append((coord[0]-i, coord[1]-i, 'mov'))
                elif (piece and piece.color != self.color):
                    self.possible_moves.append((coord[0]-i, coord[1]-i, 'mov'))
                    break
                else:
                    break

    def check_upper_right(self, coord, matrix):
        for i in range(1,8):
            if (coord[0]-i >= 0 and coord[1]+i <= 7):
                piece = matrix[(coord[0]-i, coord[1]+i)]['piece']
                if (not piece):
                    self.possible_moves.append((coord[0]-i, coord[1]+i, 'mov'))
                elif (piece and piece.color != self.color):
                    self.possible_moves.append((coord[0]-i, coord[1]+i, 'mov'))
                    break
                else:
                    break
    
    def check_lower_right(self, coord, matrix):
        for i in range(1,8):
            if (coord[0]+i <= 7 and coord[1]+i <= 7):
                piece = matrix[(coord[0]+i, coord[1]+i)]['piece']
                if (not piece):
                    self.possible_moves.append((coord[0]+i,coord[1]+i,'mov'))
                elif (piece and piece.color != self.color):
                    self.possible_moves.append((coord[0]+i,coord[1]+i,'mov'))
                    break
                else:
                    break
    
    def check_lower_left(self, coord, matrix):
        for i in range(1,8):
            if (coord[0]+i <= 7 and coord[1]-i >= 0):
                piece = matrix[(coord[0]+i, coord[1]-i)]['piece']
                if (not piece):
                    self.possible_moves.append((coord[0]+i, coord[1]-i, 'mov'))
                elif (piece and piece.color != self.color):
                    self.possible_moves.append((coord[0]+i, coord[1]-i, 'mov'))
                    break
                else:
                    break