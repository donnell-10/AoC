import pygame
from pygame.locals import *
import os
from random import *
from sys import exit

#################### COLOURS ##########################
black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
pink=(255,51,204)
green=(0,102,0)
lightGreen=(0,255,0)
purple=(153,51,255)
blue=(0,102,255)
lightBlue=(51,204,255)
yellow=(255,204,0)
brown=(153,51,0)
grey=(179,179,179)
greenBlue=(0,102,102)
greyBackground =(225, 225, 225)
########################################################
normalBlue,normalBlack, kingBlue, kingBlack =1,2,3,4
width = 65 #width and height of each square on board
height = 65
radius = 30 # radius of each piece
margin = 0 #margin between each square on board
D_from_edge = 220
moveCounter = 0
clickCounter=0
turn = 'blue'
playerOneColour = 'blue'
playerTwoColour = 'black'
vs_cpu = False
# stores coordinates, when -1 board is not affected
startX = -1
startY = -1
endX = -1
endY = -1

pygame.init()
gameBoard = []
windowSize = [960,640]
win = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Ace Of Checkers")
win.fill(greyBackground)

done = False

clock = pygame.time.Clock();

def square_colour(row,col): #find colour of each square
    return black if (row + col)%2 ==0 else white 

def newGameBoard():
    global gameBoard, newGame
    gameBoard[:] = [[None]*8 for i in range(8)]  # Empty the game board.

    for x in range(8):
        for y in range(8):
            if square_colour(x, y) == white:
                if y in range(3):
                    gameBoard[x][y]=normalBlue
                if y in range(5,8):
                    gameBoard[x][y]=normalBlack

    newGame=False

def board_GUI(black,white): #draws the board onto the window
    for boardRow in range(8):
        for boardColumn in range(8):
            xCoord = ((margin + width)* boardColumn + margin)+D_from_edge
            yCoord=(margin+height) * boardRow + margin
            currentColour = square_colour(boardRow, boardColumn)
            pygame.draw.rect(win,currentColour,[xCoord,yCoord, width, height])



def calculatePieceTotal():
    bluePieceTotal=0
    blackPieceTotal=0
    for x in range(8):
        for y in range(8):
            if gameBoard[x][y]==normalBlack:
                blackPieceTotal=blackPieceTotal+1 #if there is a black piece in pos, add 1 to to total
            elif gameBoard[x][y]==kingBlack:
                blackPieceTotal=blackPieceTotal+1 #if there is a black king is pos, add 1 to total
            elif gameBoard[x][y]==normalBlue:
                bluePieceTotal=bluePieceTotal+1 #if there is a blue piece in pos, add 1 to total 
            elif gameBoard[x][y]==kingBlue:
                bluePieceTotal=bluePieceTotal+1 #if there is a blue king in pos, add 1 to total
    return bluePieceTotal,blackPieceTotal


def drawPieces():
    global redPieceTotal,blackPieceTotal
    font=pygame.font.SysFont("comicsansms", 30) 
    kingLbl=font.render('K', True, (255,255,255)) #write the letter K on King Pieces
    for x in range(8):
        for y in range(8):
            xCoord=((margin+width) * x + margin+32)+D_from_edge
            yCoord=(margin+height) * y + margin+33
            if gameBoard[x][y]==normalBlack:
                pygame.draw.circle(win,black,(xCoord,yCoord),radius)#draws black piece
            if gameBoard[x][y]==kingBlack:
                pygame.draw.circle(win,black,(xCoord,yCoord),radius)#draws black king 
                win.blit(kingLbl,(xCoord-10,yCoord-20))#adds K label
            if gameBoard[x][y]==normalBlue:
                pygame.draw.circle(win,blue,(xCoord,yCoord),radius)#draws blue piece
            if gameBoard[x][y]==kingBlue:
                pygame.draw.circle(win,blue,(xCoord,yCoord),radius)#draws blue king
                win.blit(kingLbl,(xCoord-10,yCoord-20))#adds k label
            if gameBoard[x][y]==None and square_colour(x,y)==white:
                pygame.draw.circle(win,white,(xCoord,yCoord),radius)#white circles in empty spots
    # will update board every time a move is played
    pygame.display.update()

