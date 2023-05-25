import pygame
from Var import *


class Piece():

    def __init__(self,x,y,size,color,col,row,name,id):
        super().__init__()
        self.rect = pygame.Rect(x, y, size, size)
        self.font = pygame.font.Font("Fonts/DejaVuSans.ttf", size)
        self.id=id
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
                if board.piecesPos[col][row]!=0 and board.piecesPos[col][row].clicked:
                    clicked =True
        return clicked


    def MouvementPlayer(self,posMouse,board): 
        if self.clicked :
            self.rect.center=posMouse
        elif self.rect!=pygame.Rect(self.col*WIDTH_SQUARE+board.x,self.row*WIDTH_SQUARE+board.y,WIDTH_SQUARE,WIDTH_SQUARE):
            self.rect=pygame.Rect(self.col*WIDTH_SQUARE+board.x,self.row*WIDTH_SQUARE+board.y,WIDTH_SQUARE,WIDTH_SQUARE)

    def Clicked(self,posMouse,players,board):
        if not self.CheckClicked(board) and self.rect==pygame.Rect(self.col*WIDTH_SQUARE+board.x,self.row*WIDTH_SQUARE+board.y,WIDTH_SQUARE,WIDTH_SQUARE) :
            self.clicked=True
        else:
            self.clicked=False
        

        if not self.clicked:
            for row in range(ROW):
                for col in range(COL):
                    if board.squares[col][row].rect.collidepoint(posMouse)  :
                        if self.possibleMoves[col][row]:
                           
                            ###Dead piece
                            if not board.squares[col][row].empty:
                                board.piecesDie.append(board.piecesPos[col][row])

                            ### Change piece information
                            board.allMovement.append((self.col,self.row,col,row))
                            board.piecesPos[col][row]=board.piecesPos[self.col][self.row]
                            board.piecesPos[self.col][self.row]=0
                            board.squares[self.col][self.row].empty=True
                            board.squares[col][row].empty=False
                            self.col=col
                            self.row=row
                            self.rect=pygame.Rect(self.col*WIDTH_SQUARE+board.x,self.row*WIDTH_SQUARE+board.y,WIDTH_SQUARE,WIDTH_SQUARE)
                            self.firstMove=True
                            self.possibleMoves.clear()

                            ###Change player
                            for obj in players:
                                obj.ChangePlayer()
                            
