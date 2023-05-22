import pygame
from Piece import Piece
from Var import *
from Circle import Circle

class Pawn(Piece):

    def __init__(self,x,y,size,color,unicode,col,row):
        super().__init__(x,y,size,color,col,row,"pawn")
        self.image = self.font.render(unicode, True, color)
        self.firstMove=False
            

    def Mouvement(self,board):
        self.possibleMoves.clear()
        ##ChatGPT : Create a 2 dimensions table
        self.possibleMoves= [[0] * 8 for _ in range(8)]
        if self.clicked :
            if self.color==BLUE:
                if self.row < COL-2  and board.Square[self.col][self.row+2].empty and board.Square[self.col][self.row+1].empty and not self.firstMove :
                    self.possibleMoves[self.col][self.row+2]=True
                if self.row < COL-1  and board.Square[self.col][self.row+1].empty:
                    self.possibleMoves[self.col][self.row+1]=True



                if self.row < COL-1 and self.col >= 0 and self.col < 7  :
                    if board.PiecesPos[self.col+1][self.row+1]!=0 :
                        if board.PiecesPos[self.col+1][self.row+1].color!=self.color:
                            self.possibleMoves[self.col+1][self.row+1]=True
                    
                if self.row < COL-1 and self.col >= 0 and self.col <= 7  :
                    if board.PiecesPos[self.col-1][self.row+1]!=0 :
                        if board.PiecesPos[self.col-1][self.row+1].color!=self.color:
                            self.possibleMoves[self.col-1][self.row+1]=True





            if self.color==RED:
                if self.row > 0 and board.Square[self.col][self.row-2].empty and board.Square[self.col][self.row-1].empty and not self.firstMove :
                    self.possibleMoves[self.col][self.row-2]=True
                if self.row > 0 and board.Square[self.col][self.row-1].empty:
                    self.possibleMoves[self.col][self.row-1]=True

        
                if self.row > 0 and self.col >= 0 and self.col < 7  :
                    if board.PiecesPos[self.col+1][self.row-1]!=0 :
                        if board.PiecesPos[self.col+1][self.row-1].color==BLUE:
                            self.possibleMoves[self.col+1][self.row-1]=True
                    
                if self.row > 0 and self.col >= 0 and self.col <= 7 :
                    if board.PiecesPos[self.col-1][self.row-1]!=0 :
                        if board.PiecesPos[self.col-1][self.row-1].color==BLUE:
                            self.possibleMoves[self.col-1][self.row-1]=True

        

    

                        


        

       




    

    