###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023

#Import of library and files
from Piece import Piece
from Var import *

#####
### Class queen handles all authorized movements of the queen and is font/character. 
### image represents the character/shape of the queen
### queenMoves represents the directions in which a queen can move
#####
class Queen(Piece):

    def __init__(self,x,y,size,color,unicode,col,row,id):
        super().__init__(x,y,size,color,col,row,"queen",id)
        self.image = self.font.render(unicode, True, color)
        self.queenMoves = [(1, 1), (-1, 1), (1, -1), (-1, -1), (1, 0), (-1, 0), (0, 1), (0, -1)]


        
    ###This function is used to check all the available movements of the queen on the chessboard
    def Mouvement(self,board):
        self.possibleMoves.clear()
        self.possibleMoves= [[0] * COL for _ in range(ROW)]
        if self.clicked:
            for obj in self.queenMoves:
                for i in range(1, 8):
                    col = self.col + obj[0] * i
                    row = self.row + obj[1] * i
                    if 0 <= col < 8 and 0 <= row < 8 and board.squares[col][row].empty:
                        self.possibleMoves[col][row] = True
                    elif 0 <= col < 8 and 0 <= row < 8 and not board.squares[col][row].empty:
                        if board.piecesPos[col][row] != 0:
                            if board.piecesPos[col][row].color != self.color:
                                self.possibleMoves[col][row] = True
                            break
                    else:
                        break
 

        

    