from tkinter import *
from tkinter import ttk
import sqlite3
from time import time,ctime,sleep

class Home():
    def __init__(self, master):
        self.master = master
        self.master.title("Taxi And Minibus")
        self.master.configure(background='turquoise3')
        
        # Creating Database
        self.createCustomerTable("main.db")
        self.createLoginTable("main.db")
        self.createBookingsTable("main.db")
        self.createVehicleTable("main.db")
        self.createStaffTable("main.db")
        self.createTimeTable("main.db")

        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)
        

        # 'Home' Page Buttons
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=3)
        Button(self.master,text='Login',command=self.login,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=0)
        Button(self.master,text='About',command=self.about,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=2)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=4)


    # Quit Program
    def end(self):
        quit()
    
    # Toggling full screen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state 
        self.master.attributes("-fullscreen", self.state)
        return "break"
    def end_fullscreen(self, event=None):
        self.state = False
        self.master.attributes("-fullscreen", False)
        return "break"
    
    # Initializing New Windows
    def login(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=loginWindow(root2)
    
    def about(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=aboutWindow(root2)


    # Finding The Databases
    def getTables(self,dbName):
        db =sqlite3.connect(dbName)
        cursor = db.cursor()
        sql =  "SELECT name FROM sqlite_master WHERE type='table'"
        cursor.execute(sql)
        names = [row[0] for row in cursor.fetchall()]
        return names

    # Creating Customer Database Or Checking If It Exist
    def createCustomerTable(self,dbName):
        if 'Customer' in self.getTables(dbName):
            pass
        else:
            with sqlite3.connect(dbName) as db:
                cursor=db.cursor()
                sql ="""CREATE TABLE Customer(
                    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Forename TEXT NOT NULL,
                    Surname TEXT NOT NULL,
                    Email TEXT NOT NULL,
                    MobileNum INTEGER NOT NULL,
                    StreetNum INTEGER NOT NULL,
                    StreetName TEXT NOT NULL,
                    Town TEXT NOT NULL,
                    Postcode TEXT NOT NULL)
                    """
                cursor.execute(sql)
                db.commit()
                print("---------------------------------------------\nCustomer Table Created")
                # Adding Fake Data For Testing
                sql="""INSERT into Customer(Forename,Surname,Email,MobileNum,StreetNum,StreetName,Town,Postcode)
                    VALUES("Dummy","McDummy","dummy@example.com",0161,10,"Downing Street","London","SW1A 2AA")"""
                cursor.execute(sql)
                sql="""INSERT into Customer(Forename,Surname,Email,MobileNum,StreetNum,StreetName,Town,Postcode)
                    VALUES("Jimmy","Newtron","scientist@example.com",01282524084,436,"Briercliffe Road","Burnley","BB10 2HA")"""
                cursor.execute(sql)
                db.commit()
                sql="""INSERT into Customer(Forename,Surname,Email,MobileNum,StreetNum,StreetName,Town,Postcode)
                    VALUES("Joe","King","ma@example.com",01282622067,14,"Southfield Terrace","Colne","BB8 7JA")"""
                cursor.execute(sql)
                db.commit()
                print("~~Test Customers Created~~")
    
    # Creating Login Database Or Checking If It Exist
    def createLoginTable(self,dbName):
        if 'Login' in self.getTables(dbName):
            pass
        else:
            with sqlite3.connect(dbName) as db:
                cursor=db.cursor()
                sql ="""CREATE TABLE Login(
                    StaffEmail TEXT NOT NULL,
                    StaffPassword TEXT NOT NULL)"""
                cursor.execute(sql)
                db.commit()
                print("Login Table Created")
                # Adding Fake Data For Testing
                sql ="""INSERT into Login(StaffEmail,StaffPassword)
                    VALUES("test@example.com","Bean")"""
                cursor.execute(sql)
                db.commit()
                sql ="""INSERT into Login(StaffEmail,StaffPassword)
                    VALUES("staff@hypothetical.com","password")"""
                cursor.execute(sql)
                db.commit()
                print("~~Test Logins Created~~")
    
    # Creating Bookings Database Or Checking If It Exist
    def createBookingsTable(self,dbName):
        if 'Bookings' in self.getTables(dbName):
            pass
        else:
            with sqlite3.connect(dbName) as db:
                cursor=db.cursor()
                sql ="""CREATE TABLE Bookings(
                    BookingsID INTEGER PRIMARY KEY AUTOINCREMENT,
                    CustomerID INTEGER NOT NULL,
                    Start TEXT NOT NULL,
                    Destination TEXT NOT NULL,
                    AmountPaid INTEGER NOT NULL,
                    Fufilled TEXT NOT NULL,
                    Date TEXT NOT NULL,
                    Time TEXT NOT NULL,
                    VehicleID INTEGER NOT NULL)"""
                cursor.execute(sql)
                db.commit()
                print("Bookings Table Created")
                # Adding Fake Data For Testing
                sql ="""INSERT into Bookings(CustomerID,Start,Destinantion,AmountPaid,Fufilled,Date,Time,VehicleID)
                    VALUES(1,"Downing Street, SW1A 2AA","Barnes Holme, BB3 3NZ",60,"True","09/07/2016","07:30",1)"""
                cursor.execute(sql)
                db.commit()
                sql ="""INSERT into Bookings(CustomerID,Start,Destinantion,AmountPaid,Fufilled,Date,Time,VehicleID)
                    VALUES(2,"Briercliffe Road, BB10 2HA","Snape Street, BB3 1EN",25,"True","11/11/2017","11:45",2)"""
                cursor.execute(sql)
                db.commit()
                sql ="""INSERT into Bookings(CustomerID,Start,Destinantion,AmountPaid,Fufilled,Date,Time,VehicleID)
                    VALUES(3,"Southfield Terrace, BB8 7JA","Pendle Drive, BB2 3DT",40,"True","23/12/2017","06:00",2)"""
                cursor.execute(sql)
                db.commit()
                print("~~Test Bookings Created~~")
    
    # Creating Vehicle Database Or Checking If It Exist
    def createVehicleTable(self,dbName):
        if 'Vehicle' in self.getTables(dbName):
            pass
        else:
            with sqlite3.connect(dbName) as db:
                cursor=db.cursor()
                sql ="""CREATE TABLE Vehicle(
                    VehicleID INTEGER PRIMARY KEY AUTOINCREMENT,
                    MOT TEXT NOT NULL,
                    Mileage INTEGER NOT NULL,
                    Seats INTEGER NOT NULL,
                    Make TEXT NOT NULL,
                    Availability TEXT NOT NULL,
                    StaffID  INTEGER NOT NULL)"""
                cursor.execute(sql)
                db.commit()
                print("Vehicle Table Created")
                # Adding Fake Data For Testing
                sql ="""INSERT into Vehicle(MOT,Mileage,Seats,Make,Availability,StaffID)
                    VALUES("16/02/2020",3376,5,"TX4","Available",1)"""
                cursor.execute(sql)
                db.commit()
                sql ="""INSERT into Vehicle(MOT,Mileage,Seats,Make,Availability,StaffID)
                    VALUES("04/08/2020",1943,6,"TXE","Available",2)"""
                cursor.execute(sql)
                db.commit()
                print("~~Test Vehicles Created~~")
    
    # Creating Staff Database Or Checking If It Exist
    def createStaffTable(self,dbName):
        if 'Staff' in self.getTables(dbName):
            pass
        else:
            with sqlite3.connect(dbName) as db:
                cursor=db.cursor()
                sql ="""CREATE TABLE Staff(
                    StaffID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Forename TEXT NOT NULL,
                    Surname TEXT NOT NULL,
                    Email TEXT NOT NULL,
                    MobileNum INTEGER NOT NULL,
                    Capabilities TEXT NOT NULL,
                    Availability TEXT NOT NULL,
                    StreetNum INTEGER NOT NULL,
                    StreetName TEXT NOT NULL,
                    Town TEXT NOT NULL,
                    Postcode TEXT NOT NULL)"""
                cursor.execute(sql)
                db.commit()
                print("Staff Table Created")
                # Adding Fake Data For Testing
                sql ="""INSERT into Staff(Forename,Surname,Email,MobileNum,Capabilities,Availability,StreetNum,StreetName,Town,Postcode)
                    VALUES("John","Baxter","test@example.com","076537875789","Taxi And Minibus","Unavailable",8,"Pendle Street","Nelson","BB9 7NH")"""
                cursor.execute(sql)
                db.commit()
                sql ="""INSERT into Staff(Forename,Surname,Email,MobileNum,Capabilities,Availability,StreetNum,StreetName,Town,Postcode)
                    VALUES("Terry","Johnson","staff@hypothetical.com","079878556408","Taxi","Available",3,"Granby Street","Burnley","BB12 0PP")"""
                cursor.execute(sql)
                db.commit()
                
    # Creating Staff Database Or Checking If It Exist
    def createTimeTable(self,dbName):
        if 'Time' in self.getTables(dbName):
            pass
        else:
            with sqlite3.connect(dbName) as db:
                cursor=db.cursor()
                sql ="""CREATE TABLE Time(
                    TimeID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Email TEXT NOT NULL,
                    LogIn TEXT NOT NULL,
                    LogOut TEXT NOT NULL)
                    """
                cursor.execute(sql)
                db.commit()
                print("---------------------------------------------\Time Table Created")

class aboutWindow():
    def __init__(self, master):
        self.master = master
        self.master.title("About")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)
        
        # About Window Buttons
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
    
        # Text Entry
        Label(self.master,bg='turquoise3',bd=0,font='Bembo',text='uhbjhyvjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjgv',fg='black').grid(row=0,column=3)
        Label(self.master,bg='turquoise3',bd=0,font='Bembo',text='uhbjhyvjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjgv',fg='black').grid(row=1,column=3,pady=20)
    
    # Quit Program
    def end(self):
        quit()
    
    # Toggling full screen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state 
        self.master.attributes("-fullscreen", self.state)
        return "break"
    def end_fullscreen(self, event=None):
        self.state = False
        self.master.attributes("-fullscreen", False)
        return "break"    
    
    # Return To 'Home' Screen
    def back(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=Home(root2)

class loginWindow():
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)
        
        # Login Page Labels
        Label(self.master,text='Email',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=0,pady=10)
        Label(self.master,text='Password',bg='turquoise3',font='Bembo',fg='black').grid(row=3,column=0)
        
        # Entry Page Entry
        self.emailEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.emailEntry.grid(row=2,column=2,pady=10,columnspan=2)
        self.passwordEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35,show = "*")
        self.passwordEntry.grid(row=3,column=2,columnspan=2)

        # Login Page Buttons
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=3)
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=0)
        Button(self.master,text='Login',command=self.checkLogin,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=2)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=4)

        Button(self.master,text='temp bypass',command=self.menu2,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=5)

    
    # Quit Program
    def end(self):
        quit()

    # Toggling full screen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state 
        self.master.attributes("-fullscreen", self.state)
        return "break"
    def end_fullscreen(self, event=None):
        self.state = False
        self.master.attributes("-fullscreen", False)
        return "break"
        
    # Return To 'Home' Screen
    def back(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=Home(root2)
    
    # Connecting To Database To Check Login
    def checkLogin(self):
        email=self.emailEntry.get()
        password=self.passwordEntry.get()
        t = time()
        ct = ctime(t)
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        sql = """SELECT * from Login WHERE StaffEmail= ? AND StaffPassword = ?"""
        cursor.execute(sql,[(email),(password)])
        result=cursor.fetchall()
        if result:
            print("--------------------------------")
            print(ct + "\n" + email + " has logged in")
            print("--------------------------------")
            sql = """INSERT INTO Time(Email,LogIn,LogOut)
                VALUES(?,?,?)"""
            cursor.execute(sql,[(email),(ct),('NULL')])
            db.commit()
            self.menu()
        else:
            print("Login Failed")
            Label(self.master,text='Login Failed',bg='turquoise3',font='Bembo',fg='red').grid(row=2,column=4)

    # Redirecting After Login Page
    def menu(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=menuWindow(root2)
    def menu2(self):
        email=self.emailEntry.get()
        t = time()
        ct = ctime(t)
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        print("--------------------------------")
        print(ct + "\n" + email + " has logged in")
        print("--------------------------------")
        sql = """INSERT INTO Time(Email,LogIn,LogOut)
            VALUES(?,?,?)"""
        cursor.execute(sql,[(email),(ct),('NULL')])
        db.commit()
        
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=menuWindow(root2)

class menuWindow():
    def __init__(self, master):
        self.master = master
        self.master.title("Logged In")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)
        
        # Menu Up Page Buttons
        Button(self.master,text='Log Out',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
        Button(self.master,text='Add',command=self.add_data,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
        Button(self.master,text='Show',command=self.show_data,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=3)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=4)

    # Quit Program
    def end(self):
        t = time()
        ct = ctime(t)
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        print("--------------------------------")
        print(ct + "\n" + "Logged out")
        print("--------------------------------")
        sql = """UPDATE Time
            SET LogOut = ?
            WHERE LogOut = 'NULL'"""
        cursor.execute(sql,[(ct)])
        db.commit()
        
        quit()
    
    # Toggling full screen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state 
        self.master.attributes("-fullscreen", self.state)
        return "break"
    def end_fullscreen(self, event=None):
        self.state = False
        self.master.attributes("-fullscreen", False)
        return "break"
    
    def add_data(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=addWindow(root2)
        
    # Return To Login Screen
    def back(self):
        t = time()
        ct = ctime(t)
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        print("--------------------------------")
        print(ct + "\n" + "Logged out")
        print("--------------------------------")
        sql = """UPDATE Time
            SET LogOut = ?
            WHERE LogOut = 'NULL'"""
        cursor.execute(sql,[(ct)])
        db.commit()
        
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=loginWindow(root2)
        
    def show_data(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=showWindow(root2)

class addWindow():

    def __init__(self, master):
        self.master = master
        self.master.title("Add")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)
        
        # Sign Up Page Buttons
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
        
        Button(self.master,text='Add Customer',command=self.add_customer,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=0)
        Button(self.master,text='Add Login',command=self.add_login,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=1)
        Button(self.master,text='Add Booking',command=self.add_booking,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=2)
        Button(self.master,text='Add Vehicle',command=self.add_vehicle,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=3)
        Button(self.master,text='Add Staff',command=self.add_staff,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=4)


    # Quit Program
    def end(self):
        t = time()
        ct = ctime(t)
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        print("--------------------------------")
        print(ct + "\n" + "Logged out")
        print("--------------------------------")
        sql = """UPDATE Time
            SET LogOut = ?
            WHERE LogOut = 'NULL'"""
        cursor.execute(sql,[(ct)])
        db.commit()
        
        quit()
    
    # Toggling full screen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state 
        self.master.attributes("-fullscreen", self.state)
        return "break"
    def end_fullscreen(self, event=None):
        self.state = False
        self.master.attributes("-fullscreen", False)
        return "break"
    
    # Return To 'Home' Screen
    def back(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=menuWindow(root2)
        
        
    def add_customer(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=new_customer(root2)
    
    def add_login(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=new_login(root2)
    
    def add_booking(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=new_booking(root2)
    
    def add_vehicle(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=new_vehicle(root2)
    
    def add_staff(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=new_staff(root2)

class showWindow():
    def __init__(self, master):
        self.master = master
        self.master.title("Show")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)
        
        # Sign Up Page Buttons
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
        
        Button(self.master,text='Show Customer',command=self.show_customer,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=0)
        Button(self.master,text='Show Login',command=self.show_login,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=1)
        Button(self.master,text='Show Booking',command=self.show_booking,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=2)
        Button(self.master,text='Show Vehicle',command=self.show_vehicle,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=3)
        Button(self.master,text='Show Staff',command=self.show_staff,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=4)
        Button(self.master,text='Show Logs',command=self.show_logs,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=5)


    # Quit Program
    def end(self):
        t = time()
        ct = ctime(t)
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        print("--------------------------------")
        print(ct + "\n" + "Logged out")
        print("--------------------------------")
        sql = """UPDATE Time
            SET LogOut = ?
            WHERE LogOut = 'NULL'"""
        cursor.execute(sql,[(ct)])
        db.commit()
        
        quit()
    
    # Toggling full screen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state 
        self.master.attributes("-fullscreen", self.state)
        return "break"
    def end_fullscreen(self, event=None):
        self.state = False
        self.master.attributes("-fullscreen", False)
        return "break"
    
    # Return To 'Home' Screen
    def back(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=menuWindow(root2)
        
        
    def show_customer(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=display_customer(root2)
    
    def show_login(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=display_login(root2)
    
    def show_booking(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=display_booking(root2)
    
    def show_vehicle(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=display_vehicle(root2)
    
    def show_staff(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=display_staff(root2)
        
    def show_logs(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=display_logs(root2)

################################################################################################
################################################################################################
class display_customer():
    def __init__(self, master):
        self.master = master
        self.master.title("Show Customer")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)
        
        # New_Customer Window Buttons
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
        Button(self.master,text='Find',command=self.findData,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=3)
        Button(self.master,text='Clear',command=self.clear,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=4)


    # New Customer Label
        Label(self.master,text='Forename',bg='turquoise3',font='Bembo',fg='black').grid(row=1,column=0,pady=10)
        Label(self.master,text='Surname',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=0,pady=10)
        Label(self.master,text='Email',bg='turquoise3',font='Bembo',fg='black').grid(row=3,column=0,pady=10)
        Label(self.master,text='Mobile Number',bg='turquoise3',font='Bembo',fg='black').grid(row=4,column=0,pady=10)
        Label(self.master,text='Street Number',bg='turquoise3',font='Bembo',fg='black').grid(row=5,column=0,pady=10)
        Label(self.master,text='Street Name',bg='turquoise3',font='Bembo',fg='black').grid(row=6,column=0,pady=10)
        Label(self.master,text='Town',bg='turquoise3',font='Bembo',fg='black').grid(row=7,column=0,pady=10)
        Label(self.master,text='Postcode',bg='turquoise3',font='Bembo',fg='black').grid(row=8,column=0,pady=10)
        Label(self.master,text='Customer ID',bg='turquoise3',font='Bembo',fg='black').grid(row=9,column=0,pady=10)
        
    # Creating TreeView
        table=ttk.Treeview(self)
        table['columns']=("CustomerID","Forename","Surname","Email","MobileNum","StreetNum","StreetName","Town","Postcode")
        table.column("#0",width=0,minwidth=0)
        table.column("CustomerID",width=120,minwidth=25,anchor=CENTER)
        table.column("Forename",width=120,minwidth=25,anchor=W)
        table.column("Surname",width=120,minwidth=25,anchor=W)
        table.column("Email",width=120,minwidth=25,anchor=W)
        table.column("MobileNum",width=120,minwidth=25,anchor=W)
        table.column("StreetName",width=120,minwidth=25,anchor=W)
        table.column("Town",width=120,minwidth=25,anchor=W)
        table.column("Postcode",width=120,minwidth=25,anchor=W)

        table.heading("#0",text="Label",anchor=W)
        table.heading("CustomerID",text="CustomerID",anchor=CENTER)
        table.heading("Forename",text="Forename",anchor=W)
        table.heading("Surname",text="Surname",anchor=W)
        table.heading("Email",text="Email",anchor=W)
        table.heading("MobileNum",text="MobileNum",anchor=W)
        table.heading("StreetName",text="StreetName",anchor=W)
        table.heading("Town",text="Town",anchor=W)
        table.heading("Postcode",text="Postcode",anchor=W)
        
    # New Customer Entry
        self.forenameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.forenameEntry.grid(row=1,column=1,pady=10,columnspan=2)
        
        self.surnameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.surnameEntry.grid(row=2,column=1,pady=10,columnspan=2)
        
        self.emailEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.emailEntry.grid(row=3,column=1,pady=10,columnspan=2)
        
        self.mobileEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.mobileEntry.grid(row=4,column=1,pady=10,columnspan=2)
        
        self.streetNumEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.streetNumEntry.grid(row=5,column=1,pady=10,columnspan=2)
        
        self.streetNameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.streetNameEntry.grid(row=6,column=1,pady=10,columnspan=2)
        
        self.townEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.townEntry.grid(row=7,column=1,pady=10,columnspan=2)
        
        self.postcodeEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.postcodeEntry.grid(row=8,column=1,pady=10,columnspan=2)
        
        self.idEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.idEntry.grid(row=9,column=1,pady=10,columnspan=2)

    
    # Quit Program
    def end(self):
        t = time()
        ct = ctime(t)
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        print("--------------------------------")
        print(ct + "\n" + "Logged out")
        print("--------------------------------")
        sql = """UPDATE Time
            SET LogOut = ?
            WHERE LogOut = 'NULL'"""
        cursor.execute(sql,[(ct)])
        db.commit()
        
        quit()
        
    def clear(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=display_customer(root2)
    
    # Toggling full screen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state 
        self.master.attributes("-fullscreen", self.state)
        return "break"
    def end_fullscreen(self, event=None):
        self.state = False
        self.master.attributes("-fullscreen", False)
        return "break"    
    
    # Return To 'Menu' Screen
    def back(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=showWindow(root2)
        
    # Adding To Database
    def findData(self):
        
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=1,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=2,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=3,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=4,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=5,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=6,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=7,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=8,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=9,column=3,columnspan=2)
        
        forename=self.forenameEntry.get()
        surname=self.surnameEntry.get()
        email=self.emailEntry.get()
        mobile=self.mobileEntry.get()
        streetNum=self.streetNumEntry.get()
        streetName=self.streetNameEntry.get()
        town=self.townEntry.get()
        postcode=self.postcodeEntry.get()
        cusID=self.idEntry.get()
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        if len(forename) > 0 or len(surname) > 0 or len(email) > 0 or len(mobile) > 0 or len(streetNum) > 0 or len(streetName) > 0 or len(postcode) > 0 or len(cusID) > 0:
            
            if len(forename) > 0:
                temp=forename
                sql = """SELECT Forename FROM Customer WHERE Forename LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT Surname FROM Customer WHERE Forename LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Email FROM Customer WHERE Forename LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT MobileNum FROM Customer WHERE Forename LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT StreetNum FROM Customer WHERE Forename LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT StreetName FROM Customer WHERE Forename LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT Town FROM Customer WHERE Forename LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT Postcode FROM Customer WHERE Forename LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                    
                sql = """SELECT CustomerID FROM Customer WHERE Forename LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)
            elif len(surname) > 0:
                temp=surname
                sql = """SELECT Forename FROM Customer WHERE Surname LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT Surname FROM Customer WHERE Surname LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Email FROM Customer WHERE Surname LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT MobileNum FROM Customer WHERE Surname LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT StreetNum FROM Customer WHERE Surname LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    la5=Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT StreetName FROM Customer WHERE Surname LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT Town FROM Customer WHERE Surname LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT Postcode FROM Customer WHERE Surname LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                
                sql = """SELECT CustomerID FROM Customer WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)
                    
            elif len(email) > 0:
                temp=email
                sql = """SELECT Forename FROM Customer WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT Surname FROM Customer WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Email FROM Customer WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT MobileNum FROM Customer WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT StreetNum FROM Customer WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT StreetName FROM Customer WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT Town FROM Customer WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT Postcode FROM Customer WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                    
                sql = """SELECT CustomerID FROM Customer WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)
            elif len(mobile) > 0:
                temp=mobile
                sql = """SELECT Forename FROM Customer WHERE MobileNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT Surname FROM Customer WHERE MobileNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Email FROM Customer WHERE MobileNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT MobileNum FROM Customer WHERE MobileNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT StreetNum FROM Customer WHERE MobileNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT StreetName FROM Customer WHERE MobileNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT Town FROM Customer WHERE MobileNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT Postcode FROM Customer WHERE MobileNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                
                sql = """SELECT CustomerID FROM Customer WHERE MobileNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)
            
            elif len(streetNum) > 0:
                temp=streetNum
                sql = """SELECT Forename FROM Customer WHERE StreetNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT Surname FROM Customer WHERE StreetNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Email FROM Customer WHERE StreetNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT MobileNum FROM Customer WHERE StreetNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT StreetNum FROM Customer WHERE StreetNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT StreetName FROM Customer WHERE StreetNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT Town FROM Customer WHERE StreetNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT Postcode FROM Customer WHERE StreetNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                    
                sql = """SELECT CustomerID FROM Customer WHERE StreetNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)
            elif len(streetName) > 0:
                temp=streetName
                sql = """SELECT Forename FROM Customer WHERE StreetName LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT Surname FROM Customer WHERE StreetName LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Email FROM Customer WHERE StreetName LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT MobileNum FROM Customer WHERE StreetName LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT StreetNum FROM Customer WHERE StreetName LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT StreetName FROM Customer WHERE StreetName LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT Town FROM Customer WHERE StreetName LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT Postcode FROM Customer WHERE StreetName LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                    
                sql = """SELECT CustomerID FROM Customer WHERE StreetName LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)

            elif len(town) > 0:
                temp=town
                sql = """SELECT Forename FROM Customer WHERE Town LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT Surname FROM Customer WHERE Town LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Email FROM Customer WHERE Town LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT MobileNum FROM Customer WHERE Town LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT StreetNum FROM Customer WHERE Town LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT StreetName FROM Customer WHERE Town LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT Town FROM Customer WHERE Town LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT Postcode FROM Customer WHERE Town LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                    
                sql = """SELECT CustomerID FROM Customer WHERE Town LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)
            elif len(postcode) > 0:
                temp=postcode
                sql = """SELECT Forename FROM Customer WHERE Postcode LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT Surname FROM Customer WHERE Postcode LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Email FROM Customer WHERE Postcode LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT MobileNum FROM Customer WHERE Postcode LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT StreetNum FROM Customer WHERE Postcode LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT StreetName FROM Customer WHERE Postcode LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT Town FROM Customer WHERE Postcode LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT Postcode FROM Customer WHERE Postcode LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                    
                sql = """SELECT CustomerID FROM Customer WHERE Postcode LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)
                    
            elif len(cusID) > 0:
                temp=cusID
                sql = """SELECT Forename FROM Customer WHERE CustomerID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT Surname FROM Customer WHERE CustomerID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Email FROM Customer WHERE CustomerID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT MobileNum FROM Customer WHERE CustomerID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT StreetNum FROM Customer WHERE CustomerID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT StreetName FROM Customer WHERE CustomerID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT Town FROM Customer WHERE CustomerID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT Postcode FROM Customer WHERE CustomerID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                    
                sql = """SELECT CustomerID FROM Customer WHERE CustomerID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)

class display_login():
    def __init__(self, master):
        self.master = master
        self.master.title("Show Login")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)
        
        # New_Customer Window Buttons
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
        Button(self.master,text='Find',command=self.findData,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=3)
        Button(self.master,text='Clear',command=self.clear,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=4)


    # New Customer Label
        Label(self.master,text='Email',bg='turquoise3',font='Bembo',fg='black').grid(row=1,column=0,pady=10)
        Label(self.master,text='Password',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=0,pady=10)
        
    # New Customer Entry
        self.emailEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.emailEntry.grid(row=1,column=1,pady=10,columnspan=2)
        
        self.passwordEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.passwordEntry.grid(row=2,column=1,pady=10,columnspan=2)
        
        
    
    # Quit Program
    def end(self):
        t = time()
        ct = ctime(t)
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        print("--------------------------------")
        print(ct + "\n" + "Logged out")
        print("--------------------------------")
        sql = """UPDATE Time
            SET LogOut = ?
            WHERE LogOut = 'NULL'"""
        cursor.execute(sql,[(ct)])
        db.commit()
        
        quit()
        
    def clear(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=display_login(root2)
    
    # Toggling full screen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state 
        self.master.attributes("-fullscreen", self.state)
        return "break"
    def end_fullscreen(self, event=None):
        self.state = False
        self.master.attributes("-fullscreen", False)
        return "break"    
    
    # Return To 'Menu' Screen
    def back(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=showWindow(root2)
        
    # Adding To Database
    def findData(self):
        
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=1,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=2,column=3,columnspan=2)
        
        email=self.emailEntry.get()
        password=self.passwordEntry.get()
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        if len(email) > 0 or len(password) > 0 :
            
            if len(email) > 0:
                temp=email
                sql = """SELECT StaffEmail FROM Login WHERE StaffEmail LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT StaffPassword FROM Login WHERE StaffEmail LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                
            elif len(password) > 0:
                temp=password
                sql = """SELECT StaffEmail FROM Login WHERE StaffPassword LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT StaffPassword FROM Login WHERE StaffPassword LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)

class display_booking():
    def __init__(self, master):
        self.master = master
        self.master.title("Show Booking")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)
        
        # New_Customer Window Buttons
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
        Button(self.master,text='Find',command=self.findData,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=3)
        Button(self.master,text='Clear',command=self.clear,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=4)


    # New Customer Label
        Label(self.master,text='Bookings ID',bg='turquoise3',font='Bembo',fg='black').grid(row=1,column=0,pady=10)
        Label(self.master,text='Customer ID',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=0,pady=10)
        Label(self.master,text='Start',bg='turquoise3',font='Bembo',fg='black').grid(row=3,column=0,pady=10)
        Label(self.master,text='Destination',bg='turquoise3',font='Bembo',fg='black').grid(row=4,column=0,pady=10)
        Label(self.master,text='Amount Paid',bg='turquoise3',font='Bembo',fg='black').grid(row=5,column=0,pady=10)
        Label(self.master,text='Fufilled',bg='turquoise3',font='Bembo',fg='black').grid(row=6,column=0,pady=10)
        Label(self.master,text='Date',bg='turquoise3',font='Bembo',fg='black').grid(row=7,column=0,pady=10)
        Label(self.master,text='Time',bg='turquoise3',font='Bembo',fg='black').grid(row=8,column=0,pady=10)
        Label(self.master,text='Vehicle ID',bg='turquoise3',font='Bembo',fg='black').grid(row=9,column=0,pady=10)


    # New Customer Entry
        self.BookingsIDEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.BookingsIDEntry.grid(row=1,column=1,pady=10,columnspan=2)
        
        self.CustomerIDEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.CustomerIDEntry.grid(row=2,column=1,pady=10,columnspan=2)
        
        self.StartEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.StartEntry.grid(row=3,column=1,pady=10,columnspan=2)
        
        self.DestinationEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.DestinationEntry.grid(row=4,column=1,pady=10,columnspan=2)
        
        self.AmountEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.AmountEntry.grid(row=5,column=1,pady=10,columnspan=2)
        
        self.FufilledEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.FufilledEntry.grid(row=6,column=1,pady=10,columnspan=2)
        
        self.DateEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.DateEntry.grid(row=7,column=1,pady=10,columnspan=2)
        
        self.TimeEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.TimeEntry.grid(row=8,column=1,pady=10,columnspan=2)
        
        self.VehicleIDEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.VehicleIDEntry.grid(row=9,column=1,pady=10,columnspan=2)

    
    # Quit Program
    def end(self):
        t = time()
        ct = ctime(t)
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        print("--------------------------------")
        print(ct + "\n" + "Logged out")
        print("--------------------------------")
        sql = """UPDATE Time
            SET LogOut = ?
            WHERE LogOut = 'NULL'"""
        cursor.execute(sql,[(ct)])
        db.commit()
        
        quit()
        
    def clear(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=display_booking(root2)
    
    # Toggling full screen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state 
        self.master.attributes("-fullscreen", self.state)
        return "break"
    def end_fullscreen(self, event=None):
        self.state = False
        self.master.attributes("-fullscreen", False)
        return "break"    
    
    # Return To 'Menu' Screen
    def back(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=showWindow(root2)
        
    # Adding To Database
    def findData(self):
        
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=1,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=2,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=3,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=4,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=5,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=6,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=7,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=8,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=9,column=3,columnspan=2)
        
        bookingID=self.BookingsIDEntry.get()
        customerID=self.CustomerIDEntry.get()
        start=self.StartEntry.get()
        destination=self.DestinationEntry.get()
        amount=self.AmountEntry.get()
        fufilled=self.FufilledEntry.get()
        date=self.DateEntry.get()
        time=self.TimeEntry.get()
        vehicleID=self.VehicleIDEntry.get()
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        if len(bookingID) > 0 or len(customerID) > 0 or len(start) > 0 or len(destination) > 0 or len(amount) > 0 or len(fufilled) > 0 or len(time) > 0 or len(vehicleID) > 0:
            
            if len(bookingID) > 0:
                temp=bookingID
                sql = """SELECT BookingsID FROM Bookings WHERE BookingsID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT CustomerID FROM Bookings WHERE BookingsID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Start FROM Bookings WHERE BookingsID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT Destinantion FROM Bookings WHERE BookingsID LIKE ?"""   #######spelt wrong on purpose
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT AmountPaid FROM Bookings WHERE BookingsID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Fufilled FROM Bookings WHERE BookingsID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT Date FROM Bookings WHERE BookingsID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT Time FROM Bookings WHERE BookingsID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                    
                sql = """SELECT VehicleID FROM Bookings WHERE BookingsID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)
            elif len(customerID) > 0:
                temp=customerID
                sql = """SELECT BookingsID FROM Bookings WHERE CustomerID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT CustomerID FROM Bookings WHERE CustomerID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Start FROM Bookings WHERE CustomerID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT Destination FROM Bookings WHERE CustomerID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT AmountPaid FROM Bookings WHERE CustomerID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Fufilled FROM Bookings WHERE CustomerID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT Date FROM Bookings WHERE CustomerID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT Time FROM Bookings WHERE CustomerID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                    
                sql = """SELECT VehicleID FROM Bookings WHERE CustomerID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)
            
            elif len(start) > 0:
                temp=start
                sql = """SELECT BookingsID FROM Bookings WHERE Start LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT CustomerID FROM Bookings WHERE Start LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Start FROM Bookings WHERE Start LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT Destination FROM Bookings WHERE Start LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT AmountPaid FROM Bookings WHERE Start LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Fufilled FROM Bookings WHERE Start LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT Date FROM Bookings WHERE Start LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT Time FROM Bookings WHERE Start LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                    
                sql = """SELECT VehicleID FROM Bookings WHERE Start LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)
            elif len(destination) > 0:
                temp=destination
                sql = """SELECT BookingsID FROM Bookings WHERE Destination LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT CustomerID FROM Bookings WHERE Destination LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Start FROM Bookings WHERE Destination LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT Destination FROM Bookings WHERE Destination LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT AmountPaid FROM Bookings WHERE Destination LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Fufilled FROM Bookings WHERE Destination LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT Date FROM Bookings WHERE Destination LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT Time FROM Bookings WHERE Destination LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                    
                sql = """SELECT VehicleID FROM Bookings WHERE Destination LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)
            
            elif len(amount) > 0:
                temp=amount
                sql = """SELECT BookingsID FROM Bookings WHERE AmountPaid LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT CustomerID FROM Bookings WHERE AmountPaid LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Start FROM Bookings WHERE AmountPaid LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT Destination FROM Bookings WHERE AmountPaid LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT AmountPaid FROM Bookings WHERE AmountPaid LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Fufilled FROM Bookings WHERE AmountPaid LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT Date FROM Bookings WHERE AmountPaid LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT Time FROM Bookings WHERE AmountPaid LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                    
                sql = """SELECT VehicleID FROM Bookings WHERE AmountPaid LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)
            elif len(fufilled) > 0:
                temp=fufilled
                sql = """SELECT BookingsID FROM Bookings WHERE Fufilled LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT CustomerID FROM Bookings WHERE Fufilled LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Start FROM Bookings WHERE Fufilled LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT Destination FROM Bookings WHERE Fufilled LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT AmountPaid FROM Bookings WHERE Fufilled LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Fufilled FROM Bookings WHERE Fufilled LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT Date FROM Bookings WHERE Fufilled LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT Time FROM Bookings WHERE Fufilled LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                    
                sql = """SELECT VehicleID FROM Bookings WHERE Fufilled LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)

            elif len(date) > 0:
                temp=date
                sql = """SELECT BookingsID FROM Bookings WHERE Date LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT CustomerID FROM Bookings WHERE Date LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Start FROM Bookings WHERE Date LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT Destination FROM Bookings WHERE Date LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT AmountPaid FROM Bookings WHERE Date LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Fufilled FROM Bookings WHERE Date LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT Date FROM Bookings WHERE Date LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT Time FROM Bookings WHERE Date LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                    
                sql = """SELECT VehicleID FROM Bookings WHERE Date LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)
            elif len(time) > 0:
                temp=time
                sql = """SELECT BookingsID FROM Bookings WHERE Time LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT CustomerID FROM Bookings WHERE Time LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Start FROM Bookings WHERE Time LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT Destination FROM Bookings WHERE Time LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT AmountPaid FROM Bookings WHERE Time LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Fufilled FROM Bookings WHERE Time LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT Date FROM Bookings WHERE Time LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT Time FROM Bookings WHERE Time LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                    
                sql = """SELECT VehicleID FROM Bookings WHERE Time LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)
                    
            elif len(vehicleID) > 0:
                temp=vehicleID
                sql = """SELECT BookingsID FROM Bookings WHERE VehicleID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT CustomerID FROM Bookings WHERE VehicleID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Start FROM Bookings WHERE VehicleID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT Destination FROM Bookings WHERE VehicleID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT AmountPaid FROM Bookings WHERE VehicleID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Fufilled FROM Bookings WHERE VehicleID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT Date FROM Bookings WHERE VehicleID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT Time FROM Bookings WHERE VehicleID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                    
                sql = """SELECT VehicleID FROM Bookings WHERE VehicleID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)

class display_vehicle():
    def __init__(self, master):
        self.master = master
        self.master.title("Show Vehicle")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)
        
        # New_Customer Window Buttons
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
        Button(self.master,text='Find',command=self.findData,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=3)
        Button(self.master,text='Clear',command=self.clear,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=4)


    # New Customer Label
        Label(self.master,text='Vehicle ID',bg='turquoise3',font='Bembo',fg='black').grid(row=1,column=0,pady=10)
        Label(self.master,text='MOT',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=0,pady=10)
        Label(self.master,text='Mileage',bg='turquoise3',font='Bembo',fg='black').grid(row=3,column=0,pady=10)
        Label(self.master,text='Seats',bg='turquoise3',font='Bembo',fg='black').grid(row=4,column=0,pady=10)
        Label(self.master,text='Make',bg='turquoise3',font='Bembo',fg='black').grid(row=5,column=0,pady=10)
        Label(self.master,text='Availability',bg='turquoise3',font='Bembo',fg='black').grid(row=6,column=0,pady=10)
        Label(self.master,text='StaffID',bg='turquoise3',font='Bembo',fg='black').grid(row=7,column=0,pady=10)

    # New Customer Entry
        self.VehicleIDEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.VehicleIDEntry.grid(row=1,column=1,pady=10,columnspan=2)
        
        self.MOTEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.MOTEntry.grid(row=2,column=1,pady=10,columnspan=2)
        
        self.MileageEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.MileageEntry.grid(row=3,column=1,pady=10,columnspan=2)
        
        self.SeatsEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.SeatsEntry.grid(row=4,column=1,pady=10,columnspan=2)
        
        self.MakeEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.MakeEntry.grid(row=5,column=1,pady=10,columnspan=2)
        
        self.AvailabilityEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.AvailabilityEntry.grid(row=6,column=1,pady=10,columnspan=2)
        
        self.StaffIDEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.StaffIDEntry.grid(row=7,column=1,pady=10,columnspan=2)
    
    # Quit Program
    def end(self):
        t = time()
        ct = ctime(t)
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        print("--------------------------------")
        print(ct + "\n" + "Logged out")
        print("--------------------------------")
        sql = """UPDATE Time
            SET LogOut = ?
            WHERE LogOut = 'NULL'"""
        cursor.execute(sql,[(ct)])
        db.commit()
        
        quit()
        
    def clear(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=display_vehicle(root2)
    
    # Toggling full screen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state 
        self.master.attributes("-fullscreen", self.state)
        return "break"
    def end_fullscreen(self, event=None):
        self.state = False
        self.master.attributes("-fullscreen", False)
        return "break"    
    
    # Return To 'Menu' Screen
    def back(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=showWindow(root2)
        
    # Adding To Database
    def findData(self):
        
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=1,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=2,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=3,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=4,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=5,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=6,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=7,column=3,columnspan=2)
        
        vehicleID=self.VehicleIDEntry.get()
        mot=self.MOTEntry.get()
        mileage=self.MileageEntry.get()
        seats=self.SeatsEntry.get()
        make=self.MakeEntry.get()
        availability=self.AvailabilityEntry.get()
        staffID=self.StaffIDEntry.get()
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        if len(vehicleID) > 0 or len(mot) > 0 or len(mileage) > 0 or len(seats) > 0 or len(make) > 0 or len(availability) > 0 or len(staffID) > 0:
            
            if len(vehicleID) > 0:
                temp=vehicleID
                sql = """SELECT VehicleID FROM Vehicle WHERE VehicleID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT MOT FROM Vehicle WHERE VehicleID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Mileage FROM Vehicle WHERE VehicleID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT Seats FROM Vehicle WHERE VehicleID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT Make FROM Vehicle WHERE VehicleID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Availability FROM Vehicle WHERE VehicleID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT StaffID FROM Vehicle WHERE VehicleID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
            elif len(mot) > 0:
                temp=mot
                sql = """SELECT VehicleID FROM Vehicle WHERE MOT LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT MOT FROM Vehicle WHERE MOT LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Mileage FROM Vehicle WHERE MOT LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT Seats FROM Vehicle WHERE MOT LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT Make FROM Vehicle WHERE MOT LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Availability FROM Vehicle WHERE MOT LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT StaffID FROM Vehicle WHERE MOT LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
            
            elif len(mileage) > 0:
                temp=mileage
                sql = """SELECT VehicleID FROM Vehicle WHERE Mileage LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT MOT FROM Vehicle WHERE Mileage LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Mileage FROM Vehicle WHERE Mileage LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT Seats FROM Vehicle WHERE Mileage LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT Make FROM Vehicle WHERE Mileage LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Availability FROM Vehicle WHERE Mileage LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT StaffID FROM Vehicle WHERE Mileage LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
            elif len(seats) > 0:
                temp=seats
                sql = """SELECT VehicleID FROM Vehicle WHERE Seats LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT MOT FROM Vehicle WHERE Seats LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Mileage FROM Vehicle WHERE Seats LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT Seats FROM Vehicle WHERE Seats LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT Make FROM Vehicle WHERE Seats LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Availability FROM Vehicle WHERE Seats LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT StaffID FROM Vehicle WHERE Seats LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
            
            elif len(make) > 0:
                temp=make
                sql = """SELECT VehicleID FROM Vehicle WHERE Make LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT MOT FROM Vehicle WHERE Make LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Mileage FROM Vehicle WHERE Make LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT Seats FROM Vehicle WHERE Make LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT Make FROM Vehicle WHERE Make LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Availability FROM Vehicle WHERE Make LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT StaffID FROM Vehicle WHERE Make LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
            elif len(availability) > 0:
                temp=availability
                sql = """SELECT VehicleID FROM Vehicle WHERE Availability LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT MOT FROM Vehicle WHERE Availability LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Mileage FROM Vehicle WHERE Availability LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT Seats FROM Vehicle WHERE Availability LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT Make FROM Vehicle WHERE Availability LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Availability FROM Vehicle WHERE Availability LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT StaffID FROM Vehicle WHERE Availability LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)

            elif len(staffID) > 0:
                temp=staffID
                sql = """SELECT VehicleID FROM Vehicle WHERE StaffID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT MOT FROM Vehicle WHERE StaffID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Mileage FROM Vehicle WHERE StaffID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT Seats FROM Vehicle WHERE StaffID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
                sql = """SELECT Make FROM Vehicle WHERE StaffID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Availability FROM Vehicle WHERE StaffID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT StaffID FROM Vehicle WHERE StaffID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)

class display_staff():
    def __init__(self, master):
        self.master = master
        self.master.title("Show Staff")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)
        
        # New_Customer Window Buttons
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
        Button(self.master,text='Find',command=self.findData,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=3)
        Button(self.master,text='Clear',command=self.clear,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=4)

    # New Customer Label
        Label(self.master,text='Forename',bg='turquoise3',font='Bembo',fg='black').grid(row=1,column=0,pady=10)
        Label(self.master,text='Surname',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=0,pady=10)
        Label(self.master,text='Email',bg='turquoise3',font='Bembo',fg='black').grid(row=3,column=0,pady=10)
        Label(self.master,text='Mobile Number',bg='turquoise3',font='Bembo',fg='black').grid(row=4,column=0,pady=10)
        Label(self.master,text='Capabilities',bg='turquoise3',font='Bembo',fg='black').grid(row=5,column=0,pady=10)
        Label(self.master,text='Availability',bg='turquoise3',font='Bembo',fg='black').grid(row=6,column=0,pady=10)
        Label(self.master,text='Street Number',bg='turquoise3',font='Bembo',fg='black').grid(row=7,column=0,pady=10)
        Label(self.master,text='Street Name',bg='turquoise3',font='Bembo',fg='black').grid(row=8,column=0,pady=10)
        Label(self.master,text='Town',bg='turquoise3',font='Bembo',fg='black').grid(row=9,column=0,pady=10)
        Label(self.master,text='Postcode',bg='turquoise3',font='Bembo',fg='black').grid(row=10,column=0,pady=10)
        Label(self.master,text='StaffID',bg='turquoise3',font='Bembo',fg='black').grid(row=11,column=0,pady=10)
    
    # New Customer Entry
        self.forenameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.forenameEntry.grid(row=1,column=1,pady=10,columnspan=2)
        
        self.surnameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.surnameEntry.grid(row=2,column=1,pady=10,columnspan=2)
        
        self.EmailEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.EmailEntry.grid(row=3,column=1,pady=10,columnspan=2)
        
        self.mobileEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.mobileEntry.grid(row=4,column=1,pady=10,columnspan=2)
        
        self.CapabilitiesEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.CapabilitiesEntry.grid(row=5,column=1,pady=10,columnspan=2)
        
        self.AvailabilityEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.AvailabilityEntry.grid(row=6,column=1,pady=10,columnspan=2)
        
        self.streetNumEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.streetNumEntry.grid(row=7,column=1,pady=10,columnspan=2)
        
        self.streetNameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.streetNameEntry.grid(row=8,column=1,pady=10,columnspan=2)
        
        self.townEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.townEntry.grid(row=9,column=1,pady=10,columnspan=2)
        
        self.postcodeEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.postcodeEntry.grid(row=10,column=1,pady=10,columnspan=2)
        
        self.staffIDEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.staffIDEntry.grid(row=11,column=1,pady=10,columnspan=2)

    
    
    # Quit Program
    def end(self):
        t = time()
        ct = ctime(t)
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        print("--------------------------------")
        print(ct + "\n" + "Logged out")
        print("--------------------------------")
        sql = """UPDATE Time
            SET LogOut = ?
            WHERE LogOut = 'NULL'"""
        cursor.execute(sql,[(ct)])
        db.commit()
        
        quit()
        
    def clear(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=display_staff(root2)
    
    # Toggling full screen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state 
        self.master.attributes("-fullscreen", self.state)
        return "break"
    def end_fullscreen(self, event=None):
        self.state = False
        self.master.attributes("-fullscreen", False)
        return "break"    
    
    # Return To 'Menu' Screen
    def back(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=showWindow(root2)
        
    # Adding To Database
    def findData(self):
        
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=1,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=2,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=3,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=4,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=5,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=6,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=7,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=8,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=9,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=10,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=11,column=3,columnspan=2)

        forename=self.forenameEntry.get()
        surname=self.surnameEntry.get()
        email=self.EmailEntry.get()
        capability=self.CapabilitiesEntry.get()
        availability=self.AvailabilityEntry.get()
        mobile=self.mobileEntry.get()
        streetNum=self.streetNumEntry.get()
        streetName=self.streetNameEntry.get()
        town=self.townEntry.get()
        postcode=self.postcodeEntry.get()
        staffID=self.staffIDEntry.get()
        
        if len(forename) > 0 or len(surname) > 0 or len(email) > 0 or len(capability) > 0 or len(availability) > 0 or len(mobile) > 0 or len(streetNum) > 0 or len(streetName) > 0 or len(town) > 0 or len(postcode) > 0 or len(staffID) > 0:
            
            db =sqlite3.connect("main.db")
            cursor = db.cursor()
            if len(forename) > 0:
                temp=forename
                sql = """SELECT Forename FROM Staff WHERE Forename LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT Surname FROM Staff WHERE Forename LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Email FROM Staff WHERE Forename LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT MobileNum FROM Staff WHERE Forename LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                    
                sql = """SELECT Capabilities FROM Staff WHERE Forename LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Availability FROM Staff WHERE Forename LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT StreetNum FROM Staff WHERE Forename LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT StreetName FROM Staff WHERE Forename LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                
                sql = """SELECT Town FROM Staff WHERE Forename LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)
                
                sql = """SELECT Postcode FROM Staff WHERE Forename LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=10,column=3,columnspan=2)
                
                sql = """SELECT StaffId FROM Staff WHERE Forename LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=11,column=3,columnspan=2)

            elif len(surname) > 0:
                temp=surname
                sql = """SELECT Forename FROM Staff WHERE Surname LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT Surname FROM Staff WHERE Surname LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Email FROM Staff WHERE Surname LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT MobileNum FROM Staff WHERE Surname LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                    
                sql = """SELECT Capabilities FROM Staff WHERE Surname LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Availability FROM Staff WHERE Surname LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT StreetNum FROM Staff WHERE Surname LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT StreetName FROM Staff WHERE Surname LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                
                sql = """SELECT Town FROM Staff WHERE Surname LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)
                
                sql = """SELECT Postcode FROM Staff WHERE Surname LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=10,column=3,columnspan=2)
                
                sql = """SELECT StaffId FROM Staff WHERE Surname LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=11,column=3,columnspan=2)
            
            elif len(email) > 0:
                temp=email
                sql = """SELECT Forename FROM Staff WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT Surname FROM Staff WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Email FROM Staff WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT MobileNum FROM Staff WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                    
                sql = """SELECT Capabilities FROM Staff WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Availability FROM Staff WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT StreetNum FROM Staff WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT StreetName FROM Staff WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                
                sql = """SELECT Town FROM Staff WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)
                
                sql = """SELECT Postcode FROM Staff WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=10,column=3,columnspan=2)
                
                sql = """SELECT StaffId FROM Staff WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=11,column=3,columnspan=2)

            elif len(capability) > 0:
                temp=capability
                sql = """SELECT Forename FROM Staff WHERE Capabilities LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT Surname FROM Staff WHERE Capabilities LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Email FROM Staff WHERE Capabilities LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT MobileNum FROM Staff WHERE Capabilities LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                    
                sql = """SELECT Capabilities FROM Staff WHERE Capabilities LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Availability FROM Staff WHERE Capabilities LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT StreetNum FROM Staff WHERE Capabilities LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT StreetName FROM Staff WHERE Capabilities LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                
                sql = """SELECT Town FROM Staff WHERE Capabilities LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)
                
                sql = """SELECT Postcode FROM Staff WHERE Capabilities LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=10,column=3,columnspan=2)
                
                sql = """SELECT StaffId FROM Staff WHERE Capabilities LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=11,column=3,columnspan=2)

            elif len(availability) > 0:
                temp=availability
                sql = """SELECT Forename FROM Staff WHERE Availability LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT Surname FROM Staff WHERE Availability LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Email FROM Staff WHERE Availability LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT MobileNum FROM Staff WHERE Availability LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                    
                sql = """SELECT Capabilities FROM Staff WHERE Availability LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Availability FROM Staff WHERE Availability LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT StreetNum FROM Staff WHERE Availability LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT StreetName FROM Staff WHERE Availability LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                
                sql = """SELECT Town FROM Staff WHERE Availability LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)
                
                sql = """SELECT Postcode FROM Staff WHERE Availability LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=10,column=3,columnspan=2)
                
                sql = """SELECT StaffId FROM Staff WHERE Availability LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=11,column=3,columnspan=2)

            elif len(mobile) > 0:
                temp=mobile
                sql = """SELECT Forename FROM Staff WHERE MobileNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT Surname FROM Staff WHERE MobileNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Email FROM Staff WHERE MobileNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT MobileNum FROM Staff WHERE MobileNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                    
                sql = """SELECT Capabilities FROM Staff WHERE MobileNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Availability FROM Staff WHERE MobileNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT StreetNum FROM Staff WHERE MobileNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT StreetName FROM Staff WHERE MobileNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                
                sql = """SELECT Town FROM Staff WHERE MobileNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)
                
                sql = """SELECT Postcode FROM Staff WHERE MobileNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=10,column=3,columnspan=2)
                
                sql = """SELECT StaffId FROM Staff WHERE MobileNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=11,column=3,columnspan=2)

            elif len(streetNum) > 0:
                temp=streetNum
                sql = """SELECT Forename FROM Staff WHERE StreetNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT Surname FROM Staff WHERE StreetNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Email FROM Staff WHERE StreetNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT MobileNum FROM Staff WHERE StreetNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                    
                sql = """SELECT Capabilities FROM Staff WHERE StreetNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Availability FROM Staff WHERE StreetNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT StreetNum FROM Staff WHERE StreetNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT StreetName FROM Staff WHERE StreetNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                
                sql = """SELECT Town FROM Staff WHERE StreetNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)
                
                sql = """SELECT Postcode FROM Staff WHERE StreetNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=10,column=3,columnspan=2)
                
                sql = """SELECT StaffId FROM Staff WHERE StreetNum LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=11,column=3,columnspan=2)

            elif len(streetName) > 0:
                temp=streetName
                sql = """SELECT Forename FROM Staff WHERE StreetName LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT Surname FROM Staff WHERE StreetName LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Email FROM Staff WHERE StreetName LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT MobileNum FROM Staff WHERE StreetName LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                    
                sql = """SELECT Capabilities FROM Staff WHERE StreetName LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Availability FROM Staff WHERE StreetName LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT StreetNum FROM Staff WHERE StreetName LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT StreetName FROM Staff WHERE StreetName LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                
                sql = """SELECT Town FROM Staff WHERE StreetName LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)
                
                sql = """SELECT Postcode FROM Staff WHERE StreetName LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=10,column=3,columnspan=2)
                
                sql = """SELECT StaffId FROM Staff WHERE StreetName LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=11,column=3,columnspan=2)

            elif len(town) > 0:
                temp=town
                sql = """SELECT Forename FROM Staff WHERE Town LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT Surname FROM Staff WHERE Town LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT Email FROM Staff WHERE Town LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT MobileNum FROM Staff WHERE Town LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                    
                sql = """SELECT Capabilities FROM Staff WHERE Town LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=5,column=3,columnspan=2)
                
                sql = """SELECT Availability FROM Staff WHERE Town LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=6,column=3,columnspan=2)
                
                sql = """SELECT StreetNum FROM Staff WHERE Town LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=7,column=3,columnspan=2)
                
                sql = """SELECT StreetName FROM Staff WHERE Town LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=8,column=3,columnspan=2)
                
                sql = """SELECT Town FROM Staff WHERE Town LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=3,columnspan=2)
                
                sql = """SELECT Postcode FROM Staff WHERE Town LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=10,column=3,columnspan=2)
                
                sql = """SELECT StaffId FROM Staff WHERE Town LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=11,column=3,columnspan=2)

class display_logs():
    def __init__(self, master):
        self.master = master
        self.master.title("Show Logs")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)
        
        # New_Customer Window Buttons
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
        Button(self.master,text='Find',command=self.findData,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=3)
        Button(self.master,text='Clear',command=self.clear,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=4)


    # New Customer Label
        Label(self.master,text='TimeID',bg='turquoise3',font='Bembo',fg='black').grid(row=1,column=0,pady=10)
        Label(self.master,text='Email',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=0,pady=10)
        Label(self.master,text='LogIn',bg='turquoise3',font='Bembo',fg='black').grid(row=3,column=0,pady=10)
        Label(self.master,text='LogOut',bg='turquoise3',font='Bembo',fg='black').grid(row=4,column=0,pady=10)
        
    # New Customer Entry
        self.timeIDEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.timeIDEntry.grid(row=1,column=1,pady=10,columnspan=2)
        
        self.emailEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.emailEntry.grid(row=2,column=1,pady=10,columnspan=2)
        
        self.loginEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.loginEntry.grid(row=3,column=1,pady=10,columnspan=2)
        
        self.logoutEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.logoutEntry.grid(row=4,column=1,pady=10,columnspan=2)
    
    # Quit Program
    def end(self):
        t = time()
        ct = ctime(t)
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        print("--------------------------------")
        print(ct + "\n" + "Logged out")
        print("--------------------------------")
        sql = """UPDATE Time
            SET LogOut = ?
            WHERE LogOut = 'NULL'"""
        cursor.execute(sql,[(ct)])
        db.commit()
        
        quit()
        
    def clear(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=display_logs(root2)
    
    # Toggling full screen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state 
        self.master.attributes("-fullscreen", self.state)
        return "break"
    def end_fullscreen(self, event=None):
        self.state = False
        self.master.attributes("-fullscreen", False)
        return "break"    
    
    # Return To 'Menu' Screen
    def back(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=showWindow(root2)
        
    # Adding To Database
    def findData(self):
        
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=1,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=2,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=3,column=3,columnspan=2)
        Label(self.master,text="                                                                          ",bg='turquoise3',fg='turquoise3').grid(row=4,column=3,columnspan=2)
        
        timeID=self.timeIDEntry.get()
        email=self.emailEntry.get()
        login=self.loginEntry.get()
        logout=self.logoutEntry.get()
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        if len(timeID) > 0 or len(email) > 0 or len(login) > 0 or len(logout) > 0:
            
            if len(timeID) > 0:
                temp=timeID
                sql = """SELECT TimeID FROM Time WHERE TimeID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT Email FROM Time WHERE TimeID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT LogIn FROM Time WHERE TimeID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT LogOut FROM Time WHERE TimeID LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
            elif len(email) > 0:
                temp=email
                sql = """SELECT TimeID FROM Time WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT Email FROM Time WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT LogIn FROM Time WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT LogOut FROM Time WHERE Email LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
            elif len(login) > 0:
                temp=login
                sql = """SELECT TimeID FROM Time WHERE LogIn LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT Email FROM Time WHERE LogIn LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT LogIn FROM Time WHERE LogIn LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT LogOut FROM Time WHERE LogIn LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)
                
            elif len(logout) > 0:
                temp=logout
                sql = """SELECT TimeID FROM Time WHERE LogOut LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3,columnspan=2)
                
                sql = """SELECT Email FROM Time WHERE Logout LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=2,column=3,columnspan=2)
                
                sql = """SELECT LogIn FROM Time WHERE LogOut LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=3,column=3,columnspan=2)
                
                sql = """SELECT LogOut FROM Time WHERE LogOut LIKE ?"""
                cursor.execute(sql,["%"+(temp)+"%"])
                result=cursor.fetchone()
                if result:
                    Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='green').grid(row=4,column=3,columnspan=2)

################################################################################################
################################################################################################
class new_customer():
    def __init__(self, master):
        self.master = master
        self.master.title("Add New Customer")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)
        
        # New_Customer Window Buttons
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
        Button(self.master,text='Add',command=self.addTo,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=3)
    
    # New Customer Label
        Label(self.master,text='Forename',bg='turquoise3',font='Bembo',fg='black').grid(row=1,column=0,pady=10)
        Label(self.master,text='Surname',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=0,pady=10)
        Label(self.master,text='Email',bg='turquoise3',font='Bembo',fg='black').grid(row=3,column=0,pady=10)
        Label(self.master,text='Mobile Number',bg='turquoise3',font='Bembo',fg='black').grid(row=4,column=0,pady=10)
        Label(self.master,text='Street Number',bg='turquoise3',font='Bembo',fg='black').grid(row=5,column=0,pady=10)
        Label(self.master,text='Street Name',bg='turquoise3',font='Bembo',fg='black').grid(row=6,column=0,pady=10)
        Label(self.master,text='Town',bg='turquoise3',font='Bembo',fg='black').grid(row=7,column=0,pady=10)
        Label(self.master,text='Postcode',bg='turquoise3',font='Bembo',fg='black').grid(row=8,column=0,pady=10)

    # New Customer Entry
        self.forenameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.forenameEntry.grid(row=1,column=1,pady=10,columnspan=2)
        
        self.surnameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.surnameEntry.grid(row=2,column=1,pady=10,columnspan=2)
        
        self.emailEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.emailEntry.grid(row=3,column=1,pady=10,columnspan=2)
        
        self.mobileEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.mobileEntry.grid(row=4,column=1,pady=10,columnspan=2)
        
        self.streetNumEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.streetNumEntry.grid(row=5,column=1,pady=10,columnspan=2)
        
        self.streetNameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.streetNameEntry.grid(row=6,column=1,pady=10,columnspan=2)
        
        self.townEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.townEntry.grid(row=7,column=1,pady=10,columnspan=2)
        
        self.postcodeEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.postcodeEntry.grid(row=8,column=1,pady=10,columnspan=2)

    
    # Quit Program
    def end(self):
        t = time()
        ct = ctime(t)
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        print("--------------------------------")
        print(ct + "\n" + "Logged out")
        print("--------------------------------")
        sql = """UPDATE Time
            SET LogOut = ?
            WHERE LogOut = 'NULL'"""
        cursor.execute(sql,[(ct)])
        db.commit()
        
        quit()
    
    # Toggling full screen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state 
        self.master.attributes("-fullscreen", self.state)
        return "break"
    def end_fullscreen(self, event=None):
        self.state = False
        self.master.attributes("-fullscreen", False)
        return "break"    
    
    # Return To 'Menu' Screen
    def back(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=addWindow(root2)
        
    # Adding To Database
    def addTo(self):
        forename=self.forenameEntry.get()
        surname=self.surnameEntry.get()
        email=self.emailEntry.get()
        mobile=self.mobileEntry.get()
        streetNum=self.streetNumEntry.get()
        streetName=self.streetNameEntry.get()
        town=self.townEntry.get()
        postcode=self.postcodeEntry.get()
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        sql = """INSERT INTO Customer(Forename,Surname,Email,MobileNum,StreetNum,StreetName,Town,Postcode)
            VALUES(?,?,?,?,?,?,?,?)"""
        cursor.execute(sql,[(forename),(surname),(email),(mobile),(streetNum),(streetName),(town),(postcode)])
        
        if len(forename) > 0 and len(surname) > 0 and len(email) > 0 and len(mobile) > 0 and len(streetNum) > 0 and len(streetName) > 0 and len(town) > 0 and len(postcode) > 0:
            db.commit()
            print("\n---------------------------------------------\nNew Customer Committed")
            Label(self.master,text='Addition Added  ',bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3)
        else:
            print("\n---------------------------------------------\n~~New Customer Commit Failed")
            Label(self.master,text='Addition Failed ',bg='turquoise3',font='Bembo',fg='red').grid(row=1,column=3)

class new_login():
    def __init__(self, master):
        self.master = master
        self.master.title("Add New Login")
        self.master.configure(background='turquoise3')
        
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)
        
        # New_Login Window Buttons
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
        Button(self.master,text='Add',command=self.addTo,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=3)

    
    # New Login Label
        Label(self.master,text='Email',bg='turquoise3',font='Bembo',fg='black').grid(row=1,column=0,pady=10)
        Label(self.master,text='Password',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=0,pady=10)

    # New Login Entry
        self.emailEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.emailEntry.grid(row=1,column=1,pady=10,columnspan=2)
        
        self.passwordEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.passwordEntry.grid(row=2,column=1,pady=10,columnspan=2)

    
    # Quit Program
    def end(self):
        t = time()
        ct = ctime(t)
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        print("--------------------------------")
        print(ct + "\n" + "Logged out")
        print("--------------------------------")
        sql = """UPDATE Time
            SET LogOut = ?
            WHERE LogOut = 'NULL'"""
        cursor.execute(sql,[(ct)])
        db.commit()
        
        quit()
    
    # Toggling full screen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state 
        self.master.attributes("-fullscreen", self.state)
        return "break"
    def end_fullscreen(self, event=None):
        self.state = False
        self.master.attributes("-fullscreen", False)
        return "break"    
    
    # Return To 'Menu' Screen
    def back(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=addWindow(root2)
        
    # Adding To Database
    def addTo(self):
        email=self.emailEntry.get()
        password=self.passwordEntry.get()

        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        sql = """INSERT INTO Login(StaffEmail,StaffPassword)
            VALUES(?,?)"""
        cursor.execute(sql,[(email),(password)])
        
        if len(email) > 0 and len(password) > 0 :
            db.commit()
            print("\n---------------------------------------------\nNew Login Committed")
            Label(self.master,text='Addition Added  ',bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3)
        else:
            print("\n---------------------------------------------\n~~New Login Commit Failed")
            Label(self.master,text='Addition Failed  ',bg='turquoise3',font='Bembo',fg='red').grid(row=1,column=3)

class new_booking():
    def __init__(self, master):
        self.master = master
        self.master.title("Add New Booking")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)
        
        # New_Customer Window Buttons
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
        Button(self.master,text='Add',command=self.addTo,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=3)
        Button(self.master,text='Find',command=self.find,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black').grid(row=3,column=6,padx=10)

    
    # New Customer Label
        Label(self.master,text='CustomerID',bg='turquoise3',font='Bembo',fg='black').grid(row=1,column=0,pady=10)
        Label(self.master,text='Start',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=0,pady=10)
        Label(self.master,text='Destination',bg='turquoise3',font='Bembo',fg='black').grid(row=3,column=0,pady=10)
        Label(self.master,text='Amount',bg='turquoise3',font='Bembo',fg='black').grid(row=4,column=0,pady=10)
        Label(self.master,text='Fufilled',bg='turquoise3',font='Bembo',fg='black').grid(row=5,column=0,pady=10)
        Label(self.master,text='Date',bg='turquoise3',font='Bembo',fg='black').grid(row=6,column=0,pady=10)
        Label(self.master,text='Time',bg='turquoise3',font='Bembo',fg='black').grid(row=7,column=0,pady=10)
        Label(self.master,text='Vehicle',bg='turquoise3',font='Bembo',fg='black').grid(row=8,column=0,pady=10)
        Label(self.master,text='Find CustomerID',bg='turquoise3',font='Bembo',fg='black').grid(row=1,column=4,pady=10,padx=10)
        Label(self.master,text='Forname',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=3,pady=10,padx=10)
        Label(self.master,text='Surname',bg='turquoise3',font='Bembo',fg='black').grid(row=3,column=3,pady=10,padx=10)



    # New Customer Entry
        self.CustomerIDEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.CustomerIDEntry.grid(row=1,column=1,pady=10,columnspan=2)
        
        self.StartEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.StartEntry.grid(row=2,column=1,pady=10,columnspan=2)
        
        self.DestinationEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.DestinationEntry.grid(row=3,column=1,pady=10,columnspan=2)
        
        self.AmountEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.AmountEntry.grid(row=4,column=1,pady=10,columnspan=2)

        self.fufilledEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.fufilledEntry.grid(row=5,column=1,pady=10,columnspan=2)
        
        self.DateEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.DateEntry.grid(row=6,column=1,pady=10,columnspan=2)
        
        self.TimeEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.TimeEntry.grid(row=7,column=1,pady=10,columnspan=2)
        
        self.VehicleEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.VehicleEntry.grid(row=8,column=1,pady=10,columnspan=2)
        
        self.FornameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.FornameEntry.grid(row=2,column=4,pady=10,columnspan=2)
        
        self.SurnameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.SurnameEntry.grid(row=3,column=4,pady=10,columnspan=2)
    
    
    # Quit Program
    def end(self):
        t = time()
        ct = ctime(t)
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        print("--------------------------------")
        print(ct + "\n" + "Logged out")
        print("--------------------------------")
        sql = """UPDATE Time
            SET LogOut = ?
            WHERE LogOut = 'NULL'"""
        cursor.execute(sql,[(ct)])
        db.commit()
        
        quit()
    
    # Toggling full screen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state 
        self.master.attributes("-fullscreen", self.state)
        return "break"
    def end_fullscreen(self, event=None):
        self.state = False
        self.master.attributes("-fullscreen", False)
        return "break"    
    
    # Return To 'Menu' Screen
    def back(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=addWindow(root2)
        
    # Adding To Database
    def addTo(self):
        customer=self.CustomerIDEntry.get()
        start=self.StartEntry.get()
        destination=self.DestinationEntry.get()
        amount=self.AmountEntry.get()
        fufilled=self.fufilledEntry.get()
        date=self.DateEntry.get()
        time=self.TimeEntry.get()
        vehicle=self.VehicleEntry.get()
        
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        sql = """INSERT INTO Bookings(CustomerID,Start,Destinantion,AmountPaid,Fufilled,Date,Time,VehicleID)
            VALUES(?,?,?,?,?,?,?,?)"""
        cursor.execute(sql,[(customer),(start),(destination),(amount),(fufilled),(date),(time),(vehicle)])
        
        if len(customer) > 0 and len(start) > 0 and len(destination) > 0 and len(amount) > 0 and len(fufilled) > 0 and len(date) > 0 and len(time) > 0 and len(vehicle) > 0:
            db.commit()
            print("\n---------------------------------------------\nNew Booking Committed")
            Label(self.master,text='Addition Added  ',bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=1)
        else:
            print("\n---------------------------------------------\n~~New Booking Commit Failed")
            Label(self.master,text='Addition Failed ',bg='turquoise3',font='Bembo',fg='red').grid(row=9,column=1)


    def find(self):
        forname=self.FornameEntry.get()
        surname=self.SurnameEntry.get()
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        sql = """SELECT CustomerID from Customer WHERE Forename = ? AND Surname = ?"""
        cursor.execute(sql,[(forname),(surname)])
        result=cursor.fetchall()
        
        if result:
            Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='black').grid(row=4,column=4,pady=10,padx=10)

class new_vehicle():
    def __init__(self, master):
        self.master = master
        self.master.title("Add New Vehicle")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)
        
        # New_Customer Window Buttons
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
        Button(self.master,text='Add',command=self.addTo,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=3)
        Button(self.master,text='Find',command=self.find,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black').grid(row=3,column=6,padx=10)

    
    # New Customer Label
        Label(self.master,text='MOT',bg='turquoise3',font='Bembo',fg='black').grid(row=1,column=0,pady=10)
        Label(self.master,text='Mileage',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=0,pady=10)
        Label(self.master,text='Seats',bg='turquoise3',font='Bembo',fg='black').grid(row=3,column=0,pady=10)
        Label(self.master,text='Make',bg='turquoise3',font='Bembo',fg='black').grid(row=4,column=0,pady=10)
        Label(self.master,text='Availability',bg='turquoise3',font='Bembo',fg='black').grid(row=5,column=0,pady=10)
        Label(self.master,text='StaffID',bg='turquoise3',font='Bembo',fg='black').grid(row=6,column=0,pady=10)
        Label(self.master,text='Find StaffID',bg='turquoise3',font='Bembo',fg='black').grid(row=1,column=4,pady=10,padx=10)
        Label(self.master,text='Forname',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=3,pady=10,padx=10)
        Label(self.master,text='Surname',bg='turquoise3',font='Bembo',fg='black').grid(row=3,column=3,pady=10,padx=10)

    # New Customer Entry
        self.MOTEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.MOTEntry.grid(row=1,column=1,pady=10,columnspan=2)
        
        self.MileageEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.MileageEntry.grid(row=2,column=1,pady=10,columnspan=2)
        
        self.SeatsEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.SeatsEntry.grid(row=3,column=1,pady=10,columnspan=2)
        
        self.MakeEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.MakeEntry.grid(row=4,column=1,pady=10,columnspan=2)
        
        self.AvailabilityEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.AvailabilityEntry.grid(row=5,column=1,pady=10,columnspan=2)
        
        self.StaffIdEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.StaffIdEntry.grid(row=6,column=1,pady=10,columnspan=2)
        
        self.FornameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.FornameEntry.grid(row=2,column=4,pady=10,columnspan=2)
        
        self.SurnameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.SurnameEntry.grid(row=3,column=4,pady=10,columnspan=2)
        
    
    # Quit Program
    def end(self):
        t = time()
        ct = ctime(t)
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        print("--------------------------------")
        print(ct + "\n" + "Logged out")
        print("--------------------------------")
        sql = """UPDATE Time
            SET LogOut = ?
            WHERE LogOut = 'NULL'"""
        cursor.execute(sql,[(ct)])
        db.commit()
        
        quit()
    
    # Toggling full screen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state 
        self.master.attributes("-fullscreen", self.state)
        return "break"
    def end_fullscreen(self, event=None):
        self.state = False
        self.master.attributes("-fullscreen", False)
        return "break"    
    
    # Return To 'Menu' Screen
    def back(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=addWindow(root2)
        
    # Adding To Database
    def addTo(self):
        MOT=self.MOTEntry.get()
        mileage=self.MileageEntry.get()
        seats=self.SeatsEntry.get()
        make=self.MakeEntry.get()
        availability=self.AvailabilityEntry.get()
        staff=self.StaffIdEntry.get()
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        sql = """INSERT INTO Vehicle(MOT,Mileage,Seats,Make,Availability,StaffID)
            VALUES(?,?,?,?,?,?)"""
        cursor.execute(sql,[(MOT),(mileage),(seats),(make),(availability),(staff)])
        
        if len(MOT) > 0 and len(mileage) > 0 and len(seats) > 0 and len(make) > 0 and len(availability) > 0 and len(staff) > 0:
            db.commit()
            print("\n---------------------------------------------\nNew Vehicle Committed")
            Label(self.master,text='Addition Added  ',bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3)
        else:
            print("\n---------------------------------------------\n~~New Vehicle Commit Failed")
            Label(self.master,text='Addition Failed ',bg='turquoise3',font='Bembo',fg='red').grid(row=1,column=3)

    def find(self):
            forname=self.FornameEntry.get()
            surname=self.SurnameEntry.get()
            
            db =sqlite3.connect("main.db")
            cursor = db.cursor()
            sql = """SELECT StaffID from Staff WHERE Forename = ? AND Surname = ?"""
            cursor.execute(sql,[(forname),(surname)])
            result=cursor.fetchall()
            
            if result:
                Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='black').grid(row=4,column=4,pady=10,padx=10)

class new_staff():
    def __init__(self, master):
        self.master = master
        self.master.title("Add New Staff")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)
        
        # New_Customer Window Buttons
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
        Button(self.master,text='Add',command=self.addTo,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=3)
    
    # New Customer Label
        Label(self.master,text='Forename',bg='turquoise3',font='Bembo',fg='black').grid(row=1,column=0,pady=10)
        Label(self.master,text='Surname',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=0,pady=10)
        Label(self.master,text='Email',bg='turquoise3',font='Bembo',fg='black').grid(row=3,column=0,pady=10)
        Label(self.master,text='Mobile Number',bg='turquoise3',font='Bembo',fg='black').grid(row=4,column=0,pady=10)
        Label(self.master,text='Capabilities',bg='turquoise3',font='Bembo',fg='black').grid(row=5,column=0,pady=10)
        Label(self.master,text='Availability',bg='turquoise3',font='Bembo',fg='black').grid(row=6,column=0,pady=10)
        Label(self.master,text='Street Number',bg='turquoise3',font='Bembo',fg='black').grid(row=7,column=0,pady=10)
        Label(self.master,text='Street Name',bg='turquoise3',font='Bembo',fg='black').grid(row=8,column=0,pady=10)
        Label(self.master,text='Town',bg='turquoise3',font='Bembo',fg='black').grid(row=9,column=0,pady=10)
        Label(self.master,text='Postcode',bg='turquoise3',font='Bembo',fg='black').grid(row=10,column=0,pady=10)

    # New Customer Entry
        self.forenameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.forenameEntry.grid(row=1,column=1,pady=10,columnspan=2)
        
        self.surnameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.surnameEntry.grid(row=2,column=1,pady=10,columnspan=2)
        
        self.EmailEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.EmailEntry.grid(row=3,column=1,pady=10,columnspan=2)
        
        self.mobileEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.mobileEntry.grid(row=4,column=1,pady=10,columnspan=2)
        
        self.CapabilitiesEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.CapabilitiesEntry.grid(row=5,column=1,pady=10,columnspan=2)
        
        self.AvailabilityEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.AvailabilityEntry.grid(row=6,column=1,pady=10,columnspan=2)
        
        self.streetNumEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.streetNumEntry.grid(row=7,column=1,pady=10,columnspan=2)
        
        self.streetNameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.streetNameEntry.grid(row=8,column=1,pady=10,columnspan=2)
        
        self.townEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.townEntry.grid(row=9,column=1,pady=10,columnspan=2)
        
        self.postcodeEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.postcodeEntry.grid(row=10,column=1,pady=10,columnspan=2)

    
    # Quit Program
    def end(self):
        t = time()
        ct = ctime(t)
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        print("--------------------------------")
        print(ct + "\n" + "Logged out")
        print("--------------------------------")
        sql = """UPDATE Time
            SET LogOut = ?
            WHERE LogOut = 'NULL'"""
        cursor.execute(sql,[(ct)])
        db.commit()
        
        quit()
    
    # Toggling full screen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state 
        self.master.attributes("-fullscreen", self.state)
        return "break"
    def end_fullscreen(self, event=None):
        self.state = False
        self.master.attributes("-fullscreen", False)
        return "break"    
    
    # Return To 'Menu' Screen
    def back(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=addWindow(root2)
        
    # Adding To Database
    def addTo(self):
        forename=self.forenameEntry.get()
        surname=self.surnameEntry.get()
        email=self.EmailEntry.get()
        capability=self.CapabilitiesEntry.get()
        availability=self.AvailabilityEntry.get()
        mobile=self.mobileEntry.get()
        streetNum=self.streetNumEntry.get()
        streetName=self.streetNameEntry.get()
        town=self.townEntry.get()
        postcode=self.postcodeEntry.get()
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        sql = """INSERT INTO Staff(Forename,Surname,Email,MobileNum,Capabilities,Availability,StreetNum,StreetName,Town,Postcode)
            VALUES(?,?,?,?,?,?,?,?,?,?)"""
        cursor.execute(sql,[(forename),(surname),(email),(mobile),(capability),(availability),(streetNum),(streetName),(town),(postcode)])
        
        if len(forename) > 0 and len(surname) > 0 and len(email) > 0 and len(mobile) > 0 and len(streetNum) > 0 and len(streetName) > 0 and len(town) > 0 and len(postcode) > 0:
            db.commit()
            print("\n---------------------------------------------\nNew Staff Committed")
            Label(self.master,text='Addition Added  ',bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3)
        else:
            print("\n---------------------------------------------\n~~New Staff Commit Failed")
            Label(self.master,text='Addition Failed ',bg='turquoise3',font='Bembo',fg='red').grid(row=1,column=3)

###############################################################################################
###############################################################################################

def main():
    root=Tk()
    myGUIWelcome=Home(root)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.mainloop()
if __name__ == '__main__':
    main()



# class addWindow():

#     def __init__(self, master):
#         self.master = master
#         self.master.title("Add")
#         self.master.configure(background='turquoise3')
#         self.ADV_CustomerID=0
        
#         # Binding F11 and ESCAPE keys to full screen
#         self.master.bind("<F11>", self.toggle_fullscreen)
#         self.master.bind("<Escape>", self.end_fullscreen)
#         self.state = True
#         self.master.attributes("-fullscreen", True)
        
#         # Sign Up Page Buttons
#         Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
#         Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
#         Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
        
#         Button(self.master,text='Add Customer',command=self.add_customer,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=0)
#         Button(self.master,text='Add Login',command=self.add_login,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=1)
#         Button(self.master,text='Add Booking',command=self.add_booking,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=2)
#         Button(self.master,text='Add Vehicle',command=self.add_vehicle,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=3)
#         Button(self.master,text='Add Staff',command=self.add_staff,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=4)

#     # Quit Program
#     def end(self):
#         t = time()
#         ct = ctime(t)
        
#         db =sqlite3.connect("main.db")
#         cursor = db.cursor()
#         print("--------------------------------")
#         print(ct + "\n" + "Logged out")
#         print("--------------------------------")
#         sql = """UPDATE Time
#             SET LogOut = ?
#             WHERE LogOut = 'NULL'"""
#         cursor.execute(sql,[(ct)])
#         db.commit()
#         db.close()
#         quit()
    
