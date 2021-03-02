class Piece:

    def __init__(self, color, name):
        self.wasMovedBefore = False
        self.possibleMoves = []
        self.spriteID = None
        self.name = name
    
    def getPossibleMoves(self, coord, matrix):# essa função deve retornar um vetor de tuplas(x,y)
                                              # que indicam as possíveis coordenadas da movimentação de uma peça
                                              # considerando suas regras de movimentação
        # possibleMoves=[]
        # if(self.wasMovedBefore):
        #     aux=int(coord[0])+1
        #     aux2=str(aux)+coord[1]
        #     possibleMoves.append((aux2))
        # else:
        #     for i in range(2):
        #         aux=int(coord[0])+i+1
        #         aux2=str(aux)+coord[1]
        #         possibleMoves.append(aux2)
        # return possibleMoves
        pass
