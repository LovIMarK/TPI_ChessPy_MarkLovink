import pygame
from Piece import Piece
from Var import *
from Circle import Circle

class Pawn(Piece):

    def __init__(self,x,y,size,color,unicode,colX,colY):
        super().__init__(x,y,size,color,colX,colY,"pawn")
        self.unicode_char = unicode
        self.image = self.font.render(self.unicode_char, True, color)
        self.firstMove=False
        
        
        
    
    def MouvementPlayer(self,posMouse):
        if self.clicked :
            self.rect.center=posMouse
        elif self.rect!=pygame.Rect(self.colX*WIDTHSQUARE+20,self.colY*WIDTHSQUARE+20,WIDTHSQUARE,WIDTHSQUARE):
            self.rect=pygame.Rect(self.colX*WIDTHSQUARE+20,self.colY*WIDTHSQUARE+20,WIDTHSQUARE,WIDTHSQUARE)

            

    def Mouvement(self,allBoards,allPieces):
        
        self.possibleMoves= [[0] * 8 for _ in range(8)]
        if self.clicked :
            if self.color==BLUE:
                if self.colY < COL-2  and allBoards[self.colX][self.colY+2].empty and not self.firstMove :
                    self.possibleMoves[self.colX][self.colY+2]=True
                if self.colY < COL-1  and allBoards[self.colX][self.colY+1].empty:
                    self.possibleMoves[self.colX][self.colY+1]=True



                if self.colY < COL-1 and self.colX >= 0 and self.colX < 7  :
                    if allPieces[self.colX+1][self.colY+1]!=0 :
                        if allPieces[self.colX+1][self.colY+1].color==RED:
                            self.possibleMoves[self.colX+1][self.colY+1]=True
                    
                if self.colY < COL-1 and self.colX >= 0 and self.colX <= 7  :
                    if allPieces[self.colX-1][self.colY+1]!=0 :
                        if allPieces[self.colX-1][self.colY+1].color==RED:
                            self.possibleMoves[self.colX-1][self.colY+1]=True





            if self.color==RED:
                if self.colY > 0 and allBoards[self.colX][self.colY-2].empty and not self.firstMove :
                    self.possibleMoves[self.colX][self.colY-2]=True
                if self.colY > 0 and allBoards[self.colX][self.colY-1].empty:
                    self.possibleMoves[self.colX][self.colY-1]=True

        
                if self.colY > 0 and self.colX >= 0 and self.colX < 7  :
                    if allPieces[self.colX+1][self.colY-1]!=0 :
                        if allPieces[self.colX+1][self.colY-1].color==BLUE:
                            self.possibleMoves[self.colX+1][self.colY-1]=True
                    
                if self.colY > 0 and self.colX >= 0 and self.colX <= 7 :
                    if allPieces[self.colX-1][self.colY-1]!=0 :
                        if allPieces[self.colX-1][self.colY-1].color==BLUE:
                            self.possibleMoves[self.colX-1][self.colY-1]=True

        

    def Clicked(self,posMouse,allBoards,allPieces,players):
        if not self.clicked and  self.rect==pygame.Rect(self.colX*WIDTHSQUARE+20,self.colY*WIDTHSQUARE+20,WIDTHSQUARE,WIDTHSQUARE):
            self.clicked=True
        else:
            self.clicked=False

        if not self.clicked:
            for i in range(ROW):
                for j in range(COL):
                    if allBoards[j][i].rect.collidepoint(posMouse)  :
                        if self.possibleMoves[j][i]:
                            if not allBoards[j][i].empty:
                                self.die.append(allPieces[j][i])
                            allPieces[j][i]=allPieces[self.colX][self.colY]
                            allPieces[self.colX][self.colY]=0
                            allBoards[self.colX][self.colY].empty=True
                            allBoards[j][i].empty=False
                            self.colX=j
                            self.colY=i
                            self.rect=pygame.Rect(self.colX*WIDTHSQUARE+20,self.colY*WIDTHSQUARE+20,WIDTHSQUARE,WIDTHSQUARE)
                            self.firstMove=True
                            for obj in players:
                                obj.ChangePlayer()
                            self.possibleMoves.clear()
                            print(self.die)

                        


        

       




    

    