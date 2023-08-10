from tkinter import*
import tkinter as tk
from tkinter import ttk

Large_Font = ('Eras Bold ITC',30)
Button_Font = ('Eras Bold ITC',15)

class AoC (tk.Tk):

    def __init__(self, *args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        tk.Tk.wm_title(self,'AoC')
        tk.Tk.geometry(self,'600x600')
      
        
        container = tk.Frame(self)
        container.pack(side='top',fill='both', expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky='nswe')

            self.show_frame(StartPage)

    def show_frame(self, cont):
        frame= self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.config(bg='powder blue')
        self.frame=Frame(self,bg='powder blue')
        
        label =Label(self, text ='Start Page', font= Large_Font,
                     bg='powder blue')
        label.pack(pady=10, padx=10)

        button1 = Button(self,text = 'visit page 1',
                         command = lambda: controller.show_frame(PageOne),
                             width=10, font= Button_Font, bg= 'cadet blue')
        button1.place(x=235,y=200)

        button2 = Button(self,text = 'visit page 2',
                         command = lambda: controller.show_frame(PageTwo),
                          width=10, font= Button_Font, bg= 'cadet blue')
        button2.place(x=235, y=400)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label =Label(self, text ='Page One', font= Large_Font)
        label.pack(pady=10, padx=10)

        button1 = Button(self,text = 'Back',
                         command = lambda: controller.show_frame(StartPage) )
        button1.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label =Label(self, text ='Page Two', font= Large_Font)
        label.pack(pady=10, padx=10)

        button1 = Button(self,text = 'Back',
                         command = lambda: controller.show_frame(StartPage) )
        button1.pack()
    
        
app = AoC()
app.mainloop()