#     # Toggling full screen
#     def toggle_fullscreen(self, event=None):
#         self.state = not self.state 
#         self.master.attributes("-fullscreen", self.state)
#         return "break"
#     def end_fullscreen(self, event=None):
#         self.state = False
#         self.master.attributes("-fullscreen", False)
#         return "break"
    
#     # Return To 'Home' Screen
#     def back(self):
#         self.master.withdraw()
#         root2=Toplevel(self.master)
#         root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
#         muGUI=MasterMenu(root2)
        
        
#     def add_customer(self):
#         self.master.withdraw()
#         root2=Toplevel(self.master)
#         root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
#         muGUI=new_customer(root2)
    
#     def add_login(self):
#         self.master.withdraw()
#         root2=Toplevel(self.master)
#         root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
#         muGUI=new_login(root2)
    
#     def add_booking(self):
#         self.master.withdraw()
#         root2=Toplevel(self.master)
#         root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
#         muGUI=new_booking(root2,self.ADV_CustomerID)
    
#     def add_vehicle(self):
#         self.master.withdraw()
#         root2=Toplevel(self.master)
#         root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
#         muGUI=new_vehicle(root2)
    
#     def add_staff(self):
#         self.master.withdraw()
#         root2=Toplevel(self.master)
#         root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
#         muGUI=new_staff(root2)
        
