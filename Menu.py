#Import of library and files
import pygame
from Var import *
from Button import Button
from Program import Chess

pygame.init()

#Set the window dimensions
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


buttonTwoPlayers=Button(100,HEIGHT/2-80,100,80,"2 Players")
buttonLastGame=Button(100,buttonTwoPlayers.rect.y+buttonTwoPlayers.rect.height,100,80,"Last Game")

chessGame=Chess(window)

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
                chessGame.Game()
                pass
            elif buttonLastGame.rect.collidepoint(posMouse):
                chessGame.load=True
                chessGame.Game()
                pass

    buttonTwoPlayers.Draw(window)
    buttonLastGame.Draw(window)
    pygame.draw.rect(window, BLACK, (10,10,WIDTH-20,HEIGHT-20),5)

    pygame.display.flip()
    print (clock.get_fps())
    #function to control the frame rate or the maximum number of frames per second (FPS) 
    clock.tick(60)

