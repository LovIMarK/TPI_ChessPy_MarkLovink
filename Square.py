###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023
###Description : Square files handling each square on a chess board

#Import of library and files
import pygame

class Square():

    def __init__(self, x, y,size,color,empty=True):
        super().__init__()
        self.rect = pygame.Rect(x, y, size, size)
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.empty=empty
