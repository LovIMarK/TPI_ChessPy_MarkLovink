import pygame
from Piece import Piece
from Var import *


class King(Piece):

    def __init__(self,x,y,size,color,unicode,colX,colY):
        super().__init__(x,y,size,color,colX,colY,"king")
        self.unicode_char = unicode
        self.image = self.font.render(self.unicode_char, True, color)
        #self.rock=False
        
    
    
            

    def MouvementPlayer(self,posMouse):
        if self.clicked :
            self.rect.center=posMouse
        elif self.rect!=pygame.Rect(self.colX*WIDTHSQUARE+20,self.colY*WIDTHSQUARE+20,WIDTHSQUARE,WIDTHSQUARE):
            self.rect=pygame.Rect(self.colX*WIDTHSQUARE+20,self.colY*WIDTHSQUARE+20,WIDTHSQUARE,WIDTHSQUARE)

            

    def Mouvement(self,allBoards,allPieces):
        self.possibleMoves.clear()
        self.possibleMoves= [[0] * 8 for _ in range(8)]
        if self.clicked :
            if self.color==BLUE:

                offsets = [(0, 1), (1, 1), (-1, 1), (0, -1), (1, -1), (-1, -1), (1, 0), (-1, 0)]

                for offset in offsets:
                    x = self.colX + offset[0]
                    y = self.colY + offset[1]
                    if 0 <= x < 8 and 0 <= y < 8 and allBoards[x][y].empty:
                        self.possibleMoves[x][y] = True
                    elif 0 <= x < 8 and 0 <= y < 8 and not allBoards[x][y].empty :
                        if allPieces[x][y]!=0 :
                            if allPieces[x][y].color==RED:
                                self.possibleMoves[x][y] = 1

                # if self.colY <7  and allBoards[self.colX][self.colY+1].empty:
                #     self.possibleMoves[self.colX][self.colY+1]=True
                # if self.colY <7  and self.colX<7 and allBoards[self.colX+1][self.colY+1].empty:
                #     self.possibleMoves[self.colX+1][self.colY+1]=True
                # if self.colY <7  and self.colX>0 and allBoards[self.colX-1][self.colY+1].empty:
                #     self.possibleMoves[self.colX-1][self.colY+1]=True
                # if self.colY >0  and allBoards[self.colX][self.colY-1].empty:
                #     self.possibleMoves[self.colX][self.colY-1]=True
                # if self.colY >0  and self.colX<7 and allBoards[self.colX+1][self.colY-1].empty:
                #     self.possibleMoves[self.colX+1][self.colY-1]=True
                # if  self.colY >0  and self.colX>0 and allBoards[self.colX-1][self.colY-1].empty:
                #     self.possibleMoves[self.colX-1][self.colY-1]=True
                # if  self.colX<7 and allBoards[self.colX+1][self.colY].empty:
                #     self.possibleMoves[self.colX+1][self.colY]=True
                # if self.colX>0 and allBoards[self.colX-1][self.colY].empty:
                #     self.possibleMoves[self.colX-1][self.colY]=True

            elif self.color==RED:
                offsets = [(0, 1), (1, 1), (-1, 1), (0, -1), (1, -1), (-1, -1), (1, 0), (-1, 0)]

                for offset in offsets:
                    x = self.colX + offset[0]
                    y = self.colY + offset[1]
                    if 0 <= x < 8 and 0 <= y < 8 and allBoards[x][y].empty:
                        self.possibleMoves[x][y] = True
                    elif 0 <= x < 8 and 0 <= y < 8 and not allBoards[x][y].empty :
                        if allPieces[x][y]!=0 :
                            if allPieces[x][y].color==BLUE:
                                self.possibleMoves[x][y] = 1
        

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
                        elif self.possibleMoves[j][i]==1: 
                            allPieces[j][i]=0
                            allBoards[self.colX][self.colY].empty=True
                            allBoards[j][i].empty=False
                            self.colX=j
                            self.colY=i
                            self.rect=pygame.Rect(self.colX*WIDTHSQUARE+20,self.colY*WIDTHSQUARE+20,WIDTHSQUARE,WIDTHSQUARE)
                            self.firstMove=True
                            for obj in players:
                                obj.ChangePlayer()

    