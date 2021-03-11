from .piece import Piece

class Pawn(Piece):
    
    def __init__(self, color, name):
        self.spriteDir = 'assets/img/' + color + 'Pawn.png'
        self.name = name
        self.color=color
        super(Pawn,self).__init__(color,name)
    
    def getPossibleMoves(self, coord, matrix):
        self.possibleMoves=[]
        
        if(self.color=='white'):
            if(self.wasMovedBefore):
                self.movD(coord,matrix)
                self.movV(coord,matrix)
            else:
                self.movD(coord,matrix)
                self.movV(coord,matrix)
                
        else:
            if(self.wasMovedBefore):
                self.movD(coord,matrix)
                self.movV(coord,matrix)
            else:
                self.movD(coord,matrix)
                self.movV(coord,matrix)
        return self.possibleMoves

    def movV(self, coord, matrix): 

        # Achar possíveis mov.
        # P/ 1 casa
        if(coord[0]-1>=0): # limite superior
            f=matrix[(coord[0]-1,coord[1])]['piece']    # ⬆⬆⬆
            if(not f):
                self.possibleMoves.append((coord[0]-1,coord[1]))

        # P/ 2 casas  
        if not self.wasMovedBefore:
            i=0
            while(i<2):
                if(coord[0]-(i+1)>=0): # limite superior
                    f=matrix[(coord[0]-(i+1),coord[1])]['piece']    # ⬆⬆⬆
                    if (not f):
                        self.possibleMoves.append((coord[0]-(i+1),coord[1]))
                        i+=1
                    else:
                        i=2
                else:
                    i=2

    def movD(self, coord, matrix):
        if(coord[1]!=7 and coord[0]!=0): #limite superior e lateral direito 
            fr=matrix[(coord[0]-1,coord[1]+1)]['piece']#↗↗↗
            if(fr and fr.color!=self.color):
                self.possibleMoves.append((coord[0]-1,coord[1]+1))

        if(coord[1]!=0 and coord[0]!=0):  #limite superior e lateral esquerdo
            fl=matrix[(coord[0]-1,coord[1]-1)]['piece']#↖↖↖
            if(fl and fl.color!=self.color):
                self.possibleMoves.append((coord[0]-1,coord[1]-1))