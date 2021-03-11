from .piece import Piece

class Knight(Piece):
    
    def __init__(self, color, name):
        self.spriteDir = 'assets/img/' + color + 'Knight.png'
        self.name = name
        super(Knight,self).__init__(color,name)

    def movL(self,ncasa,coord,matrix,sent):#
        if (ncasa==1):
            pass
        elif (ncasa==2):
            pass
        else:
            pass