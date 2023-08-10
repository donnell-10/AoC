from tkinter import*
import os
import sqlite3

global result

def title():

    BgColour = ('powder blue')
    LargeFont =('Bahnschrift SemiBold',30)
    ButtonFont1 = ('Bahnschrift SemiBold',15)
    BtnColour = ('cadet blue')
    MedFont =('Bahnschrift SemiBold',20)
    SmallFont=('Bahnschrift SemiBold',8)

    root = Tk()

    root.geometry('900x600')




    button = Button(root, text= 'sdf', font = LargeFont, command=lambda: change())
    button.place(x=400,y=10)

    button2 = Button(root, text= 'syf', font = LargeFont, command=lambda: change2())
    button2.place(x=400,y=90)




def change():

    conn=sqlite3.connect('AoC database.db')
    with conn:
        cursor=conn.cursor()
    sql="INSERT INTO Characters(Jotaro) VALUES('Yes')"
    cursor.execute(sql)
    conn.commit()

def change2():
    conn=sqlite3.connect('AoC database.db')
    with conn:
        cursor=conn.cursor()
    sql = "SELECT Jotaro FROM Characters WHere Jotaro ='Yes' "
    cursor.execute(sql)
    conn.commit()
    myresult = cursor.fetchall()

    for result in myresult:
        result1 = result[0]
        if result1 == 'Yes':
            title2()


def title2():
    root = Tk()

    root.geometry('900x600')
    title = Label(root, text = 'swdf')
    title.place(x=50,y=50)



        
title()
