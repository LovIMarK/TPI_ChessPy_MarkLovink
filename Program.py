###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023
###Description : Main files to display the game and handle the interaction with the players

#Import of library and files
import pygame
import json
from Var import *
from Board import Board
from Player import Player

pygame.init()

#Set the window dimensions
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()



board=Board(20,20)


playerOne=Player(board.x+board.size+WIDTHSQUARE,board.y,BLUE,"Player One",True)
playerTwo=Player(board.x+board.size+WIDTHSQUARE,board.y+board.size-WIDTHSQUARE,RED,"Player Two")#playerTwo=Player(RED,True)
players=[playerOne,playerTwo]



def SafeGame(board,players):
    
    pieces_data = []
    if players[0].playing:
        player=players[0].name
    else:
        player=players[1].name
    for row in range(ROW):
        for col in range(COL):
            if board.PiecesPos[col][row]!=0:    
                piece_data = {
                    'id': board.PiecesPos[col][row].id,
                    'col': board.PiecesPos[col][row].col,
                    'row': board.PiecesPos[col][row].row,
                    'player':player
                }
                pieces_data.append(piece_data)

    # Définissez le chemin du fichier JSON
    file_path = 'pieces.json'

    # Enregistrez les données dans le fichier JSON
    with open(file_path, 'w') as file:
        json.dump(pieces_data, file)





def LoadGame(board,players):
    file_path = 'pieces.json'

    # Charger les données depuis le fichier JSON
    with open(file_path, 'r') as file:
        pieces_data = json.load(file)

    # Liste pour stocker les objets Piece
    pieces = []

    # Parcourir les données des pièces
    for piece_data in pieces_data:
        id = piece_data['id']
        col = piece_data['col']
        row = piece_data['row']
        player = piece_data['player']
        
        
        # Ajouter l'objet Piece à la liste
        pieces.append((id,col,row,player))
         
    for row in range(ROW):
        for col in range(COL):
            if board.PiecesPos[col][row]!=0:
                for i in range(len(pieces)):
                    ###ChatGPT how to check if a number is not in a list
                    if not any(i == id[0] for id in pieces) and board.PiecesPos[col][row].id==i:
                    ###
                        board.pieceDies.append(board.PiecesPos[col][row])
                        break
                    if board.PiecesPos[col][row].id==pieces[i][0]:
                        if board.PiecesPos[col][row].col!=pieces[i][1] or board.PiecesPos[col][row].row!=pieces[i][2]:
                            board.PiecesPos[col][row].col=pieces[i][1]
                            board.PiecesPos[col][row].row=pieces[i][2]
                            board.PiecesPos[col][row].firstMove=True
                            tempPiece = board.PiecesPos[col][row]
                            board.PiecesPos[pieces[i][1]][pieces[i][2]]=tempPiece
                            board.PiecesPos[col][row]=0
                        break

    for row in range(ROW):
        for col in range(COL):        
            if board.PiecesPos[col][row]!=0:
                board.Square[col][row].empty=False
            else:
                board.Square[col][row].empty=True
    for obj in players:
        if obj.name==pieces[0][3]:
            obj.playing=True
        else:
            obj.playing=False


   

# Function that get all the squares positions and display it in the pygame window 
def Draw(board,window,players):   
    
    ###Draw board
    for row in range(ROW):
        for col in range(COL):
            window.blit(board.Square[col][row].image, board.Square[col][row].rect)
           

    ###Draw pieces
    for row in range(ROW):
        for col in range(COL):
            if not board.lastShowMovement:
                if board.PiecesPos[col][row]!=0 and not board.PiecesPos[col][row].clicked :
                    window.blit(board.PiecesPos[col][row].image,(board.PiecesPos[col][row].col*WIDTHSQUARE+board.x,board.PiecesPos[col][row].row*WIDTHSQUARE+board.y))
                   # pygame.draw.rect(window, (255, 0, 0), board.PiecesPos[col][row].rect, 2)
                    
                elif board.PiecesPos[col][row]!=0 and board.PiecesPos[col][row].clicked:
                    window.blit(board.PiecesPos[col][row].image,board.PiecesPos[col][row].rect)
                    #pygame.draw.rect(window, (255, 0, 0), board.PiecesPos[col][row].rect, 2)

                    
            # else :
            #     if board.lastMovement[col][row]!=0:
            #         window.blit(board.lastMovement[col][row].image,board.lastMovement[col][row].rect)


    ###Draw possible movements                
    for row in range(ROW):
        for col in range(COL):
            if board.PiecesPos[col][row]!=0 and board.PiecesPos[col][row].clicked:
                for rowP in range(ROW):
                    for colP in range(COL):
                        if board.PiecesPos[col][row].possibleMoves[colP][rowP]!=0:
                            pygame.draw.circle(window, GOLD, (colP*WIDTHSQUARE+board.x+(WIDTHSQUARE/2),rowP*WIDTHSQUARE+board.y+(WIDTHSQUARE/2)), 15 )


    ###Draw dead pieces
    ###ChatGPT how to sort a list by name
    sorted_list = sorted(board.pieceDies, key=lambda obj: ( obj.color,obj.name))
    ###
    index=0
    reset_index = False
    for obj in sorted_list:
        
        if obj.color==players[0].color:
            index+=1
            window.blit(obj.image,(board.size+board.x+(index*30),players[0].rect.y+obj.image.get_height()))
        else:
            if not reset_index:
                index=0
                reset_index=True
            index+=1
            window.blit(obj.image,(board.size+board.x+(index*30),board.size+(obj.image.get_height()/2)))
    
    


    ###Draw players
    for obj in players:
        obj.Draw(window)
                
                



def HandlePossibleMouvement(board): 
    for row in range(ROW):
        for col in range(COL):
            if board.PiecesPos[col][row]!=0:
                board.PiecesPos[col][row].Mouvement(board)

#LoadGame(board,players)
Run=True
#Main loop that display the pygame window and the game(board,pawn,pieces)
while Run:
    window.fill(GREY)
    board.DrawBorder(window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SafeGame(board,players)
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEMOTION :
            posMouse = pygame.mouse.get_pos()
            if not board.lastShowMovement:
                for row in range(ROW):
                    for col in range(COL):
                        if board.PiecesPos[col][row]!=0:
                                board.PiecesPos[col][row].MouvementPlayer(posMouse,board) 
        elif event.type == pygame.MOUSEBUTTONDOWN :
            posMouse = pygame.mouse.get_pos()
            stopLoops = False
            if playerOne.rect.collidepoint(posMouse):
                board.lastShowMovement=True
            if not board.lastShowMovement:    
                for row in range(ROW):
                    for col in range(COL):
                        if board.PiecesPos[col][row]!=0:
                            if playerOne.playing  and board.PiecesPos[col][row].color==playerOne.color:
                                if board.PiecesPos[col][row].rect.collidepoint(posMouse):
                                    board.PiecesPos[col][row].Clicked(posMouse,players,board)
                                    stopLoops=True
                                    break
                            elif playerTwo.playing   and board.PiecesPos[col][row].color==playerTwo.color:
                                if board.PiecesPos[col][row].rect.collidepoint(posMouse):
                                    board.PiecesPos[col][row].Clicked(posMouse,players,board)
                                    stopLoops=True
                                    break

                    if stopLoops:
                        break    
                        

       

    HandlePossibleMouvement(board)
    Draw(board,window,players)
    pygame.display.flip()
    #print (clock.get_fps())
    #function to control the frame rate or the maximum number of frames per second (FPS) 
    clock.tick(60)