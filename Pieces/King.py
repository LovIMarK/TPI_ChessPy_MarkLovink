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
    
  
    ##### Summary
    ###This function is used to check all the available movements of the king on the chessboard
    ##### Summary
    def Movement(self,board):
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

        self.KingSimulation(board,self.possibleMoves)
        

    ##### Summary
    ### This function restricts the king's movement if he tries to put himself in check
    ##### Summary
    ### Return the list with the new available moves
    def KingSimulation(self,board,possibleMoves):
        ### Create a copy of the king
        simulation = copy.copy(King(self.rect.x,self.rect.y,self.rect.size[0],self.color,self.unicode,self.col,self.row,self.id,False))
        simulateCol=copy.copy(self.col)
        simulateRoW=copy.copy( self.row)
        for obj in self.kingMoves:
            cols = self.col + obj[0]
            rows = self.row + obj[1]

            ### Create a copy of the board
            simulateBoard=[[0] * COL for i in range(ROW)]
            for row in range(ROW):
                for col in range(COL):
                    simulateBoard[col][row]=copy.copy(board.piecesPos[col][row])
                    if simulateBoard[col][row]!=0:  
                        simulateBoard[col][row].check=False

            ###Change the kings position with all is possible moves 
            if 0 <= cols < 8 and 0 <= rows < 8 and possibleMoves[cols][rows]:
                simulateBoard[cols][rows]=simulation
                simulateBoard[simulateCol][simulateRoW]=0
                board.squares[cols][rows].empty=False
                board.squares[simulateCol][simulateRoW].empty=True
                
                ###Simulate the next round with the new position of the king
                for row in range(ROW):
                    for col in range(COL):
                        if simulateBoard[col][row]!=0 and  simulateBoard[col][row].color!=self.color :
                            simulateBoard[col][row].MovementSimulation(simulateBoard,board) 

                ### If the new position of the king puts himself in check, remove this position from the list of possible positions for the king
                for row in range(ROW):
                    for col in range(COL):
                        if simulateBoard[col][row]!=0 and  simulateBoard[col][row].color==self.color and simulateBoard[col][row].check:
                            possibleMoves[cols][rows]=0
                            simulateBoard[col][row].check=False
                
                ### Reset simulation variable 
                simulateBoard[cols][rows]=board.piecesPos[cols][rows]
                simulateBoard[simulateCol][simulateRoW]=simulation
                board.squares[simulateCol][simulateRoW].empty=False
                if board.piecesPos[cols][rows]==0:
                    board.squares[cols][rows].empty=True
                else:
                    board.squares[cols][rows].empty=False


        return possibleMoves
    

    ##### Summary
    ### This function is used to simulate all the available movements of the king on the chessboard for the next round
    ##### Summary
    def MovementSimulation(self,simulateBoard,board):
        possibleMoves= [[0] * COL for i in range(ROW)]
       
        for obj in self.kingMoves:
            col = self.col + obj[0]
            row = self.row + obj[1]
            if 0 <= col < 8 and 0 <= row < 8 and board.squares[col][row].empty :
                
                possibleMoves[col][row] = True
            elif 0 <= col < 8 and 0 <= row < 8 and not board.squares[col][row].empty :
                if simulateBoard[col][row]!=0 :
                    if simulateBoard[col][row].color!=self.color:
                        possibleMoves[col][row] = True

           
    