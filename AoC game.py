import pygame
from pygame.locals import *
import os

global board
board = pygame.image.load(os.path.join("board3.png"))#imports board image
                                                                                
b_piece = pygame.image.load(os.path.join("Black Piece.png"))#imports piece image
b_king = pygame.image.load(os.path.join("Black King.png"))

w_piece = pygame.image.load(os.path.join("White Piece.png"))
w_king = pygame.image.load(os.path.join("White King.png"))

black_spot = pygame.image.load(os.path.join("Taken.png"))

global b
global w
global T

b = [ b_piece, b_king]
w = [w_piece, w_king]
T = [black_spot]

rect = (0,15,623,640)



def redraw_gameWindow():
    global win, B 
    
    win.blit(board,(0,0))

    
    B.add_Piece(win )

                   

    
    pygame.display.update()

def click(pos):
    
    """
    return: pos (x , y) in range 0-7 0-7 

    """ # show the position of the piece on board
    x = pos [0]
    y = pos [1]
    if rect[0] < x < rect[0] + rect[2]:
        if rect[1] < y < rect[1] + rect[3]:
            divX = x - rect[0] 
            divY = y -rect[0] 
            i = int(divX / (rect[2]/8)) #finds x coordinate
            j = int(divY / (rect[3]/8)) #finds y coordinate
            return i, j #returns coordinates to shell
    

def main():
    global B
    B = Board(8,8)
    clock = pygame.time.Clock()
    run = True
    while run:
            clock.tick(10)
             
            redraw_gameWindow()
                 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    quit()
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    B.update_moves()
                    i, j =click(pos)
                 #   B.board[j][i].selected = True
                    B.select(i,j)
                    B.update_moves()


class Piece: #class to help with placement of every piece
    image = -1
    rect = (0,15,623,640) #dimensions of board
    startX = rect[0]
    startY = rect[1]
    def __init__(self, row, col, colour):
        self.row = row 
        self.col = col
        self.colour= colour
        self.selected = False
    
        self.moves_list = [ ]
        self.taken_list = [ ]
 



    def isSelected(self): #a function that runs if a piece is selected
        return self.selected



    def update_valid_moves(self, board):
        self.moves_list = self.valid_moves(board) #updates moves on board

    def update_taken_spots(self, board):
        self.taken_list = self.valid_moves(board)


    def add_Piece(self): #adds pieces to board
        if self.colour == 'w': #adds white piece
            addPiece = w[self.image]

        else:
            addPiece = b[self.image] #adds black piece

        if self.selected:
            
            moves = self.moves_list
            taken = self.taken_list
            blank = T[self.image]

            for move in moves:
                x =  round(35+self.startX + (move[0] * self.rect[2]/8))
                y =  round(24+self.startY + (move[1] * self.rect[3]/8)) #dividing board into sections
                pygame.draw.circle(win, (255,0,0), (x,y), 10)

            for t in taken:
                x =  round(self.startX + (t[0] * self.rect[2]/8))
                y =  round(self.startY + (t[1] * self.rect[3]/8)) #dividing board into sections
                win.blit(blank,(x,y))
  
        x = round(self.startX + (self.col * self.rect[2]/8))
        y = round(self.startY + (self.row * self.rect[3]/8)) #dividing board into sections

        if self.selected:
            pygame.draw.rect(win, (255,0,0), (x-2, y-14,75,79), 2) #draws rect around piece
        
            
        win.blit(addPiece,(x,y)) #adds piece to board

        

    def change_pos(self, pos):
        self.row = pos[0]
        self.col = pos[1]

    def __str__(self):
        return str(self.col) + " " + str(self.row)



class normal(Piece): #class for normal pieces
    image = 0
    startX = rect[0]
    startY = rect[1]
    def __init__(self, row, col, colour):
        super().__init__(row, col, colour)
        #self.first = True  #setting first move to true
        self.king = False #cannot be king at start of game so set to false

    def valid_moves(self,board):
        i = self.row
        j = self.col

        moves = [ ]
        taken=[]

        

        if self.colour == "w":
            
            #UP RIGHT
            if i < 7 or i==7:
                if  j <7 :
                    p = B.board[ i-1 ][ j+1 ]
                    if p == 0 :
                        moves.append((j+1, i-1))

            if i < 7 or i == 7:
                if  j <6 :
                    q = B.board[ i-1 ][j+1]
                    if q != 0:
                        if board[ i-1 ][j+1]!=0 and board[ i-2 ][j+2] ==0:
                            if q.colour != self.colour:
                                moves.append((j+2, i-2 ))
                        

            #UP LEFT
            if i < 7 or i ==7:  
                if j > 0:
                    p = B.board[ i-1 ][j-1]
                    if p == 0 :
                        moves.append((j-1, i-1 ))


            if i < 7 or i ==7:
                if  j > 1 :
                    q = B.board[ i-1 ][j-1]
                    if q != 0:
                        if board[ i-1 ][j-1]!=0 and board[ i-2 ][j-2] ==0:
                            if q.colour != self.colour:
                                moves.append((j-2, i-2 ))

        if self.colour == "b":
            
            #DOWN RIGHT
            if i > 0 or i==0:
                if  j < 7 :
                    p = B.board[ i+1 ][ j+1 ]
                    if p == 0 :
                        moves.append((j+1, i+1))


            if i > 0 or i ==0:
                if  j < 6 :
                    q = B.board[ i+1 ][j+1]
                    if q != 0:
                        if board[ i+1 ][j+1]:
                            if q.colour != self.colour:
                                moves.append((j+2, i+2 ))

            #DOWN LEFT
            if i  > 0 or i ==0:  
                if j > 0:
                    p = B.board[ i+1 ][j-1]
                    if p == 0 :
                        moves.append((j-1, i+1 ))


            if i > 0 or i==0:
                if  j > 1 :
                    q = B.board[ i+1 ][j-1]
                    if q != 0:
                        if board[ i+1 ][j-1]:
                            if q.colour != self.colour:
                                moves.append((j-2, i+2 )) #piece jumps
                                taken.append((j-1, i+1)) #adds this pos to list of taken positions

                                
                           
    
        return moves
        return taken
            
