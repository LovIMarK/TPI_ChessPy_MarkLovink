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
        
        
    ##### Summary
    ###This function is used to check all the available movements of the rook on the chessboard
    ##### Summary
    def Movement(self,board):

        #Create a two-dimensional table that save all the possible moves
        self.possibleMoves= [[0] * COL for i in range(ROW)]
        #if not self.check and not self.Simulation(board):
        for obj in self.rookMoves:
            for i in range(1, 8):
                col = self.col + obj[0] * i
                row = self.row + obj[1] * i
                if 0 <= col < 8 and 0 <= row < 8 and board.squares[col][row].empty:
                    self.possibleMoves[col][row] = True
                
                ###If a piece from another color (possible moves = true), if it is the king (all pieces check)
                elif 0 <= col < 8 and 0 <= row < 8 and not board.squares[col][row].empty :
                    if board.piecesPos[col][row]!=0 :
                        if board.piecesPos[col][row].color!=self.color:
                            self.possibleMoves[col][row] = True
                            if board.piecesPos[col][row].name=="king":
                                for row2 in range(ROW):
                                    for col2 in range(COL):
                                        if board.piecesPos[col2][row2]!=0 and board.piecesPos[col2][row2].color!=self.color :
                                            board.piecesPos[col2][row2].check=True
                                
                                board.checkPos=self.getPositionsBetween(row,col,self.row,self.col)
                        break  
                else:
                    break
        if self.check or self.Simulation(board) :
            ### If the possible movement of the piece equals the position to protect the king
            possibleMoves= [[0] * COL for i in range(ROW)]
            for a in range(len(board.checkPos)):
                if self.possibleMoves[board.checkPos[a][1]][board.checkPos[a][0]]!=0:
                    possibleMoves[board.checkPos[a][1]][board.checkPos[a][0]]=True
            ### Previous position list equals new position list
            self.possibleMoves=possibleMoves


        

    ##### Summary
    ###This function is used to simulate all the available movements of the rook on the chessboard for the next round
    ##### Summary
    def MovementSimulation(self,simulateBoard,board):

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
                        if simulateBoard[col][row]!=0 :
                            if simulateBoard[col][row].color!=self.color:
                                possibleMoves[col][row] = True
                                if simulateBoard[col][row].name=="king":
                                    for row2 in range(ROW):
                                        for col2 in range(COL):
                                            if simulateBoard[col2][row2]!=0 and simulateBoard[col2][row2].color!=self.color :
                                                simulateBoard[col2][row2].check=True
                                            if board.piecesPos[col2][row2]!=0 and  board.piecesPos[col2][row2].color!=self.color and not board.piecesPos[col2][row2].check:
                                                board.checkPos=self.getPositionsBetween(row,col,self.row,self.col) 
                                    
                            break  
                    else:
                        break
            
   
    ##### Summary
    ###This function is used get all the position between the rook and the king when check
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

            