#     def add_driver(self):
#         self.master.withdraw()
#         root2=Toplevel(self.master)
#         root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))

# class new_customer():
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Add New Customer")
#         self.master.configure(background='turquoise3')
        
#         # Binding F11 and ESCAPE keys to full screen
#         self.master.bind("<F11>", self.toggle_fullscreen)
#         self.master.bind("<Escape>", self.end_fullscreen)
#         self.state = True
#         self.master.attributes("-fullscreen", True)
        
#         # New_Customer Window Buttons
#         Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
#         Button(self.master,text='Add Customer',command=self.addTo,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
#         Button(self.master,text='Add And Continue',command=self.advBooking,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
#         Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=3)
#         Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=4)
    
#     # New Customer Label
#         Label(self.master,text='Forename',bg='turquoise3',font='Bembo',fg='black').grid(row=1,column=0,pady=10)
#         Label(self.master,text='Surname',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=0,pady=10)
#         Label(self.master,text='Email',bg='turquoise3',font='Bembo',fg='black').grid(row=3,column=0,pady=10)
#         Label(self.master,text='Mobile Number',bg='turquoise3',font='Bembo',fg='black').grid(row=4,column=0,pady=10)

#     # New Customer Entry
#         self.forenameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.forenameEntry.grid(row=1,column=1,pady=10,columnspan=2)
        
