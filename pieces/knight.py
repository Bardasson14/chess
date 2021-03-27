from .piece import Piece

class Knight(Piece):
    
    def __init__(self, color, name):
        self.spriteDir = 'assets/img/' + color + 'Knight.png'
        self.name = name
        super(Knight,self).__init__(color,name)


# UL = Uper Left
# UR = Uper Right
# LL = Lower Left
# LR = Lower Right

# 0 = linha
# 1 = coluna    

    def getPossibleMoves(self, coord, matrix):
        self.possibleMoves=[]
        self.movUL(coord,matrix)
        self.movUR(coord,matrix)
        self.movLL(coord,matrix)
        self.movLR(coord,matrix)
        return self.possibleMoves

    def movUL(self, coord, matrix):
        if (coord[0]-2 >= 0 and coord[1]-1 >= 0):
            f = matrix[(coord[0]-2,coord[1]-1)]['piece']
            if (not f):
                self.possibleMoves.append((coord[0]-2,coord[1]-1,'mov'))
            elif(f and f.color != self.color):
                self.possibleMoves.append((coord[0]-2,coord[1]-1,'mov'))
          
        
        if (coord[1]-2 >=0 and coord[0]-1 >=0):
            f = matrix[(coord[0]-1,coord[1]-2)]['piece']
            if (not f):
                self.possibleMoves.append((coord[0]-1,coord[1]-2,'mov'))
            elif(f and f.color != self.color):
                self.possibleMoves.append((coord[0]-1,coord[1]-2,'mov'))

    def movUR(self, coord, matrix):
        if (coord[0]-2 >= 0 and coord[1]+1 <= 7):
            f = matrix[(coord[0]-2,coord[1]+1)]['piece']
            if (not f):
                self.possibleMoves.append((coord[0]-2,coord[1]+1,'mov'))
            elif(f and f.color != self.color):
                self.possibleMoves.append((coord[0]-2,coord[1]+1,'mov'))
          
        
        if (coord[1]+2 <=7 and coord[0]-1 >=0):
            f = matrix[(coord[0]-1,coord[1]+2)]['piece']
            if (not f):
                self.possibleMoves.append((coord[0]-1,coord[1]+2,'mov'))
            elif(f and f.color != self.color):
                self.possibleMoves.append((coord[0]-1,coord[1]+2,'mov'))

    def movLL(self, coord, matrix):
        if (coord[0]+2 <= 7 and coord[1]-1 >=0):
            f = matrix[(coord[0]+2,coord[1]-1)]['piece']
            if (not f):
                self.possibleMoves.append((coord[0]+2,coord[1]-1,'mov'))
            elif(f and f.color != self.color):
                self.possibleMoves.append((coord[0]+2,coord[1]-1,'mov'))
          
        
        if (coord[0]+1 <= 7 and coord[1]-2 >=0):
            f = matrix[(coord[0]+1,coord[1]-2)]['piece']
            if (not f):
                self.possibleMoves.append((coord[0]+1,coord[1]-2,'mov'))
            elif(f and f.color != self.color):
                self.possibleMoves.append((coord[0]+1,coord[1]-2,'mov'))


    def movLR(self, coord, matrix):
        if (coord[0]+2 <= 7 and coord[1]+1 <=7):
            f = matrix[(coord[0]+2,coord[1]+1)]['piece']
            if (not f):
                self.possibleMoves.append((coord[0]+2,coord[1]+1,'mov'))
            elif(f and f.color != self.color):
                self.possibleMoves.append((coord[0]+2,coord[1]+1,'mov'))
          
        
        if (coord[0]+1 <= 7 and coord[1]+2 <= 7):
            f = matrix[(coord[0]+1,coord[1]+2)]['piece']
            if (not f):
                self.possibleMoves.append((coord[0]+1,coord[1]+2,'mov'))
            elif(f and f.color != self.color):
                self.possibleMoves.append((coord[0]+1,coord[1]+2,'mov'))


