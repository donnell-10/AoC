

from tkinter import*
import tkinter as tk
import sqlite3
from pygame import mixer
from tkinter import messagebox


BgColour = ('powder blue')
LargeFont =('Bahnschrift SemiBold',30)
ButtonFont1 = ('Bahnschrift SemiBold',15)
BtnColour = ('cadet blue')
MedFont =('Bahnschrift SemiBold',20)
SmallFont=('Bahnschrift SemiBold',8)
SmallFont2=('Bahnschrift SemiBold',11)





class AoC (tk.Tk): #creating a class for framework of every page

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, 'Ace Of Checkers') #title of window
        tk.Tk.geometry(self, '900x600') #sets window to this size
        tk.Tk.resizable(self, 0,0)
        #mixer.init() #initailises the mixer
        #mixer.music.load('bgMusic2.wav') #load music from file
        #mixer.music.play(50) #plays the music on loop 50 times
        #mixer.music.set_volume(15/100) #sets the volume to 8 out 100

        page = tk.Frame(self)
        page.pack(side='top', fill='both', expand = True)
        page.grid_rowconfigure(0, weight =1)
        page.grid_columnconfigure(0, weight=1)

        self.frames = {} #creates dictionary that will hold every page

        for F in (TitlePage, LoginPage, RegisterPage, FP_page, main_menu,
                  play_options, Settings, Rules, Controls, Sound, LBoard_optns,
                  Shop, Jotaro_Buy, Kakyoin_Buy, Polnareff_Buy, Avdol_Buy,
                  Hatsune_Buy, Nami_Buy, C_List, Locked, Jotaro_List, Kakyoin_List,
                  Polnareff_List, Avdol_List, Hatsune_List, Nami_List, Cheats, Minigames,
                  snake, PvP, Quick_Match):
            
            frame=F(page, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nswe') #puts frame in top left corner
            self.show_frame(TitlePage)

    def show_frame(self,cont):
        frame= self.frames[cont]
        frame.tkraise()
        
class TitlePage(tk.Frame): #new class for the title page

    def __init__(self,parent,page):
        tk.Frame.__init__(self,parent)
        self.config(bg=BgColour)
        self.frame =Frame(self,bg=BgColour) #changes colour of page
        self.image= PhotoImage(file='AoC Title.png')

        title = Label(self, image=self.image, bg=BgColour) #creates a label which will be used as title
        title.place(x=300, y=10)

        loginBtn = Button(self, text ='Login', width=10, font= ButtonFont1,
                          bg= BtnColour,
                          command= lambda: page.show_frame(LoginPage)) #creates clickable button
        loginBtn.place(x=390, y=200)

        SkipBtn = Button(self, text ='Skip', width=1, font= ButtonFont1,
                          bg= BtnColour,
                          command= lambda: page.show_frame(main_menu)) #creates clickable button
        SkipBtn.place(x=1, y=550)        

        RegBtn = Button(self, text ='Register', width=10, font= ButtonFont1,
                          bg= BtnColour,
                         command= lambda: page.show_frame(RegisterPage)) #creates clickable button
        RegBtn.place(x=390, y=300)


class LoginPage(tk.Frame):

     def __init__(self, parent, page):
        tk.Frame.__init__(self,parent)
        self.config(bg=BgColour)
        self.frame=Frame(self,bg=BgColour)
        self.image= PhotoImage(file='AoC Title.png')

        global Username2
        global Password2
        
        
        title =Label(self, image = self.image, font= LargeFont, bg=BgColour)
        title.place(x=300, y=10)

        BackBtn = Button(self,text = 'Back', bg=BtnColour,
                         command = lambda: page.show_frame(TitlePage) ) #command takes back to Title pg
        BackBtn.place(x=1, y=1)

        username = Label(self, text = 'Username',  font=MedFont, bg=BgColour) #area for user to type into
        username.place(x=385, y=150)

        Username2 = tk.StringVar()
        unameEntry= Entry(self, width=50, textvariable = Username2)
        unameEntry.place(x=305, y=200)

        password = Label(self, text = 'Password',  font=MedFont, bg=BgColour) #area for user to type into
        password.place(x=385, y=300)

        Password2 = tk.StringVar()
        pwordEntry= Entry(self, width=50, textvariable=Password2)
        pwordEntry.place(x=305, y=350)
        pwordEntry.config(show='*')

        loginBtn = Button(self, text='Login', width=15, font=ButtonFont1, bg=BtnColour,
                          command = lambda:[self.login_user(page, Username2.get(), Password2.get())])
        loginBtn.place(x=500, y=450)

        FPBtn = Button(self, text='Forgot Password', width=15, font=ButtonFont1, bg=BtnColour,
                       command = lambda: page.show_frame(FP_page))
        FPBtn.place(x=250, y=450)

     def login_user(self, page,Username, Password): #function used to log user in
            conn = sqlite3.connect('AoC database.db', timeout = 3) #connects to database
            with conn:
                cursor=conn.cursor()
            sql =" SELECT *  FROM players WHERE Username = ? AND Password = ? " #Will check if entered info in is db
            cursor.execute(sql,[(Username), (Password)])
            results = cursor.fetchall()
             
            if results:
                    page.show_frame(main_menu)              
            else:
                    messagebox.showinfo("Error", "Username or Password incorrect")                          
           
            

          
class RegisterPage(tk.Frame):
    
    def __init__(self, parent, page):
        tk.Frame.__init__(self,parent)
        self.config(bg=BgColour)
        self.frame=Frame(self,bg=BgColour)
        self.image= PhotoImage(file='AoC Title.png')
        global Username1
        global password1
        global DoB1
        global FullName1
        
        title =Label(self, image=self.image, font= LargeFont, bg=BgColour)
        title.place(x=300, y=10)

        BackBtn = Button(self,text = 'Back', bg=BtnColour,
                         command = lambda: page.show_frame(TitlePage) ) #command takes back to Title pg
        BackBtn.place(x=1, y=1)

        FullName = Label(self, text = 'Full Name', width = 15, font=MedFont, bg=BgColour)
        FullName.place(x=25, y=150)

        FullName1 = tk.StringVar() 
        FullNameEntry = Entry(self,width=50, textvariable = FullName1)
        FullNameEntry.place(x=300, y=160)

        DoB = Label(self, text = 'DoB', width = 15, font=MedFont, bg=BgColour)
        DoB.place(x=25, y=200)

        DoB1 = tk.IntVar()
        DoBEntry = Entry(self,width=50, textvariable= DoB1)
        DoBEntry.place(x=300, y=210)
        

        NewUsername = Label(self, text = 'Create Username', width = 15, font=MedFont, bg=BgColour)
        NewUsername.place(x=25, y=250)

        Username1 = tk.StringVar()  
        NewUnameEntry = Entry(self,width=50, textvariable= Username1)
        NewUnameEntry.place(x=300, y=260)
        
        NewPassword = Label(self, text = 'Create Password', width = 15, font=MedFont, bg=BgColour)
        NewPassword.place(x=25, y=300)

        password1 = tk.StringVar() 
        NewPwordEntry = Entry(self,width=50, textvariable = password1)
        NewPwordEntry.place(x=300, y=310)
        NewPwordEntry.config(show="*")

        DoBInfo = Label(self, text = 'DoB must be in ddmmyy form', width = 30, font=SmallFont, bg=BgColour)
        DoBInfo.place(x=1, y=480)

        UnameInfo = Label(self, text = 'Username must include a number or special character',
                        width = 50, font=SmallFont, bg=BgColour)
        UnameInfo.place(x=1, y=510)

        PwordInfo = Label(self, text = 'Password must be 8 characters & include a number',
                        width = 48, font=SmallFont, bg=BgColour)
        PwordInfo.place(x=1, y=540)

        RegBtn = Button(self, text='Register', width=15, font=ButtonFont1, bg=BtnColour,
                        command =lambda: self.reg_acc(page,Username1.get(), password1.get(), DoB1.get(),FullName1.get()))
        RegBtn.place(x=400, y=500)

    def reg_acc(self,page,Username, Password, DoB, FullName):

        conn = sqlite3.connect('AoC database.db')
        with conn:
            cursor=conn.cursor()
        c = "0"
        cursor.execute('CREATE TABLE IF NOT EXISTS players (Username TEXT , Password TEXT, Name TEXT, DoB INTEGER)')
        cursor.execute('CREATE TABLE IF NOT EXISTS bank (Username TEXT , Coins INTEGER )')        
        sql='INSERT INTO players (Username, Password,Name,Dob) VALUES(?,?,?,?)'
        sql2='INSERT INTO bank(Username, Coins) VALUES(?,?)'
        cursor.execute( sql, [(Username),(Password),(FullName),(DoB)])
        cursor.execute( sql2, [(Username), (c)])
        conn.commit()
        page.show_frame(LoginPage)  
        


class FP_page(tk.Frame):


        def __init__(self, parent, page):
            tk.Frame.__init__(self,parent)
            self.config(bg=BgColour)
            self.frame=Frame(self,bg=BgColour)
            self.image= PhotoImage(file='AoC Title.png')

            global ExName
            global ExDob
            global ExUname
            global NewPword
            
            title =Label(self, image=self.image, font= LargeFont, bg=BgColour)
            title.place(x=300, y=10)

            BackBtn = Button(self, text = 'Back', bg=BtnColour,
                             command = lambda: page.show_frame(LoginPage) ) #command takes back to Title pg
            BackBtn.place(x=1, y=1)

            FullName = Label(self, text = 'Full Name', width = 15, font=MedFont, bg=BgColour)
            FullName.place(x=25, y=150)

            ExName = tk.StringVar()
            FullNameEntry = Entry(self,width=50, textvariable = ExName)
            FullNameEntry.place(x=300, y=160)

            DoB = Label(self, text = 'DoB', width = 15, font=MedFont, bg=BgColour)
            DoB.place(x=25, y=200)

            ExDoB = tk.IntVar() 
            DoBEntry = Entry(self,width=50, textvariable = ExDoB)
            DoBEntry.place(x=300, y=210)

            Username = Label(self, text = 'Username', width = 15, font=MedFont, bg=BgColour)
            Username.place(x=25, y=250)

            ExUname = tk.StringVar() 
            UnameEntry = Entry(self,width=50, textvariable = ExUname)
            UnameEntry.place(x=300, y=260)

            NewPassword = Label(self, text = 'Create Password', width = 15, font=MedFont, bg=BgColour)
            NewPassword.place(x=25, y=300)

            NewPword = tk.StringVar()
            NewPwordEntry = Entry(self,width=50, textvariable = NewPword)
            NewPwordEntry.place(x=300, y=310)

            CreatePwordBtn = Button(self, text='Create Password', width=15, font=ButtonFont1, bg=BtnColour,
                                    command =lambda: self.update_pass(page,ExUname.get(), NewPword.get(), ExName.get(), ExDoB.get()))
            CreatePwordBtn.place(x=400, y=500)

        def update_pass(self, page, Username, Password, FullName, DoB):
            conn = sqlite3.connect('AoC database.db')
            with conn:
                cursor = conn.cursor()
            sql =" DELETE FROM players  WHERE Username = ? AND Name =?  AND DoB = ?" #Will check if entered info in is db
            sql2 ="INSERT INTO players (Username, Password, Name, DoB) VALUES(?,?,?,?)"
            cursor.execute(sql,[(Username),(FullName), (DoB)])
            cursor.execute(sql2,[(Username),(Password), (FullName), (DoB)])
            conn.commit()

            

class main_menu(tk.Frame): #new class for new page

        def __init__(self, parent, page): #initialises anything within this function
                tk.Frame.__init__(self,parent)
                self.config(bg=BgColour)
                self.frame=Frame(self,bg=BgColour)
                self.image= PhotoImage(file='AoC Title.png') #calls image from file

                title = Label(self, image=self.image, bg=BgColour) #creates a label which will be used as title
                title.place(x=300, y=10)

                PlayBtn = Button(self, text='Play', font = ButtonFont1, bg=BtnColour,width =15,
                                 command = lambda: page.show_frame(play_options))
                PlayBtn.place(x=80, y =200)

                SettingsBtn = Button(self, text='Settings', font = ButtonFont1, bg=BtnColour,width =15,
                                     command = lambda: page.show_frame(Settings))
                SettingsBtn.place(x=80, y =275)

                LBoardBtn = Button(self, text='Leaderboard', font = ButtonFont1, bg=BtnColour,width =15,
                                   command = lambda: page.show_frame(LBoard_optns) )
                LBoardBtn.place(x=80, y =350)

                ShopBtn = Button(self, text='Shop', font = ButtonFont1, bg=BtnColour,width =15,
                                 command = lambda: page.show_frame(Shop))
                ShopBtn.place(x=80, y =425)

                ClBtn = Button(self, text='Character List', font = ButtonFont1, bg=BtnColour,width =15,
                                 command = lambda: page.show_frame(C_List))
                ClBtn.place(x=600, y =200)

                CheatBtn = Button(self, text='****', font = SmallFont, bg=BtnColour,
                                 command = lambda: page.show_frame(Cheats))
                CheatBtn.place(x=850, y =1)                

                ExitBtn = Button(self, text='Exit', font = ButtonFont1, bg=BtnColour,width =15,
                                 command = lambda: quit(self))
                ExitBtn.place(x=600, y =425)


class play_options(tk.Frame):

        def __init__(self, parent, page): #initialises anything within this function
                    tk.Frame.__init__(self,parent)
                    self.config(bg=BgColour)
                    self.frame=Frame(self,bg=BgColour)

                    title =Label(self, text ='Play', font= LargeFont, bg=BgColour)
                    title.place(x=410, y=10)

                    BackBtn = Button(self,text = 'Back', bg=BtnColour,
                                     command = lambda: page.show_frame(main_menu)) #command takes back to Title pg
                    BackBtn.place(x=1, y=1)


                    CampaignBtn = Button(self, text='Campaign', bg =BtnColour, font = ButtonFont1)
                    CampaignBtn.config(width=50, height = 2)
                    CampaignBtn.place(x=175, y =140)

                    QMBtn = Button(self, text='Quick Match', bg =BtnColour, font = ButtonFont1,
                                   command = lambda:page.show_frame(Quick_Match))
                    QMBtn.config(width=50, height = 2)
                    QMBtn.place(x=175, y =270)

                    PvPBtn = Button(self, text='Player vs Player', bg =BtnColour, font = ButtonFont1,
                                    command = lambda: page.show_frame(PvP))
                    PvPBtn.config(width=50, height = 2)
                    PvPBtn.place(x=175, y =400)

                    MgBtn = Button(self, text='Minigames', bg =BtnColour, font = ButtonFont1,
                                   command = lambda: page.show_frame(Minigames))
                    MgBtn.config(width=50, height = 2)
                    MgBtn.place(x=175, y =530)

class Quick_Match(tk.Frame):
            def __init__(self, parent, page): #initialises anything within this function
                    tk.Frame.__init__(self,parent)
                    self.config(bg=BgColour)
                    self.frame=Frame(self,bg=BgColour)

                    title =Label(self, text ='Quick Match', font= LargeFont, bg=BgColour)
                    title.place(x=330, y=10)

                    BackBtn = Button(self,text = 'Back', bg=BtnColour,
                                     command = lambda: page.show_frame(play_options)) #command takes back to Title pg
                    BackBtn.place(x=1, y=1)

                    OG_Btn = Button(self, text='Original Checkers', bg =BtnColour, font = ButtonFont1,
                                    command = lambda:self.VsCpuOG(page) )
                    OG_Btn.config(width=50, height = 2)
                    OG_Btn.place(x=175, y =230)

                    AC_Btn = Button(self, text="Ace's Checkers", bg =BtnColour, font = ButtonFont1)
                    AC_Btn.config(width=50, height = 2)
                    AC_Btn.place(x=175, y =330)

            def VsCpuOG(self,page):
                    import Vs_Cpu 
                    # board_GUI(black,white)
                    # newGameBoard()
                    # clock.tick(60)
                    # pygame.display.flip()
                    # drawGameStatusBox(black)
                    # drawPieces()

                    
                    


class PvP(tk.Frame):
            def __init__(self, parent, page): #initialises anything within this function
                    tk.Frame.__init__(self,parent)
                    self.config(bg=BgColour)
                    self.frame=Frame(self,bg=BgColour)

                    title =Label(self, text ='Player vs Player', font= LargeFont, bg=BgColour)
                    title.place(x=300, y=10)

                    BackBtn = Button(self,text = 'Back', bg=BtnColour,
                                     command = lambda: page.show_frame(play_options)) #command takes back to Title pg
                    BackBtn.place(x=1, y=1)

                    OG_Btn = Button(self, text='Original Checkers', bg =BtnColour, font = ButtonFont1,
                                    command = lambda:self.play_OG(page) )
                    OG_Btn.config(width=50, height = 2)
                    OG_Btn.place(x=175, y =230)

                    AC_Btn = Button(self, text="Ace's Checkers", bg =BtnColour, font = ButtonFont1)
                    AC_Btn.config(width=50, height = 2)
                    AC_Btn.place(x=175, y =330)

            def play_OG(self, page):
                import player_vs_player 
                board_GUI(black,white)
                newGameBoard()
                clock.tick(60)
                pygame.display.flip()
                drawGameStatusBox(black)
                drawPieces()
                page.show_frame(PvP)
                    
    


class Minigames(tk.Frame):

        def __init__(self, parent, page): #initialises anything within this function
                    tk.Frame.__init__(self,parent)
                    self.config(bg=BgColour)
                    self.frame=Frame(self,bg=BgColour)
                    self.snake_icon = PhotoImage(file='snake_icon.png')

                    title =Label(self, text ='Minigames', font= LargeFont, bg=BgColour)
                    title.place(x=410, y=10)

                    BackBtn = Button(self,text = 'Back', bg=BtnColour,
                                     command = lambda: page.show_frame(play_options)) #command takes back to Title pg
                    BackBtn.place(x=1, y=1)

                    Snake_Btn = Button(self, image = self.snake_icon, bg = BtnColour,
                                        command = lambda: page.show_frame(snake))
                    Snake_Btn.place(x=50, y=180)

                    Snake_Name = Label(self, text = 'Snake', font = SmallFont2, bg= BgColour)
                    Snake_Name.place(x=53,y=270)

class snake(tk.Frame):

        def __init__(self, parent, page): #initialises anything within this function
                    tk.Frame.__init__(self,parent)
                    self.config(bg=BgColour)
                    self.frame=Frame(self,bg=BgColour)
                    self.snake_game = PhotoImage(file='snake_game.png')
                    self.snake_des = PhotoImage(file='snake_des.png')

                    title =Label(self, text ='Snake', font= LargeFont, bg=BgColour)
                    title.place(x=410, y=10)

                    snake_img = Label(self, image =self.snake_game, bg=BgColour)
                    snake_img.place(x=150, y=120)

                    snake_description = Label(self, image =self.snake_des, bg=BgColour)
                    snake_description.place(x=500, y=120)

                    PlayBtn = Button(self, text = 'Play', bg = BtnColour, font = ButtonFont1,
                                    command = lambda: self.playSnake(page))
                    PlayBtn.place(x=600, y=400)   
                    
                    BackBtn = Button(self,text = 'Back', bg=BtnColour,
                                     command = lambda: page.show_frame(Minigames)) #command takes back to Title pg
                    BackBtn.place(x=1, y=1)

        def playSnake(self,page):
            from Snake_minigame import main
            main()
            page.show_frame(Minigames)
            

class Settings(tk.Frame):
        def __init__(self, parent, page): #initialises anything within this function
            tk.Frame.__init__(self,parent)
            self.config(bg=BgColour)
            self.frame=Frame(self,bg=BgColour)

            title =Label(self, text ='Settings', font= LargeFont, bg=BgColour)
            title.place(x=380, y=10)

            BackBtn = Button(self,text = 'Back', bg=BtnColour,
                             command = lambda: page.show_frame(main_menu)) #command takes back to Title pg
            BackBtn.place(x=1, y=1)


            RulesBtn = Button(self, text='Rules', bg =BtnColour, font = ButtonFont1,
                              command = lambda: page.show_frame(Rules))
            RulesBtn.config(width=50, height = 2)
            RulesBtn.place(x=175, y =150)

            ControlsBtn = Button(self, text='Controls', bg =BtnColour, font = ButtonFont1,
                                 command = lambda: page.show_frame(Controls))
            ControlsBtn.config(width=50, height = 2)
            ControlsBtn.place(x=175, y =280)

            SoundBtn = Button(self, text='Sound', bg =BtnColour, font = ButtonFont1,
                              command = lambda: page.show_frame(Sound))
            SoundBtn.config(width=50, height = 2)
            SoundBtn.place(x=175, y =410)

class Rules(tk.Frame):
        def __init__(self, parent, page): #initialises anything within this function
            tk.Frame.__init__(self,parent)
            self.config(bg=BgColour)
            self.frame=Frame(self,bg=BgColour)

            title =Label(self, text ='Rules', font= LargeFont, bg=BgColour)
            title.place(x=400, y=10)

            BackBtn = Button(self,text = 'Back', bg=BtnColour,
                             command = lambda: page.show_frame(Settings)) #command takes back to Title pg
            BackBtn.place(x=1, y=1)

            C_rules = Label(self,text= 'Checkers Rules', font = MedFont, bg = BgColour)
            C_rules.place(x=120, y=120)

            G_rules = Label(self,text= 'Game Rules', font = MedFont, bg = BgColour)
            G_rules.place(x=580, y=120)


class Controls(tk.Frame):
            def __init__(self, parent, page): #initialises anything within this function
                tk.Frame.__init__(self,parent)
                self.config(bg=BgColour)
                self.frame=Frame(self,bg=BgColour)

                title =Label(self, text ='Controls', font= LargeFont, bg=BgColour)
                title.place(x=400, y=10)
                
                BackBtn = Button(self,text = 'Back', bg=BtnColour,
                                 command = lambda: page.show_frame(Settings)) #command takes back to Title pg
                BackBtn.place(x=1, y=1)


class Sound(tk.Frame):
            def __init__(self, parent, page): #initialises anything within this function
                tk.Frame.__init__(self,parent)
                self.config(bg=BgColour)
                self.frame=Frame(self,bg=BgColour)

                title =Label(self, text ='Sound', font= LargeFont, bg=BgColour)
                title.place(x=400, y=10)
                
                BackBtn = Button(self,text = 'Back', bg=BtnColour,
                                 command = lambda: page.show_frame(Settings)) #command takes back to Title pg
                BackBtn.place(x=1, y=1)

                Music = Label(self,text= 'Music', font = LargeFont, bg = BgColour)
                Music.place(x=180, y=180)

                SFX = Label(self,text= 'SFX', font = LargeFont, bg = BgColour)
                SFX.place(x=180, y=360)

                Music_cb1= Button(self, text = 'ON' ,font =MedFont, bg = BtnColour,
                                 command = lambda:self.music_on())
                Music_cb1.place(x=550,y=190)

                Music_cb2= Button(self, text = 'OFF' ,font =MedFont, bg = BtnColour,
                                       command = lambda:self.music_off())
                Music_cb2.place(x=650,y=190)

                SFX_cb1= Button(self, text = 'ON' ,font =MedFont, bg =BtnColour)
                SFX_cb1.place(x=550,y=370)

                SFX_cb2= Button(self, text = 'OFF' ,font =MedFont, bg =BtnColour)
                SFX_cb2.place(x=650,y=370)


            def music_on(self):
                mixer.music.play(50)
            
            def music_off(self):
                mixer.music.stop()
                
class Cheats(tk.Frame):
            def __init__(self, parent, page): #initialises anything within this function
                tk.Frame.__init__(self,parent)
                self.config(bg=BgColour)
                self.frame=Frame(self,bg=BgColour)

                title =Label(self, text ='Cheat codes', font= LargeFont, bg=BgColour)
                title.place(x=330, y=10)

                code = tk.StringVar()  
                CheatCode = Entry(self,width=50, textvariable= code)
                CheatCode.place(x=305, y=200)
                
                BackBtn = Button(self,text = 'Back', bg=BtnColour,
                                 command = lambda: page.show_frame(main_menu)) #command takes back to Title pg
                BackBtn.place(x=1, y=1)

                EnterBtn = Button(self,text = 'Enter', bg=BtnColour, font =MedFont,
                                 command = lambda: self.CheatCodes(page, Username2.get(),code.get())) #command takes back to Title pg
                EnterBtn.place(x=400, y=400)


            def CheatCodes(self, page,Username, code):
                MillionCoins = "A2C7b9HYD2" #code that will give user a million coins
                if code == MillionCoins:
                    conn=sqlite3.connect('AoC database.db') #connects to database
                    with conn:
                        cursor=conn.cursor()
                    sql = "SELECT Coins FROM bank WHERE Username =? " #looks for usernames in bank table and selects the coins
                    cursor.execute(sql, [(Username)])
                    conn.commit()
                    myresult = cursor.fetchall()
                    for result in myresult:
                            result1 = result[0]
                            NewCoins= str(result1 + 1000000) #adds a million to the no. of coins found in database

                            sql2 = "DELETE FROM bank WHERE Username = ?" #deletes the previous entry with the same username
                            sql3 = "INSERT INTO bank (Username, Coins) VALUES(?,?)" #adds new entry with new value of coins
                            cursor.execute(sql2,[(Username)])
                            cursor.execute(sql3,[(Username), (NewCoins)])
                            conn.commit()
                            messagebox.showinfo("Success", "1,000,000 coins added")

                    
            
class LBoard_optns(tk.Frame):
            def __init__(self, parent, page): #initialises anything within this function
                tk.Frame.__init__(self,parent)
                self.config(bg=BgColour)
                self.frame=Frame(self,bg=BgColour)

                title =Label(self, text ='Leaderboards', font= LargeFont, bg=BgColour)
                title.place(x=330, y=10)

                BackBtn = Button(self,text = 'Back', bg=BtnColour,
                                 command = lambda: page.show_frame(main_menu)) #command takes back to Title pg
                BackBtn.place(x=1, y=1)


                CampaignBtn = Button(self, text='Campaign', bg =BtnColour, font = ButtonFont1)
                CampaignBtn.config(width=50, height = 2)
                CampaignBtn.place(x=175, y =150)

                QMBtn = Button(self, text='Quick Match', bg =BtnColour, font = ButtonFont1)
                QMBtn.config(width=50, height = 2)
                QMBtn.place(x=175, y =280)

                PvPBtn = Button(self, text='Player vs Player', bg =BtnColour, font = ButtonFont1)
                PvPBtn.config(width=50, height = 2)
                PvPBtn.place(x=175, y =410)

class Shop(tk.Frame):
        def __init__(self, parent, page): #initialises anything within this function
            tk.Frame.__init__(self,parent)
            self.config(bg=BgColour)
            self.frame=Frame(self,bg=BgColour)
            self.J_sprite =PhotoImage(file='sprites/Jotaro_sprite.png')
            self.K_sprite = PhotoImage(file='sprites/Kakyoin_sprite.png')
            self.P_sprite = PhotoImage(file='sprites/Polnareff_sprite.png')
            self.Av_sprite = PhotoImage(file='sprites/Avdol_sprite.png')
            self.H_sprite = PhotoImage(file='sprites/Hatsune_sprite.png')
            self.N_sprite=  PhotoImage(file='sprites/Nami_sprite.png')
            
            title =Label(self, text ='Shop', font= LargeFont, bg=BgColour)
            title.place(x=400, y=10)

            BackBtn = Button(self,text = 'Back', bg=BtnColour,
                             command = lambda: page.show_frame(main_menu)) #command takes back to Title pg
            BackBtn.place(x=1, y=1)

            C = Label(self,text= 'Characters', font = MedFont, bg = BgColour)
            C.place(x=120, y=120)

            I = Label(self,text= 'Items', font = MedFont, bg = BgColour)
            I.place(x=600, y=120)
########################### JOTARO ####################################
            Jotaro_Btn = Button(self, image = self.J_sprite, bg = BtnColour,
                                command = lambda: self.J_bought(page, Username2.get()))
            Jotaro_Btn.place(x=50, y=180)

            Jotaro_Name = Label(self, text = 'Jotaro', font = SmallFont2, bg= BgColour)
            Jotaro_Name.place(x=53,y=270)

########################## KAKYOIN ####################################
            Kakyoin_Btn = Button(self, image = self.K_sprite, bg = BtnColour,
                                command = lambda: self.K_bought(page, Username2.get()))
            Kakyoin_Btn.place(x=160, y=180)

            Kakyoin_Name = Label(self, text = 'Kakyoin', font = SmallFont2, bg= BgColour)
            Kakyoin_Name.place(x=163,y=270)

########################## POLNAREFF ####################################            
            Polnareff_Btn = Button(self, image = self.P_sprite, bg = BtnColour,
                                command = lambda: self.P_bought(page, Username2.get()))
            Polnareff_Btn.place(x=270, y=180)

            Polnareff_Name = Label(self, text = 'Polnareff', font = SmallFont2, bg= BgColour)
            Polnareff_Name.place(x=273,y=270)
            
########################### AVDOL ####################################               
            Avdol_Btn = Button(self, image = self.Av_sprite, bg = BtnColour,
                                command = lambda: self.Av_bought(page, Username2.get()))
            Avdol_Btn.place(x=50, y=300)

            Avdol_Name = Label(self, text = 'Avdol', font = SmallFont2, bg= BgColour)
            Avdol_Name.place(x=53,y=390)

########################### HATSUNE ####################################
            Hatsune_Btn = Button(self, image = self.H_sprite, bg = 'white',
                                command = lambda: self.H_bought(page, Username2.get()))
            Hatsune_Btn.place(x=160, y=300)

            Hatsune_Name = Label(self, text = 'Hatsune', font = SmallFont2, bg= BgColour)
            Hatsune_Name.place(x=163,y=390)

########################### NAMI ####################################
            Nami_Btn = Button(self, image = self.N_sprite, bg = 'white',
                                command = lambda: self.N_bought(page, Username2.get()))
            Nami_Btn.place(x=270, y=300)

            Nami_Name = Label(self, text = 'Nami', font = SmallFont2, bg= BgColour)
            Nami_Name.place(x=273,y=390)

        def J_bought(self,page, Username):
            conn=sqlite3.connect('AoC database.db') #connects to database
            with conn:
                cursor=conn.cursor()
            sql = "SELECT Obtained FROM Jotaro WHERE Username =? " # looks for usernames in the jotaro list
            cursor.execute(sql, [(Username)])
            conn.commit()
            myresult = cursor.fetchall()
            if myresult:
                for result in myresult:
                    result1 = result[0]
                    if result1 == 'Yes': #if obtained column is filled with yes implying it has bee bought
                        page.show_frame(Jotaro_List) #this page will be shown
            else:
                page.show_frame(Jotaro_Buy) #if not the page is locked        

        def K_bought(self,page, Username):
            conn=sqlite3.connect('AoC database.db') #connects to database
            with conn:
                cursor=conn.cursor()
            sql = "SELECT Obtained FROM Kakyoin WHERE Username =? " # looks for usernames in the jotaro list
            cursor.execute(sql, [(Username)])
            conn.commit()
            myresult = cursor.fetchall()
            if  myresult:
                for result in myresult:
                    result1 = result[0]
                    if result1 == 'Yes': #if obtained column is filled with yes implying it has bee bought
                        page.show_frame(Kakyoin_List) #this page will be shown
            else:
                page.show_frame(Kakyoin_Buy) #if not the page is locked

        def P_bought(self,page, Username):
            conn=sqlite3.connect('AoC database.db') #connects to database
            with conn:
                cursor=conn.cursor()
            sql = "SELECT Obtained FROM Polnareff WHERE Username =? " # looks for usernames in the jotaro list
            cursor.execute(sql, [(Username)])
            conn.commit()
            myresult = cursor.fetchall()
            if myresult:
                for result in myresult:
                    result1 = result[0]
                    if result1 == 'Yes': #if obtained column is filled with yes implying it has bee bought
                        page.show_frame(Polnareff_List) #this page will be shown
            else:
                page.show_frame(Polnareff_Buy) #if not the page is locked       

        def Av_bought(self,page, Username):
            conn=sqlite3.connect('AoC database.db') #connects to database
            with conn:
                cursor=conn.cursor()
            sql = "SELECT Obtained FROM Avdol WHERE Username =? " # looks for usernames in the jotaro list
            cursor.execute(sql, [(Username)])
            conn.commit()
            myresult = cursor.fetchall()
            if myresult:
                for result in myresult:
                    result1 = result[0]
                    if result1 == 'Yes': #if obtained column is filled with yes implying it has bee bought
                        page.show_frame(Avdol_List) #this page will be shown
            else:
                page.show_frame(Avdol_Buy) #if not the page is locked       

        def H_bought(self,page, Username):
            conn=sqlite3.connect('AoC database.db') #connects to database
            with conn:
                cursor=conn.cursor()
            sql = "SELECT Obtained FROM Hatsune WHERE Username =? " # looks for usernames in the jotaro list
            cursor.execute(sql, [(Username)])
            conn.commit()
            myresult = cursor.fetchall()
            if myresult:
                for result in myresult:
                    result1 = result[0]
                    if result1 == 'Yes': #if obtained column is filled with yes implying it has bee bought
                        page.show_frame(Hatsune_List) #this page will be shown
            else:
                page.show_frame(Hatsune_Buy) #if not the page is locked       

        def N_bought(self,page, Username):
            conn=sqlite3.connect('AoC database.db') #connects to database
            with conn:
                cursor=conn.cursor()
            sql = "SELECT Obtained FROM Nami WHERE Username =? " # looks for usernames in the jotaro list
            cursor.execute(sql, [(Username)])
            conn.commit()
            myresult = cursor.fetchall()
            if myresult:
                for result in myresult:
                    result1 = result[0]
                    if result1 == 'Yes': #if obtained column is filled with yes implying it has bee bought
                        page.show_frame(Nami_List) #this page will be shown
            else:
                page.show_frame(Nami_Buy) #if not the page is locked       



                    
class C_List(tk.Frame):
        def __init__(self, parent, page): #initialises anything within this function
            tk.Frame.__init__(self,parent)
            self.config(bg=BgColour)
            self.frame=Frame(self,bg=BgColour)
            self.A_sprite= PhotoImage(file='sprites/Ace_sprite.png')
            self.J_sprite =PhotoImage(file='sprites/Jotaro_sprite.png')
            self.K_sprite = PhotoImage(file='sprites/Kakyoin_sprite.png')
            self.P_sprite = PhotoImage(file='sprites/Polnareff_sprite.png')
            self.Av_sprite = PhotoImage(file='sprites/Avdol_sprite.png')
            self.H_sprite = PhotoImage(file='sprites/Hatsune_sprite.png')
            self.N_sprite=  PhotoImage(file='sprites/Nami_sprite.png')
            
            title =Label(self, text ='Character List', font= LargeFont, bg=BgColour)
            title.place(x=330, y=10)
            BackBtn = Button(self,text = 'Back', bg=BtnColour,
                             command = lambda: page.show_frame(main_menu)) #command takes back to Title pg
            BackBtn.place(x=1, y=1)
########################## ACE ####################################
            Ace_Btn = Button(self, image = self.A_sprite, bg = 'white')
            Ace_Btn.place(x=50, y=180)

            Ace_Name = Label(self, text = 'Ace', font = SmallFont2, bg= BgColour)
            Ace_Name.place(x=57,y=270)
########################### JOTARO ####################################
            Jotaro_Btn = Button(self, image = self.J_sprite, bg = BtnColour,
                                command = lambda: self.J_unlocked(page, Username2.get()))
            Jotaro_Btn.place(x=150, y=180)

            Jotaro_Name = Label(self, text = 'Jotaro', font = SmallFont2, bg= BgColour)
            Jotaro_Name.place(x=153,y=270)          
########################## KAKYOIN ####################################
            Kakyoin_Btn = Button(self, image = self.K_sprite, bg = BtnColour,
                                 command = lambda: self.K_unlocked(page, Username2.get()))
            Kakyoin_Btn.place(x=270, y=180)

            Kakyoin_Name = Label(self, text = 'Kakyoin', font = SmallFont2, bg= BgColour)
            Kakyoin_Name.place(x=273,y=270)

########################## POLNAREFF ####################################
            Polnareff_Btn = Button(self, image = self.P_sprite, bg = BtnColour,
                                   command = lambda: self.P_unlocked(page, Username2.get()))
            Polnareff_Btn.place(x=380, y=180)

            Polnareff_Name = Label(self, text = 'Polnareff', font = SmallFont2, bg= BgColour)
            Polnareff_Name.place(x=383,y=270)
            
########################## AVDOL ####################################
            Avdol_Btn = Button(self, image = self.Av_sprite, bg = BtnColour,
                               command = lambda: self.Av_unlocked(page, Username2.get()))
            Avdol_Btn.place(x=490, y=180)

            Avdol_Name = Label(self, text = 'Avdol', font = SmallFont2, bg= BgColour)
            Avdol_Name .place(x=493,y=270)

########################## HATSUNE ####################################
            Hatsune_Btn = Button(self, image = self.H_sprite, bg = 'white',
                                 command = lambda: self.H_unlocked(page, Username2.get()))
            Hatsune_Btn.place(x=600, y=180)

            Hatsune_Name = Label(self, text = 'Hatsune', font = SmallFont2, bg= BgColour)
            Hatsune_Name.place(x=603,y=270)

########################## NAMI ####################################
            Nami_Btn = Button(self, image = self.N_sprite, bg = 'white',
                               command = lambda: self.N_unlocked(page, Username2.get()))
            Nami_Btn.place(x=710, y=180)

            Nami_Name = Label(self, text = 'Nami', font = SmallFont2, bg= BgColour)
            Nami_Name.place(x=713,y=270)


        def J_unlocked(self,page, Username):
            conn=sqlite3.connect('AoC database.db') #connects to database
            with conn:
                cursor=conn.cursor()
            sql = "SELECT Obtained FROM Jotaro WHERE Username =? " # looks for usernames in the jotaro list
            cursor.execute(sql, [(Username)])
            conn.commit()
            myresult = cursor.fetchall()
            if myresult:
                for result in myresult:
                    result1 = result[0]
                    if result1 == 'Yes': #if obtained column is filled with yes implying it has bee bought
                        page.show_frame(Jotaro_List) #this page will be shown
            else:
                page.show_frame(Locked) #if not the page is locked
                

        def K_unlocked(self,page, Username):
            conn=sqlite3.connect('AoC database.db') #connects to database
            with conn:
                cursor=conn.cursor()
            sql = "SELECT Obtained FROM Kakyoin WHERE Username =? " # looks for usernames in the jotaro list
            cursor.execute(sql, [(Username)])
            conn.commit()
            myresult = cursor.fetchall()
            if myresult:
                for result in myresult:
                    result1 = result[0]
                    if result1 == 'Yes': #if obtained column is filled with yes implying it has bee bought
                        page.show_frame(Kakyoin_List) #this page will be shown
            else:
                page.show_frame(Locked) #if not the page is locked
                    
        def P_unlocked(self,page, Username):
            conn=sqlite3.connect('AoC database.db') #connects to database
            with conn:
                cursor=conn.cursor()
            sql = "SELECT Obtained FROM Polnareff WHERE Username =? " # looks for usernames in the jotaro list
            cursor.execute(sql, [(Username)])
            conn.commit()
            myresult = cursor.fetchall()
            if myresult:
                for result in myresult:
                    result1 = result[0]
                    if result1 == 'Yes': #if obtained column is filled with yes implying it has bee bought
                        page.show_frame(Polnareff_List) #this page will be shown
            else:
                page.show_frame(Locked) #if not the page is locked
                    
        def Av_unlocked(self,page, Username):
            conn=sqlite3.connect('AoC database.db') #connects to database
            with conn:
                cursor=conn.cursor()
            sql = "SELECT Obtained FROM Avdol WHERE Username =? " # looks for usernames in the jotaro list
            cursor.execute(sql, [(Username)])
            conn.commit()
            myresult = cursor.fetchall()
            if myresult:
                for result in myresult:
                    result1 = result[0]
                    if result1 == 'Yes': #if obtained column is filled with yes implying it has bee bought
                        page.show_frame(Avdol_List) #this page will be shown
            else:
                page.show_frame(Locked) #if not the page is locked
                    

        def H_unlocked(self,page, Username):
            conn=sqlite3.connect('AoC database.db') #connects to database
            with conn:
                cursor=conn.cursor()
            sql = "SELECT Obtained FROM Hatsune WHERE Username =? " # looks for usernames in the jotaro list
            cursor.execute(sql, [(Username)])
            conn.commit()
            myresult = cursor.fetchall()
            if myresult:
                for result in myresult:
                    result1 = result[0]
                    if result1 == 'Yes': #if obtained column is filled with yes implying it has bee bought
                        page.show_frame(Hatsune_List) #this page will be shown
            else:
                page.show_frame(Locked) #if not the page is locked
                    
        def N_unlocked(self,page, Username):
            conn=sqlite3.connect('AoC database.db') #connects to database
            with conn:
                cursor=conn.cursor()
            sql = "SELECT Obtained FROM Nami WHERE Username =? " # looks for usernames in the jotaro list
            cursor.execute(sql, [(Username)])
            conn.commit()
            myresult = cursor.fetchall()
            if myresult:
                for result in myresult:
                    result1 = result[0]
                    if result1 == 'Yes': #if obtained column is filled with yes implying it has bee bought
                        page.show_frame(Nami_List) #this page will be shown
            else:
                page.show_frame(Locked) #if not the page is locked
                    
                        
            
class Locked(tk.Frame):
        def __init__(self, parent, page): #initialises anything within this function
            tk.Frame.__init__(self,parent)
            self.config(bg=BgColour)
            self.frame=Frame(self,bg=BgColour)
            self.Locked_Des =PhotoImage(file='locked_des.png')
            self.Locked_img = PhotoImage(file='locked.png')
            
            title =Label(self, text ='??????', font= LargeFont, bg=BgColour)
            title.place(x=350, y=10)

            BackBtn = Button(self,text = 'Back', bg=BtnColour,
                             command = lambda: page.show_frame(C_List)) #command takes back to Title pg
            BackBtn.place(x=1, y=1)

            Pic = Label(self, image= self.Locked_img, bg = BgColour)
            Pic.place(x=150, y=120)

            C = Label(self, image = self.Locked_Des , font = MedFont, bg = BgColour)
            C.place(x=500, y=120)           

class Jotaro_List(tk.Frame):
        def __init__(self, parent, page): #initialises anything within this function
            tk.Frame.__init__(self,parent)
            self.config(bg=BgColour)
            self.frame=Frame(self,bg=BgColour)
            self.J_Des =PhotoImage(file='JotaroDescription.png')
            self.J_img = PhotoImage(file='Jotaro_img.png')
            
            title =Label(self, text ='Jotaro Kujo', font= LargeFont, bg=BgColour)
            title.place(x=350, y=10)

            BackBtn = Button(self,text = 'Back', bg=BtnColour,
                             command = lambda: page.show_frame(C_List)) #command takes back to Title pg
            BackBtn.place(x=1, y=1)

            C = Label(self, image = self.J_Des , font = MedFont, bg = BgColour)
            C.place(x=500, y=120)

            Pic = Label(self, image= self.J_img, bg = BgColour)
            Pic.place(x=150, y=120)

            Price= Label(self, text = "Obtained", font = MedFont, bg=BgColour)
            Price.place(x=580, y = 450)

class Kakyoin_List(tk.Frame):
        def __init__(self, parent, page): #initialises anything within this function
            tk.Frame.__init__(self,parent)
            self.config(bg=BgColour)
            self.frame=Frame(self,bg=BgColour)
            self.K_Des =PhotoImage(file='KakyoinDescription.png')
            self.K_img = PhotoImage(file='Kakyoin_img.png')
            
            title =Label(self, text ='Kakyoin Noriaki', font= LargeFont, bg=BgColour)
            title.place(x=350, y=10)

            BackBtn = Button(self,text = 'Back', bg=BtnColour,
                             command = lambda: page.show_frame(C_List)) #command takes back to Title pg
            BackBtn.place(x=1, y=1)

            C = Label(self, image = self.K_Des , font = MedFont, bg = BgColour)
            C.place(x=500, y=120)

            Pic = Label(self, image= self.K_img, bg = BgColour)
            Pic.place(x=150, y=120)

            Price= Label(self, text = "Obtained", font = MedFont, bg=BgColour)
            Price.place(x=580, y = 450)

class Polnareff_List(tk.Frame):
        def __init__(self, parent, page): #initialises anything within this function
            tk.Frame.__init__(self,parent)
            self.config(bg=BgColour)
            self.frame=Frame(self,bg=BgColour)
            self.P_Des =PhotoImage(file='PolnareffDescription.png')
            self.P_img = PhotoImage(file='Polnareff_img.png')
            
            title =Label(self, text ='Jean-Piere Polnareff', font= LargeFont, bg=BgColour)
            title.place(x=280, y=10)

            BackBtn = Button(self,text = 'Back', bg=BtnColour,
                             command = lambda: page.show_frame(C_List)) #command takes back to Title pg
            BackBtn.place(x=1, y=1)

            C = Label(self, image = self.P_Des , font = MedFont, bg = BgColour)
            C.place(x=500, y=120)

            Pic = Label(self, image= self.P_img, bg = BgColour)
            Pic.place(x=150, y=120)

            Price= Label(self, text = "Obtained", font = MedFont, bg=BgColour)
            Price.place(x=580, y = 450)

class Avdol_List(tk.Frame):
        def __init__(self, parent, page): #initialises anything within this function
            tk.Frame.__init__(self,parent)
            self.config(bg=BgColour)
            self.frame=Frame(self,bg=BgColour)
            self.Av_Des =PhotoImage(file='AvdolDescription.png')
            self.Av_img = PhotoImage(file='Avdol_img.png')
            
            title =Label(self, text ='Muhammad Avdol', font= LargeFont, bg=BgColour)
            title.place(x=280, y=10)

            BackBtn = Button(self,text = 'Back', bg=BtnColour,
                             command = lambda: page.show_frame(C_List)) #command takes back to Title pg
            BackBtn.place(x=1, y=1)

            C = Label(self, image = self.Av_Des , font = MedFont, bg = BgColour)
            C.place(x=500, y=120)

            Pic = Label(self, image= self.Av_img, bg = BgColour)
            Pic.place(x=150, y=120)

            Price= Label(self, text = "Obtained", font = MedFont, bg=BgColour)
            Price.place(x=580, y = 450)

class Hatsune_List(tk.Frame):
        def __init__(self, parent, page): #initialises anything within this function
            tk.Frame.__init__(self,parent)
            self.config(bg=BgColour)
            self.frame=Frame(self,bg=BgColour)
            self.H_Des =PhotoImage(file='HatsuneDescription.png')
            self.H_img = PhotoImage(file='Hatsune_img.png')
            
            title =Label(self, text ='Hatsune Miku', font= LargeFont, bg=BgColour)
            title.place(x=280, y=10)

            BackBtn = Button(self,text = 'Back', bg=BtnColour,
                             command = lambda: page.show_frame(C_List)) #command takes back to Title pg
            BackBtn.place(x=1, y=1)

            C = Label(self, image = self.H_Des , font = MedFont, bg = BgColour)
            C.place(x=500, y=120)

            Pic = Label(self, image= self.H_img, bg = BgColour)
            Pic.place(x=150, y=120)

            Price= Label(self, text = "Obtained", font = MedFont, bg=BgColour)
            Price.place(x=580, y = 450)

class Nami_List(tk.Frame):
        def __init__(self, parent, page): #initialises anything within this function
            tk.Frame.__init__(self,parent)
            self.config(bg=BgColour)
            self.frame=Frame(self,bg=BgColour)
            self.N_Des =PhotoImage(file='NamiDescription.png')
            self.N_img = PhotoImage(file='Nami_img.png')
            
            title =Label(self, text ='Nami', font= LargeFont, bg=BgColour)
            title.place(x=280, y=10)

            BackBtn = Button(self,text = 'Back', bg=BtnColour,
                             command = lambda: page.show_frame(C_List)) #command takes back to Title pg
            BackBtn.place(x=1, y=1)

            C = Label(self, image = self.N_Des , font = MedFont, bg = BgColour)
            C.place(x=500, y=120)

            Pic = Label(self, image= self.N_img, bg = BgColour)
            Pic.place(x=150, y=120)

            Price= Label(self, text = "Obtained", font = MedFont, bg=BgColour)
            Price.place(x=580, y = 450)
            
class Jotaro_Buy(tk.Frame):
        def __init__(self, parent, page): #initialises anything within this function
            tk.Frame.__init__(self,parent)
            self.config(bg=BgColour)
            self.frame=Frame(self,bg=BgColour)
            self.J_Des =PhotoImage(file='JotaroDescription.png')
            self.J_img = PhotoImage(file='Jotaro_img.png')
            
            title =Label(self, text ='Jotaro Kujo', font= LargeFont, bg=BgColour)
            title.place(x=350, y=10)

            BackBtn = Button(self,text = 'Back', bg=BtnColour,
                             command = lambda: page.show_frame(Shop)) #command takes back to Title pg
            BackBtn.place(x=1, y=1)

            C = Label(self, image = self.J_Des , font = MedFont, bg = BgColour)
            C.place(x=500, y=120)

            Pic = Label(self, image= self.J_img, bg = BgColour)
            Pic.place(x=150, y=120)

            Price= Label(self, text = "$150000", font = MedFont, bg=BgColour)
            Price.place(x=580, y = 450)

            BuyBtn = Button(self, text = 'Buy', bg = BtnColour, font = ButtonFont1,
                            command = lambda: self.bought(page, Username2.get()))
            BuyBtn.place(x=600, y=400)

        def bought(self,page,Username):
            conn=sqlite3.connect('AoC database.db') #connects to database
            with conn:
                cursor=conn.cursor()
            sql = "SELECT Coins FROM bank WHERE Username =? " # looks for usernames in the jotaro list
            cursor.execute(sql, [(Username)])
            conn.commit()
            myresult = cursor.fetchall()
            for result in myresult:
                coins = result[0]
                if coins >= 150000: #checks if user has more or an equal no. of coins
                    NewCoins = coins-150000
                    success = "Yes"
                    sql2 = "DELETE FROM bank WHERE Username = ?"#deletes the previous entry with the same username
                    sql3 = "INSERT INTO bank (Username, Coins) VALUES(?,?)" #adds new entry with new value of coins
                    sql4 = "INSERT INTO Jotaro (Username, Obtained) VALUES(?, ?)"
                    cursor.execute(sql2,[(Username)])
                    cursor.execute(sql3,[(Username), (NewCoins)])
                    cursor.execute(sql4,[(Username),(success)])
                    conn.commit()
                    messagebox.showinfo("Bought", "Character Purchased")
                    page.show_frame(Shop)
                else:
                      messagebox.showinfo("Error", "Not enough coins")                             

class Kakyoin_Buy(tk.Frame):
        def __init__(self, parent, page): #initialises anything within this function
            tk.Frame.__init__(self,parent)
            self.config(bg=BgColour)
            self.frame=Frame(self,bg=BgColour)
            self.K_Des =PhotoImage(file='KakyoinDescription.png')
            self.K_img = PhotoImage(file='Kakyoin_img.png')
            
            title =Label(self, text ='Kakyoin Noriaki', font= LargeFont, bg=BgColour)
            title.place(x=350, y=10)

            BackBtn = Button(self,text = 'Back', bg=BtnColour,
                             command = lambda: page.show_frame(Shop)) #command takes back to Title pg
            BackBtn.place(x=1, y=1)

            C = Label(self, image = self.K_Des , font = MedFont, bg = BgColour)
            C.place(x=500, y=120)

            Pic = Label(self, image= self.K_img, bg = BgColour)
            Pic.place(x=150, y=120)

            Price= Label(self, text = "$10000", font = MedFont, bg=BgColour)
            Price.place(x=580, y = 450)

            BuyBtn = Button(self, text = 'Buy', bg = BtnColour, font = ButtonFont1,
                            command = lambda: self.bought(page, Username2.get()))
            BuyBtn.place(x=600, y=400)

        def bought(self,page,Username):
            conn=sqlite3.connect('AoC database.db') #connects to database
            with conn:
                cursor=conn.cursor()
            sql = "SELECT Coins FROM bank WHERE Username =? " # looks for usernames in the jotaro list
            cursor.execute(sql, [(Username)])
            conn.commit()
            myresult = cursor.fetchall()
            for result in myresult:
                coins = result[0]
                if coins >= 10000: #checks if user has more or an equal no. of coins
                    NewCoins = coins-10000
                    success = "Yes"
                    sql2 = "DELETE FROM bank WHERE Username = ?"#deletes the previous entry with the same username
                    sql3 = "INSERT INTO bank (Username, Coins) VALUES(?,?)" #adds new entry with new value of coins
                    sql4 = "INSERT INTO Kakyoin (Username, Obtained) VALUES(?, ?)"
                    cursor.execute(sql2,[(Username)])
                    cursor.execute(sql3,[(Username), (NewCoins)])
                    cursor.execute(sql4,[(Username),(success)])
                    conn.commit()
                    messagebox.showinfo("Bought", "Character Purchased")
                    page.show_frame(Shop)
                else:
                    messagebox.showinfo("Error", "Not enough coins")                    

class Polnareff_Buy(tk.Frame):
        def __init__(self, parent, page): #initialises anything within this function
            tk.Frame.__init__(self,parent)
            self.config(bg=BgColour)
            self.frame=Frame(self,bg=BgColour)
            self.P_Des =PhotoImage(file='PolnareffDescription.png')
            self.P_img = PhotoImage(file='Polnareff_img.png')
            
            title =Label(self, text ='Jean-Piere Polnareff', font= LargeFont, bg=BgColour)
            title.place(x=280, y=10)

            BackBtn = Button(self,text = 'Back', bg=BtnColour,
                             command = lambda: page.show_frame(Shop)) #command takes back to Title pg
            BackBtn.place(x=1, y=1)

            C = Label(self, image = self.P_Des , font = MedFont, bg = BgColour)
            C.place(x=500, y=120)

            Pic = Label(self, image= self.P_img, bg = BgColour)
            Pic.place(x=150, y=120)

            Price= Label(self, text = "$12000", font = MedFont, bg=BgColour)
            Price.place(x=580, y = 450)

            BuyBtn = Button(self, text = 'Buy', bg = BtnColour, font = ButtonFont1,
                            command = lambda: self.bought(page, Username2.get()))
            BuyBtn.place(x=600, y=400)

        def bought(self,page,Username):
            conn=sqlite3.connect('AoC database.db') #connects to database
            with conn:
                cursor=conn.cursor()
            sql = "SELECT Coins FROM bank WHERE Username =? " # looks for usernames in the jotaro list
            cursor.execute(sql, [(Username)])
            conn.commit()
            myresult = cursor.fetchall()
            for result in myresult:
                coins = result[0]
                if coins >= 12000: #checks if user has more or an equal no. of coins
                    NewCoins = coins-12000
                    success = "Yes"
                    sql2 = "DELETE FROM bank WHERE Username = ?"#deletes the previous entry with the same username
                    sql3 = "INSERT INTO bank (Username, Coins) VALUES(?,?)" #adds new entry with new value of coins
                    sql4 = "INSERT INTO Polnareff (Username, Obtained) VALUES(?, ?)"
                    cursor.execute(sql2,[(Username)])
                    cursor.execute(sql3,[(Username), (NewCoins)])
                    cursor.execute(sql4,[(Username),(success)])
                    conn.commit()
                    messagebox.showinfo("Bought", "Character Purchased")
                    page.show_frame(Shop)
                else:
                    messagebox.showinfo("Error", "Not enough coins")   
                    
class Avdol_Buy(tk.Frame):
        def __init__(self, parent, page): #initialises anything within this function
            tk.Frame.__init__(self,parent)
            self.config(bg=BgColour)
            self.frame=Frame(self,bg=BgColour)
            self.Av_Des =PhotoImage(file='AvdolDescription.png')
            self.Av_img = PhotoImage(file='Avdol_img.png')
            
            title =Label(self, text ='Muhammad Avdol', font= LargeFont, bg=BgColour)
            title.place(x=280, y=10)

            BackBtn = Button(self,text = 'Back', bg=BtnColour,
                             command = lambda: page.show_frame(Shop)) #command takes back to Title pg
            BackBtn.place(x=1, y=1)

            C = Label(self, image = self.Av_Des , font = MedFont, bg = BgColour)
            C.place(x=500, y=120)

            Pic = Label(self, image= self.Av_img, bg = BgColour)
            Pic.place(x=150, y=120)

            Price= Label(self, text = "$10500", font = MedFont, bg=BgColour)
            Price.place(x=580, y = 450)

            BuyBtn = Button(self, text = 'Buy', bg = BtnColour, font = ButtonFont1,
                            command = lambda: self.bought(page, Username2.get()))
            BuyBtn.place(x=600, y=400)

        def bought(self,page,Username):
            conn=sqlite3.connect('AoC database.db') #connects to database
            with conn:
                cursor=conn.cursor()
            sql = "SELECT Coins FROM bank WHERE Username =? " # looks for usernames in the jotaro list
            cursor.execute(sql, [(Username)])
            conn.commit()
            myresult = cursor.fetchall()
            for result in myresult:
                coins = result[0]
                if coins >= 10500: #checks if user has more or an equal no. of coins
                    NewCoins = coins-10500
                    success = "Yes"
                    sql2 = "DELETE FROM bank WHERE Username = ?"#deletes the previous entry with the same username
                    sql3 = "INSERT INTO bank (Username, Coins) VALUES(?,?)" #adds new entry with new value of coins
                    sql4 = "INSERT INTO Avdol (Username, Obtained) VALUES(?, ?)"
                    cursor.execute(sql2,[(Username)])
                    cursor.execute(sql3,[(Username), (NewCoins)])
                    cursor.execute(sql4,[(Username),(success)])
                    conn.commit()
                    messagebox.showinfo("Bought", "Character Purchased")
                    page.show_frame(Shop)
                else:
                    messagebox.showinfo("Error", "Not enough coins")   

class Hatsune_Buy(tk.Frame):
        def __init__(self, parent, page): #initialises anything within this function
            tk.Frame.__init__(self,parent)
            self.config(bg=BgColour)
            self.frame=Frame(self,bg=BgColour)
            self.H_Des =PhotoImage(file='HatsuneDescription.png')
            self.H_img = PhotoImage(file='Hatsune_img.png')
            
            title =Label(self, text ='Hatsune Miku', font= LargeFont, bg=BgColour)
            title.place(x=280, y=10)

            BackBtn = Button(self,text = 'Back', bg=BtnColour,
                             command = lambda: page.show_frame(Shop)) #command takes back to Title pg
            BackBtn.place(x=1, y=1)

            C = Label(self, image = self.H_Des , font = MedFont, bg = BgColour)
            C.place(x=500, y=120)

            Pic = Label(self, image= self.H_img, bg = BgColour)
            Pic.place(x=150, y=120)

            Price= Label(self, text = "$14000", font = MedFont, bg=BgColour)
            Price.place(x=580, y = 450)

            BuyBtn = Button(self, text = 'Buy', bg = BtnColour, font = ButtonFont1,
                            command = lambda: self.bought(page, Username2.get()))
            BuyBtn.place(x=600, y=400)

        def bought(self,page,Username):
            conn=sqlite3.connect('AoC database.db') #connects to database
            with conn:
                cursor=conn.cursor()
            sql = "SELECT Coins FROM bank WHERE Username =? " # looks for usernames in the jotaro list
            cursor.execute(sql, [(Username)])
            conn.commit()
            myresult = cursor.fetchall()
            for result in myresult:
                coins = result[0]
                if coins >= 14000: #checks if user has more or an equal no. of coins
                    NewCoins = coins-14000
                    success = "Yes"
                    sql2 = "DELETE FROM bank WHERE Username = ?"#deletes the previous entry with the same username
                    sql3 = "INSERT INTO bank (Username, Coins) VALUES(?,?)" #adds new entry with new value of coins
                    sql4 = "INSERT INTO Hatsune (Username, Obtained) VALUES(?, ?)"
                    cursor.execute(sql2,[(Username)])
                    cursor.execute(sql3,[(Username), (NewCoins)])
                    cursor.execute(sql4,[(Username),(success)])
                    conn.commit()
                    messagebox.showinfo("Bought", "Character Purchased")
                    page.show_frame(Shop)
                else:
                    messagebox.showinfo("Error", "Not enough coins")   
                    
class Nami_Buy(tk.Frame):
        def __init__(self, parent, page): #initialises anything within this function
            tk.Frame.__init__(self,parent)
            self.config(bg=BgColour)
            self.frame=Frame(self,bg=BgColour)
            self.N_Des =PhotoImage(file='NamiDescription.png')
            self.N_img = PhotoImage(file='Nami_img.png')
            
            title =Label(self, text ='Nami', font= LargeFont, bg=BgColour)
            title.place(x=280, y=10)

            BackBtn = Button(self,text = 'Back', bg=BtnColour,
                             command = lambda: page.show_frame(Shop)) #command takes back to Title pg
            BackBtn.place(x=1, y=1)

            C = Label(self, image = self.N_Des , font = MedFont, bg = BgColour)
            C.place(x=500, y=120)

            Pic = Label(self, image= self.N_img, bg = BgColour)
            Pic.place(x=150, y=120)

            Price= Label(self, text = "$200000", font = MedFont, bg=BgColour)
            Price.place(x=580, y = 450)

            BuyBtn = Button(self, text = 'Buy', bg = BtnColour, font = ButtonFont1,
                            command = lambda: self.bought(page, Username2.get()))
            BuyBtn.place(x=600, y=400)    
                    
        def bought(self,page,Username):
            conn=sqlite3.connect('AoC database.db') #connects to database
            with conn:
                cursor=conn.cursor()
            sql = "SELECT Coins FROM bank WHERE Username =? " # looks for usernames in the jotaro list
            cursor.execute(sql, [(Username)])
            conn.commit()
            myresult = cursor.fetchall()
            for result in myresult:
                coins = result[0]
                if coins >= 200000: #checks if user has more or an equal no. of coins
                    NewCoins = coins-200000
                    success = "Yes"
                    sql2 = "DELETE FROM bank WHERE Username = ?"#deletes the previous entry with the same username
                    sql3 = "INSERT INTO bank (Username, Coins) VALUES(?,?)" #adds new entry with new value of coins
                    sql4 = "INSERT INTO Nami (Username, Obtained) VALUES(?, ?)"
                    cursor.execute(sql2,[(Username)])
                    cursor.execute(sql3,[(Username), (NewCoins)])
                    cursor.execute(sql4,[(Username),(success)])
                    conn.commit()
                    messagebox.showinfo("Bought", "Character Purchased")
                    page.show_frame(Shop)
                else:
                    messagebox.showinfo("Error", "Not enough coins")       


         
      

        

        


start = AoC()
start.mainloop()
