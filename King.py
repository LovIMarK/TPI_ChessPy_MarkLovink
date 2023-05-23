import pygame
from Piece import Piece
from Var import *


class King(Piece):

    def __init__(self,x,y,size,color,unicode,col,row,id):
        super().__init__(x,y,size,color,col,row,"king",id)
        self.image = self.font.render(unicode, True, color)
        self.kingMoves = [(0, 1), (1, 1), (-1, 1), (0, -1), (1, -1), (-1, -1), (1, 0), (-1, 0)]
        #self.rock=False
        
    

            

    def Mouvement(self,board):

        self.possibleMoves.clear()
        self.possibleMoves= [[0] * COL for _ in range(ROW)]
        if self.clicked :

                for obj in self.kingMoves:
                    col = self.col + obj[0]
                    row = self.row + obj[1]
                    if 0 <= col < 8 and 0 <= row < 8 and board.Square[col][row].empty:
                        self.possibleMoves[col][row] = True
                    elif 0 <= col < 8 and 0 <= row < 8 and not board.Square[col][row].empty :
                        if board.PiecesPos[col][row]!=0 :
                            if board.PiecesPos[col][row].color!=self.color:
                                self.possibleMoves[col][row] = True

        

    
    