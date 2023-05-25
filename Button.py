import pygame
from Var import *



class Button:
    def __init__(self, x, y, width, height, text=""):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.clicked=False
        self.font = pygame.font.Font(None, 36)
        self.clickCount=0
        self.bgColor=WHITE
        self.onButton=False

    def Draw(self,window):
        
        
        texte = self.font.render(self.text, True, BLACK)
        texte_rect = texte.get_rect(center=self.rect.center)
        window.blit(texte, texte_rect)
    
    def OnButton(self, posMouse):
        if self.rect.collidepoint(posMouse):
            self.onButton = True
        else:
            self.onButton = False

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

    def Clicked(self):
        self.clicked=True
        
            