#         self.surnameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.surnameEntry.grid(row=2,column=1,pady=10,columnspan=2)
        
#         self.emailEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.emailEntry.grid(row=3,column=1,pady=10,columnspan=2)
        
#         self.mobileEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.mobileEntry.grid(row=4,column=1,pady=10,columnspan=2)

#     # Quit Program
#     def end(self):
#         t = time()
#         ct = ctime(t)
        
#         db =sqlite3.connect("main.db")
#         cursor = db.cursor()
#         print("--------------------------------")
#         print(ct + "\n" + "Logged out")
#         print("--------------------------------")
#         sql = """UPDATE Time
#             SET LogOut = ?
#             WHERE LogOut = 'NULL'"""
#         cursor.execute(sql,[(ct)])
#         db.commit()
#         db.close()
#         quit()
    
#     # Toggling full screen
#     def toggle_fullscreen(self, event=None):
#         self.state = not self.state 
#         self.master.attributes("-fullscreen", self.state)
#         return "break"
#     def end_fullscreen(self, event=None):
#         self.state = False
#         self.master.attributes("-fullscreen", False)
#         return "break"    
    
#     # Return To 'Menu' Screen
#     def back(self):
#         self.master.withdraw()
#         root2=Toplevel(self.master)
#         root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
#         muGUI=addWindow(root2)
        
