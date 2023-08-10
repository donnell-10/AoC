import pygame
import os


b_piece = pygame.image.load(os.path.join("image","Black Piece.png"))
b_king = pygame.image.load(os.path.join("image","Black King.png"))

w_piece = pygame.image.load(os.path.join("image","White Piece.png"))
w_king = pygame.image.load(os.path.join("image","White King.png"))

b = [ b_piece, b_king]
w = [w_piece, w_king]

B = [ ]
W = [ ]

def redraw_gameWindow():
    global win
    
    win.blit(board,(0,0))

    black = Board(8,8)
    black.add_Piece(win)
                   

    
    pygame.display.update()



class Piece:
    image = -1
    rect = (0,0,623,640)
    startX = rect[0]
    startY = rect[1]
    def __init__(self, row, col, colour):
        self.row = row
        self.col = col
        self.colour= colour
        self.selected = False


    def move(self):
        pass


    def isSelected(self):
        return self.selected

    def draw(self):
        if self.colour == 'w':
            drawIt = W[self.image]

        else:
            drawIt = B[self.image]

        x = self.startX + (self.col * self.rect[2]/8)
        y = self.startY + (self.row * self.rect[2]/8)

        win.blit(draw,(x,y))
        

class normal(Piece):
    image = 0
    

class King(Piece):
    image = 1

