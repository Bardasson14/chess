from .piece import Piece

class Rook(Piece):
    
    def __init__(self, color, name):
        self.spriteDir = 'assets/img/' + color + 'Rook.png'
        self.name = name
        super(Rook,self).__init__(color,name)
    
    def getPossibleMoves(self, coord, matrix):
        self.possibleMoves=[]
        self.movH(coord,matrix)
        self.movV(coord,matrix)
        return self.possibleMoves

    def movV(self,coord,matrix):
        self.checkUpper(coord, matrix)
        self.checkLower(coord, matrix)
    
    def movH(self,coord,matrix):
        self.checkLeft(coord,matrix)
        self.checkRight(coord,matrix)
    
    def checkUpper(self, coord, matrix):
        for i in range(1,8):
            if (coord[0] - i >= 0):
                f = matrix[(coord[0]-i,coord[1])]['piece']
                if (not f):
                    self.possibleMoves.append((coord[0]-i,coord[1],'mov'))
                elif(f and f.color != self.color):
                    self.possibleMoves.append((coord[0]-i,coord[1],'mov'))
                    break
                else:
                    break
    
    def checkLower(self, coord, matrix):
        for i in range(1,8):
            if (coord[0] + i <= 7):
                f = matrix[(coord[0]+i,coord[1])]['piece']
                if (not f):
                    self.possibleMoves.append((coord[0]+i,coord[1],'mov'))
                elif(f and f.color != self.color):
                    self.possibleMoves.append((coord[0]+i,coord[1],'mov'))
                    break
                else:
                    break

    def checkRight(self, coord, matrix):
        for i in range(1,8):
            if (coord[1] + i <= 7):
                f = matrix[(coord[0],coord[1]+i)]['piece']
                if (not f):
                    self.possibleMoves.append((coord[0],coord[1]+i,'mov'))
                elif(f and f.color != self.color):
                    self.possibleMoves.append((coord[0],coord[1]+i,'mov'))
                    break
                else:
                    break

    def checkLeft(self, coord, matrix):
        for i in range(1,8):
            if (coord[1] - i >= 0):
                f = matrix[(coord[0],coord[1]-i)]['piece']
                if (not f):
                    self.possibleMoves.append((coord[0],coord[1]-i,'mov'))
                elif(f and f.color != self.color):
                    self.possibleMoves.append((coord[0],coord[1]-i,'mov'))
                    break
                else:
                    break