#     # Adding To Database
#     def addTo(self):
#         forename=self.forenameEntry.get()
#         surname=self.surnameEntry.get()
#         email=self.emailEntry.get()
#         mobile=self.mobileEntry.get()
        
#         db =sqlite3.connect("main.db")
#         cursor = db.cursor()
#         sql = """INSERT INTO Customer(Forename,Surname,Email,MobileNum)
#             VALUES(?,?,?,?)"""
#         cursor.execute(sql,[(forename),(surname),(email),(mobile)])
        
#         if len(forename) > 0 and len(surname) > 0 and len(email) > 0 and len(mobile):
#             db.commit()
#             print("\n---------------------------------------------\nNew Customer Committed")
#             Label(self.master,text='Addition Added  ',bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3)
#         else:
#             print("\n---------------------------------------------\n~~New Customer Commit Failed")
#             Label(self.master,text='Addition Failed ',bg='turquoise3',font='Bembo',fg='red').grid(row=1,column=3)
#         db.close()
            
#     def advBooking(self):
#         forename=self.forenameEntry.get()
#         surname=self.surnameEntry.get()
#         email=self.emailEntry.get()
#         mobile=self.mobileEntry.get()
        
        
#         db =sqlite3.connect("main.db")
#         cursor = db.cursor()

