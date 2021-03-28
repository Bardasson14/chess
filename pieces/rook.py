from .piece import Piece

class Rook(Piece):
    
    def __init__(self, color, name):
        self.sprite_dir = 'assets/img/' + color + 'Rook.png'
        self.name = name
        super(Rook,self).__init__(color,name)
    
    def get_possible_moves(self, coord, matrix):
        self.possible_moves = []
        self.mov_h(coord, matrix)
        self.mov_v(coord, matrix)
        return self.possible_moves

    def mov_v(self,coord,matrix):
        self.check_upper(coord, matrix)
        self.check_lower(coord, matrix)
    
    def mov_h(self,coord,matrix):
        self.check_left(coord, matrix)
        self.check_right(coord, matrix)
    
    def check_upper(self, coord, matrix):
        for i in range(1,8):
            if (coord[0]-i >= 0):
                piece = matrix[(coord[0]-i,coord[1])]['piece']
                if (not piece):
                    self.possible_moves.append((coord[0]-i,coord[1],'mov'))
                elif (piece and piece.color != self.color):
                    self.possible_moves.append((coord[0]-i,coord[1],'mov'))
                    break
                else:
                    break
    
    def check_lower(self, coord, matrix):
        for i in range(1,8):
            if (coord[0] + i <= 7):
                piece = matrix[(coord[0]+i,coord[1])]['piece']
                if (not piece):
                    self.possible_moves.append((coord[0]+i,coord[1],'mov'))
                elif (piece and piece.color != self.color):
                    self.possible_moves.append((coord[0]+i,coord[1],'mov'))
                    break
                else:
                    break

    def check_right(self, coord, matrix):
        for i in range(1,8):
            if (coord[1] + i <= 7):
                piece = matrix[(coord[0],coord[1]+i)]['piece']
                if (not piece):
                    self.possible_moves.append((coord[0],coord[1]+i,'mov'))
                elif(piece and piece.color != self.color):
                    self.possible_moves.append((coord[0],coord[1]+i,'mov'))
                    break
                else:
                    break

    def check_left(self, coord, matrix):
        for i in range(1,8):
            if (coord[1] - i >= 0):
                piece = matrix[(coord[0],coord[1]-i)]['piece']
                if (not piece):
                    self.possible_moves.append((coord[0],coord[1]-i,'mov'))
                elif(piece and piece.color != self.color):
                    self.possible_moves.append((coord[0],coord[1]-i,'mov'))
                    break
                else:
                    break