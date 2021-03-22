from game_state import GameState

class SpecialMoves:

    @classmethod
    def enPassant(self, board, piece, row, col, ref):
        if (board.squares[(col+1, row)]['piece'] == GameState.possibleEnPassant):
            board.pieceCapture((col+1, row))
        else:
            board.pieceCapture((col+1, row))

    def pawnPromotion(board):
        pass

    #create menu 
    

    def castling(self):
        pass