#         sql = """INSERT INTO Customer(Forename,Surname,Email,MobileNum)
#             VALUES(?,?,?,?)"""
#         cursor.execute(sql,[(forename),(surname),(email),(mobile)])
        
#         if len(forename) > 0 and len(surname) > 0 and len(email) > 0 and len(mobile):
#             db.commit()
#             print("\n---------------------------------------------\nNew Customer Committed")
#             Label(self.master,text='Addition Added  ',bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3)
        
#             sql = """SELECT CustomerID FROM Customer WHERE Forename = ?"""
#             cursor.execute(sql,[(forename)])
#             self.ADV_CustomerID=cursor.fetchall()
            
#             self.master.withdraw()
#             root2=Toplevel(self.master)
#             root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
#             muGUI=new_booking(root2,self.ADV_CustomerID)
#         else:
#             print("\n---------------------------------------------\n~~New Customer Commit Failed")
#             Label(self.master,text='Addition Failed ',bg='turquoise3',font='Bembo',fg='red').grid(row=1,column=3)
#         db.close()
# class new_booking():
#     def __init__(self,master,ADV_CustomerID):
#         self.master = master
#         self.master.title("Add New Booking")
#         self.master.configure(background='turquoise3')
#         self.NewCustomerID=ADV_CustomerID
        
