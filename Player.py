###ETML
###Auteur : Mark Lovink
###Date : 16.05.2023

#Import of library and files
import pygame
import time
from Var import *


##### Summary
### player class to handle who's turn it is
### rect represents the position and surface of the player
### image represents the surface and color of is rectangle
### name represents the name of the player    
### playing represents a variable that know wich player is playing
### winning represents a variable that know wich player has won
### color represents the color of the player
### font represents the character font, and size of the text 
### text represents the text of the player 
### textRect represents the position of the text
### border represents the color and thickness of the player rectangle
##### Summary
class Player():

    def __init__(self,x,y,color,name,playing=False,timerPaused=True):
        super().__init__()
        self.rect = pygame.Rect(x, y, 200, WIDTH_SQUARE)
        self.image = pygame.Surface((200, 80))
        self.image.fill(WHITE)
        self.name=name
        self.playing=playing
        self.winning=False
        self.draw=False
        self.color=color
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render(self.name, True, BLACK)
        self.textRect = self.text.get_rect(center=self.rect.center)
        self.border=5
        self.timer=time.time()
        self.timerPaused=timerPaused
        self.pausedTime=0
        self.PausedDuration=0
        self.actualTime=0
        



    ##### Summary
    ### Function that change the players turn and time
    ##### Summary
    def ChangePlayer(self):
        self.playing= not self.playing
        self.timerPaused=not self.timerPaused
        self.pausedTime = time.time() 
        
       
        
    
    ##### Summary
    ### Function that draw the rectangle of the player and his name
    ##### Summary
    def Draw(self,window):
        if self.playing:
            pygame.draw.rect(window, self.color, (self.rect.x-self.border,self.rect.y-self.border,self.rect.width+(2*self.border),self.rect.height+(2*self.border)),self.border)

        window.blit(self.image, self.rect)
        window.blit(self.text,self.textRect)

    ##### Summary
    ### Function that draw the rectangle of the winner and his name
    ##### Summary
    def DrawWinner(self,window,board):
        font = pygame.font.Font(None, 42)
        text=font.render("{0} : à gagné".format(self.name), True, BLACK)
        rect=pygame.Rect(board.size/2+board.x-(text.get_width()/2),board.size/2+board.y-80,300,80)
        texte_rect = text.get_rect(center=rect.center)
        pygame.draw.rect(window, WHITE, rect)
        pygame.draw.rect(window, self.color, rect,5)
        window.blit(text, texte_rect)


    ##### Summary
    ### Function that draw the rectangle where draw is writren
    ##### Summary
    def DrawDraw(self,window,board):
        font = pygame.font.Font(None, 42)
        text=font.render("Match nul", True, BLACK)
        rect=pygame.Rect(board.size/2+board.x-(text.get_width()/2),board.size/2+board.y-80,300,80)
        texte_rect = text.get_rect(center=rect.center)
        pygame.draw.rect(window, WHITE, rect)
        pygame.draw.rect(window, self.color, rect,5)
        window.blit(text, texte_rect)

    
    ##### Summary
    ### Function that draw the time of each player
    ##### Summary
    def DrawTimer(self,window):
        font = pygame.font.Font(None, 36)
        chrono = time.strftime("%M:%S", time.gmtime(self.actualTime))
        textChrono = font.render(chrono, True, (0, 0, 0))
        window.blit(textChrono, (self.rect.x+ (self.text.get_width()/2),self.rect.y+ self.border+(self.text.get_height()*2) ,self.rect.width,self.rect.height))

       

