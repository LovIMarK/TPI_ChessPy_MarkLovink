###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023
###Description : Square files handling each square on a chess board

#Import of library and files
import pygame

class Square():

    def __init__(self, x, y,colX,ColY,size,color,empty=True,name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, size, size)
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.colX=colX
        self.colY=ColY
        self.empty=empty
        self.name=name
    
    
