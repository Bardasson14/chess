class GameState:
    possible_en_passant = None
    first_move = True
    blackcoord = (0,4)
    whitecoord = (7,4)
    white_king_checked = False
    black_king_checked = False

    player='white' #indica o turno
    
    def __init__(self, board, players):
        self.board = board
        self.players = players
        if (board is not None and players is not None): # workaround p/ facilitar o teste
            self.board.position_pieces(players[0])
            self.board.position_pieces(players[1])
        
    @classmethod
    def switch(self):
        if(self.player=='white'):
                self.player='black'
        else:
            self.player='white'

    @classmethod
    def turn(self,color):
        ##print(self.player)
        r=(self.player==color)
        return r
