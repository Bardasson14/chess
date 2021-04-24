from pieces import bishop, king, knight, pawn, queen, rook

COLORS = ['black',  'white']

class Player:

    def __init__(self, color):
        #0 - white
        #1 - black
        self.color = color
        self.pieces = generate_piece_list(color)
       
def generate_piece_list(color):
    piece_list = []
    piece_list.append(king.King(COLORS[color], COLORS[color] + '_king'))
    piece_list.append(queen.Queen(COLORS[color], COLORS[color] + '_queen'))
    
    for i in range(2):    
        piece_list.append(rook.Rook(COLORS[color], COLORS[color] + '_rook_' + str(i+1)))
    for i in range(2):
        piece_list.append(bishop.Bishop(COLORS[color], COLORS[color] + '_bishop_' + str(i+1)))
    for i in range(2):
        piece_list.append(knight.Knight(COLORS[color], COLORS[color] + '_knight_' + str(i+1)))
    for i in range(8):
        piece_list.append(pawn.Pawn(COLORS[color], COLORS[color] + '_pawn_' + str(i+1)))

    return piece_list