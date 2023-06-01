 ###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023

#Import of library and files
from Var import *
from Pieces.Piece import Piece
import copy



##### Summary
### Class Bishop handles all authorized movements of the bishop and is font/character. 
### image represents the character/shape of the bishop
### bishopMoves represents the directions in which a bishop can move
##### Summary
class Bishop(Piece):

    def __init__(self,x,y,size,color,unicode,col,row,id, check=False):
        super().__init__(x,y,size,color,col,row,"bishop",id,check)
        self.image = self.font.render(unicode, True, color)
        self.bishopMoves = [(1, 1), (-1, 1), (1, -1), (-1, -1)]

        
    ###This function is used to check all the available movements of the bishop on the chessboard
    def Mouvement(self,board):
    

        #Create a two-dimensional table that save all the possible moves
        self.possibleMoves= [[0] * COL for i in range(ROW)]
        if not self.check and not self.Simulation(board):
            for obj in self.bishopMoves:
                for i in range(1, 8):
                    #Move diagonally in all directions until the board ends or it touch a piece the same color or from another color
                    col = self.col + obj[0] * i
                    row = self.row + obj[1] * i
                    if 0 <= col < 8 and 0 <= row < 8 and board.squares[col][row].empty :
                        self.possibleMoves[col][row] = True
                    elif 0 <= col < 8 and 0 <= row < 8 and not board.squares[col][row].empty  :
                        if board.piecesPos[col][row]!=0 :
                            if board.piecesPos[col][row].color!=self.color:
                                self.possibleMoves[col][row] = True
                                if board.piecesPos[col][row].name=="king":
                                    for rowP in range(ROW):
                                        for colP in range(COL):
                                            if board.piecesPos[colP][rowP]!=0 and board.piecesPos[colP][rowP].color!=self.color :
                                                board.piecesPos[colP][rowP].check=True
                                    
                                    board.checkPos=self.getPositionsBetween(row,col,self.row,self.col)
                                    
                            break  
                    else:
                        break
        else:
                 
            board.checkPos.reverse()     
            for a in range(len(board.checkPos)):
                for obj in self.bishopMoves:
                    for i in range(1, 8):
                        #Move diagonally in all directions until the board ends or it touch a piece the same color or from another color
                        cols = self.col + obj[0] * i
                        rows = self.row + obj[1] * i
                        if cols == board.checkPos[a][1] and rows == board.checkPos[a][0]  and board.squares[cols][rows].empty:
                            self.possibleMoves[cols][rows] = True
                            return
                        elif cols == board.checkPos[a][1] and rows == board.checkPos[a][0]  and not board.squares[cols][rows].empty:
                            self.possibleMoves[cols][rows] = True
                            return
    

    def MouvementSimulation(self,testBoard,board):

        #Create a two-dimensional table that save all the possible moves
        possibleMoves= [[0] * COL for i in range(ROW)]
        if not self.check:
            for obj in self.bishopMoves:
                for i in range(1, 8):
                    #Move diagonally in all directions until the board ends or it touch a piece the same color or from another color
                    col = self.col + obj[0] * i
                    row = self.row + obj[1] * i
                    if 0 <= col < 8 and 0 <= row < 8 and board.squares[col][row].empty:
                        possibleMoves[col][row] = True
                    
                    elif 0 <= col < 8 and 0 <= row < 8 and not board.squares[col][row].empty :
                        if testBoard[col][row]!=0 :
                            if testBoard[col][row].color!=self.color:
                                possibleMoves[col][row] = True
                                if testBoard[col][row].name=="king":
                                    for rowP in range(ROW):
                                        for colP in range(COL):
                                            if testBoard[colP][rowP]!=0 and testBoard[colP][rowP].color!=self.color :
                                                testBoard[colP][rowP].check=True
                                    
                                    
                            break  
                    else:
                        break
        

    def getPositionsBetween(self, kingRow,kingCol, bishopRow,bishopCol):

        positionsBetween = []
        positionsBetween.append((bishopRow, bishopCol))
        
        if kingRow < bishopRow:
            distanceRowBetween = 1
        else:
            distanceRowBetween = -1

        if kingCol < bishopCol:
            distanceColBetween = 1
        else:
            distanceColBetween = -1
        row = kingRow + distanceRowBetween
        col = kingCol + distanceColBetween

        while row != bishopRow and col != bishopCol:
            positionsBetween.append((row, col))
            row += distanceRowBetween
            col += distanceColBetween
        positionsBetween.append((bishopRow, bishopCol))
        return positionsBetween




  