class King(Piece): #class for king
    image = 1

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self.board = [[0 for x in range (8) ] for _ in range(rows)] #index for rows and columns

        #black pieces
        self.board[0][1] = normal(0 , 1 , "b") #places pieces on specific spot
        self.board[0][3] = normal(0 , 3 , "b")
        self.board[0][5] = normal(0 , 5 , "b")
        self.board[0][7] = normal(0 , 7 , "b")
        self.board[1][0] = normal(1 , 0 , "b")
        self.board[1][2] = normal(1 , 2 , "b")
        self.board[1][4] = normal(1 , 4 , "b")
        self.board[1][6] = normal(1 , 6 , "b")
        self.board[2][1] = normal(2 , 1 , "b")
        self.board[2][3] = normal(2 , 3 , "b")
        self.board[2][5] = normal(2 , 5 , "b")
        self.board[2][7] = normal(2 , 7 , "b")

        #white pieces
        self.board[7][0] = normal(7 , 0 , "w") #places pieces on specific spot
        self.board[7][2] = normal(7 , 2 , "w")
        self.board[7][4] = normal(7 , 4 , "w")
        self.board[7][6] = normal(7 , 6 , "w")
        self.board[6][1] = normal(6 , 1 , "w")
        self.board[6][3] = normal(6 , 3 , "w")
        self.board[6][5] = normal(6 , 5 , "w")
        self.board[6][7] = normal(6 , 7 , "w")
        self.board[5][0] = normal(5 , 0 , "w")
        self.board[5][2] = normal(5 , 2 , "w")
        self.board[5][4] = normal(5 , 4 , "w")
        self.board[5][6] = normal(5 , 6 , "w")

    def update_moves(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0: #continues to update pieces 
                    self.board[i][j].update_valid_moves(self.board) #updates moves list

    def update_taken(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] != 0: #continues to update pieces 
                    self.board[i][j].update_taken_spots(self.board) #updates moves list
                      

    def add_Piece(self,win):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j]  != 0: #when the column or row isn't 0 piece is added
                    self.board[i][j].add_Piece()

    def taken(self,win):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j]  != 0: #when the column or row isn't 0 piece is added
                    self.board[i][j].add_Piece()
                
    def select(self, col, row):
        last = (-1,-1) #position of previous move before first move has been made
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j]  != 0:
                    if self.board[i][j].selected:
                        last = (i,j) # new position chosen becomes latest position

        # if piece chosen
        if self.board[row][col] == 0 :
            moves = self.board[last[0]][last[1]].moves_list #adds latest move to moves list
            if (col, row) in moves:
                self.move(last, (row, col)) #moves piece
                self.reset_selected()

        else:           
                    self.reset_selected() 
                    self.board[row][col].selected = True #if there is a no possible moves just higlights
                                                                                                #piece

    
    def reset_selected(self): #sets selected piece to false

        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j]  != 0: 
                    if self.board[i][j]:
                        self.board[i][j].selected = False

##    def reset_taken(self): #sets selected piece to false
##
##        for i in range(self.rows):
##            for j in range(self.cols):
##                if self.board[i][j]  != 0: 
##                    if self.board[i][j]:
##                        self.board[i][j].taken = False




    def move(self, start, end):

        nBoard = self.board[:] #copies board
        nBoard[start[0]][start[1]].change_pos((end[0], end[1])) #original pos becomes end pos    
        nBoard[end[0]][end[1]] = nBoard[start[0]][start[1]] #new pos becomes starting pos

        nBoard[start[0]][start[1]] = 0

        self.board = nBoard # re draws boards board with changes





width = 900
height = 640
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ace Of Checkers")
main()





            
