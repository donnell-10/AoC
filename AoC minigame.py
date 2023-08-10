import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

class cube(object):
    rows = 20
    w = 500

    def __init__(self, start, dirnx=1, dirny=0, colour=(255,0,0)):
                 self.pos = start
                 self.dirnx = 1
                 self.dirny = 0
                 self.colour = colour

    def move(self, dirnx, dirny):
                 self.dirnx = dirnx 
                 self.dirny = dirny
                 self.pos=(self.pos[0] + self.dirnx, self.pos[1] +self.dirny)

    def draw(self, surface, eyes = False):
                 dis = self.w // self.rows #divides the distance of the pages by no. of rows
                 i = self.pos[0] #every row
                 j = self.pos[1] #every column

                 pygame.draw.rect(surface, self.colour, (i*dis+1, j*dis+1, dis-2, dis-2))
                 if eyes: #determining the position of the eyes of the snake
                     centre = dis//2
                     radius = 3
                     circleMid = (i*dis+centre-radius, j*dis+8)
                     circleMid2 = (i*dis + dis - radius*2, j*dis+8)
                     pygame.draw.circle(surface, (0,0,0), circleMid, radius)
                     pygame.draw.circle(surface, (0,0,0), circleMid2, radius)


class snake(object):
        body = []
        turns = {}
        def __init__(self, colour, pos):
                 self.colour = colour
                 self.head =cube(pos)
                 self.body.append(self.head)
                 self.dirnx = 0  # keeps track of which direction the snake is moving
                 self.dirmy = 1 # "                                                                                                    "

        def move(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                keys = pygame.key.get_pressed()

                for key in keys:
                    if keys[pygame.K_LEFT]: #turns head left
                        self.dirnx = -1
                        self.dirny = 0
                        self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                    elif keys[pygame.K_RIGHT]: #turns head right
                        self.dirnx = 1
                        self.dirny = 0
                        self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                    elif keys[pygame.K_UP]: #turns head up
                        self.dirnx = 0
                        self.dirny = -1
                        self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                    elif keys[pygame.K_DOWN]: #turns head down
                        self.dirnx = 0
                        self.dirny = 1
                        self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

            for i, c in enumerate(self.body): #moves any part of body that reaches point
                p = c.pos[:]                                       #where head turned
                if p in self.turns:
                    turn = self.turns[p]
                    c.move(turn[0],turn[1])
                    if i == len(self.body)-1:
                        self.turns.pop(p) #once last part of body reaches point, removed from list
                else:
                    if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                    elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0,c.pos[1])
                    elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                    elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0],c.rows-1)
                    else: c.move(c.dirnx,c.dirny) #keeps head moving

        def reset(self, pos):
                 pass

        def addCube(self):
            tail = self.body[-1]
            dx, dy = tail.dirnx, tail.dirny
            #checks what direction body is moving so new cube will be moving in the same direction
            if dx == 1 and dy == 0:
                self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
            elif dx == -1 and dy == 0:
                self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
            elif dx == 0 and dy == 1:
                self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
            elif dx == 0 and dy == -1:
                self.body.append(cube((tail.pos[0],tail.pos[1]+1)))

            #sets added cube to direction that body is moving
            self.body[-1].dirnx = dx
            self.body[-1].dirny = dy

        def draw(self, surface):
                 for i, c in enumerate (self.body):
                     if i == 0:
                         c.draw(surface, True)
                     else:
                            c.draw(surface)



def drawGrid(w, rows, surface):
                 sizeB = w//rows #divides the window in to equal increments

                 x = 0
                 y =0
                 for l in range(rows):
                     x = x+ sizeB #equation of vertical lines
                     y = y+ sizeB #equation of horizontal lines

                     pygame.draw.line(surface, (255,255,255), (x,0), (x,w)) #draws vertical lines
                     pygame.draw.line(surface, (255,255,255), (0,y), (w,y)) #draws horizontal lines


def redrawWindow(surface):
                 global rows, width, s, snack
                 surface.fill((0,0,0))
                 s.draw(surface)
                 snack.draw(surface)
                 drawGrid(width, rows, surface)
                 pygame.display.update()

def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows) #generate random positions
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0: #filter list so snack is not put in same position of 
            continue                                                                                           #snake
        else:
            break
        
    return (x,y)

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def main():
                 global width, rows, s, snack
                 width=500
                 rows = 20
                 win = pygame.display.set_mode((width, width)) #setting dimensions of windows
                 s = snake((255,0,0), (10,10)) #defining the snake
                 snack = cube(randomSnack(rows, s), colour=(0,255,0)) #defining the snack
                 flag = True
                 clock = pygame.time.Clock()
                 while flag: #loop to keep snake moving
                        pygame.time.delay(50) #determines speed of the snake
                        clock.tick(10) #determines speed of the snake
                        s.move()
                        if s.body[0].pos == snack.pos:
                            s.addCube()
                            snack = cube(randomSnack(rows, s), colour=(0,255,0))                        

                        for x in range(len(s.body)):
                            if s.body[x].pos in list(map(lambda z:z.pos,s.body[x+1:])):
                                #if pos of head is the same as another part of body
                                print('Score: ', len(s.body)) #prints score
                                message_box('You Lost!', 'Unlucky!')
                                pygame.quit() #closes window when you lose
                                break




                        redrawWindow(win)
                        
                 pass



main()                 
























    
