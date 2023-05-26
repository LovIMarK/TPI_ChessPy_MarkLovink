###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023

#Import of library and files
from Var import *
from Piece import Piece


##### Summary
### Class Bishop handles all authorized movements of the bishop and is font/character. 
### image represents the character/shape of the bishop
### bishopMoves represents the directions in which a bishop can move
##### Summary
class Bishop(Piece):

    def __init__(self,x,y,size,color,unicode,col,row,id):
        super().__init__(x,y,size,color,col,row,"bishop",id)
        self.image = self.font.render(unicode, True, color)
        self.bishopMoves = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

        
    ###This function is used to check all the available movements of the bishop on the chessboard
    def Mouvement(self,board):

        #Create a two-dimensional table that save all the possible moves
        self.possibleMoves= [[0] * COL for i in range(ROW)]
        if self.clicked :
                for obj in self.bishopMoves:
                    for i in range(1, 8):
                        #Move diagonally in all directions until the board ends or it touch a piece the same color or from another color
                        col = self.col + obj[0] * i
                        row = self.row + obj[1] * i
                        if 0 <= col < 8 and 0 <= row < 8 and board.squares[col][row].empty:
                            self.possibleMoves[col][row] = True
                        elif 0 <= col < 8 and 0 <= row < 8 and not board.squares[col][row].empty :
                            if board.piecesPos[col][row]!=0 :
                                if board.piecesPos[col][row].color!=self.color:
                                    self.possibleMoves[col][row] = True
                                break
                        else:
                            break

