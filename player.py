from pieces import bishop, king, knight, pawn, queen, rook

COLORS = ['black',  'white']

class Player:

    def __init__(self, color):
        #0 - white
        #1 - black
        self.color = color
        self.remainingPieces = 16
        self.pieces = generatePieceList(color)
       
def generatePieceList(color):
    pieceList = []
    print(color)
    pieceList.append(king.King(COLORS[color], COLORS[color] + '_king'))
    pieceList.append(queen.Queen(COLORS[color], COLORS[color] + '_queen'))
    
    for i in range(2):    
        pieceList.append(rook.Rook(COLORS[color], COLORS[color] + '_rook_' + str(i+1)))
    for i in range(2):
        pieceList.append(bishop.Bishop(COLORS[color], COLORS[color] + '_bishop_' + str(i+1)))
    for i in range(2):
        pieceList.append(knight.Knight(COLORS[color], COLORS[color] + '_knight_' + str(i+1)))
    
    for i in range(8):
        pieceList.append(pawn.Pawn(COLORS[color], COLORS[color] + '_pawn_' + str(i+1)))

    return pieceList