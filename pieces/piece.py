class Piece:

    def __init__(self, color, name):
        self.wasMovedBefore = False
        self.possibleMoves = []
        self.spriteID = None
        self.name = name
        self.color = color
        self.selected = False

    def getPossibleMoves(self, coord, matrix):
        pass

    #movH- movimentacao horizontal
    #movD- movimentacao diagonal
    #movV- movimentacao vertical
    #movL- movimentacao cavalo
    #ncasa- 1->pode andar ate uma casa
    #       2->pode andar ate duas casas
    #       3->pode andar andar todas as casas disponiveis na direcao escolhida
    #coord- tupla coordenada da peca atual (row,column)
    #matrix- dicionario da classe board
    #peao- boolean indicando se a peca atual eh peao
    #sent-  1->top(⬆,↗,↖)
    #       2->bottom(↘,↙,⬇)
    #       3->top&bottom(↘,↙,⬇,⬆,↗,↖)

    def capture (self):
        pass
    
    def movL(self, coord, matrix): # cavalo
        pass
        
    def movH(self, coord, matrix):
        pass

    def movD(self, coord, matrix):
        pass

    def movV(self, coord, matrix): 
        pass


        
    