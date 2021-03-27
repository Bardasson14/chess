from .piece import Piece

class Bishop(Piece):
    
    def __init__(self, color, name):
        self.spriteDir = 'assets/img/' + color + 'Bishop.png'
        self.name = name
        super(Bishop,self).__init__(color,name)

    def getPossibleMoves(self, coord, matrix):
        self.possibleMoves=[]
        self.movD(coord,matrix)
        return self.possibleMoves


    def movD(self,coord,matrix):
        self.checkUpperLeft(coord, matrix)
        self.checkUpperRight(coord, matrix)
        self.checkLowerLeft(coord, matrix)
        self.checkLowerRight(coord, matrix)

    def checkUpperLeft(self, coord, matrix):
        for i in range(1,8):
            if (coord[0]-i >= 0 and coord[1]-i >= 0):
                f = matrix[(coord[0]-i,coord[1]-i)]['piece']
                if (not f):
                    self.possibleMoves.append((coord[0]-i,coord[1]-i,'mov'))
                elif(f and f.color != self.color):
                    self.possibleMoves.append((coord[0]-i,coord[1]-i,'mov'))
                    break
                else:
                    break

    def checkUpperRight(self, coord, matrix):
        for i in range(1,8):
            if (coord[0]-i >= 0 and coord[1]+i <= 7):
                f = matrix[(coord[0]-i,coord[1]+i)]['piece']
                if (not f):
                    self.possibleMoves.append((coord[0]-i,coord[1]+i,'mov'))
                elif(f and f.color != self.color):
                    self.possibleMoves.append((coord[0]-i,coord[1]+i,'mov'))
                    break
                else:
                    break
    
    def checkLowerRight(self, coord, matrix):
        for i in range(1,8):
            if (coord[0]+i <= 7 and coord[1]+i <= 7):
                f = matrix[(coord[0]+i,coord[1]+i)]['piece']
                if (not f):
                    self.possibleMoves.append((coord[0]+i,coord[1]+i,'mov'))
                elif(f and f.color != self.color):
                    self.possibleMoves.append((coord[0]+i,coord[1]+i,'mov'))
                    break
                else:
                    break
    
    def checkLowerLeft(self, coord, matrix):
        for i in range(1,8):
            if (coord[0]+i <= 7 and coord[1]-i >= 0):
                f = matrix[(coord[0]+i,coord[1]-i)]['piece']
                if (not f):
                    self.possibleMoves.append((coord[0]+i,coord[1]-i,'mov'))
                elif(f and f.color != self.color):
                    self.possibleMoves.append((coord[0]+i,coord[1]-i,'mov'))
                    break
                else:
                    break