import pygame

class Piece():

    def __init__(self,x,y,size,color):
        super().__init__()
        self.rect = pygame.Rect(x, y, size, size)
        self.size=size
        self.color=color
        self.font = pygame.font.Font("Fonts/DejaVuSans.ttf", self.rect.size[0])
        self.startPosX=x
        self.startPosY=y
        self.size=size
        self.exist=False
        self.clicked=False
