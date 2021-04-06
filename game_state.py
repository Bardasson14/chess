class GameState:
    possible_en_passant = None
    first_move = True
    player='white'#indica o turno
    
    def __init__(self, board, players):
        self.board = board
        self.players = players
        self.board.position_pieces(players[0])
        self.board.position_pieces(players[1])


        
    @classmethod
    def troca(self):
        if(self.player=='white'):
                self.player='black'
        else:
            self.player='white'

    @classmethod
    def turno(self,color):
        #print(self.player)
        r=(self.player==color)
        return r
