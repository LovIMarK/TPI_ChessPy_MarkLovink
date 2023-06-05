###ETML
###Auteur : Mark Lovink
###Date : 15.05.2023

#Import of library and files
import pygame
import json
from Var import *
from ChessBoard.Board import Board
from Player import Player
from Button import Button
import time



#####
### Class Game handles the game display, player interaction, and saved game handling
### window represents dimensions of the PyGame window
### load variable determines whether the saved game should be displayed or not
### font variable determines the character font, and size of the text
### gameOn variable that determines if a game has been won 
#####
class Game:
    def __init__(self,window,load=False):
        self.window=window
        self.load=load
        self.font = pygame.font.Font(None, 36)
        self.gameOn=True
        

        


    ##### Summary
    ### Function that saves the id, all the movement played, column, row of each pieces on the chess board and the player playing in a JSON file
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
                        'player':player,
                        'AllMovement':board.allMovement
                    }
                    piecesData.append(pieceData)

        filePath = 'pieces.json'

        # Open a JSON file with "w" to write the list of all piece information into it
        with open(filePath, 'w') as file:
            json.dump(piecesData, file)




    ##### Summary
    ### Function get the id, all the movement played, column, row of each pieces and the player playing in the JSON file and display it in the current game
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
            AllMovement= pieceData['AllMovement']
            pieces.append((id,col,row,player,AllMovement))

        #Get all movement of the JSON file
        board.allMovement=AllMovement

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
    ### Function that get all the squares, the pieces, the player, buttons and display it in the pygame window 
    ##### Summary
    def Draw(self,board,window,players,showAllMovement,buttons):   
        
        ###Draw board
        for row in range(ROW):
            for col in range(COL):
                board.squares[col][row].Draw(window)
                if col==0:
                    board.squares[col][row].DrawNumber(window,ROW-row)
                if row ==ROW-1:
                    board.squares[col][row].DrawAlphabet(window,col)
            

        ###Draw pieces
        for row in range(ROW):
            for col in range(COL):
                if board.piecesPos[col][row]!=0 and not board.piecesPos[col][row].clicked :
                    window.blit(board.piecesPos[col][row].image,(board.piecesPos[col][row].col*WIDTH_SQUARE+board.x,board.piecesPos[col][row].row*WIDTH_SQUARE+board.y))
                elif board.piecesPos[col][row]!=0 and board.piecesPos[col][row].clicked:
                    window.blit(board.piecesPos[col][row].image,board.piecesPos[col][row].rect)


       
        ###Draw last movement 
        if board.showLastMovement:
            window.blit(board.piecesPos[board.allMovement[len(board.allMovement)-1][0]][board.allMovement[len(board.allMovement)-1][1]].image,(board.piecesPos[board.allMovement[len(board.allMovement)-1][0]][board.allMovement[len(board.allMovement)-1][1]].rect))
            pygame.draw.rect(window, GOLD, board.piecesPos[board.allMovement[len(board.allMovement)-1][0]][board.allMovement[len(board.allMovement)-1][1]].rect,5 )
            pygame.draw.rect(window, GOLD, (board.allMovement[len(board.allMovement)-1][2]*WIDTH_SQUARE+board.x,board.allMovement[len(board.allMovement)-1][3]*WIDTH_SQUARE+board.y,WIDTH_SQUARE,WIDTH_SQUARE),5 )
            
        ###Draw possible movements                
        for row in range(ROW):
            for col in range(COL):
                if board.piecesPos[col][row]!=0 and board.piecesPos[col][row].clicked:
                    for row2 in range(ROW):
                        for col2 in range(COL):
                            if board.piecesPos[col][row].possibleMoves[col2][row2]!=0:
                                pygame.draw.circle(window, GOLD, (col2*WIDTH_SQUARE+board.x+(WIDTH_SQUARE/2),row2*WIDTH_SQUARE+board.y+(WIDTH_SQUARE/2)), 15 )


        ###Draw dead pieces
        ###ChatGPT how to sort a list by name
        sortedList = sorted(board.piecesDie, key=lambda obj: ( obj.color,obj.name))
        ###
        index=0
        reset_index = False
        for obj in sortedList:
            
            if obj.color==players[0].color:
                index+=1
                window.blit(obj.image,(board.size+board.x+(index*30),players[0].rect.y+WIDTH_SQUARE))
            else:
                if not reset_index:
                    index=0
                    reset_index=True
                index+=1

                window.blit(obj.image,(board.size+board.x+(index*30),players[1].rect.y-WIDTH_SQUARE-5))
        


        ###Draw players
        for obj in players:
            obj.Draw(window)
            obj.DrawTimer(window)
            if obj.winning:
                obj.DrawWinner(window,board)
            if obj.draw:
                obj.DrawDraw(window,board)

        ###Draw Buttons
        for obj in buttons:
            
            obj.DrawBackGround(self.window)
            obj.font = pygame.font.Font(None, 26)
            obj.Draw(self.window)
            

        ### draw all movement         
        for obj in showAllMovement:
            window.blit(obj,(buttons[len(buttons)-1].rect.x+5,buttons[len(buttons)-1].rect.y+((obj.get_height()*2)*showAllMovement.index(obj))+5)) 


    ##### Summary
    ### Function that check all the possible/legal moves of all pieces 
    ##### Summary
    def HandlePossibleMouvement(self,board): 
        for row in range(ROW):
            for col in range(COL):
                if board.piecesPos[col][row]!=0 :
                    board.piecesPos[col][row].Mouvement(board)
        

    ##### Summary
    ### Function that get the 5 last piece movement and save it in a text list
    ##### Summary
    ### Return the list with the 5 last piece movement
    def ShowAllMovement(self,board):
        showAllMovement=[]
        end = len(board.allMovement) - 1
        start = len(board.allMovement) - 5
        indexMove=1                     
        for i in range(end, max(start-1, -1), -1):
            if i%2==0:
                color=RED  
                texte = self.font.render("{0} : {1}{2}".format(indexMove, chr(board.allMovement[i][2] + 97), board.allMovement[i][3]), True, color)
                showAllMovement.append(texte)
                indexMove+=1
            else:
                color=BLUE   
                texte = self.font.render("{0} : {0}{1}".format(indexMove,chr(board.allMovement[i][2] + 97), board.allMovement[i][3]), True, color)
                showAllMovement.append(texte)
                

        return showAllMovement

        
    ##### Summary
    ### Function that checks if the king is in checkmate by verifying if the player has available moves for their pieces or not
    ##### Summary
    ### Return the value if checkmate and the winner
    def CheckCheckMate(self,board,players):
        kingCol=0
        kingRow=0    
        if players[0].playing:
            player=players[0]
        if players[1].playing:
            player=players[1]
        for row in range(ROW):
            for col in range(COL):
                if board.piecesPos[col][row]!=0  and board.piecesPos[col][row].color==player.color:
                    for row2 in range(ROW):
                        for col2 in range(COL):
                            if board.piecesPos[col][row].possibleMoves[col2][row2]!=0:
                                return False 
                    if board.piecesPos[col][row].name=="king":
                        kingCol=col
                        kingRow=row
        
        if board.piecesPos[kingCol][kingRow].check:
            if players[0].playing:
                players[1].winning=True
            if players[1].playing:
                players[0].winning=True
        else:
            for obj in players:
                obj.draw=True
        return True

    ##### Summary
    ### Function that change the time of each player
    ##### Summary
    ### Return the value if checkmate and the winner
    def HandleTime(self,players):
        if self.gameOn:
            for obj in players:
                if obj.playing :
                    obj.actualTime = time.time() - obj.timer -obj.PausedDuration
                    
                if not obj.playing:
                    if obj.pausedTime:
                        obj.PausedDuration = time.time() - obj.pausedTime
             



            
                
            
            


    ##### Summary
    ### Main function handle the display of the game and manage the interaction with the players
    ##### Summary
    def StartGame(self):
        

        ###Variable implementation
        clock = pygame.time.Clock()
        board=Board(20,20)
        playerOne=Player(board.x+board.size+WIDTH_SQUARE,board.y,BLUE,"Player Two")
        playerOne.pausedTime= time.time()
        playerTwo=Player(board.x+board.size+WIDTH_SQUARE,board.y+board.size-WIDTH_SQUARE,RED,"Player One",True,False)#playerTwo=Player(RED,True)
        players=[playerOne,playerTwo]

        buttons=[]
        menuButton=Button(WIDTH_WINDOW-120,board.y,100,WIDTH_SQUARE,"Menu")
        saveButton=Button(WIDTH_WINDOW-120-menuButton.rect.width,board.y,100,WIDTH_SQUARE,"Save")
        showLastMovementButton=Button(board.x+board.size+WIDTH_SQUARE,board.y+(WIDTH_SQUARE*2),200,WIDTH_SQUARE+5,"LastMove")
        showMovementButton=Button(board.x+board.size+WIDTH_SQUARE,board.y+(WIDTH_SQUARE*3),200,(3*WIDTH_SQUARE))
        buttons.append(menuButton)
        buttons.append(saveButton)
        buttons.append(showLastMovementButton)
        buttons.append(showMovementButton)
        
        

        
        
        

        ###Load last game
        if self.load:
            self.LoadGame(board,players)
        self.gameOn=True
        run=True
        #Main loop that display the pygame window and the game(board,pawn,pieces)
        while run:
            self.window.fill(GREY)
            board.DrawBorder(self.window)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                ###Handle mouse motion    
                elif event.type == pygame.MOUSEMOTION :
                    posMouse = pygame.mouse.get_pos()
                    if not board.showLastMovement and self.gameOn:
                        for row in range(ROW):
                            for col in range(COL):
                                if board.piecesPos[col][row]!=0:
                                        board.piecesPos[col][row].MouvementPlayer(posMouse,board)
                    for obj in buttons:
                        obj.OnButton(posMouse)

                ###Handle mouse clicks    
                elif event.type == pygame.MOUSEBUTTONDOWN :
                    posMouse = pygame.mouse.get_pos()
                    #self.HandlePossibleMouvement(board)
                    if saveButton.rect.collidepoint(posMouse) and  self.gameOn:
                        saveButton.Clicked()
                        if not board.showLastMovement: 
                            self.SaveGame(board,players)
                    elif menuButton.rect.collidepoint(posMouse):
                        for obj in players:
                            if obj.winning:
                                obj.winning=False
                        
                        run= False
                        menuButton.Clicked()
                    elif showLastMovementButton.rect.collidepoint(posMouse) :
                        showLastMovementButton.Clicked()
                        if len(board.allMovement)>0:
                            board.showLastMovement= not board.showLastMovement
                            board.ShowLastMovement()


                    ###Handle the player playing and the movement of the piece selected 
                    stopLoops = False
                    if not board.showLastMovement and self.gameOn and run:    
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
            

                        
            showAllMovement=self.ShowAllMovement(board)                    
            
            self.Draw(board,self.window,players,showAllMovement,buttons)
            self.HandlePossibleMouvement(board)
            if self.CheckCheckMate(board,players):
                self.gameOn=False
            self.HandleTime(players)
            pygame.display.flip()
            #print (clock.get_fps())
            #function to control the frame rate or the maximum number of frames per second (FPS) 
            clock.tick(60)