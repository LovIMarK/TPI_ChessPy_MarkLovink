###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023

#Import of library and files
import pygame
from Var import *
import copy

##### Summary
### parent class piece handling all the position, surface, font, name, possible movement of the pieces and pawn
### rect represents the position and surface of the pieces
### font represents the character font, and size of the pieces 
### id represents unique id of the pieces    
### color represents the color of the pieces   
### name represents the name of the pieces
### col represents the column position of a piece 
### row represents the row position of a piece 
### clicked represents a variable to know if the pieces has been clicked or not 
### check represents a variable to know if the king and is pieces are in check
### possibleMoves represents a list with the possible movement of a piece
##### Summary
class Piece():

    def __init__(self,x,y,size,color,col,row,name,id,check=False):
        super().__init__()
        self.rect = pygame.Rect(x, y, size, size)
        self.font = pygame.font.Font("Fonts/DejaVuSans.ttf", size)
        self.id=id
        self.color=color
        self.name=name
        self.col=col
        self.row=row
        self.clicked=False
        self.check=check
        self.possibleMoves=[]
        

    ##### Summary
    ### Function that check if one piece has already been selected
    ##### Summary
    ### Return true or false
    def CheckClicked(self,board):
        clicked=False
        for row in range(ROW):
            for col in range(COL):
                if board.piecesPos[col][row]!=0 and board.piecesPos[col][row].clicked:
                    clicked =True
        return clicked

    ##### Summary
    ### Function that change the position of the piece selected with the mouse position
    ##### Summary
    def MouvementPlayer(self,posMouse,board): 
        if self.clicked :
            self.rect.center=posMouse
        # Else change the surface to prevent a false click
        elif self.rect!=pygame.Rect(self.col*WIDTH_SQUARE+board.x,self.row*WIDTH_SQUARE+board.y,WIDTH_SQUARE,WIDTH_SQUARE):
            self.rect=pygame.Rect(self.col*WIDTH_SQUARE+board.x,self.row*WIDTH_SQUARE+board.y,WIDTH_SQUARE,WIDTH_SQUARE)


    ##### Summary
    ### Function that change the variable if already clicked or not and change the values of the old piece to is new position
    ##### Summary
    def Clicked(self,posMouse,players,board):
        # If mouse on piece and another piece has not been selected
        if not self.CheckClicked(board) and self.rect==pygame.Rect(self.col*WIDTH_SQUARE+board.x,self.row*WIDTH_SQUARE+board.y,WIDTH_SQUARE,WIDTH_SQUARE) :
            self.clicked=True
        else:
            self.clicked=False
        
        if not self.clicked:
            for row in range(ROW):
                for col in range(COL):
                    # Check on wich square is the position of the piece
                    if board.squares[col][row].rect.collidepoint(posMouse)  :
                        #if the move is possible
                        if self.possibleMoves[col][row]:
                           
                            ###Dead piece
                            if not board.squares[col][row].empty:
                                board.piecesDie.append(board.piecesPos[col][row])

                            ### Change piece information
                            board.allMovement.append((self.col,self.row,col,row))
                            board.piecesPos[col][row]=board.piecesPos[self.col][self.row]
                            board.piecesPos[self.col][self.row]=0
                            board.squares[self.col][self.row].empty=True
                            board.squares[col][row].empty=False
                            self.col=col
                            self.row=row
                            self.rect=pygame.Rect(self.col*WIDTH_SQUARE+board.x,self.row*WIDTH_SQUARE+board.y,WIDTH_SQUARE,WIDTH_SQUARE)
                            self.firstMove=False
                            
                            ### Change the check status
                            if board.piecesPos[col][row].check and board.piecesPos[col][row].color==self.color:
                                for row2 in range(ROW):
                                    for col2 in range(COL):
                                        if board.piecesPos[col2][row2]!=0:
                                            board.piecesPos[col2][row2].check=False

                            
                            ###Change player
                            for obj in players:
                                obj.ChangePlayer()

                            

    ##### Summary
    ### This function is used to simulate all the piece moves to verify if the king will be in check on the next move
    ##### Summary
    ### Returns the value indicating whether the king will be in check or not 
    def Simulation(self,board):
        ### Copy the actual board
        simulateBoard=[[0] * COL for i in range(ROW)]
        for row in range(ROW):
            for col in range(COL):
                simulateBoard[col][row]=copy.copy(board.piecesPos[col][row])
  
        ###Remove the piece to simulate a move
        simulateBoard[self.col][self.row]=0

        ###Simulate the next round with the actual piece removed
        for row in range(ROW):
            for col in range(COL):
                if simulateBoard[col][row]!=0 and  simulateBoard[col][row].color!=self.color :
                    simulateBoard[col][row].MouvementSimulation(simulateBoard,board) 

        ### If a piece is removed and it puts its own king in check, the possible moves of that piece are restricte
        for row in range(ROW):
            for col in range(COL):
                if simulateBoard[col][row]!=0 and  simulateBoard[col][row].color==self.color and simulateBoard[col][row].check:
                    return True

        return False
