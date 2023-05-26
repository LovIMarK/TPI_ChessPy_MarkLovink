###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023
###Description : Square files handling each square on a chess board

#Import of library and files
import pygame


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
        self.image.fill(color)
        self.col=col
        self.row=row
        self.empty=empty
        self.name=name
    
    
