import pygame
from Piece import Piece

class Knight(Piece):

    def __init__(self,x,y,size,color,unicode,col,row):
        super().__init__(x,y,size,color,col,row,"knight")
        self.image = self.font.render(unicode, True, color)
        self.knightMoves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

        
    
    def Mouvement(self,board):

        self.possibleMoves.clear()
        self.possibleMoves= [[0] * 8 for _ in range(8)]
        if self.clicked :
                

                for obj in self.knightMoves:
                    col = self.col + obj[0]
                    row = self.row + obj[1]
                    if 0 <= col < 8 and 0 <= row < 8 and board.Square[col][row].empty:
                        self.possibleMoves[col][row] = True
                    elif 0 <= col < 8 and 0 <= row < 8 and not board.Square[col][row].empty :
                        if board.PiecesPos[col][row]!=0 :
                            if board.PiecesPos[col][row].color!=self.color:
                                self.possibleMoves[col][row] = True