############################### POSSIBLE MOVES #########################################    
def southWestMove(startX,startY):
    return startX-1,startY+1
def southEastMove(startX,startY):
    return startX+1,startY+1
def northWestMove(startX,startY):
    return startX-1,startY-1
def northEastMove(startX,startY):
    return startX+1,startY-1
def southWestJump(startX,startY):
    middleX,middleY=southWestMove(startX,startY)#middle x & y are the spot of the piece being jumped over
    return middleX-1,middleY+1  #returns position of moving piece
def southEastJump(startX,startY):
    middleX,middleY=southEastMove(startX,startY)
    return middleX+1,middleY+1 
def northWestJump(startX,startY):
    middleX,middleY=northWestMove(startX,startY)
    return middleX-1,middleY-1
def northEastJump(startX,startY):
    middleX,middleY=northEastMove(startX,startY)
    return middleX+1,middleY-1

def makeBlueMove(startX,startY,endX,endY):

    gameBoard[startX][startY]=None
    if endY==7:
        gameBoard[endX][endY]=kingBlue #if at the opposite end of board turn into king
    else:
        gameBoard[endX][endY]=normalBlue #stays normal blue anywhere else on board

    endTurn()

###this will make a jump for the blue piece in the gameBoard
def makeBlueJump(startX,startY,endX,endY,takeX,takeY):
    gameBoard[startX][startY]=None 
    gameBoard[takeX][takeY]=None #checks if anything in pos piece will jump to
    if endY==7:
        gameBoard[endX][endY]=kingBlue
    else:
        gameBoard[endX][endY]=normalBlue

    endTurn()
#this will make a move for the blue king in the game Board
def makeKingBlueMove(startX,startY,endX,endY):
    gameBoard[startX][startY]=None
    gameBoard[endX][endY]=kingBlue
    endTurn()
    
#this willl make a jump for the blue king in the gameboard
def makeKingBlueJump(startX,startY,endX,endY,takeX,takeY):
    gameBoard[startX][startY]=None
    gameBoard[takeX][takeY]=None
    gameBoard[endX][endY]=kingBlue
    endTurn()
    
# this will make a move for black king in the gameboard
def makeKingBlackMove(startX,startY,endX,endY):
    gameBoard[startX][startY]=None
    gameBoard[endX][endY]=kingBlack
    endTurn()
    
#this will make a jump for the king black in the gameboard
def makeKingBlackJump(startX,startY,endX,endY,takeX,takeY):
    gameBoard[startX][startY]=None
    gameBoard[takeX][takeY]=None
    gameBoard[endX][endY]=kingBlack
    endTurn()

#this will make a move for the black piece in the game board
def makeBlackMove(startX,startY,endX,endY):
    gameBoard[startX][startY]=None
    if endY==0:
        gameBoard[endX][endY]=kingBlack
    else:
        gameBoard[endX][endY]=normalBlack

    endTurn()

#this will make a jump for the black piece in the gameBoard
def makeBlackJump(startX,startY,endX,endY,takeX,takeY):
    gameBoard[startX][startY]=None
    gameBoard[takeX][takeY]=None
    if endY==0:
        gameBoard[endX][endY]=kingBlack
    else:
        gameBoard[endX][endY]=normalBlack

    endTurn()




