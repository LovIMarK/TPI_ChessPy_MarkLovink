###ETML
###Auteur : Mark Lovink
###Date : 16.05.2023

#Import of library and files
import pygame
from Var import *


##### Summary
### player class to handle who's turn it is
### rect represents the position and surface of the player
### image represents the surface and color of is rectangle
### name represents the name of the player    
### playing represents a variable that know wich player is playing
### color represents the color of the player
### font represents the character font, and size of the text 
### text represents the text of the player 
### textRect represents the position of the text
### border represents the color and thickness of the player rectangle
##### Summary
class Player():

    def __init__(self,x,y,color,name,playing=False):
        super().__init__()
        self.rect = pygame.Rect(x, y, 200, WIDTH_SQUARE)
        self.image = pygame.Surface((200, 80))
        self.image.fill(WHITE)
        self.name=name
        self.playing=playing
        self.color=color
        self.font = pygame.font.Font(None, 24)
        self.text = self.font.render(self.name, True, BLACK)
        self.textRect = self.text.get_rect(center=self.rect.center)
        self.border=5


    ##### Summary
    ### Function that change the players turn
    ##### Summary
    def ChangePlayer(self):
        self.playing=not self.playing
    
    ##### Summary
    ### Function that draw hte rectangle of the player and his name
    ##### Summary
    def Draw(self,window):
        if self.playing:
            pygame.draw.rect(window, self.color, (self.rect.x-self.border,self.rect.y-self.border,self.rect.width+(2*self.border),self.rect.height+(2*self.border)),self.border)

        window.blit(self.image, self.rect)
        window.blit(self.text,self.textRect)
