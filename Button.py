###ETML
###Auteur : Mark Lovink
###Date : 23.05.2023

#Import of library and files
import pygame
from Var import *


##### Summary
### class button handling the position, background, text and interaction with a button
### rect represents the position and surface of the button
### text represents the text of the button 
### clicked represents a variabole to know if the button has been clicked or not
### font represents the character font, and size of the text
### clickCount stores the frames per second in order to perform an action after a certain period of time
### bgColor represents the background color of the button
### onButton represents a variable that check if the mouse is on the button
##### Summary
class Button:
    def __init__(self, x, y, width, height, text=""):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.clicked=False
        self.font = pygame.font.Font(None, 36)
        self.clickCount=0
        self.bgColor=WHITE
        self.onButton=False


    ##### Summary
    ### Function that draw the button and is text in the middle of the button
    ##### Summary
    def Draw(self,window):
        texte = self.font.render(self.text, True, BLACK)
        texte_rect = texte.get_rect(center=self.rect.center)
        window.blit(texte, texte_rect)
    

    ##### Summary
    ### Function that check if the mouse is on the button or not
    ##### Summary
    def OnButton(self, posMouse):
        if self.rect.collidepoint(posMouse):
            self.onButton = True
        else:
            self.onButton = False


    ##### Summary
    ### Function that draw the background of the button and change color if clicked or on the button
    ##### Summary
    def DrawBackGround(self,window):
        if self.clicked:
            self.clickCount+=1
            self.bgColor=BLACK
            if self.clickCount>10:
                self.bgColor=WHITE
                self.clickCount=0
                self.clicked=False
        if self.onButton and self.text:
            self.bgColor=BLUE
        else:
            self.bgColor=WHITE

        
        pygame.draw.rect(window, self.bgColor, self.rect)
        pygame.draw.rect(window, BLACK, self.rect,5)     


    ##### Summary
    ### Function that change the clicked variable
    ##### Summary
    def Clicked(self):
        self.clicked=True
        
            


