from .piece import Piece

class King(Piece):
    
    def __init__(self, color, name):
        self.spriteDir = 'assets/img/' + color + 'King.png'
        self.name = name
        super(King,self).__init__(color,name)

    def getPossibleMoves(self, coord, matrix):
        self.possibleMoves=[]
        self.movD(coord, matrix)
        self.movV(coord, matrix)
        self.movH(coord, matrix)
        return self.possibleMoves

    def movH(self, coord, matrix):
        if(coord[1]+1<=7):  #limite lateral direito
            r = matrix[(coord[0],coord[1]+1)]['piece']    #➡➡➡
            if (r and (r.color != self.color)):
                self.possibleMoves.append((coord[0],coord[1]+1))
            elif not r:
                self.possibleMoves.append((coord[0],coord[1]+1))

        if(coord[1]-1>=0):  #limite lateral esquerdo
            l = matrix[(coord[0],coord[1]-1)]['piece']    #⬅⬅⬅
            if (l and l.color!=self.color or (not l)):
                self.possibleMoves.append((coord[0],coord[1]-1))
    
    def movD(self, coord, matrix):
        if(coord[1]!=7 and coord[0]!=0): #limite superior e lateral direito 
            fr = matrix[(coord[0]-1,coord[1]+1)]['piece']#↗↗↗
            if ((fr and fr.color!=self.color) or (not fr)):
                self.possibleMoves.append((coord[0]-1,coord[1]+1))

        if(coord[1]!=0 and coord[0]!=0):  #limite superior e lateral esquerdo
            fl = matrix[(coord[0]-1,coord[1]-1)]['piece']#↖↖↖
            if((fl and fl.color!=self.color) or (not fl)) :
                self.possibleMoves.append((coord[0]-1,coord[1]-1))

        if(coord[1]!=7 and coord[0]!=7): #limite inferior e lateral direito
            br = matrix[(coord[0]+1,coord[1]+1)]['piece']#↘↘↘
            if(br and br.color!=self.color or (not br)):
                self.possibleMoves.append((coord[0]+1,coord[1]+1))

        if(coord[1]!=0 and coord[0]!=7): #limite inferior e lateral esquerdo
            bl = matrix[(coord[0]+1,coord[1]-1)]['piece']#↙↙↙
            if((bl and bl.color!=self.color) or (not bl)):
                self.possibleMoves.append((coord[0]+1,coord[1]-1))

    def movV(self, coord, matrix): 
        if((coord[0]-1>=0)):    #limite superior
            f = matrix[(coord[0]-1,coord[1])]['piece']    #⬆⬆⬆
            if ((f and f.color!=self.color) or (not f)):
                self.possibleMoves.append((coord[0]-1,coord[1]))
                
        if(coord[0]+1<=7): #limite inferior
            b = matrix[(coord[0]+1,coord[1])]['piece']    #⬇⬇⬇
            if (b and b.color!=self.color or (not b)):
                self.possibleMoves.append((coord[0]+1,coord[1]))
                self.possibleMoves.append((coord[0]+1,coord[1]))
    