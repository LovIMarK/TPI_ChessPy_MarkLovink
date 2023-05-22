import pygame
from Piece import Piece
from Var import *


class Rook(Piece):

    def __init__(self,x,y,size,color,unicode,col,row):
        super().__init__(x,y,size,color,col,row,"rook")
        self.image = self.font.render(unicode, True, color)
        self.rookMoves=[]
        
        
    
    

            

    def Mouvement(self,board):
        self.possibleMoves.clear()
        self.possibleMoves= [[0] * 8 for _ in range(8)]
        if self.clicked :
            

                for col in range(1,COL-self.col):
                    if board.Square[self.col+col][self.row].empty:
                        self.possibleMoves[self.col+col][self.row]=True
                    elif board.PiecesPos[self.col+col][self.row].color!=self.color:
                        self.possibleMoves[self.col+col][self.row]=True
                    else :
                        break

                for col in range(1,self.col+1):
                    if board.Square[self.col-col][self.row].empty:
                        self.possibleMoves[self.col-col][self.row]=True
                    elif board.PiecesPos[self.col-col][self.row].color!=self.color:
                        self.possibleMoves[self.col-col][self.row]=True
                    else :
                        break


                for row in range(1,ROW-self.row):
                    if board.Square[self.col][self.row+row].empty:
                        self.possibleMoves[self.col][self.row+row]=True
                    elif board.PiecesPos[self.col][self.row+row].color!=self.color:
                        self.possibleMoves[self.col][self.row+row]=True
                    else :
                        break

                for row in range(1,self.row+1):
                    if board.Square[self.col][self.row-row].empty:
                        self.possibleMoves[self.col][self.row-row]=True
                    elif board.PiecesPos[self.col][self.row-row].color!=self.color:
                        self.possibleMoves[self.col][self.row-row]=True
                    else :
                        break