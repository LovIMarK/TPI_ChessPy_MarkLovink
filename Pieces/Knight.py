###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023

#Import of library and files
from Pieces.Piece import Piece
from Var import *


#####
### Class knight handles all authorized movements of the knight and is font/character. 
### image represents the character/shape of the knight
### knightMoves represents the directions in which a knight can move
#####
class Knight(Piece):

    def __init__(self,x,y,size,color,unicode,col,row,id, check=False):
        super().__init__(x,y,size,color,col,row,"knight",id,check)
        self.image = self.font.render(unicode, True, color)
        
        self.knightMoves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
        

        
    ###This function is used to check all the available movements of the knight on the chessboard
    def Mouvement(self,board):
        #Create a two-dimensional table that save all the possible moves
        self.possibleMoves= [[0] * COL for i in range(ROW)]
        if not self.check and not self.Simulation(board):
            for obj in self.knightMoves:
                col = self.col + obj[0]
                row = self.row + obj[1]
                if 0 <= col < 8 and 0 <= row < 8 and board.squares[col][row].empty and not self.Simulation(board):
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
                                    
                                    board.checkPos=([(self.row,self.col)])

        else:
                 
            for a in range(len(board.checkPos)):
                for obj in self.knightMoves:
                    #Move diagonally in all directions until the board ends or it touch a piece the same color or from another color
                    cols = self.col + obj[0] 
                    rows = self.row + obj[1] 
                    if cols == board.checkPos[a][1] and rows == board.checkPos[a][0]:
                        self.possibleMoves[cols][rows] = True



    def MouvementSimulation(self,testBoard,board):
        #Create a two-dimensional table that save all the possible moves
        possibleMovessss= [[0] * COL for i in range(ROW)]
        if not self.check:
            for obj in self.knightMoves:
                col = self.col + obj[0]
                row = self.row + obj[1]
                if 0 <= col < 8 and 0 <= row < 8 and board.squares[col][row].empty :
                    possibleMovessss[col][row] = True
                elif 0 <= col < 8 and 0 <= row < 8 and not board.squares[col][row].empty :
                        if testBoard[col][row]!=0 :
                            if testBoard[col][row].color!=self.color:
                                possibleMovessss[col][row] = True
                                if testBoard[col][row].name=="king":
                                    for rowP in range(ROW):
                                        for colP in range(COL):
                                            if testBoard[colP][rowP]!=0 and testBoard[colP][rowP].color!=self.color :
                                                testBoard[colP][rowP].check=True
                                    


        else:
                 
            for a in range(len(board.checkPos)):
                for obj in self.knightMoves:
                    #Move diagonally in all directions until the board ends or it touch a piece the same color or from another color
                    cols = self.col + obj[0] 
                    rows = self.row + obj[1] 
                    if cols == board.checkPos[a][1] and rows == board.checkPos[a][0] and ( board.squares[cols][rows].empty or ( not board.squares[cols][rows].empty and board.piecesPos[cols][rows].color!=self.color ) ):
                        possibleMovessss[cols][rows] = True