def checkLegalMove(endX,endY,startX,startY):
    global gameBoard
    checkX,checkY=southWestMove(startX,startY) 
    checkX1,checkY1=southEastMove(startX,startY)
    jumpX,jumpY=southWestJump(startX,startY)
    jumpX1,jumpY1=southEastJump(startX,startY)
    checkX2,checkY2=northWestMove(startX,startY)
    checkX3,checkY3=northEastMove(startX,startY)
    jumpX2,jumpY2=northWestJump(startX,startY)
    jumpX3,jumpY3=northEastJump(startX,startY)
    if turn=="blue":
        if gameBoard[startX][startY]==normalBlue: #checks if piece in this pos is a normal blue
            if endX==checkX and endY==checkY: #checks if there is a piece in the pos that the piece will move to
                if gameBoard[endX][endY]==None: #if there isn't then the piece will move
                    makeBlueMove(startX,startY,endX,endY)

            elif endX==checkX1 and endY==checkY1:
                if gameBoard[endX][endY]==None:
                    makeBlueMove(startX,startY,endX,endY)

            elif (gameBoard[checkX][checkY]==normalBlack):
                if endX==jumpX and endY==jumpY:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX,checkY
                        makeBlueJump(startX,startY,endX,endY,takeX,takeY)

            elif (gameBoard[checkX1][checkY1]==normalBlack):
                if endX==jumpX1 and endY==jumpY1:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX1,checkY1
                        makeBlueJump(startX,startY,endX,endY,takeX,takeY)

        elif gameBoard[startX][startY]==kingBlue:
            if endX==checkX2 and endY==checkY2:
                if gameBoard[endX][endY]==None:
                    makeKingBlueMove(startX,startY,endX,endY)

            elif endX==checkX3 and endY==checkY3:
                if gameBoard[endX][endY]==None:
                    makeKingBlueMove(startX,startY,endX,endY)

            elif (gameBoard[checkX2][checkY2]==normalBlack):
                if endX==jumpX and endY==jumpY:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX2,checkY2
                        makeKingBlueJump(startX,startY,endX,endY,takeX,takeY)
            elif (gameBoard[checkX2][checkY2]==kingBlack):
                if endX==jumpX2 and endY==jumpY2:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX2,checkY2
                        makeKingBlueJump(startX,startY,endX,endY,takeX,takeY)

            elif (gameBoard[checkX3][checkY3]==normalBlack):
                if endX==jumpX3 and endY==jumpY3:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX3,checkY3
                        makeKingBlueJump(startX,startY,endX,endY,takeX,takeY)
            elif (gameBoard[checkX3][checkY3]==kingBlack):
                if endX==jumpX3 and endY==jumpY3:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX3,checkY3
                        makeKingBlueJump(startX,startY,endX,endY,takeX,takeY)
            elif endX==checkX and endY==checkY:
                if gameBoard[endX][endY]==None:
                    makeKingBlueMove(startX,startY,endX,endY)

            elif endX==checkX1 and endY==checkY1:
                if gameBoard[endX][endY]==None:
                    makeKingBlueMove(startX,startY,endX,endY)

            elif (gameBoard[checkX][checkY]==normalBlack):
                if endX==jumpX and endY==jumpY:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX,checkY
                        makeKingBlueJump(startX,startY,endX,endY,takeX,takeY)

            elif (gameBoard[checkX][checkY]==kingBlack):
                if endX==jumpX and endY==jumpY:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX,checkY
                        makeKingBlueJump(startX,startY,endX,endY,takeX,takeY)

            elif (gameBoard[checkX1][checkY1]==normalBlack):
                if endX==jumpX1 and endY==jumpY1:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX1,checkY1
                        makeKingBlueJump(startX,startY,endX,endY,takeX,takeY)
            elif (gameBoard[checkX1][checkY1]==normalBlack):
                if endX==jumpX1 and endY==jumpY1:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX1,checkY1
                        makeKingBlueJump(startX,startY,endX,endY,takeX,takeY)


    else:
        if gameBoard[startX][startY]==normalBlack:
            if endX==checkX2 and endY==checkY2:
                if gameBoard[endX][endY]==None:
                    makeBlackMove(startX,startY,endX,endY)

            elif endX==checkX3 and endY==checkY3:
                if gameBoard[endX][endY]==None:
                    makeBlackMove(startX,startY,endX,endY)

            elif (gameBoard[checkX2][checkY2]==normalBlue):
                if endX==jumpX2 and endY==jumpY2:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX2,checkY2
                        makeBlackJump(startX,startY,endX,endY,takeX,takeY)

            elif (gameBoard[checkX3][checkY3]==normalBlue):
                if endX==jumpX3 and endY==jumpY3:
                    if gameBoard[endX][endY]==None:
                        takeX,takeY=checkX3,checkY3
                        makeBlackJump(startX,startY,endX,endY,takeX,takeY)

        elif gameBoard[startX][startY]==kingBlack:
                        if endX==checkX and endY==checkY:
                            if gameBoard[endX][endY]==None:
                                makeKingBlackMove(startX,startY,endX,endY)

                        elif endX==checkX1 and endY==checkY1:
                            if gameBoard[endX][endY]==None:
                                makeKingBlackMove(startX,startY,endX,endY)

                        elif (gameBoard[checkX][checkY]==normalBlue):
                            if endX==jumpX and endY==jumpY:
                                if gameBoard[endX][endY]==None:
                                    takeX,takeY=checkX,checkY
                                    makeKingBlackJump(startX,startY,endX,endY,takeX,takeY)

                        elif (gameBoard[checkX][checkY]==kingBlue):
                            if endX==jumpX and endY==jumpY:
                                if gameBoard[endX][endY]==None:
                                    takeX,takeY=checkX,checkY
                                    makeKingBlackJump(startX,startY,endX,endY,takeX,takeY)

                        elif (gameBoard[checkX1][checkY1]==normalBlue):
                            if endX==jumpX1 and endY==jumpY1:
                                if gameBoard[endX][endY]==None:
                                    takeX,takeY=checkX1,checkY1
                                    makeKingBlackJump(startX,startY,endX,endY,takeX,takeY)

                        elif (gameBoard[checkX1][checkY1]==kingBlue):
                            if endX==jumpX1 and endY==jumpY1:
                                if gameBoard[endX][endY]==None:
                                    takeX,takeY=checkX1,checkY1
                                    makeKingBlackJump(startX,startY,endX,endY,takeX,takeY)

                        elif endX==checkX2 and endY==checkY2:
                            if gameBoard[endX][endY]==None:
                                makeKingBlackMove(startX,startY,endX,endY)

                        elif endX==checkX3 and endY==checkY3:
                            if gameBoard[endX][endY]==None:
                                makeKingBlackMove(startX,startY,endX,endY)

                        elif (gameBoard[checkX2][checkY2]==normalBlue):
                            if endX==jumpX2 and endY==jumpY2:
                                if gameBoard[endX][endY]==None:
                                    takeX,takeY=checkX2,checkY2
                                    makeKingBlackJump(startX,startY,endX,endY,takeX,takeY)

                        elif (gameBoard[checkX2][checkY2]==kingBlue):
                            if endX==jumpX2 and endY==jumpY2:
                                if gameBoard[endX][endY]==None:
                                    takeX,takeY=checkX2,checkY2
                                    makeKingBlackJump(startX,startY,endX,endY,takeX,takeY)


                        elif (gameBoard[checkX3][checkY3]==normalBlue):
                            if endX==jumpX3 and endY==jumpY3:
                                if gameBoard[endX][endY]==None:
                                    takeX,takeY=checkX3,checkY3
                                    makeKingBlackJump(startX,startY,endX,endY,takeX,takeY)

                        elif (gameBoard[checkX3][checkY3]==kingBlue):
                            if endX==jumpX3 and endY==jumpY3:
                                if gameBoard[endX][endY]==None:
                                    takeX,takeY=checkX3,checkY3
                                    makeKingBlackJump(startX,startY,endX,endY,takeX,takeY)

    print(gameBoard)


