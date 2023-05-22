###ETML
###Auteur : Mark Lovink
###Date : 16.05.2023
###Description : Player files to Handle who's turn it is 

import pygame
from Var import *

class Player():

    def __init__(self,x,y,color,name,playing=False):
        super().__init__()
        self.rect = pygame.Rect(x, y, 200, 80)
        self.image = pygame.Surface((200, 80))
        self.image.fill(WHITE)
        self.name=name
        self.playing=playing
        self.color=color
        self.font = pygame.font.Font(None, 24)
        self.text = self.font.render(self.name, True, BLACK)
        self.textRect = self.text.get_rect(center=self.rect.center)
        self.border=5
    
    def ChangePlayer(self):
        self.playing=not self.playing
    
    def Draw(self,window):
        if self.playing:
            pygame.draw.rect(window, self.color, (self.rect.x-self.border,self.rect.y-self.border,self.rect.width+(2*self.border),self.rect.height+(2*self.border)),self.border)

        
        window.blit(self.image, self.rect)
        window.blit(self.text,self.textRect)
