###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023

#Import of library and files
from Piece import Piece
from Var import *

#####
### Class pawn handles all authorized movements of the pawn and is font/character. 
### image represents the character/shape of the pawn
### pawnMoves represents the directions in which a pawn can move
#####

class Pawn(Piece):

    def __init__(self,x,y,size,color,unicode,col,row,id):
        super().__init__(x,y,size,color,col,row,"pawn",id)
        self.image = self.font.render(unicode, True, color)
        self.firstMove=False
        self.pawnFirstMoves=[(0,1),(0,-1)] 
        self.pawnMoves=[(0,1),(0,-1),(0,2),(0,-2)] 


    ###This function is used to check all the available movements of the pawn on the chessboard
    def Mouvement(self,board):
        self.possibleMoves.clear()
        ##ChatGPT : Create a 2 dimensions table
        self.possibleMoves= [[0] * COL for _ in range(ROW)]
        if self.clicked :
            if self.color==BLUE:
                if self.row < COL-2  and board.squares[self.col][self.row+2].empty and board.squares[self.col][self.row+1].empty and not self.firstMove :
                    self.possibleMoves[self.col][self.row+2]=True
                if self.row < COL-1  and board.squares[self.col][self.row+1].empty:
                    self.possibleMoves[self.col][self.row+1]=True



                if self.row < COL-1 and self.col >= 0 and self.col < 7  :
                    if board.piecesPos[self.col+1][self.row+1]!=0 :
                        if board.piecesPos[self.col+1][self.row+1].color!=self.color:
                            self.possibleMoves[self.col+1][self.row+1]=True
                    
                if self.row < COL-1 and self.col >= 0 and self.col <= 7  :
                    if board.piecesPos[self.col-1][self.row+1]!=0 :
                        if board.piecesPos[self.col-1][self.row+1].color!=self.color:
                            self.possibleMoves[self.col-1][self.row+1]=True





            if self.color==RED:
                if self.row > 0 and board.squares[self.col][self.row-2].empty and board.squares[self.col][self.row-1].empty and not self.firstMove :
                    self.possibleMoves[self.col][self.row-2]=True
                if self.row > 0 and board.squares[self.col][self.row-1].empty:
                    self.possibleMoves[self.col][self.row-1]=True

        
                if self.row > 0 and self.col >= 0 and self.col < 7  :
                    if board.piecesPos[self.col+1][self.row-1]!=0 :
                        if board.piecesPos[self.col+1][self.row-1].color==BLUE:
                            self.possibleMoves[self.col+1][self.row-1]=True
                    
                if self.row > 0 and self.col >= 0 and self.col <= 7 :
                    if board.piecesPos[self.col-1][self.row-1]!=0 :
                        if board.piecesPos[self.col-1][self.row-1].color==BLUE:
                            self.possibleMoves[self.col-1][self.row-1]=True

        

    

                        


        

       




    

    