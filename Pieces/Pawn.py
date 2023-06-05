###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023

#Import of library and files
from Pieces.Piece import Piece
from Var import *

#####
### Class pawn handles all authorized movements of the pawn and is font/character. 
### image represents the character/shape of the pawn
### firstMove represents a variable to know if the pawn has already been moved
#####

class Pawn(Piece):

    def __init__(self,x,y,size,color,unicode,col,row,id, check=False):
        super().__init__(x,y,size,color,col,row,"pawn",id,check)
        self.unicode=unicode
        self.image = self.font.render(unicode, True, color)
        self.firstMove=True


    ##### Summary
    ### This function is used to check all the available movements of the pawn on the chessboard
    ##### Summary
    def Mouvement(self,board):


        #Create a two-dimensional table that save all the possible moves
        ###ChatGPT : How to create a empty 2 dimensions table
        self.possibleMoves= [[0] * COL for i in range(ROW)]
        if not self.check and not self.Simulation(board):
            if self.color==BLUE :
                if self.row < COL-2  and board.squares[self.col][self.row+2].empty and board.squares[self.col][self.row+1].empty and self.firstMove  :
                    self.possibleMoves[self.col][self.row+2]=True
                if self.row < COL-1  and board.squares[self.col][self.row+1].empty  :
                    self.possibleMoves[self.col][self.row+1]=True



                if self.row < COL-1 and self.col >= 0 and self.col < 7  :
                    if board.piecesPos[self.col+1][self.row+1]!=0 :
                        if board.piecesPos[self.col+1][self.row+1].color!=self.color:
                            self.possibleMoves[self.col+1][self.row+1]=True
                            if board.piecesPos[self.col+1][self.row+1].name=="king":
                                for row2 in range(ROW):
                                    for col2 in range(COL):
                                        if board.piecesPos[col2][row2]!=0 and board.piecesPos[col2][row2].color!=self.color :
                                            board.piecesPos[col2][row2].check=True
                                        
                                board.checkPos=([(self.row,self.col)])
                    
                if self.row < COL-1 and self.col > 0 and self.col <= 7  :
                    if board.piecesPos[self.col-1][self.row+1]!=0 :
                        if board.piecesPos[self.col-1][self.row+1].color!=self.color:
                            self.possibleMoves[self.col-1][self.row+1]=True
                            if board.piecesPos[self.col-1][self.row+1].name=="king":
                                for row2 in range(ROW):
                                    for col2 in range(COL):
                                        if board.piecesPos[col2][row2]!=0 and board.piecesPos[col2][row2].color!=self.color :
                                            board.piecesPos[col2][row2].check=True
                                        
                                board.checkPos=([(self.row,self.col)])





            if self.color==RED:
                if self.row > 0 and board.squares[self.col][self.row-2].empty and board.squares[self.col][self.row-1].empty and self.firstMove :
                    self.possibleMoves[self.col][self.row-2]=True
                if self.row > 0 and board.squares[self.col][self.row-1].empty  :
                    self.possibleMoves[self.col][self.row-1]=True

        
                if self.row > 0 and self.col >= 0 and self.col < 7  :
                    if board.piecesPos[self.col+1][self.row-1]!=0 :
                        if board.piecesPos[self.col+1][self.row-1].color==BLUE:
                            self.possibleMoves[self.col+1][self.row-1]=True
                            if board.piecesPos[self.col+1][self.row-1].name=="king":
                                for row2 in range(ROW):
                                    for col2 in range(COL):
                                        if board.piecesPos[col2][row2]!=0 and board.piecesPos[col2][row2].color!=self.color :
                                            board.piecesPos[col2][row2].check=True
                                        
                                board.checkPos=([(self.row,self.col)])
                    
                if self.row > 0 and self.col > 0 and self.col <= 7 :
                    if board.piecesPos[self.col-1][self.row-1]!=0 :
                        if board.piecesPos[self.col-1][self.row-1].color==BLUE:
                            self.possibleMoves[self.col-1][self.row-1]=True
                            if board.piecesPos[self.col-1][self.row-1].name=="king":
                                for row2 in range(ROW):
                                    for col2 in range(COL):
                                        if board.piecesPos[col2][row2]!=0 and board.piecesPos[col2][row2].color!=self.color :
                                            board.piecesPos[col2][row2].check=True
                                        
                                board.checkPos=([(self.row,self.col)])

        else:
            for a in range(len(board.checkPos)):
                
                if self.color==BLUE :

                    if self.row < COL-2  and board.squares[self.col][self.row+2].empty and board.squares[self.col][self.row+1].empty and self.firstMove  :
                        if self.col==board.checkPos[a][1] and self.row+2==board.checkPos[a][0]:
                            self.possibleMoves[self.col][self.row+2]=True
                    if self.row < COL-1  and board.squares[self.col][self.row+1].empty :
                        if self.col==board.checkPos[a][1] and self.row+1==board.checkPos[a][0]:
                            self.possibleMoves[self.col][self.row+1]=True



                    if self.row < COL-1 and self.col >= 0 and self.col < 7  :
                        if board.piecesPos[self.col+1][self.row+1]!=0 :
                            if board.piecesPos[self.col+1][self.row+1].color!=self.color:
                                if self.col+1==board.checkPos[a][1] and self.row+1==board.checkPos[a][0]:
                                    self.possibleMoves[self.col+1][self.row+1]=True
                                    if board.piecesPos[self.col+1][self.row+1].name=="king":
                                        for row2 in range(ROW):
                                            for col2 in range(COL):
                                                if board.piecesPos[col2][row2]!=0 and board.piecesPos[col2][row2].color!=self.color :
                                                    board.piecesPos[col2][row2].check=True
                                                
                                        board.checkPos=([(self.row,self.col)])
                        
                    if self.row < COL-1 and self.col > 0 and self.col <= 7  :
                        if board.piecesPos[self.col-1][self.row+1]!=0 :
                            if board.piecesPos[self.col-1][self.row+1].color!=self.color:
                                if self.col-1==board.checkPos[a][1] and self.row+1==board.checkPos[a][0]:
                                    self.possibleMoves[self.col-1][self.row+1]=True
                                    if board.piecesPos[self.col-1][self.row+1].name=="king":
                                        for row2 in range(ROW):
                                            for col2 in range(COL):
                                                if board.piecesPos[col2][row2]!=0 and board.piecesPos[col2][row2].color!=self.color :
                                                    board.piecesPos[col2][row2].check=True
                                                
                                        board.checkPos=([(self.row,self.col)])





                if self.color==RED :
                    if self.row > 0 and board.squares[self.col][self.row-2].empty and board.squares[self.col][self.row-1].empty and self.firstMove:
                        if self.col==board.checkPos[a][1] and self.row-2==board.checkPos[a][0]:
                            self.possibleMoves[self.col][self.row-2]=True
                    if self.row > 0 and board.squares[self.col][self.row-1].empty:
                        if self.col==board.checkPos[a][1] and self.row-1==board.checkPos[a][0]:
                            self.possibleMoves[self.col][self.row-1]=True

            
                    if self.row > 0 and self.col >= 0 and self.col < 7  :
                        if board.piecesPos[self.col+1][self.row-1]!=0 :
                            if board.piecesPos[self.col+1][self.row-1].color==BLUE:
                                if self.col+1==board.checkPos[a][1] and self.row-1==board.checkPos[a][0]:
                                    self.possibleMoves[self.col+1][self.row-1]=True
                                    if board.piecesPos[self.col+1][self.row-1].name=="king":
                                        for row2 in range(ROW):
                                            for col2 in range(COL):
                                                if board.piecesPos[col2][row2]!=0 and board.piecesPos[col2][row2].color!=self.color :
                                                    board.piecesPos[col2][row2].check=True
                                                
                                        board.checkPos=([(self.row,self.col)])
                        
                    if self.row > 0 and self.col > 0 and self.col <= 7 :
                        if board.piecesPos[self.col-1][self.row-1]!=0 :
                            if board.piecesPos[self.col-1][self.row-1].color==BLUE:
                                if self.col-1==board.checkPos[a][1] and self.row-1==board.checkPos[a][0]:
                                    self.possibleMoves[self.col-1][self.row-1]=True
                                    if board.piecesPos[self.col-1][self.row-1].name=="king":
                                        for row2 in range(ROW):
                                            for col2 in range(COL):
                                                if board.piecesPos[col2][row2]!=0 and board.piecesPos[col2][row2].color!=self.color :
                                                    board.piecesPos[col2][row2].check=True
                                                
                                        board.checkPos=([(self.row,self.col)])

    
    ##### Summary
    ###This function is used to simulate all the available movements of the pawn on the chessboard for the next round
    ##### Summary
    def MouvementSimulation(self,simulateBoard,board):


        #Create a two-dimensional table that save all the possible moves
        ###ChatGPT : How to create a empty 2 dimensions table
        possibleMoves= [[0] * COL for i in range(ROW)]
        
        if self.color==BLUE and  not self.check:
            if self.row < COL-2  and board.squares[self.col][self.row+2].empty and board.squares[self.col][self.row+1].empty and self.firstMove :
                possibleMoves[self.col][self.row+2]=True
            if self.row < COL-1  and board.squares[self.col][self.row+1].empty:
                possibleMoves[self.col][self.row+1]=True



            if self.row < COL-1 and self.col >= 0 and self.col < 7  :
                if simulateBoard[self.col+1][self.row+1]!=0 :
                    if simulateBoard[self.col+1][self.row+1].color!=self.color:
                        possibleMoves[self.col+1][self.row+1]=True
                        if simulateBoard[self.col+1][self.row+1].name=="king":
                            for row2 in range(ROW):
                                for col2 in range(COL):
                                    if simulateBoard[col2][row2]!=0 and simulateBoard[col2][row2].color!=self.color :
                                        simulateBoard[col2][row2].check=True
                                    
                
            if self.row < COL-1 and self.col > 0 and self.col <= 7  :
                if simulateBoard[self.col-1][self.row+1]!=0 :
                    if simulateBoard[self.col-1][self.row+1].color!=self.color:
                        possibleMoves[self.col-1][self.row+1]=True
                        if simulateBoard[self.col-1][self.row+1].name=="king":
                            for row2 in range(ROW):
                                for col2 in range(COL):
                                    if simulateBoard[col2][row2]!=0 and simulateBoard[col2][row2].color!=self.color :
                                        simulateBoard[col2][row2].check=True
                                    





        if self.color==RED and  not self.check:
            if self.row > 0 and board.squares[self.col][self.row-2].empty and board.squares[self.col][self.row-1].empty and self.firstMove :
                possibleMoves[self.col][self.row-2]=True
            if self.row > 0 and board.squares[self.col][self.row-1].empty:
                possibleMoves[self.col][self.row-1]=True

    
            if self.row > 0 and self.col >= 0 and self.col < 7  :
                if simulateBoard[self.col+1][self.row-1]!=0 :
                    if simulateBoard[self.col+1][self.row-1].color==BLUE:
                        possibleMoves[self.col+1][self.row-1]=True
                        if simulateBoard[self.col+1][self.row-1].name=="king":
                            for row2 in range(ROW):
                                for col2 in range(COL):
                                    if simulateBoard[col2][row2]!=0 and simulateBoard[col2][row2].color!=self.color :
                                        simulateBoard[col2][row2].check=True
                                    
                
            if self.row > 0 and self.col > 0 and self.col <= 7 :
                if simulateBoard[self.col-1][self.row-1]!=0 :
                    if simulateBoard[self.col-1][self.row-1].color==BLUE:
                        possibleMoves[self.col-1][self.row-1]=True
                        if simulateBoard[self.col-1][self.row-1].name=="king":
                            for row2 in range(ROW):
                                for col2 in range(COL):
                                    if simulateBoard[col2][row2]!=0 and simulateBoard[col2][row2].color!=self.color :
                                        simulateBoard[col2][row2].check=True
                                    


        

       




    

    