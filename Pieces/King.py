###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023

#Import of library and files
from Pieces.Piece import Piece
from Var import *
import copy


#####
### Class king handles all authorized movements of the king and is font/character. 
### image represents the character/shape of the king
### kingMoves represents the directions in which a king can move
#####
class King(Piece):

    def __init__(self,x,y,size,color,unicode,col,row,id, check=False):
        super().__init__(x,y,size,color,col,row,"king",id,check)
        self.unicode=unicode
        self.image = self.font.render(unicode, True, color)
        self.kingMoves = [(0, 1), (1, 1), (-1, 1), (0, -1), (1, -1), (-1, -1), (1, 0), (-1, 0)]
        self.check=False
    
  

    ###This function is used to check all the available movements of the king on the chessboard
    def Mouvement(self,board):
        #Create a two-dimensional table that save all the possible moves
        self.possibleMoves= [[0] * COL for i in range(ROW)]

        for obj in self.kingMoves:
            col = self.col + obj[0]
            row = self.row + obj[1]
            if 0 <= col < 8 and 0 <= row < 8 and board.squares[col][row].empty  :
                
                self.possibleMoves[col][row] = True
            elif 0 <= col < 8 and 0 <= row < 8 and not board.squares[col][row].empty :
                if board.piecesPos[col][row]!=0 :
                    if board.piecesPos[col][row].color!=self.color:
                        self.possibleMoves[col][row] = True
                        if board.piecesPos[col][row].name=="king":
                            board.piecesPos[col][row].check=True
        self.KingSimulation(board,self.possibleMoves)
        
    def KingSimulation(self,board,possibleMoves):
        simulation = copy.copy(King(self.rect.x,self.rect.y,self.rect.size[0],self.color,self.unicode,self.col,self.row,self.id,self.check))
        simulateCol=copy.copy(self.col)
        simulateRoW=copy.copy( self.row)
        for obj in self.kingMoves:
            cols = self.col + obj[0]
            rows = self.row + obj[1]
            testBoard=[[0] * COL for i in range(ROW)]
            
            for row in range(ROW):
                for col in range(COL):
                    testBoard[col][row]=copy.copy(board.piecesPos[col][row])
                    if testBoard[col][row]!=0:  
                        testBoard[col][row].check=False

            if 0 <= cols < 8 and 0 <= rows < 8 and possibleMoves[cols][rows]:
                testBoard[cols][rows]=simulation
                testBoard[simulateCol][simulateRoW]=0
                board.squares[cols][rows].empty=False
                board.squares[simulateCol][simulateRoW].empty=True

                for row in range(ROW):
                    for col in range(COL):
                        if testBoard[col][row]!=0 and  testBoard[col][row].color!=self.color :
                            testBoard[col][row].MouvementSimulation(testBoard,board) 

                        
                for row in range(ROW):
                    for col in range(COL):
                        if testBoard[col][row]!=0 and  testBoard[col][row].color==self.color and testBoard[col][row].check:
                            possibleMoves[cols][rows]=0
                            testBoard[col][row].check=False
                
                        
                testBoard[cols][rows]=board.piecesPos[cols][rows]
                testBoard[simulateCol][simulateRoW]=simulation
                board.squares[simulateCol][simulateRoW].empty=False
                if board.piecesPos[cols][rows]==0:
                    board.squares[cols][rows].empty=True
                else:
                    board.squares[cols][rows].empty=False


        return possibleMoves

    ###This function is used to simulate all the available movements of the king on the chessboard for the next round
    def MouvementSimulation(self,testBoard,board):
        possibleMoves= [[0] * COL for i in range(ROW)]
       
        for obj in self.kingMoves:
            col = self.col + obj[0]
            row = self.row + obj[1]
            if 0 <= col < 8 and 0 <= row < 8 and board.squares[col][row].empty :
                
                possibleMoves[col][row] = True
            elif 0 <= col < 8 and 0 <= row < 8 and not board.squares[col][row].empty :
                if testBoard[col][row]!=0 :
                    if testBoard[col][row].color!=self.color:
                        possibleMoves[col][row] = True
                        if testBoard[col][row].name=="king":
                            testBoard[col][row].check=True
           
    