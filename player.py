from pieces import bishop, king, knight, pawn, queen, rook

COLORS = ['black',  'white']

class Player:

    def __init__(self, color):
        #0 - white
        #1 - black
        self.color = color
        self.remainingPieces = 16
        self.pieces = generatePieceList(COLORS[color])
       
def generatePieceList(color):
    print(color)
    pieceList = []

    pieceList.append(king.King(color))
    pieceList.append(queen.Queen(color))
    
    for i in range(2):    
        pieceList.append(rook.Rook(color))
        pieceList.append(bishop.Bishop(color))
        pieceList.append(knight.Knight(color))
    
    for i in range(8):
        pieceList.append(pawn.Pawn(color))

    return pieceList