#         # Binding F11 and ESCAPE keys to full screen
#         self.master.bind("<F11>", self.toggle_fullscreen)
#         self.master.bind("<Escape>", self.end_fullscreen)
#         self.state = True
#         self.master.attributes("-fullscreen", True)
        
#         # New_Customer Window Buttons
#         Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
#         Button(self.master,text='Add',command=self.addTo,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
#         Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
#         Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=3)
#         Button(self.master,text='Find Customer',command=self.find_customer,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black').grid(row=3,column=6,padx=10)

#     # New Customer Label
#         Label(self.master,text='StartStreetNum',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=0,pady=10)
#         Label(self.master,text='StartStreet',bg='turquoise3',font='Bembo',fg='black').grid(row=3,column=0,pady=10)
#         Label(self.master,text='StartPostcode',bg='turquoise3',font='Bembo',fg='black').grid(row=4,column=0,pady=10)
#         Label(self.master,text='DestinationStreetNum',bg='turquoise3',font='Bembo',fg='black').grid(row=5,column=0,pady=10)
#         Label(self.master,text='DestinationStreet',bg='turquoise3',font='Bembo',fg='black').grid(row=6,column=0,pady=10)
#         Label(self.master,text='DestinationPostcode',bg='turquoise3',font='Bembo',fg='black').grid(row=7,column=0,pady=10)
#         Label(self.master,text='Fufilled',bg='turquoise3',font='Bembo',fg='black').grid(row=8,column=0,pady=10)
#         Label(self.master,text='Date',bg='turquoise3',font='Bembo',fg='black').grid(row=9,column=0,pady=10,padx=10)
#         Label(self.master,text='Time',bg='turquoise3',font='Bembo',fg='black').grid(row=10,column=0,pady=10,padx=10)
#         Label(self.master,text='CustomerID',bg='turquoise3',font='Bembo',fg='black').grid(row=11,column=0,pady=10)
#         Label(self.master,text='Forename',bg='turquoise3',font='Bembo',fg='black').grid(row=12,column=0,pady=10,padx=10)
#         Label(self.master,text='Forename',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=3,pady=10,padx=10)
#         Label(self.master,text='Surname',bg='turquoise3',font='Bembo',fg='black').grid(row=3,column=3,pady=10,padx=10)
        
#         # Cant get ADV_CustomerID Is in another class
#         # Should automatically recognise CustomerID and display
#         CustomerIDS=0
#         #CustomerIDS=self.ADV_CustomerID.get()
#         if CustomerIDS > 0:
#             Label(self.master,text='CustomerID =',bg='turquoise3',font='Bembo',fg='black').grid(row=4,column=3,pady=10,padx=10)
#             Label(self.master,text=CustomerIDS,bg='turquoise3',font='Bembo',fg='black').grid(row=5,column=3,pady=10,padx=10)

#     # New Booking Entry
        
#         self.StartStreetNumEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.StartStreetNumEntry.grid(row=2,column=1,pady=10,columnspan=2)

#         self.StartStreetEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.StartStreetEntry.grid(row=3,column=1,pady=10,columnspan=2)
        
#         self.StartPostcodeEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.StartPostcodeEntry.grid(row=4,column=1,pady=10,columnspan=2)

#         self.DestinationStreetNumEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.DestinationStreetNumEntry.grid(row=5,column=1,pady=10,columnspan=2)
        
#         self.DestinationStreetEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.DestinationStreetEntry.grid(row=6,column=1,pady=10,columnspan=2)
        
#         self.DestinationPostcodeEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.DestinationPostcodeEntry.grid(row=7,column=1,pady=10,columnspan=2)
        
#         self.FufilledEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.FufilledEntry.grid(row=8,column=1,pady=10,columnspan=2)
        
#         self.DateEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.DateEntry.grid(row=9,column=1,pady=10,columnspan=2)
        
#         self.TimeEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.TimeEntry.grid(row=10,column=1,pady=10,columnspan=2)
        
#         self.CustomerIDEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.CustomerIDEntry.grid(row=11,column=1,pady=10,columnspan=2)
        
#         self.ForenameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.ForenameEntry.grid(row=12,column=1,pady=10,columnspan=2)
        
#         self.ForenameEntryf=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.ForenameEntryf.grid(row=2,column=4,pady=10,columnspan=2)
        
#         self.SurnameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.SurnameEntry.grid(row=3,column=4,pady=10,columnspan=2)
    
#     # Quit Program
#     def end(self):
#         t = time()
#         ct = ctime(t)
        
#         db =sqlite3.connect("main.db")
#         cursor = db.cursor()
#         print("--------------------------------")
#         print(ct + "\n" + "Logged out")
#         print("--------------------------------")
#         sql = """UPDATE Time
#             SET LogOut = ?
#             WHERE LogOut = 'NULL'"""
#         cursor.execute(sql,[ct])
#         db.commit()
#         db.close()
#         quit()
    
#     # Toggling full screen
#     def toggle_fullscreen(self, event=None):
#         self.state = not self.state 
#         self.master.attributes("-fullscreen", self.state)
#         return "break"
    
#     def end_fullscreen(self, event=None):
#         self.state = False
#         self.master.attributes("-fullscreen", False)
#         return "break"    
    
#     # Return To 'Menu' Screen
#     def back(self):
#         self.master.withdraw()
#         root2=Toplevel(self.master)
#         root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
#         muGUI=addWindow(root2)
    
#     # Find CustomerID
#     def find_customer(self):
#         db =sqlite3.connect("main.db")
#         cursor = db.cursor()
        
#         Forename=self.ForenameEntryf.get()
#         Surname=self.SurnameEntry.get()
        
#         if len(Forename) >=  1 :
#             sql = """SELECT CustomerID FROM CUSTOMER WHERE Forename LIKE ?"""
#             cursor.execute(sql,[(Forename)])
#             result=cursor.fetchall()
#             if result:
#                 l=Label(self.master,text='Customer Found',bg='turquoise3',font='Bembo',fg='red').grid(row=4,column=5,padx=9)
#         elif len(Surname) >= 1:
#             sql = """SELECT CustomerID FROM CUSTOMER WHERE Surname LIKE ?"""
#             cursor.execute(sql,[(Surname)])
#             result=cursor.fetchall()
#             if result:
#                 l=Label(self.master,text='Customer Found',bg='turquoise3',font='Bembo',fg='red').grid(row=4,column=5,padx=9)

#             #################
#             # Turn To DropBox
#         print(result)
#         Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='black').grid(row=4,column=6,padx=10)
#             ###############################
            
#         FScustomer=result
#         db.close()

#     # Adding To Database
#     def addTo(self):
#         CustomerID =  0
#         StartStreetNum=self.StartStreetNumEntry.get()
#         StartStreet=self.StartStreetEntry.get()
#         StartPostcode=self.StartPostcodeEntry.get()
#         DestinationStreetNum =self.DestinationStreetNumEntry.get()
#         DestinationStreet=self.DestinationStreetEntry.get()
#         DestinationPostcode=self.DestinationPostcodeEntry.get()
#         Forename=self.forenameEntry.get()
#         Fufilled=self.FufilledEntry.get()
#         Date=self.DateEntry.get()
#         Time=self.TimeEntry.get()
#         if CustomerID == 0:
#             CustomerID=self.CustomerIDEntry.get()
#         if CustomerID == 0:
#             CustomerID=self.FScustomer.get()
#         if CustomerID == 0:
#             CustomerID=self.NewCustomerID.get()

#         #NewCustomerID Needs To turn integer

#         db =sqlite3.connect("main.db")
#         cursor = db.cursor()
#         sql = """INSERT INTO Bookings(CustomerID,Forename,StartStreetNum,StartStreet,StartPostcode,DestinationStreetnum,DestinationStreet,DestinationPostcode,Fufilled,Date,Time)
#             VALUES(?,?,?,?,?,?,?,?,?,?)"""
#         cursor.execute(sql,[(CustomerID),(Forename),(StartStreetNum),(StartStreet),(StartPostcode),(DestinationStreetNum),(DestinationStreet),(DestinationPostcode),(Fufilled),(Date),(Time)])
        
#         if (CustomerID) >= 0 and len(StartStreetNum) > 0 and len(StartStreet) > 0 and len(StartPostcode) > 0 and len(DestinationStreetNum) > 0 and len(DestinationStreet) > 0 and len(DestinationPostcode) > 0 and len(Fufilled) > 0 and len(Date) > 0 and len(Time) and len(Forename)> 0:
#             db.commit()
#             print("\n---------------------------------------------\nNew Booking Committed")
#             Label(self.master,text='Addition Added  ',bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=1)
#         else:
#             print("\n---------------------------------------------\n~~New Booking Commit Failed")
#             Label(self.master,text='Addition Failed ',bg='turquoise3',font='Bembo',fg='red').grid(row=9,column=1)
#         db.close()
# class new_login():
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Add New Login")
#         self.master.configure(background='turquoise3')
        
#         self.master.bind("<F11>", self.toggle_fullscreen)
#         self.master.bind("<Escape>", self.end_fullscreen)
#         self.state = True
#         self.master.attributes("-fullscreen", True)
        
#         # New_Login Window Buttons
#         Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
#         Button(self.master,text='Add',command=self.addTo,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
#         Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
#         Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=3)

    
#     # New Login Label
#         Label(self.master,text='Email',bg='turquoise3',font='Bembo',fg='black').grid(row=1,column=0,pady=10)
#         Label(self.master,text='Password',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=0,pady=10)

#     # New Login Entry
#         self.emailEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.emailEntry.grid(row=1,column=1,pady=10,columnspan=2)
        
#         self.passwordEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.passwordEntry.grid(row=2,column=1,pady=10,columnspan=2)

    
#     # Quit Program
#     def end(self):
#         t = time()
#         ct = ctime(t)
        
#         db =sqlite3.connect("main.db")
#         cursor = db.cursor()
#         print("--------------------------------")
#         print(ct + "\n" + "Logged out")
#         print("--------------------------------")
#         sql = """UPDATE Time
#             SET LogOut = ?
#             WHERE LogOut = 'NULL'"""
#         cursor.execute(sql,[(ct)])
#         db.commit()
#         db.close()
#         quit()
    
