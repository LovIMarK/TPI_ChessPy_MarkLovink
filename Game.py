###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023

#Import of library and files
import pygame
import json
from Var import *
from Board import Board
from Player import Player
from Button import Button



#####
### Class Game handles the game display, player interaction, and saved game handling
### window represents dimensions of the PyGame window
### load variable determines whether the saved game should be displayed or not
#####
class Game:
    def __init__(self,window,load=False):
        self.window=window
        self.load=load

        


    ##### Summary
    ### Function that saves the id, column, row of each pieces on the chess board and the player playing in a JSON file
    ##### Summary
    def SaveGame(self,board,players):
        
        piecesData = []

        if players[0].playing:
            player=players[0].name
        else:
            player=players[1].name


        for row in range(ROW):
            for col in range(COL):
                if board.piecesPos[col][row]!=0:    
                    pieceData = {
                        'id': board.piecesPos[col][row].id,
                        'col': board.piecesPos[col][row].col,
                        'row': board.piecesPos[col][row].row,
                        'player':player
                    }
                    piecesData.append(pieceData)

        filePath = 'pieces.json'

        # Open a JSON file with "w" to write the list of all piece information into it
        with open(filePath, 'w') as file:
            json.dump(piecesData, file)




    ##### Summary
    ### Function get the id, column, row of each pieces and the player playing in the JSON file and display it in the current game
    ##### Summary
    def LoadGame(self,board,players):
        filePath = 'pieces.json'

        # Open the JSON file with "r" to read the list of all piece information
        with open(filePath, 'r') as file:
            piecesData = json.load(file)

        pieces = []

        for pieceData in piecesData:
            id = pieceData['id']
            col = pieceData['col']
            row = pieceData['row']
            player = pieceData['player']
            
            pieces.append((id,col,row,player))


        # Run through all the board with the new pieces on it
        for row in range(ROW):
            for col in range(COL):
                if board.piecesPos[col][row]!=0:
                    # Run through the list with the pieces information
                    for i in range(len(pieces)):
                        ###ChatGPT how to check if a number is not in a list
                        # If the id is not in the JSON file the piece has been lost
                        if not any(i == id[0] for id in pieces) and board.piecesPos[col][row].id==i:
                        ###
                            board.piecesDie.append(board.piecesPos[col][row])
                            break
                        # If the pieces was not at the same position in the JSON file the piece change position
                        if board.piecesPos[col][row].id==pieces[i][0]:
                            if board.piecesPos[col][row].col!=pieces[i][1] or board.piecesPos[col][row].row!=pieces[i][2]:
                                board.piecesPos[col][row].col=pieces[i][1]
                                board.piecesPos[col][row].row=pieces[i][2]
                                board.piecesPos[col][row].firstMove=True
                                tempPiece = board.piecesPos[col][row]
                                board.piecesPos[pieces[i][1]][pieces[i][2]]=tempPiece
                                board.piecesPos[col][row]=0
                            break

        #Check if there is a piece on the square of the board, if yes, it is not empty
        for row in range(ROW):
            for col in range(COL):        
                if board.piecesPos[col][row]!=0:
                    board.squares[col][row].empty=False
                else:
                    board.squares[col][row].empty=True
        
        #Change the player playing
        for obj in players:
            if obj.name==pieces[0][3]:
                obj.playing=True
            else:
                obj.playing=False


    
    ##### Summary
    ### Function that get all the squares, the pieces, the player and display it in the pygame window 
    ##### Summary
    def Draw(self,board,window,players):   
        
        ###Draw board
        for row in range(ROW):
            for col in range(COL):
                window.blit(board.squares[col][row].image, board.squares[col][row].rect)
            

        ###Draw pieces
        for row in range(ROW):
            for col in range(COL):
                
                if board.piecesPos[col][row]!=0 and not board.piecesPos[col][row].clicked :
                    window.blit(board.piecesPos[col][row].image,(board.piecesPos[col][row].col*WIDTH_SQUARE+board.x,board.piecesPos[col][row].row*WIDTH_SQUARE+board.y))
                    # pygame.draw.rect(window, (255, 0, 0), board.piecesPos[col][row].rect, 2)
                    
                elif board.piecesPos[col][row]!=0 and board.piecesPos[col][row].clicked:
                    window.blit(board.piecesPos[col][row].image,board.piecesPos[col][row].rect)
                    #pygame.draw.rect(window, (255, 0, 0), board.piecesPos[col][row].rect, 2)


       
        ###Draw last movement 
        if board.showLastMovement:
            window.blit(board.piecesPos[board.allMovement[len(board.allMovement)-1][0]][board.allMovement[len(board.allMovement)-1][1]].image,(board.piecesPos[board.allMovement[len(board.allMovement)-1][0]][board.allMovement[len(board.allMovement)-1][1]].rect))
            pygame.draw.rect(window, GOLD, board.piecesPos[board.allMovement[len(board.allMovement)-1][0]][board.allMovement[len(board.allMovement)-1][1]].rect,5 )
            pygame.draw.rect(window, GOLD, (board.allMovement[len(board.allMovement)-1][2]*WIDTH_SQUARE+board.x,board.allMovement[len(board.allMovement)-1][3]*WIDTH_SQUARE+board.y,WIDTH_SQUARE,WIDTH_SQUARE),5 )
            
        ###Draw possible movements                
        for row in range(ROW):
            for col in range(COL):
                if board.piecesPos[col][row]!=0 and board.piecesPos[col][row].clicked:
                    for rowP in range(ROW):
                        for colP in range(COL):
                            if board.piecesPos[col][row].possibleMoves[colP][rowP]!=0:
                                pygame.draw.circle(window, GOLD, (colP*WIDTH_SQUARE+board.x+(WIDTH_SQUARE/2),rowP*WIDTH_SQUARE+board.y+(WIDTH_SQUARE/2)), 15 )


        ###Draw dead pieces
        ###ChatGPT how to sort a list by name
        sortedList = sorted(board.piecesDie, key=lambda obj: ( obj.color,obj.name))
        ###
        index=0
        reset_index = False
        for obj in sortedList:
            
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
                    
                    


    ##### Summary
    ### Function that check all the possible/legal moves of all pieces 
    ##### Summary
    def HandlePossibleMouvement(self,board): 
        for row in range(ROW):
            for col in range(COL):
                if board.piecesPos[col][row]!=0:
                    board.piecesPos[col][row].Mouvement(board)


    ##### Summary
    ### Main function handle the display of the game and manage the interaction with the players
    ##### Summary
    def StartGame(self):

        ###Variable implementation
        clock = pygame.time.Clock()
        board=Board(20,20)
        playerOne=Player(board.x+board.size+WIDTH_SQUARE,board.y,BLUE,"Player One",True)
        playerTwo=Player(board.x+board.size+WIDTH_SQUARE,board.y+board.size-WIDTH_SQUARE,RED,"Player Two")#playerTwo=Player(RED,True)
        players=[playerOne,playerTwo]
        saveButton=Button(WIDTH_WINDOW-120,board.y,100,80,"Save")
        menuButton=Button(WIDTH_WINDOW-120,board.y+(saveButton.rect.height*2),100,80,"Menu")
        

        if self.load:
            self.LoadGame(board,players)

        Run=True
        #Main loop that display the pygame window and the game(board,pawn,pieces)
        while Run:
            self.window.fill(GREY)
            board.DrawBorder(self.window)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                ###Handle mouse motion    
                elif event.type == pygame.MOUSEMOTION :
                    posMouse = pygame.mouse.get_pos()
                    if not board.showLastMovement:
                        for row in range(ROW):
                            for col in range(COL):
                                if board.piecesPos[col][row]!=0:
                                        board.piecesPos[col][row].MouvementPlayer(posMouse,board)

                ###Handle mouse clicks    
                elif event.type == pygame.MOUSEBUTTONDOWN :
                    posMouse = pygame.mouse.get_pos()
                    if saveButton.rect.collidepoint(posMouse):
                        if not board.showLastMovement: 
                            self.SaveGame(board,players)
                        else:
                            board.ShowLastMovement()
                            self.SaveGame(board,players)
                    elif menuButton.rect.collidepoint(posMouse):
                        Run= False
                    elif playerOne.rect.collidepoint(posMouse):
                        if len(board.allMovement)>0:
                            board.showLastMovement= not board.showLastMovement
                            board.ShowLastMovement()


                    ###Handle the player playing and the movement of the piece selected 
                    stopLoops = False
                    if not board.showLastMovement:    
                        for row in range(ROW):
                            for col in range(COL):
                                if board.piecesPos[col][row]!=0:
                                    if playerOne.playing  and board.piecesPos[col][row].color==playerOne.color:
                                        if board.piecesPos[col][row].rect.collidepoint(posMouse):
                                            board.piecesPos[col][row].Clicked(posMouse,players,board)
                                            stopLoops=True
                                            break
                                    elif playerTwo.playing   and board.piecesPos[col][row].color==playerTwo.color:
                                        if board.piecesPos[col][row].rect.collidepoint(posMouse):
                                            board.piecesPos[col][row].Clicked(posMouse,players,board)
                                            stopLoops=True
                                            break

                            if stopLoops:
                                break    
                                



            menuButton.DrawBackGround(self.window)
            menuButton.Draw(self.window)
            saveButton.DrawBackGround(self.window)
            saveButton.Draw(self.window)
            self.HandlePossibleMouvement(board)
            self.Draw(board,self.window,players)
            pygame.display.flip()
            #print (clock.get_fps())
            #function to control the frame rate or the maximum number of frames per second (FPS) 
            clock.tick(60)