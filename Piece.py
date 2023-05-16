import pygame
from Var import *


class Piece():

    def __init__(self,x,y,size,color,colX,colY,name):
        super().__init__()
        self.rect = pygame.Rect(x, y, size, size)
        self.size=size
        self.color=color
        self.name=name
        self.font = pygame.font.Font("Fonts/DejaVuSans.ttf", self.rect.size[0])
        self.colX=colX
        self.colY=colY
        self.size=size
        self.attack=False
        self.clicked=False
        self.possibleMoves=[]
        self.die=[]


