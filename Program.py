###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023
###Description : Main files to display the game and handle the interaction with the players

#Import of library and files
import pygame
from Var import *
from Board import Board
from Player import Player


pygame.init()

#Set the window dimensions
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
window.fill(GREY)


playerOne=Player(BLUE,True)
playerTwo=Player(RED)#playerTwo=Player(RED,True)
players=[playerOne,playerTwo]

board=Board(20,20)
board.DrawBorder(window)

allBoards=board.Square
allPieces=board.PiecesPos

# Function that get all the squares positions and display it in the pygame window 
def Draw(allBoards,allPieces,window):   
    
    for i in range(ROW):
        for j in range(COL):
            window.blit(allBoards[j][i].image, allBoards[j][i].rect)

    for i in range(ROW):
        for j in range(COL):
            
            if allPieces[j][i]!=0 and not allPieces[j][i].clicked :
                window.blit(allPieces[j][i].image,(allPieces[j][i].colX*WIDTHSQUARE+20,allPieces[j][i].colY*WIDTHSQUARE+20))
               # pygame.draw.rect(window, (255, 0, 0), allPieces[j][i].rect, 2)
            elif allPieces[j][i]!=0 and allPieces[j][i].clicked:
                window.blit(allPieces[j][i].image,allPieces[j][i].rect)
                #pygame.draw.rect(window, (255, 0, 0), allPieces[j][i].rect, 2)
            if allPieces[j][i]!=0:
                for obj in allPieces[j][i].die:
                    if obj.color==BLUE:
                        #obj.image=pygame.transform.scale(obj.image, (50, 60))
                        window.blit(obj.image,(board.size+200,0))
                    else:
                        #obj.image=pygame.transform.scale(obj.image, (50, 60))
                        window.blit(obj.image,(board.size+200,board.size))
                
                


def HandlePossibleMouvement(allBoards,allPieces): 
    for i in range(ROW):
        for j in range(COL):
            if allPieces[j][i]!=0:
                allPieces[j][i].Mouvement(allBoards,allPieces)


Run=True
#Main loop that display the pygame window and the game(board,pawn,pieces)
while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEMOTION:
            posMouse = pygame.mouse.get_pos()
            for i in range(ROW):
                for j in range(COL):
                    if allPieces[j][i]!=0:
                        allPieces[j][i].MouvementPlayer(posMouse) 
        elif event.type == pygame.MOUSEBUTTONDOWN :
            posMouse = pygame.mouse.get_pos()
            ##Chat GPT how to stop 2 loops
            stopLoops = False
            ##
            for i in range(ROW):
                for j in range(COL):
                    if allPieces[j][i]!=0:
                        if playerOne.playing and allPieces[j][i].color==playerOne.color:
                            if allPieces[j][i].rect.collidepoint(posMouse):
                                allPieces[j][i].Clicked(posMouse,allBoards,allPieces,players)
                                stopLoops=True
                                break
                        if playerTwo.playing and allPieces[j][i].color==playerTwo.color:
                            if allPieces[j][i].rect.collidepoint(posMouse):
                                allPieces[j][i].Clicked(posMouse,allBoards,allPieces,players)
                                stopLoops=True
                                break

                if stopLoops:
                    break    
                        

       

    HandlePossibleMouvement(allBoards,allPieces)
    Draw(allBoards,allPieces,window)
    pygame.display.flip()
    #print (clock.get_fps())
    #function to control the frame rate or the maximum number of frames per second (FPS) 
    clock.tick(60)