#     # Toggling full screen
#     def toggle_fullscreen(self, event=None):
#         self.state = not self.state 
#         self.master.attributes("-fullscreen", self.state)
#         return "break"
#     def end_fullscreen(self, event=None):
#         self.state = False
#         self.master.attributes("-fullscreen", False)
#         return "break"    
    
#     # Return To 'Menu' Screen
#     def back(self):
#         self.master.withdraw()
#         root2=Toplevel(self.master)
#         root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
#         muGUI=addWindow(root2)
        
#     # Adding To Database
#     def addTo(self):
#         email=self.emailEntry.get()
#         password=self.passwordEntry.get()

        
#         db =sqlite3.connect("main.db")
#         cursor = db.cursor()
#         sql = """INSERT INTO Login(StaffEmail,StaffPassword)
#             VALUES(?,?)"""
#         cursor.execute(sql,[(email),(password)])
        
#         if len(email) > 0 and len(password) > 0 :
#             db.commit()
#             print("\n---------------------------------------------\nNew Login Committed")
#             Label(self.master,text='Addition Added  ',bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3)
#         else:
#             print("\n---------------------------------------------\n~~New Login Commit Failed")
#             Label(self.master,text='Addition Failed  ',bg='turquoise3',font='Bembo',fg='red').grid(row=1,column=3)
#         db.close()
# class new_vehicle():
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Add New Vehicle")
#         self.master.configure(background='turquoise3')
        
#         # Binding F11 and ESCAPE keys to full screen
#         self.master.bind("<F11>", self.toggle_fullscreen)
#         self.master.bind("<Escape>", self.end_fullscreen)
#         self.state = True
#         self.master.attributes("-fullscreen", True)
        
#         # New_Customer Window Buttons
#         Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
#         Button(self.master,text='Add',command=self.addTo,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
#         Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
#         Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=3)
#         Button(self.master,text='Find',command=self.find_staff,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black').grid(row=5,column=6,padx=10)

    
#     # New Customer Label
#         Label(self.master,text='MOT',bg='turquoise3',font='Bembo',fg='black').grid(row=1,column=0,pady=10)
#         Label(self.master,text='Mileage',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=0,pady=10)
#         Label(self.master,text='Seats',bg='turquoise3',font='Bembo',fg='black').grid(row=3,column=0,pady=10)
#         Label(self.master,text='Make',bg='turquoise3',font='Bembo',fg='black').grid(row=4,column=0,pady=10)
#         Label(self.master,text='Availability',bg='turquoise3',font='Bembo',fg='black').grid(row=5,column=0,pady=10)
#         Label(self.master,text='StaffID',bg='turquoise3',font='Bembo',fg='black').grid(row=6,column=0,pady=10)
#         Label(self.master,text='Find StaffID',bg='turquoise3',font='Bembo',fg='black').grid(row=1,column=4,pady=10,padx=10)
#         Label(self.master,text='Forename',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=3,pady=10,padx=10)
#         Label(self.master,text='Surname',bg='turquoise3',font='Bembo',fg='black').grid(row=3,column=3,pady=10,padx=10)
#         Label(self.master,text='Email',bg='turquoise3',font='Bembo',fg='black').grid(row=4,column=3,pady=10,padx=10)
#         Label(self.master,text='Postcode',bg='turquoise3',font='Bembo',fg='black').grid(row=5,column=3,pady=10,padx=10)

#     # New Customer Entry
#         self.MOTEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.MOTEntry.grid(row=1,column=1,pady=10,columnspan=2)
        
#         self.MileageEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.MileageEntry.grid(row=2,column=1,pady=10,columnspan=2)
        
#         self.SeatsEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.SeatsEntry.grid(row=3,column=1,pady=10,columnspan=2)
        
#         self.MakeEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.MakeEntry.grid(row=4,column=1,pady=10,columnspan=2)
        
#         self.AvailabilityEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.AvailabilityEntry.grid(row=5,column=1,pady=10,columnspan=2)
        
#         self.StaffIdEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.StaffIdEntry.grid(row=6,column=1,pady=10,columnspan=2)
        
#         self.ForenameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.ForenameEntry.grid(row=2,column=4,pady=10,columnspan=2)
        
#         self.SurnameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.SurnameEntry.grid(row=3,column=4,pady=10,columnspan=2)
        
#         self.EmailEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.EmailEntry.grid(row=4,column=4,pady=10,columnspan=2)
        
#         self.PostcodeEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.PostcodeEntry.grid(row=5,column=4,pady=10,columnspan=2)
        
    
#     # Quit Program
#     def end(self):
#         t = time()
#         ct = ctime(t)
        
#         db =sqlite3.connect("main.db")
#         cursor = db.cursor()
#         print("--------------------------------")
#         print(ct + "\n" + "Logged out")
#         print("--------------------------------")
#         sql = """UPDATE Time
#             SET LogOut = ?
#             WHERE LogOut = 'NULL'"""
#         cursor.execute(sql,[(ct)])
#         db.commit()
#         db.close()
#         quit()
    
#     # Toggling full screen
#     def toggle_fullscreen(self, event=None):
#         self.state = not self.state 
#         self.master.attributes("-fullscreen", self.state)
#         return "break"
#     def end_fullscreen(self, event=None):
#         self.state = False
#         self.master.attributes("-fullscreen", False)
#         return "break"    
    
#     # Return To 'Menu' Screen
#     def back(self):
#         self.master.withdraw()
#         root2=Toplevel(self.master)
#         root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
#         muGUI=addWindow(root2)
    
    
#     # Adding To Database
#     def addTo(self):
#         MOT=self.MOTEntry.get()
#         mileage=self.MileageEntry.get()
#         seats=self.SeatsEntry.get()
#         make=self.MakeEntry.get()
#         availability=self.AvailabilityEntry.get()
#         staff=self.StaffIdEntry.get()
#         staff=self.staff_auto.get()
#         if staff==0:
#             print(staff)
#         db =sqlite3.connect("main.db")
#         cursor = db.cursor()
#         sql = """INSERT INTO Vehicle(MOT,Mileage,Seats,Make,Availability,StaffID)
#             VALUES(?,?,?,?,?,?)"""
#         cursor.execute(sql,[(MOT),(mileage),(seats),(make),(availability),(staff)])
        
#         if len(MOT) > 0 and len(mileage) > 0 and len(seats) > 0 and len(make) > 0 and len(availability) > 0:
#             db.commit()
#             print("\n---------------------------------------------\nNew Vehicle Committed")
#             Label(self.master,text='Addition Added  ',bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3)
#         else:
#             print("\n---------------------------------------------\n~~New Vehicle Commit Failed")
#             Label(self.master,text='Addition Failed ',bg='turquoise3',font='Bembo',fg='red').grid(row=1,column=3)
#         db.close()

#     def find_staff(self):
#         db =sqlite3.connect("main.db")
#         cursor = db.cursor()
        
#         Forename=self.ForenameEntry.get()
#         Surname=self.SurnameEntry.get()
#         Email=self.EmailEntry.get()
#         Postcode=self.PostcodeEntry.get()
        
#         if len(Forename) >=  1 :
#             sql = """SELECT StaffID FROM Staff WHERE Forename LIKE ?"""
#             cursor.execute(sql,[(Forename)])
#             result=cursor.fetchall()
#             if result:
#                 l=Label(self.master,text='Staff Found',bg='turquoise3',font='Bembo',fg='red').grid(row=6,column=3,padx=9)
#         elif len(Surname) >= 1:
#             sql = """SELECT StaffID FROM Staff WHERE Surname LIKE ?"""
#             cursor.execute(sql,[(Surname)])
#             result=cursor.fetchall()
#             if result:
#                 l=Label(self.master,text='Staff Found',bg='turquoise3',font='Bembo',fg='red').grid(row=6,column=3,padx=9)
#         elif len(Email) >=  1 :
#             sql = """SELECT StaffID FROM Staff WHERE Email LIKE ?"""
#             cursor.execute(sql,[(Email)])
#             result=cursor.fetchall()
#             if result:
#                 l=Label(self.master,text='Staff Found',bg='turquoise3',font='Bembo',fg='red').grid(row=6,column=3,padx=9)
#         elif len(Postcode) >= 1:
#             sql = """SELECT StaffID FROM Staff WHERE Postcode LIKE ?"""
#             cursor.execute(sql,[(Postcode)])
#             result=cursor.fetchall()
#             if result:
#                 l=Label(self.master,text='Staff Found',bg='turquoise3',font='Bembo',fg='red').grid(row=6,column=3,padx=9)

#             #################
#             # Turn To DropBox
#         print(result)
#         Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='black').grid(row=6,column=4,padx=10)
#             ###############################
            
#         staff_auto=result
#         db.close()
# class new_staff():
#     def __init__(self, master):
#         self.master = master
#         self.master.title("Add New Staff")
#         self.master.configure(background='turquoise3')
        
#         # Binding F11 and ESCAPE keys to full screen
#         self.master.bind("<F11>", self.toggle_fullscreen)
#         self.master.bind("<Escape>", self.end_fullscreen)
#         self.state = True
#         self.master.attributes("-fullscreen", True)
        
#         # New_Customer Window Buttons
#         Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
#         Button(self.master,text='Add',command=self.addTo,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
#         Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
#         Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=3)
    
#     # New Customer Label
#         Label(self.master,text='Forename',bg='turquoise3',font='Bembo',fg='black').grid(row=1,column=0,pady=10)
#         Label(self.master,text='Surname',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=0,pady=10)
#         Label(self.master,text='Email',bg='turquoise3',font='Bembo',fg='black').grid(row=3,column=0,pady=10)
#         Label(self.master,text='Mobile Number',bg='turquoise3',font='Bembo',fg='black').grid(row=4,column=0,pady=10)
#         Label(self.master,text='Capabilities',bg='turquoise3',font='Bembo',fg='black').grid(row=5,column=0,pady=10)
#         Label(self.master,text='Availability',bg='turquoise3',font='Bembo',fg='black').grid(row=6,column=0,pady=10)
#         Label(self.master,text='Street Number',bg='turquoise3',font='Bembo',fg='black').grid(row=7,column=0,pady=10)
#         Label(self.master,text='Street Name',bg='turquoise3',font='Bembo',fg='black').grid(row=8,column=0,pady=10)
#         Label(self.master,text='Town',bg='turquoise3',font='Bembo',fg='black').grid(row=9,column=0,pady=10)
#         Label(self.master,text='Postcode',bg='turquoise3',font='Bembo',fg='black').grid(row=10,column=0,pady=10)

#     # New Customer Entry
#         self.forenameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.forenameEntry.grid(row=1,column=1,pady=10,columnspan=2)
        
#         self.surnameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.surnameEntry.grid(row=2,column=1,pady=10,columnspan=2)
        
#         self.EmailEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.EmailEntry.grid(row=3,column=1,pady=10,columnspan=2)
        
#         self.mobileEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.mobileEntry.grid(row=4,column=1,pady=10,columnspan=2)
        
#         self.CapabilitiesEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.CapabilitiesEntry.grid(row=5,column=1,pady=10,columnspan=2)
        
#         self.AvailabilityEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.AvailabilityEntry.grid(row=6,column=1,pady=10,columnspan=2)
        
#         self.streetNumEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.streetNumEntry.grid(row=7,column=1,pady=10,columnspan=2)
        
#         self.streetNameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.streetNameEntry.grid(row=8,column=1,pady=10,columnspan=2)
        
#         self.townEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.townEntry.grid(row=9,column=1,pady=10,columnspan=2)
        
#         self.postcodeEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
#         self.postcodeEntry.grid(row=10,column=1,pady=10,columnspan=2)

    
#     # Quit Program
#     def end(self):
#         t = time()
#         ct = ctime(t)
        
#         db =sqlite3.connect("main.db")
#         cursor = db.cursor()
#         print("--------------------------------")
#         print(ct + "\n" + "Logged out")
#         print("--------------------------------")
#         sql = """UPDATE Time
#             SET LogOut = ?
#             WHERE LogOut = 'NULL'"""
#         cursor.execute(sql,[(ct)])
#         db.commit()
#         db.close()
#         quit()
    
#     # Toggling full screen
#     def toggle_fullscreen(self, event=None):
#         self.state = not self.state 
#         self.master.attributes("-fullscreen", self.state)
#         return "break"
#     def end_fullscreen(self, event=None):
#         self.state = False
#         self.master.attributes("-fullscreen", False)
#         return "break"    
    
#     # Return To 'Menu' Screen
#     def back(self):
#         self.master.withdraw()
#         root2=Toplevel(self.master)
#         root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
#         muGUI=addWindow(root2)
        
#     # Adding To Database
#     def addTo(self):
#         forename=self.forenameEntry.get()
#         surname=self.surnameEntry.get()
#         email=self.EmailEntry.get()
#         capability=self.CapabilitiesEntry.get()
#         availability=self.AvailabilityEntry.get()
#         mobile=self.mobileEntry.get()
#         streetNum=self.streetNumEntry.get()
#         streetName=self.streetNameEntry.get()
#         town=self.townEntry.get()
#         postcode=self.postcodeEntry.get()
        
#         db =sqlite3.connect("main.db")
#         cursor = db.cursor()
#         sql = """INSERT INTO Staff(Forename,Surname,Email,MobileNum,Capabilities,Availability,StreetNum,StreetName,Town,Postcode)
#             VALUES(?,?,?,?,?,?,?,?,?,?)"""
#         cursor.execute(sql,[(forename),(surname),(email),(mobile),(capability),(availability),(streetNum),(streetName),(town),(postcode)])
        
#         if len(forename) > 0 and len(surname) > 0 and len(email) > 0 and len(mobile) > 0 and len(streetNum) > 0 and len(streetName) > 0 and len(town) > 0 and len(postcode) > 0:
#             db.commit()
#             print("\n---------------------------------------------\nNew Staff Committed")
#             Label(self.master,text='Addition Added  ',bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3)
#         else:
#             print("\n---------------------------------------------\n~~New Staff Commit Failed")
#             Label(self.master,text='Addition Failed ',bg='turquoise3',font='Bembo',fg='red').grid(row=1,column=3)
#         db.close()
