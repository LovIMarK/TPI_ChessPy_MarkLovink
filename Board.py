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


####
### class handling all the position of the squares and the pieces on a chess board
####
class Board():

    def __init__(self,x,y):
        self.size=8*WIDTHSQUARE
        self.border=5
        self.x=x
        self.y=y
        self.PiecesPos=[]
        self.Square=[]
        self.DrawBoard()
        self.DrawPieces()


    def DrawBorder(self,window):
        pygame.draw.rect(window, BLACK, (self.x-(self.border*2),self.y-(self.border*2),self.size+(self.border*4),self.size+(self.border*4)),self.border)

    def DrawBoard(self):
        
  

        self.Square = [[0] * 8 for _ in range(8)]
        

        for i in range(ROW):
            for j in range(COL):
                if j%2==0 and i%2==0:
                    self.Square[j][i]=Square(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),j,i,WIDTHSQUARE,BLACK)
                elif j%1==0 and i%2==0:
                    self.Square[j][i]=Square(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),j,i,WIDTHSQUARE,WHITE)
                elif j%2==0 and i%1==0:
                    self.Square[j][i]=Square(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),j,i,WIDTHSQUARE,WHITE)
                else:
                    self.Square[j][i]=Square(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),j,i,WIDTHSQUARE,BLACK)
            
               
        return self.Square
    


    def DrawPieces(self):
        self.PiecesPos = [[0] * 8 for _ in range(8)]
        for i in range(8):
            for j in range(8): 
                if i==0:
                    if j==0 or j==7:
                        self.PiecesPos[j][i]=King(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE, BLUE,ROOK,j,i)
                        self.Square[j][i].empty=False
                    elif j==1 or j==6:
                        self.PiecesPos[j][i]=King(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE, BLUE,KNIGHT,j,i)
                        self.Square[j][i].empty=False
                    elif j==2 or j==5:
                        self.PiecesPos[j][i]=King(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE, BLUE,BISHOP,j,i)
                        self.Square[j][i].empty=False
                    elif j==3:
                        self.PiecesPos[j][i]=King(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE, BLUE,QUEEN,j,i)
                        self.Square[j][i].empty=False
                    elif j==4:
                        self.PiecesPos[j][i]=King(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE, BLUE,KING,j,i)
                        self.Square[j][i].empty=False
                elif  i==7:
                    if j==0 or j==7:
                        self.PiecesPos[j][i]=King(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE, RED,ROOK,j,i)
                        self.Square[j][i].empty=False
                    elif j==1 or j==6:
                        self.PiecesPos[j][i]=King(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE, RED,KNIGHT,j,i)
                        self.Square[j][i].empty=False
                    elif j==2 or j==5:
                        self.PiecesPos[j][i]=King(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE, RED,BISHOP,j,i)
                        self.Square[j][i].empty=False
                    elif j==3:
                        self.PiecesPos[j][i]=King(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE, RED,QUEEN,j,i)
                        self.Square[j][i].empty=False
                    elif j==4:
                        self.PiecesPos[j][i]=King(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE, RED,KING,j,i)
                        self.Square[j][i].empty=False
                if i==1 :
                    self.PiecesPos[j][i]=Pawn(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE, BLUE,PAWN,j,i)
                    self.Square[j][i].empty=False
                elif i==6:
                    self.PiecesPos[j][i]=Pawn(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE,RED,PAWN,j,i)
                    self.Square[j][i].empty=False

        return self.PiecesPos