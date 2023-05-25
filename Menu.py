###ETML
###Auteur : Mark Lovink
###Date : 23.05.2023
###Description : Main files to display the game and handle the interaction with the players


#Import of library and files
import pygame
from Var import *
from Button import Button
from Game import Game

pygame.init()

#Set the window dimensions
window = pygame.display.set_mode((WIDTH_WINDOW, HEIGHT_WINDOW))
pygame.display.set_caption("ChessPy")
clock = pygame.time.Clock()


buttonTwoPlayers=Button(100,HEIGHT_WINDOW/2-80,100,80,"2 Players")
buttonLastGame=Button(100,buttonTwoPlayers.rect.y+buttonTwoPlayers.rect.height,100,80,"Last Game")

chessGame=Game(window)

Run=True
#Main loop that display the pygame window and the game(board,pawn,pieces)
while Run:
    window.fill(GREY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN :
            posMouse = pygame.mouse.get_pos()
            if buttonTwoPlayers.rect.collidepoint(posMouse):
                    chessGame.StartGame()
                    chessGame.load=False
            elif buttonLastGame.rect.collidepoint(posMouse):
                chessGame.load=True
                chessGame.StartGame()

    buttonTwoPlayers.Draw(window)
    buttonLastGame.Draw(window)
    pygame.draw.rect(window, BLACK, (10,10,WIDTH_WINDOW-20,HEIGHT_WINDOW-20),5)

    pygame.display.flip()
    #print (clock.get_fps())
    #function to control the frame rate or the maximum number of frames per second (FPS) 
    clock.tick(60)

