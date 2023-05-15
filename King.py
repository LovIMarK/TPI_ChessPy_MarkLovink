import pygame
from Piece import Piece

class King(Piece):

    def __init__(self,x,y,size,color,unicode):
        super().__init__(x,y,size,color)
        self.unicode_char = unicode
        self.image = self.font.render(self.unicode_char, True, color)
        
        
    
    def Mouvement(self,posMouse):
        if self.clicked:
            self.rect.center=posMouse

    def Clicked(self):
        self.clicked=not self.clicked
    

    