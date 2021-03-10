class Piece:

    def __init__(self, color, name):
        self.wasMovedBefore = False
        self.possibleMoves = []
        self.spriteID = None
        self.name = name
        self.color=color
        self.selected=False
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
    def movH(self,ncasa,coord,matrix):
        if (ncasa==1):#rei
            if(coord[1]+1<=7):#limite lateral direito
                r=matrix[(coord[0],coord[1]+1)]['piece']#➡➡➡
                if (r!=None and r.color!=self.color):
                    self.possibleMoves.append((coord[0],coord[1]+1))
                elif(r==None):
                    self.possibleMoves.append((coord[0],coord[1]+1))
            if(coord[1]-1>=0):#limite lateral esquerdo
                l=matrix[(coord[0],coord[1]-1)]['piece']#⬅⬅⬅
                if (l!=None and l.color!=self.color):
                    self.possibleMoves.append((coord[0],coord[1]-1))
                elif(l==None):
                    self.possibleMoves.append((coord[0],coord[1]-1))
        else:#rainha, torre
            pass

    def movD(self,ncasa,coord,matrix,sent,peao):
        if (ncasa==1):#peao, rei
            if(sent==1 or sent==3):
                if(coord[1]!=7 and coord[0]!=0): #limite superior e lateral direito 
                    fr=matrix[(coord[0]-1,coord[1]+1)]['piece']#↗↗↗
                    if(fr!=None and fr.color!=self.color):
                        self.possibleMoves.append((coord[0]-1,coord[1]+1))
                    if(fr==None and not(peao)):
                        self.possibleMoves.append((coord[0]-1,coord[1]+1))
                if(coord[1]!=0 and coord[0]!=0):  #limite superior e lateral esquerdo
                    fl=matrix[(coord[0]-1,coord[1]-1)]['piece']#↖↖↖
                    if(fl!=None and fl.color!=self.color):
                        self.possibleMoves.append((coord[0]-1,coord[1]-1))
                    if(fl==None and not(peao)):
                        self.possibleMoves.append((coord[0]-1,coord[1]-1))
            if(sent==2 or sent==3):
                if(coord[1]!=7 and coord[0]!=7): #limite inferior e lateral direito
                    br=matrix[(coord[0]+1,coord[1]+1)]['piece']#↘↘↘
                    if(br!=None and br.color!=self.color):
                        self.possibleMoves.append((coord[0]+1,coord[1]+1))
                    if(br==None and not(peao)):
                        self.possibleMoves.append((coord[0]+1,coord[1]+1))
                if(coord[1]!=0 and coord[0]!=7): #limite inferior e lateral esquerdo
                    bl=matrix[(coord[0]+1,coord[1]-1)]['piece']#↙↙↙
                    if(bl!=None and bl.color!=self.color):
                        self.possibleMoves.append((coord[0]+1,coord[1]-1))
                    if(bl==None and not(peao)):
                        self.possibleMoves.append((coord[0]+1,coord[1]-1))
        else:#bispo, rainha
            pass
    def movV(self,ncasa,coord,matrix,sent): 
        if (ncasa==1):#peao, rei
            if((coord[0]-1>=0)): #limite superior
                if(sent==1 or sent==3):
                    f=matrix[(coord[0]-1,coord[1])]['piece']#⬆⬆⬆
                    if (f!=None and f.color!=self.color):
                        self.possibleMoves.append((coord[0]-1,coord[1]))
                    if(f==None):
                        self.possibleMoves.append((coord[0]-1,coord[1]))
            if(coord[0]+1<=7): #limite inferior
                if(sent==2 or sent==3):
                    b=matrix[(coord[0]+1,coord[1])]['piece']#⬇⬇⬇
                    if (b!=None and b.color!=self.color):
                        self.possibleMoves.append((coord[0]+1,coord[1]))
                    if(b==None):
                        self.possibleMoves.append((coord[0]+1,coord[1]))
        elif (ncasa==2):#peao
            if(sent==1 or sent==3):#⬆⬆⬆
                i=0
                while(i<2):
                    if(coord[0]-(i+1)>=0): #limite superior
                        f=matrix[(coord[0]-(i+1),coord[1])]['piece']#⬆⬆⬆
                        if(f==None):
                            self.possibleMoves.append((coord[0]-(i+1),coord[1]))
                            i+=1
                        elif(f!=None and f.color!=self.color):
                            self.possibleMoves.append((coord[0]-(i+1),coord[1]))
                            i=2
                        else:
                            i=2
                    else:
                        i=2
            if(sent==2 or sent==3):#⬇⬇⬇
                i=0
                while(i<2):
                    if(coord[0]+(i+1)<=7): #limite inferior
                        f=matrix[(coord[0]+(i+1),coord[1])]['piece']#⬇⬇⬇
                        if(f==None):
                            self.possibleMoves.append((coord[0]+(i+1),coord[1]))
                            i+=1
                        elif(f!=None and f.color!=self.color):
                            self.possibleMoves.append((coord[0]+(i+1),coord[1]))
                            i=2
                        else:
                            i=2
                    else:
                        i=2

        else:
            pass
    def movL(self,ncasa,coord,matrix,sent):#cavalo
        if (ncasa==1):
            pass
        elif (ncasa==2):
            pass
        else:
            pass
    def getPossibleMoves(self):
        return self.possibleMoves
