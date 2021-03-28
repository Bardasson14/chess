class GameState:
    possible_en_passant = None
    first_move = True
    
    def __init__(self, board, players):
        self.board = board
        self.players = players
        self.board.position_pieces(players[0])
        self.board.position_pieces(players[1])   