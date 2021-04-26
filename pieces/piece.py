class Piece:

    def __init__(self, color, name):
        self.was_moved_before = False
        self.possible_moves = []
        self.sprite_ID = None
        self.name = name
        self.color = color
        self.selected = False

    def get_possible_moves(self, coord, matrix):
        pass

    def capture (self):
        pass
    
    def mov_l(self, coord, matrix): # cavalo
        pass
        
    def mov_h(self, coord, matrix):
        pass

    def mov_d(self, coord, matrix):
        pass

    def mov_v(self, coord, matrix): 
        pass


        
    