#this will wbe used to either switch turns or find out if someone has won the game
def endTurn():
    global turn
    if turn=="blue":
        if checkEndGame(turn)==True: #will check if opponent has lost all pieces
            font=pygame.font.SysFont("comicsansms", 20)
            if playerOneColour==turn:
                winnerLbl=font.render("BLUE wins the game", True, (0,102,255))#prints if blue wins
                
            else:
                winnerLbl=font.render("BLACK wins the game", True, (0,0,0))#prints if black wins

            win.blit(winnerLbl,(430,600))
        else:
            turn="black" #alternates the turn

    else:
        if checkEndGame(turn)==True: #will check if opponent has lost all pieces
                    font=pygame.font.SysFont("calibri", 20)
                    if playerOneColour==turn:
                        winnerLbl=font.render("BLUE wins the game", True, (0,102,255))
                    else:
                        winnerLbl=font.render("BLACK wins the game", True, (0,0,0))

                    win.blit(winnerLbl,(410,600))
        else:
            turn="blue" #alternates the turn


def checkEndGame(turn): #counts amount of pieces and if 0 the player who's turn it is wins
    blueTotal,blackTotal=calculatePieceTotal()
    if turn=="blue":
        if blackTotal==0:
            return True #if there are no black pieces left the function will be true
        else:
            return False #if there are still black pieces the function will be false

    else:
        if blueTotal==0: 
            return True #if there are no blue pieces left the function will be true
        else:
            return False #if there are still blue pieces the function will be false

