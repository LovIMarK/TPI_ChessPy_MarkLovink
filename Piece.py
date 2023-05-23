import pygame
from Var import *


class Piece():

    def __init__(self,x,y,size,color,col,row,name):
        super().__init__()
        self.rect = pygame.Rect(x, y, size, size)
        self.font = pygame.font.Font("Fonts/DejaVuSans.ttf", size)
        self.color=color
        self.name=name
        self.col=col
        self.row=row
        self.clicked=False
        self.possibleMoves=[]
        

    def CheckClicked(self,board):
        clicked=False
        for row in range(ROW):
            for col in range(COL):
                if board.PiecesPos[col][row]!=0 and board.PiecesPos[col][row].clicked:
                    clicked =True
        return clicked


    def MouvementPlayer(self,posMouse,board): 
        if self.clicked :
            self.rect.center=posMouse
        elif self.rect!=pygame.Rect(self.col*WIDTHSQUARE+board.x,self.row*WIDTHSQUARE+board.y,WIDTHSQUARE,WIDTHSQUARE):
            self.rect=pygame.Rect(self.col*WIDTHSQUARE+board.x,self.row*WIDTHSQUARE+board.y,WIDTHSQUARE,WIDTHSQUARE)

    def Clicked(self,posMouse,players,board):
        if not self.CheckClicked(board) and self.rect==pygame.Rect(self.col*WIDTHSQUARE+board.x,self.row*WIDTHSQUARE+board.y,WIDTHSQUARE,WIDTHSQUARE) :
            self.clicked=True
        else:
            self.clicked=False
        

        if not self.clicked:
            for row in range(ROW):
                for col in range(COL):
                    if board.Square[col][row].rect.collidepoint(posMouse)  :
                        if self.possibleMoves[col][row]:
                            #board.lastMovement =[[0] * 8 for _ in range(8)]
                            if not board.Square[col][row].empty:
                                board.pieceDies.append(board.PiecesPos[col][row])
                            #changer avec les valeur du rect et les colonnes
                            #board.lastMovement[self.col][self.row]=board.PiecesPos[self.col][self.row]
                            board.PiecesPos[col][row]=board.PiecesPos[self.col][self.row]
                            board.PiecesPos[self.col][self.row]=0
                            board.Square[self.col][self.row].empty=True
                            board.Square[col][row].empty=False
                            self.col=col
                            self.row=row
                            self.rect=pygame.Rect(self.col*WIDTHSQUARE+board.x,self.row*WIDTHSQUARE+board.y,WIDTHSQUARE,WIDTHSQUARE)
                            self.firstMove=True
                            for obj in players:
                                obj.ChangePlayer()
                            self.possibleMoves.clear()
                            
