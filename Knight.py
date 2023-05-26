###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023

#Import of library and files
from Piece import Piece
from Var import *

#####
### Class knight handles all authorized movements of the knight and is font/character. 
### image represents the character/shape of the knight
### knightMoves represents the directions in which a knight can move
#####
class Knight(Piece):

    def __init__(self,x,y,size,color,unicode,col,row,id):
        super().__init__(x,y,size,color,col,row,"knight",id)
        self.image = self.font.render(unicode, True, color)
        self.knightMoves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

        
    ###This function is used to check all the available movements of the knight on the chessboard
    def Mouvement(self,board):
        #Create a two-dimensional table that save all the possible moves
        self.possibleMoves= [[0] * COL for i in range(ROW)]
        if self.clicked :
            for obj in self.knightMoves:
                col = self.col + obj[0]
                row = self.row + obj[1]
                if 0 <= col < 8 and 0 <= row < 8 and board.squares[col][row].empty:
                    self.possibleMoves[col][row] = True
                elif 0 <= col < 8 and 0 <= row < 8 and not board.squares[col][row].empty :
                    if board.piecesPos[col][row]!=0 :
                        if board.piecesPos[col][row].color!=self.color:
                            self.possibleMoves[col][row] = True