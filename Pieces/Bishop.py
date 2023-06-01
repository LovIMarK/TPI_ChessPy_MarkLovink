 ###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023

#Import of library and files
from Var import *
from Pieces.Piece import Piece


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

    ##### Summary
    ### This function is used to check all the available movements of the bishop on the chessboard
    ##### Summary    
    def Mouvement(self,board):
    

        #Create a two-dimensional table that save all the possible moves
        self.possibleMoves= [[0] * COL for i in range(ROW)]
        for obj in self.bishopMoves:
            for i in range(1, 8):
                ###Move diagonally in all directions until the board ends or it touch a piece the same color or from another color
                col = self.col + obj[0] * i
                row = self.row + obj[1] * i
                if 0 <= col < 8 and 0 <= row < 8 and board.squares[col][row].empty :
                    self.possibleMoves[col][row] = True
                ###If a piece from another color (possible moves = true), if it is the king (all pieces check)
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
        if self.check or self.Simulation(board) :
            ### If the possible movement of the piece equals the position to protect the king
            possibleMoves= [[0] * COL for i in range(ROW)]
            for a in range(len(board.checkPos)):
                if self.possibleMoves[board.checkPos[a][1]][board.checkPos[a][0]]!=0:
                    possibleMoves[board.checkPos[a][1]][board.checkPos[a][0]]=True
            ### Previous position list equals new position list
            self.possibleMoves=possibleMoves
    
    ##### Summary
    ###This function is used to simulate all the available movements of the bishop on the chessboard for the next round
    ##### Summary
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
        
    ##### Summary
    ###This function is used get all the position between the bishop and the king when check
    ##### Summary    
    ### Return a list with all the position                    
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




  
