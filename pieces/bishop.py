from .piece import Piece

class Bishop(Piece):
    
    def __init__(self, color, name):
        self.sprite_dir = 'assets/img/' + color + 'Bishop.png'
        self.name = name
        super(Bishop,self).__init__(color,name)

    def get_possible_moves(self, coord, matrix):
        self.possible_moves=[]
        self.mov_d(coord,matrix)
        return self.possible_moves

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