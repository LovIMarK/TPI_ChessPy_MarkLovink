import pygame
from Var import *



class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.clicked=False

    def Draw(self,window):
        
        font = pygame.font.Font(None, 36)
        texte = font.render(self.text, True, BLACK)
        texte_rect = texte.get_rect(center=self.rect.center)
        window.blit(texte, texte_rect)

    def DrawBackGround(self,window):
        pygame.draw.rect(window, WHITE, self.rect)
        pygame.draw.rect(window, BLACK, self.rect,5)     

    def Cliked(self):
        self.clicked=not self.clicked
            


