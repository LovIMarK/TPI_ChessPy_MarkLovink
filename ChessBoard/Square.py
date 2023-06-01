###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023
###Description : Square files handling each square on a chess board

#Import of library and files
import pygame
from Var import *



##### Summary
### class square handling all the position, surface, name, color of the square composing the board
### rect represents the position and surface of the player
### image represents the surface and color of is rectangle
### col represents the column position of a square 
### row represents the row position of a square 
### empty represents a variable to check if the square empty or not
### name represents the name of the player    
##### Summary
class Square():

    def __init__(self, x, y,col,row,size,color,empty=True,name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, size, size)
        self.image = pygame.Surface((size, size))
        self.font = pygame.font.Font(None, 36)
        self.color=color
        self.image.fill(self.color)
        self.col=col
        self.row=row
        self.empty=empty
        self.name=name
    

    ##### Summary
    ### Function that draw the square 
    ##### Summary
    def Draw(self,window):
        window.blit( self.image, self.rect)


    ##### Summary
    ### Function that draw the number of the board row in the top corner left 
    ##### Summary    
    def DrawNumber(self,window,text):
        if self.color==BLACK:
            color=WHITE
        else:
            color=BLACK

        number= self.font.render("{0}".format(text), True, color)
        window.blit( number, (self.rect.x,self.rect.y))
    

    ##### Summary
    ### Function that draws the alphabet on the board's column in the bottom right corner
    ##### Summary    
    def DrawAlphabet(self,window,text):
        if self.color==BLACK:
            color=WHITE
        else:
            color=BLACK

        alphabet= self.font.render("{0}".format(chr(text + 97)), True, color)
        window.blit( alphabet, (self.rect.bottomright[0]-18,self.rect.bottomright[1]-24))
    