#this is to check that the user has clicked on the right piece
def checkCorrectPlayerPiece(startX,startY):
    global clickCounter
    font=pygame.font.SysFont("comic+sansms", 15)
    if turn=="blue":#if its blue turn they can only use normal blue or king blue
        if gameBoard[startX][startY]!=normalBlue:
            if gameBoard[startX][startY]!=kingBlue:
                clickCounter=0
                moveStatusLbl=font.render("It's Blue's turn. ", True, (0,102,255))
                #if player clicks the wrong piece 'its blue's turn' will appear
                win.blit(moveStatusLbl,(50,115))

                print("wrong piece")
            else:

                print("correct piece")

        else:

            moveStatusLbl=font.render("Make your move", True, (0,102,255))
            win.blit(moveStatusLbl,(50,100))
            print("correct piece")
            pygame.draw.rect(win,(225,225,225),(800,100,879,73),67)
            #covers the 'its blue's turn'  and 'make your move' sentences
            
            
    elif turn=="black":#if its blacks turn they can only use normal black or king black
        if gameBoard[startX][startY]!=normalBlack:
            if gameBoard[startX][startY]!=kingBlack:
                clickCounter=0

                moveStatusLbl=font.render("It's Black's turn.", True, (0,0,0))
                win.blit(moveStatusLbl,(800,115))

                print("not working")
            else:
                print("correct piece")

        else:
            moveStatusLbl=font.render("Make your move", True, (0,0,0))
            win.blit(moveStatusLbl,(800,100))

            print("correct piece")
            pygame.draw.rect(win,(225,225,225),(50,100,79,73),62)
    print(startX,startY)


def drawGameStatusBox(black):
    pygame.draw.rect(win, black, [0,520,960,10])
    font=pygame.font.SysFont("calibri", 20)
    playerOne=font.render("Player one:", True, (0,0,0))
    playerTwo=font.render("Player two:", True, (0,0,0))
    win.blit(playerOne,(120,580))#putting the labels onto the gui
    win.blit(playerTwo,(700,580))
    if playerOneColour=="blue":
        pygame.draw.circle(win,blue,(260,590),radius) #draws circles blue/black showing
        pygame.draw.circle(win,black,(840,590),radius)#what colour each player is
    else:
        pygame.draw.circle(win,black,(840,590),radius)
        pygame.draw.circle(win,blue,(260,590),radius)


