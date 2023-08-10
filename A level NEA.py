from tkinter import *
import os

def title():
    global title  #allows this page to be called from any sub routine
    titlePage = Tk()

    titlePage.geometry ('900x600') #sets window size to 600 pixels by 600 pixels
    titlePage.title('Ace Of Checkers') 
    titlePage.resizable(0,0) #prevents page from being resized

    title= Label(titlePage, text='Ace Of Checkers', width = 15, font = ('Eras Bold ITC',30))
    title.place(x=110,y=10)          

    loginB = Button(titlePage, text='LOGIN', bg='blue', fg='white', font=('Eras Bold ITC',25))
    loginB.config(height=1,width=8)
    loginB.place(x=195,y=200)

    regB = Button(titlePage, text='REGISTER',bg='blue', fg='white', font=('Eras Bold ITC',25))
    regB.config(height=1)
    regB.place(x=195,y=425)


    titlePage.mainloop()



title()
