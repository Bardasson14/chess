from .piece import Piece

class King(Piece):
    
    def __init__(self, color, name):
        self.spriteDir = 'assets/img/' + color + 'King.png'
        self.name = name
        super(King,self).__init__(color,name)

    def littleRoque(self,coord,matrix):
        for i in range(1,4):
            if (coord[1] + i <= 7):
                f = matrix[(coord[0],coord[1]+i)]['piece']
                if (f and f.color==self.color):
                    if((coord[1] + i)==7 and f.name=='white_rook_2'or f.name=='black_rook_2'):
                        self.possibleMoves.append((coord[0],coord[1]+i-1,'lr'))
                    else:
                        print(f.name)
                        break

    def bigRoque(self,coord,matrix):
        for i in range(1,5):
            if (coord[1] - i >= 0):
                if (coord[1] - i >= 0):
                    f = matrix[(coord[0],coord[1]-i)]['piece']
                if (f and f.color==self.color):
                    if((coord[1] - i)==0 and f.name=='white_rook_1' or f.name=='black_rook_1'):
                        self.possibleMoves.append((coord[0],coord[1]-i+2,'br'))
                    else:
                        print(f.name)
                        break

    def roque(self,coord,matrix):
        self.bigRoque(coord,matrix)
        self.littleRoque(coord,matrix)
        
   
    def getPossibleMoves(self, coord, matrix):
        self.possibleMoves=[]
        self.movD(coord, matrix)
        self.movV(coord, matrix)
        self.movH(coord, matrix)
        self.roque(coord,matrix)
        return self.possibleMoves

    def movH(self, coord, matrix):
        self.checkRightEdge(coord, matrix)
        self.checkLeftEdge(coord, matrix)
        
    def movD(self, coord, matrix):
        self.checkUpperRightEdge(coord, matrix)
        self.checkUpperLeftEdge(coord, matrix)
        self.checkLowerRightEdge(coord, matrix)
        self.checkLowerLeftEdge(coord, matrix)
    
    def movV(self, coord, matrix): 
        self.checkUpperEdge(coord, matrix)
        self.checkLowerEdge(coord, matrix)
        

    def checkUpperEdge(self, coord, matrix):
        if((coord[0]-1>=0)): 
            f = matrix[(coord[0]-1,coord[1])]['piece']
            if ((f and f.color!=self.color) or (not f)):
                self.possibleMoves.append((coord[0]-1,coord[1],'mov'))
    
    def checkLowerEdge(self, coord, matrix):
        if(coord[0]+1<=7): #limite inferior
            b = matrix[(coord[0]+1,coord[1])]['piece']    #⬇⬇⬇
            if (b and b.color!=self.color or (not b)):
                self.possibleMoves.append((coord[0]+1,coord[1],'mov'))
                self.possibleMoves.append((coord[0]+1,coord[1],'mov'))
    
    def checkRightEdge(self, coord, matrix):
        if(coord[1]+1<=7):  
            r = matrix[(coord[0],coord[1]+1)]['piece']
            if (r and (r.color != self.color)):
                self.possibleMoves.append((coord[0],coord[1]+1,'mov'))
            elif not r:
                self.possibleMoves.append((coord[0],coord[1]+1,'mov'))

    def checkLeftEdge(self, coord, matrix):
        if(coord[1]-1>=0):
            l = matrix[(coord[0],coord[1]-1)]['piece'] 
            if (l and l.color!=self.color or (not l)):
                self.possibleMoves.append((coord[0],coord[1]-1,'mov'))
    
    def checkUpperRightEdge(self, coord, matrix):
        if(coord[1]!=7 and coord[0]!=0):
            fr = matrix[(coord[0]-1,coord[1]+1)]['piece']
            if ((fr and fr.color!=self.color) or (not fr)):
                self.possibleMoves.append((coord[0]-1,coord[1]+1,'mov'))

    def checkUpperLeftEdge(self, coord, matrix):
        if(coord[1]!=0 and coord[0]!=0):
            fl = matrix[(coord[0]-1,coord[1]-1)]['piece']
            if((fl and fl.color!=self.color) or (not fl)) :
                self.possibleMoves.append((coord[0]-1,coord[1]-1,'mov'))

    def checkLowerRightEdge(self, coord, matrix):
        if(coord[1]!=7 and coord[0]!=7):
            br = matrix[(coord[0]+1,coord[1]+1)]['piece']
            if(br and br.color!=self.color or (not br)):
                self.possibleMoves.append((coord[0]+1,coord[1]+1,'mov'))

        
    def checkLowerLeftEdge(self, coord, matrix):
        if(coord[1]!=0 and coord[0]!=7):
            bl = matrix[(coord[0]+1,coord[1]-1)]['piece']
            if((bl and bl.color!=self.color) or (not bl)):
                self.possibleMoves.append((coord[0]+1,coord[1]-1,'mov'))


    