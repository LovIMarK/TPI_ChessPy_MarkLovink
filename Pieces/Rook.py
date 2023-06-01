###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023

#Import of library and files
from Pieces.Piece import Piece
from Var import *
import copy

#####
### Class rook handles all authorized movements of the rook and is font/character. 
### image represents the character/shape of the rook
### rookMoves represents the directions in which a rook can move
#####
class Rook(Piece):

    def __init__(self,x,y,size,color,unicode,col,row,id, check=False):
        super().__init__(x,y,size,color,col,row,"rook",id,check)
        self.image = self.font.render(unicode, True, color)
        self.rookMoves=[(0,1),(1,0),(0,-1),(-1,0)]
        
        
            
    ###This function is used to check all the available movements of the rook on the chessboard
    def Mouvement(self,board):

        #Create a two-dimensional table that save all the possible moves
        self.possibleMoves= [[0] * COL for i in range(ROW)]
        if not self.check and not self.Simulation(board):
            for obj in self.rookMoves:
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
                for obj in self.rookMoves:
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

    ##### Summary
    ###This function is used to simulate all the available movements of the rook on the chessboard for the next round
    ##### Summary
    def MouvementSimulation(self,testBoard,board):

        #Create a two-dimensional table that save all the possible moves
        possibleMoves= [[0] * COL for i in range(ROW)]
        if not self.check:
            for obj in self.rookMoves:
                for i in range(1, 8):
                    #Move diagonally in all directions until the board ends or it touch a piece the same color or from another color
                    col = self.col + obj[0] * i
                    row = self.row + obj[1] * i
                    if 0 <= col < 8 and 0 <= row < 8 and board.squares[col][row].empty :
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
            
   
    ##### Summary
    ###This function is used get all the position between the rook and the king 
    ##### Summary    
    ### Return a list with all the position
    def getPositionsBetween(self, kingRow, kingCol, rookRow, rookCol):
        positionsBetween = []
        positionsBetween.append((rookRow, rookCol))
        if kingRow == rookRow:
            if kingCol < rookCol:
                postionColBetween= 1  
            else:
                postionColBetween=-1

            col = kingCol + postionColBetween
            while col != rookCol:
                positionsBetween.append((kingRow, col))
                col += postionColBetween
        
        
        elif kingCol == rookCol:
            
            if kingRow < rookRow:
                postionRowBetween= 1  
            else:
                postionRowBetween=-1
            row = kingRow + postionRowBetween

            while row != rookRow:
                positionsBetween.append((row, kingCol))
                row += postionRowBetween

        return positionsBetween

            
