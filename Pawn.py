###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023

#Import of library and files
from Piece import Piece
from Var import *

#####
### Class pawn handles all authorized movements of the pawn and is font/character. 
### image represents the character/shape of the pawn
### firstMove represents a variable to know if the pawn has already been moved
#####

class Pawn(Piece):

    def __init__(self,x,y,size,color,unicode,col,row,id):
        super().__init__(x,y,size,color,col,row,"pawn",id)
        self.image = self.font.render(unicode, True, color)
        self.firstMove=True



    ###This function is used to check all the available movements of the pawn on the chessboard
    def Mouvement(self,board):


        #Create a two-dimensional table that save all the possible moves
        ###ChatGPT : How to create a empty 2 dimensions table
        self.possibleMoves= [[0] * COL for i in range(ROW)]
        if self.clicked :
            if self.color==BLUE:
                if self.row < COL-2  and board.squares[self.col][self.row+2].empty and board.squares[self.col][self.row+1].empty and self.firstMove :
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
                if self.row > 0 and board.squares[self.col][self.row-2].empty and board.squares[self.col][self.row-1].empty and self.firstMove :
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

        

    

                        


        

       




    

    