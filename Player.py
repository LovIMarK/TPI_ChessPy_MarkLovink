###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023
###Description : Player files to Handle who's turn it is 

import pygame
from Var import *

class Player():

    def __init__(self,color,playing=False):
        self.playing=playing
        self.color=color
    
    def ChangePlayer(self):
        self.playing=not self.playing
