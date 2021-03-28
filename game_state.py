# game-related state variables (i.e: turns)

class GameState:
    possible_en_passant = None
    first_move = True
    
    def __init__(self, board, players):
        self.board = board
        self.players = players
        self.board.positionPieces(players[0])
        self.board.positionPieces(players[1])   