def ai(startX,startY):
    #this function will tell the computer what moves are allowed
    if turn=="blue":
            if gameBoard[startX][startY]==normalBlue: #checks if there is a blue piece in this pos
                endX,endY=southWestMove(startX,startY) #gives cpu option of these moves
                endX1,endY1=southEastMove(startX,startY)
                jumpX,jumpY=southWestJump(startX,startY)
                jumpX1,jumpY1=southEastJump(startX,startY)
                if gameBoard[endX][endY]==None:
                        makeBlueMove(startX,startY,endX,endY) #will move piece south west

                if gameBoard[endX1][endY1]==None:
                        makeBlueMove(startX,startY,endX,endY) #will move piece south east

                elif (gameBoard[checkX][checkY]==normalBlack): #will check if there is a black piece
                    if endX==jumpX and endY==jumpY:                         # to jump over
                        if gameBoard[endX][endY]==None:
                            takeX,takeY=checkX,checkY
                            makeBlueJump(startX,startY,endX,endY,takeX,takeY) #will make piece jump SW

                elif (gameBoard[checkX1][checkY1]==normalBlack):
                    if endX==jumpX1 and endY==jumpY1:
                        if gameBoard[endX][endY]==None:
                            takeX,takeY=checkX1,checkY1
                            makeBlueJump(startX,startY,endX,endY,takeX,takeY) #will make piece jump SE

    else:
            if gameBoard[startX][startY]==normalBlack:
                endX,endY=northWestMove(startX,startY)
                endX1,endY1=northEastMove(startX,startY)
                jumpX,jumpY=northWestJump(startX,startY)
                jumpX1,jumpY1=northEastJump(startX,startY)
                if (gameBoard[endX][endY]==normalBlue):
                        if gameBoard[jumpX][jumpY]==None:
                            takeX,takeY=endX,endY
                            makeBlackJump(startX,startY,jumpX,jumpY,takeX,takeY)

                elif (gameBoard[endX1][endY1]==normalBlue):
                        if gameBoard[jumpX1][jumpY1]==None:
                            takeX,takeY=endX1,endY1
                            makeBlackJump(startX,startY,jumpX1,jumpY1,takeX,takeY)

                elif gameBoard[endX][endY]==None:
                        makeBlackMove(startX,startY,endX,endY)

                elif gameBoard[endX1][endY1]==None:
                        makeBlackMove(startX,startY,endX1,endY1)

def computerTurn(): #will tell the computer that it is now their turn
    ai(startX,startY)
    

def findComputerPieces(): #will find where the computer's pieces are and move one
    global playerOneColour
    for x in range(8):
        for y in range(8):
            if square_colour(x,y)==white:
                if playerTwoColour=="black":
                    if (gameBoard[x][y]==normalBlack) or (gameBoard[x][y]==kingBlack): #finds black king or pawn
                        startX=x
                        startY=y
                        print(startX,startY)
                        ai(startX,startY) #will look for possible moves
                else:
                    if (gameBoard[x][y]==normalBlue) or (gameBoard[x][y]==kingBlue): #finds blue king or pawn
                        startX=x
                        startY=y
                        ai(startX,startY) #will look for possible moves

def checkTwoPiecesIntoKing():
    for x in range(8):
        for y in range(8):
            startX,startY=findComputerPieces()
            return x,y

board_GUI(black,white)
newGameBoard()
clock.tick(60)
pygame.display.flip()
drawGameStatusBox(black)

vs_cpu= True

while not done:
    if vs_cpu==True and turn==playerTwoColour:
                findComputerPieces()
                
    for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                    done = True
                    #quit()
                    pygame.display.quit()
                    pygame.quit()

                 elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    column = (pos[0]-D_from_edge) // (width+margin)
                    row = pos[1] // (height + margin)
                    clickCounter = clickCounter+1
                    
                    

                    if clickCounter==1:
                            startX=column
                            startY=row
                            checkCorrectPlayerPiece(startX,startY)
                    if clickCounter==2:
                            endX=column
                            endY=row
                            checkLegalMove(endX,endY,startX,startY)
                            clickCounter=0

                    



    drawPieces()









