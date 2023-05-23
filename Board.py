###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023
###Description : Board files handling all the position of the squares on a chess board

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


####
### class handling all the position of the squares and the pieces on a chess board
### size is the size of the all board
### border is the thickness of the border from the board 
### x is the left start value of the board  
### y is the top start value of the board
####
class Board():

    def __init__(self,x,y):
        self.size=8*WIDTHSQUARE
        self.border=5
        self.x=x
        self.y=y
        self.lastShowMovement=False
        self.PiecesPos=[]
        self.Square=[]
        self.lastMovement=[]
        self.pieceDies=[]
        self.DrawBoard()
        self.DrawPieces()


    #Function that draw the border of the board
    def DrawBorder(self,window):
        pygame.draw.rect(window, BLACK, (self.x-(self.border*2),self.y-(self.border*2),self.size+(self.border*4),self.size+(self.border*4)),self.border)

    #Function that save in a table the position of all the square for the board
    def DrawBoard(self):
        self.Square = [[0] * COL for _ in range(ROW)]
        

        for row in range(ROW):
            for col in range(COL):
                if col%2==0 and row%2==0:
                    self.Square[col][row]=Square(self.x+(WIDTHSQUARE*col),self.y+(WIDTHSQUARE*row),col,row,WIDTHSQUARE,WHITE)
                elif col%1==0 and row%2==0:
                    self.Square[col][row]=Square(self.x+(WIDTHSQUARE*col),self.y+(WIDTHSQUARE*row),col,row,WIDTHSQUARE,BLACK)
                elif col%2==0 and row%1==0:
                    self.Square[col][row]=Square(self.x+(WIDTHSQUARE*col),self.y+(WIDTHSQUARE*row),col,row,WIDTHSQUARE,BLACK)
                else:
                    self.Square[col][row]=Square(self.x+(WIDTHSQUARE*col),self.y+(WIDTHSQUARE*row),col,row,WIDTHSQUARE,WHITE)
            
               
        return self.Square
    

        

    def DrawPieces(self):
        self.PiecesPos = [[0] * COL for _ in range(ROW)]
        for row in range(8):
            for col in range(8): 
                if row==0:
                    if col==0 or col==7:
                        self.PiecesPos[col][row]=Rook(self.x+(WIDTHSQUARE*col),self.y+(WIDTHSQUARE*row),WIDTHSQUARE, BLUE,ROOK,col,row)
                        self.Square[col][row].empty=False
                    elif col==1 or col==6:
                        self.PiecesPos[col][row]=Knight(self.x+(WIDTHSQUARE*col),self.y+(WIDTHSQUARE*row),WIDTHSQUARE, BLUE,KNIGHT,col,row)
                        self.Square[col][row].empty=False
                    elif col==2 or col==5:
                        self.PiecesPos[col][row]=Bishop(self.x+(WIDTHSQUARE*col),self.y+(WIDTHSQUARE*row),WIDTHSQUARE, BLUE,BISHOP,col,row)
                        self.Square[col][row].empty=False
                    elif col==3:
                        self.PiecesPos[col][row]=Queen(self.x+(WIDTHSQUARE*col),self.y+(WIDTHSQUARE*row),WIDTHSQUARE, BLUE,QUEEN,col,row)
                        self.Square[col][row].empty=False
                    elif col==4:
                        self.PiecesPos[col][row]=King(self.x+(WIDTHSQUARE*col),self.y+(WIDTHSQUARE*row),WIDTHSQUARE, BLUE,KING,col,row)
                        self.Square[col][row].empty=False
                elif  row==7:
                    if col==0 or col==7:
                        self.PiecesPos[col][row]=Rook(self.x+(WIDTHSQUARE*col),self.y+(WIDTHSQUARE*row),WIDTHSQUARE, RED,ROOK,col,row)
                        self.Square[col][row].empty=False
                    elif col==1 or col==6:
                        self.PiecesPos[col][row]=Knight(self.x+(WIDTHSQUARE*col),self.y+(WIDTHSQUARE*row),WIDTHSQUARE, RED,KNIGHT,col,row)
                        self.Square[col][row].empty=False
                    elif col==2 or col==5:
                        self.PiecesPos[col][row]=Bishop(self.x+(WIDTHSQUARE*col),self.y+(WIDTHSQUARE*row),WIDTHSQUARE, RED,BISHOP,col,row)
                        self.Square[col][row].empty=False
                    elif col==3:
                        self.PiecesPos[col][row]=Queen(self.x+(WIDTHSQUARE*col),self.y+(WIDTHSQUARE*row),WIDTHSQUARE, RED,QUEEN,col,row)
                        self.Square[col][row].empty=False
                    elif col==4:
                        self.PiecesPos[col][row]=King(self.x+(WIDTHSQUARE*col),self.y+(WIDTHSQUARE*row),WIDTHSQUARE, RED,KING,col,row)
                        self.Square[col][row].empty=False
                if row==1 :
                    self.PiecesPos[col][row]=Pawn(self.x+(WIDTHSQUARE*col),self.y+(WIDTHSQUARE*row),WIDTHSQUARE, BLUE,PAWN,col,row)
                    self.Square[col][row].empty=False
                elif row==6:
                    self.PiecesPos[col][row]=Pawn(self.x+(WIDTHSQUARE*col),self.y+(WIDTHSQUARE*row),WIDTHSQUARE,RED,PAWN,col,row)
                    self.Square[col][row].empty=False

        return self.PiecesPos