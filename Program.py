###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023
###Description : Main files to display the game and handle the interaction with the players

#Import of library and files
import pygame
from Var import *
from Board import Board


pygame.init()


window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
window.fill((217,217,217))


board=Board(20,20)
allSquares=board.DrawBoard(window)
pieces=board.DrawPieces()

# Function that get all the squares positions and display it in the pygame window 
def Draw(allSquares,pieces,window):

    for obj in allSquares:
        window.blit(obj.image, obj.rect)
    for obj in pieces:
        pygame.draw.rect(window, (255, 0, 0), obj.rect, 2)
        window.blit(obj.image, obj.rect)


#Main loop that display the pygame window and the game(board,pawn,pieces)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
       
               
    Draw(allSquares,pieces,window)
    
    pygame.display.flip()
    print (clock.get_fps())
    #function to control the frame rate or the maximum number of frames per second (FPS) 
    clock.tick(60)