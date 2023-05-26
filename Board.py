###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023

#Import of library and files
import pygame
from Var import*
from Square import Square
from Pawn import Pawn
from King import King
from Rook import Rook
from Knight import Knight
from Queen import Queen
from Bishop import Bishop


##### Summary
### class board handling all the position of the squares and the pieces on a chess self
### size represents the size of the all self
### border represents the thickness of the border from the self 
### x represents the left start value of the self  
### y represents the top start value of the self
### showLastMovement is a variable to know if the program need to display the last movement
### piecesPos represents a list with all the pieces on the chess self
### squares represents a list with all the square of the chess self
### allMovement is a list that contains the current and previous column and row of all pieces that have been moved in a list
### piecesDie represents a list with all the pieces that have been lost
##### Summary
class Board():

    def __init__(self,x,y):
        self.size=8*WIDTH_SQUARE
        self.border=5
        self.x=x
        self.y=y
        self.showLastMovement=False
        self.piecesPos=[]
        self.squares=[]
        self.allMovement=[]
        self.piecesDie=[]
        self.Drawself()
        self.DrawPieces()

    ##### Summary
    ### Function that draw the border of the self
    ##### Summary
    def DrawBorder(self,window):
        pygame.draw.rect(window, BLACK, (self.x-(self.border*2),self.y-(self.border*2),self.size+(self.border*4),self.size+(self.border*4)),self.border)

    ##### Summary
    ### Function that saves in a table the position of all the squares for the self
    ##### Summary
    ### Return the table with all the squares
    def Drawself(self):
        self.squares = [[0] * COL for _ in range(ROW)]
        

        for row in range(ROW):
            for col in range(COL):
                if col%2==0 and row%2==0:
                    self.squares[col][row]=Square(self.x+(WIDTH_SQUARE*col),self.y+(WIDTH_SQUARE*row),col,row,WIDTH_SQUARE,WHITE)
                elif col%1==0 and row%2==0:
                    self.squares[col][row]=Square(self.x+(WIDTH_SQUARE*col),self.y+(WIDTH_SQUARE*row),col,row,WIDTH_SQUARE,BLACK)
                elif col%2==0 and row%1==0:
                    self.squares[col][row]=Square(self.x+(WIDTH_SQUARE*col),self.y+(WIDTH_SQUARE*row),col,row,WIDTH_SQUARE,BLACK)
                else:
                    self.squares[col][row]=Square(self.x+(WIDTH_SQUARE*col),self.y+(WIDTH_SQUARE*row),col,row,WIDTH_SQUARE,WHITE)
            
               
        return self.squares
    

        
    ##### Summary
    ### Function that saves in a table the position of all the pieces on the self
    ##### Summary
    ### Return the table with all the pieces
    def DrawPieces(self):
        id=0
        self.piecesPos = [[0] * COL for _ in range(ROW)]
        for row in range(8):
            for col in range(8): 
                if row==0:
                    if col==0 or col==7:
                        self.piecesPos[col][row]=Rook(self.x+(WIDTH_SQUARE*col),self.y+(WIDTH_SQUARE*row),WIDTH_SQUARE, BLUE,ROOK,col,row,id)
                        self.squares[col][row].empty=False
                    elif col==1 or col==6:
                        self.piecesPos[col][row]=Knight(self.x+(WIDTH_SQUARE*col),self.y+(WIDTH_SQUARE*row),WIDTH_SQUARE, BLUE,KNIGHT,col,row,id)
                        self.squares[col][row].empty=False
                    elif col==2 or col==5:
                        self.piecesPos[col][row]=Bishop(self.x+(WIDTH_SQUARE*col),self.y+(WIDTH_SQUARE*row),WIDTH_SQUARE, BLUE,BISHOP,col,row,id)
                        self.squares[col][row].empty=False
                    elif col==3:
                        self.piecesPos[col][row]=Queen(self.x+(WIDTH_SQUARE*col),self.y+(WIDTH_SQUARE*row),WIDTH_SQUARE, BLUE,QUEEN,col,row,id)
                        self.squares[col][row].empty=False
                    elif col==4:
                        self.piecesPos[col][row]=King(self.x+(WIDTH_SQUARE*col),self.y+(WIDTH_SQUARE*row),WIDTH_SQUARE, BLUE,KING,col,row,id)
                        self.squares[col][row].empty=False
                    id+=1
                elif  row==7:
                    if col==0 or col==7:
                        self.piecesPos[col][row]=Rook(self.x+(WIDTH_SQUARE*col),self.y+(WIDTH_SQUARE*row),WIDTH_SQUARE, RED,ROOK,col,row,id)
                        self.squares[col][row].empty=False
                    elif col==1 or col==6:
                        self.piecesPos[col][row]=Knight(self.x+(WIDTH_SQUARE*col),self.y+(WIDTH_SQUARE*row),WIDTH_SQUARE, RED,KNIGHT,col,row,id)
                        self.squares[col][row].empty=False
                    elif col==2 or col==5:
                        self.piecesPos[col][row]=Bishop(self.x+(WIDTH_SQUARE*col),self.y+(WIDTH_SQUARE*row),WIDTH_SQUARE, RED,BISHOP,col,row,id)
                        self.squares[col][row].empty=False
                    elif col==3:
                        self.piecesPos[col][row]=Queen(self.x+(WIDTH_SQUARE*col),self.y+(WIDTH_SQUARE*row),WIDTH_SQUARE, RED,QUEEN,col,row,id)
                        self.squares[col][row].empty=False
                    elif col==4:
                        self.piecesPos[col][row]=King(self.x+(WIDTH_SQUARE*col),self.y+(WIDTH_SQUARE*row),WIDTH_SQUARE, RED,KING,col,row,id)
                        self.squares[col][row].empty=False
                    id+=1
                elif row==1 :
                    self.piecesPos[col][row]=Pawn(self.x+(WIDTH_SQUARE*col),self.y+(WIDTH_SQUARE*row),WIDTH_SQUARE, BLUE,PAWN,col,row,id)
                    self.squares[col][row].empty=False
                    id+=1
                elif row==6:
                    self.piecesPos[col][row]=Pawn(self.x+(WIDTH_SQUARE*col),self.y+(WIDTH_SQUARE*row),WIDTH_SQUARE,RED,PAWN,col,row,id)
                    self.squares[col][row].empty=False
                    id+=1
        return self.piecesPos
    
    ##### Summary
    ### The function shows the last movement of the game by moving the piece back to its previous position
    ##### Summary
    def ShowLastMovement(self):
        if self.showLastMovement: 
            self.piecesPos[self.allMovement[len(self.allMovement)-1][0]][self.allMovement[len(self.allMovement)-1][1]] = self.piecesPos[self.allMovement[len(self.allMovement)-1][2]][self.allMovement[len(self.allMovement)-1][3]]
            self.piecesPos[self.allMovement[len(self.allMovement)-1][0]][self.allMovement[len(self.allMovement)-1][1]].col=self.allMovement[len(self.allMovement)-1][0]
            self.piecesPos[self.allMovement[len(self.allMovement)-1][0]][self.allMovement[len(self.allMovement)-1][1]].row=self.allMovement[len(self.allMovement)-1][1]
            self.piecesPos[self.allMovement[len(self.allMovement)-1][0]][self.allMovement[len(self.allMovement)-1][1]].rect=pygame.Rect(self.allMovement[len(self.allMovement)-1][0]*WIDTH_SQUARE+self.x,self.allMovement[len(self.allMovement)-1][1]*WIDTH_SQUARE+self.y,WIDTH_SQUARE,WIDTH_SQUARE)
            self.piecesPos[self.allMovement[len(self.allMovement)-1][2]][self.allMovement[len(self.allMovement)-1][3]]=0

            #If a piece has been lost during the last move show it again
            if len(self.piecesDie)>0 and self.piecesDie[len(self.piecesDie)-1].col==self.allMovement[len(self.allMovement)-1][2] and self.piecesDie[len(self.piecesDie)-1].row==self.allMovement[len(self.allMovement)-1][3]:
                self.piecesPos[self.piecesDie[len(self.piecesDie)-1].col][self.piecesDie[len(self.piecesDie)-1].row]=self.piecesDie[len(self.piecesDie)-1]
        else:
            self.piecesPos[self.allMovement[len(self.allMovement)-1][2]][self.allMovement[len(self.allMovement)-1][3]] =self.piecesPos[self.allMovement[len(self.allMovement)-1][0]][self.allMovement[len(self.allMovement)-1][1]] 
            self.piecesPos[self.allMovement[len(self.allMovement)-1][2]][self.allMovement[len(self.allMovement)-1][3]].col=self.allMovement[len(self.allMovement)-1][2]
            self.piecesPos[self.allMovement[len(self.allMovement)-1][2]][self.allMovement[len(self.allMovement)-1][3]].row=self.allMovement[len(self.allMovement)-1][3]
            self.piecesPos[self.allMovement[len(self.allMovement)-1][2]][self.allMovement[len(self.allMovement)-1][3]].rect=pygame.Rect(self.allMovement[len(self.allMovement)-1][2]*WIDTH_SQUARE+self.x,self.allMovement[len(self.allMovement)-1][3]*WIDTH_SQUARE+self.y,WIDTH_SQUARE,WIDTH_SQUARE)
            self.piecesPos[self.allMovement[len(self.allMovement)-1][0]][self.allMovement[len(self.allMovement)-1][1]]=0