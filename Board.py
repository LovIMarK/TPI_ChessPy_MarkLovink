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
        self.sqarePos=[]



    def DrawBoard(self,window):
        
        pygame.draw.rect(window, BLACK, (self.x-(self.border*2),self.y-(self.border*2),self.size+(self.border*4),self.size+(self.border*4)),self.border)

        for i in range(8):
            for j in range(8):
                if j%2==0 and i%2==0:
                    self.sqarePos.append(Square(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE,BLACK))
                elif j%1==0 and i%2==0:
                    self.sqarePos.append(Square(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE,WHITE))
                elif j%2==0 and i%1==0:
                    self.sqarePos.append(Square(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE,WHITE))
                else:
                    self.sqarePos.append(Square(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE,BLACK))
            
               
        return self.sqarePos
    


    def DrawPieces(self):
        pawnPos=[]
        for i in range(8):
            for j in range(8): 
                if i==0:
                    if j==0 or j==7:
                        pawnPos.append(King(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE, BLUE,ROOK))
                    elif j==1 or j==6:
                        pawnPos.append(King(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE, BLUE,KNIGHT))
                    elif j==2 or j==5:
                        pawnPos.append(King(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE, BLUE,BISHOP))
                    elif j==3:
                        pawnPos.append(King(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE, BLUE,QUEEN))
                    elif j==4:
                        pawnPos.append(King(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE, BLUE,KING))
                elif  i==7:
                    if j==0 or j==7:
                        pawnPos.append(King(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE, RED,ROOK))
                    elif j==1 or j==6:
                        pawnPos.append(King(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE, RED,KNIGHT))
                    elif j==2 or j==5:
                        pawnPos.append(King(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE, RED,BISHOP))
                    elif j==3:
                        pawnPos.append(King(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE, RED,QUEEN))
                    elif j==4:
                        pawnPos.append(King(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE, RED,KING))
                elif i==1 :
                    pawnPos.append(Pawn(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE, BLUE,PAWN))
                elif i==6:
                    pawnPos.append(Pawn(self.x+(WIDTHSQUARE*j),self.y+(WIDTHSQUARE*i),WIDTHSQUARE,RED,PAWN))

        return pawnPos