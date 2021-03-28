from .piece import Piece
from game_state import GameState

class Pawn(Piece):

    # add boundary checking functions
    
    def __init__(self, color, name):
        self.spriteDir = 'assets/img/' + color + 'Pawn.png'
        self.name = name
        self.color=color
        super(Pawn,self).__init__(color,name)
        
    def getPossibleMoves(self, coord, matrix):
        self.possibleMoves=[]
        self.movD(coord, matrix)
        self.movV(coord, matrix)
        if (GameState.possible_en_passant):
            self.check_en_passant(coord, matrix)
        return self.possibleMoves

    def movV(self, coord, matrix): 
        #print(first_move)
        if (self.color == 'white'):
            self.checkUpperEdge(coord, matrix)
        else:
            self.checkLowerEdge(coord, matrix)

    def movD(self, coord, matrix):
        #print(first_move)
        if (self.color == 'white'):
            self.checkUpperLeftEdge(coord, matrix)
            self.checkUpperRightEdge(coord, matrix)   
        else: 
            self.checkLowerLeftEdge(coord, matrix)
            self.checkLowerRightEdge(coord, matrix)

    def check_en_passant(self, coord, matrix):
        # obs.: não é necessário checar as pretas, só as brancas podem dar en passant
        if (coord[1]-1>=0 and (coord[0], coord[1]-1) == GameState.possible_en_passant):
            self.possibleMoves.append((coord[0]-1, coord[1]-1,'mov'))
        elif (coord[1]+1<=7 and (coord[0], coord[1]+1) == GameState.possible_en_passant):
            self.possibleMoves.append((coord[0]-1, coord[1]+1,'mov'))

    def checkUpperEdge(self, coord, matrix):
        if (coord[0]-1>=0):
            f = matrix[(coord[0]-1,coord[1])]['piece'] 
            if (not f):
                self.possibleMoves.append((coord[0]-1,coord[1],'mov'))

        if not self.wasMovedBefore:
            i=0
            while(i<2):
                if(coord[0]-(i+1)>=0): # limite superior
                    f = matrix[(coord[0]-(i+1),coord[1])]['piece']    # ⬆⬆⬆
                    if (not f):
                        self.possibleMoves.append((coord[0]-(i+1),coord[1],'mov'))
                        i+=1
                    else:
                        i=2
                else: 
                    i=2

    def checkLowerEdge(self, coord, matrix):
        if (coord[0]+1<=7):
            b = matrix[(coord[0]+1,coord[1])]['piece']
            if (not b):
                self.possibleMoves.append((coord[0]+1,coord[1],'mov'))

        if not self.wasMovedBefore:
            i=0
            while(i<2):
                if(coord[0]+(i+1)<=7): #limite inferior
                    f=matrix[(coord[0]+(i+1),coord[1])]['piece']#⬇⬇⬇
                    if(not f):
                        self.possibleMoves.append((coord[0]+(i+1),coord[1],'mov'))
                        i+=1
                    else:
                        i=2
                else:
                    i=2            
    
    def checkUpperRightEdge(self, coord, matrix):
        if (coord[1]!=7 and coord[0]!=0):
            fr = matrix[(coord[0]-1,coord[1]+1)]['piece']
            if (fr and fr.color != self.color):
                self.possibleMoves.append((coord[0]-1,coord[1]+1,'mov'))
        
    def checkUpperLeftEdge(self, coord, matrix):
        if (coord[1]!=0 and coord[0]!=0): 
            fl = matrix[(coord[0]-1,coord[1]-1)]['piece']
            if (fl and fl.color != self.color):
                self.possibleMoves.append((coord[0]-1,coord[1]-1,'mov'))

    def checkLowerRightEdge(self, coord, matrix):
        if (coord[1]!=7 and coord[0]!=7):
            br = matrix[(coord[0]+1,coord[1]+1)]['piece']
            if (br and br.color != self.color):
                self.possibleMoves.append((coord[0]+1,coord[1]+1,'mov'))

    def checkLowerLeftEdge(self, coord, matrix):
        if (coord[1]!=0 and coord[0]!=7):
            bl = matrix[(coord[0]+1,coord[1]-1)]['piece']
            if(bl and bl.color != self.color):
                self.possibleMoves.append((coord[0]+1,coord[1]-1,'mov'))
