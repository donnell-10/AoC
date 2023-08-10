from tkinter import*
import os

def title():

    BgColour = ('powder blue')
    LargeFont =('Bahnschrift SemiBold',30)
    ButtonFont1 = ('Bahnschrift SemiBold',15)
    BtnColour = ('cadet blue')
    MedFont =('Bahnschrift SemiBold',20)
    SmallFont=('Bahnschrift SemiBold',8)

    root = Tk()

    root.geometry('900x600')

    title =Label(root, text ='Sound', font= LargeFont, bg=BgColour)
    title.place(x=400, y=10)

    BackBtn = Button(root,text = 'Back', bg=BtnColour ) #command takes back to Title pg
    BackBtn.place(x=1, y=1)

    label1 = Label(root,text= 'Music', font = LargeFont, bg = BgColour)
    label1.place(x=180, y=180)

    label2 = Label(root,text= 'SFX', font = LargeFont, bg = BgColour)
    label2.place(x=180, y=360)

    cb1= Checkbutton(root, text = 'ON' ,font =MedFont)
    cb1.place(x=550,y=190)

    cb2= Checkbutton(root, text = 'OFF' ,font =MedFont)
    cb2.place(x=650,y=190)

    root.mainloop()

title()

    
