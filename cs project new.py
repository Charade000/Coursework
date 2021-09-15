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
        self.createMasterLoginTable("main.db")
        self.createDriverLoginTable("main.db")
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
        muGUI=loginMenu(root2)
    
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
                    MobileNum INTEGER NOT NULL)
                    """
                cursor.execute(sql)
                db.commit()
                print("---------------------------------------------\nCustomer Table Created")
                # Adding Fake Data For Testing
                sql="""INSERT into Customer(Forename,Surname,Email,MobileNum)
                    VALUES("Dummy","McDummy","dummy@example.com",0161)"""
                cursor.execute(sql)
                sql="""INSERT into Customer(Forename,Surname,Email,MobileNum)
                    VALUES("Jimmy","Newtron","scientist@example.com",01282524084)"""
                cursor.execute(sql)
                db.commit()
                sql="""INSERT into Customer(Forename,Surname,Email,MobileNum)
                    VALUES("Joe","King","ma@example.com",01282622067)"""
                cursor.execute(sql)
                db.commit()
                sql="""INSERT into Customer(Forename,Surname,Email,MobileNum)
                    VALUES("John","Dane","nextman@gmail.com",111111111)"""
                cursor.execute(sql)
                db.commit()
                print("~~Test Customers Created~~")
    
    # Creating Master Login Database Or Checking If It Exist
    def createMasterLoginTable(self,dbName):
        if 'MasterLogin' in self.getTables(dbName):
            pass
        else:
            with sqlite3.connect(dbName) as db:
                cursor=db.cursor()
                sql ="""CREATE TABLE MasterLogin(
                    StaffEmail TEXT NOT NULL,
                    StaffPassword TEXT NOT NULL)"""
                cursor.execute(sql)
                db.commit()
                print("Master Login Table Created")
                # Adding Fake Data For Testing
                sql ="""INSERT into MasterLogin(StaffEmail,StaffPassword)
                    VALUES("test@example.com","Bean")"""
                cursor.execute(sql)
                db.commit()
                sql ="""INSERT into MasterLogin(StaffEmail,StaffPassword)
                    VALUES("staff@hypothetical.com","password")"""
                cursor.execute(sql)
                db.commit()
                print("~~Test Master Logins Created~~")
                
        # Creating Driver Login Database Or Checking If It Exist
    def createDriverLoginTable(self,dbName):
        if 'DriverLogin' in self.getTables(dbName):
            pass
        else:
            with sqlite3.connect(dbName) as db:
                cursor=db.cursor()
                sql ="""CREATE TABLE DriverLogin(
                    DriverEmail TEXT NOT NULL,
                    DriverPassword TEXT NOT NULL)"""
                cursor.execute(sql)
                db.commit()
                print("Driver Login Table Created")
                # Adding Fake Data For Testing
                sql ="""INSERT into DriverLogin(DriverEmail,DriverPassword)
                    VALUES("driver@example.com","wheel")"""
                cursor.execute(sql)
                db.commit()
                sql ="""INSERT into DriverLogin(DriverEmail,DriverPassword)
                    VALUES("road@hypothetical.com","car")"""
                cursor.execute(sql)
                db.commit()
                print("~~Test Driver Logins Created~~")
    
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
                    StartStreetNum INTEGER NOT NULL,
                    StartStreet TEXT NOT NULL,
                    StartPostcode TEXT NOT NULL,
                    DestinationStreetNum INTEGER NOT NULL,
                    DestinationStreet TEXT NOT NULL,
                    DestinationPostcode TEXT NOT NULL,
                    Fufilled TEXT NOT NULL,
                    Date TEXT NOT NULL,
                    Time TEXT NOT NULL,
                    Forename TEXT NOT NULL)"""
                cursor.execute(sql)
                db.commit()
                print("Bookings Table Created")
                # Adding Fake Data For Testing
                sql ="""INSERT into Bookings(CustomerID,StartStreetNum,StartStreet,StartPostcode,DestinationStreetNum,DestinationStreet,DestinationPostcode,Fufilled,Date,Time,Forename)
                    VALUES(1,10,"Downing Street","SW1A 2AA",6,"Jameswick Avenue","BB9 5RE","True","16 August 2020","06:30","Dummy")"""
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

class loginMenu():
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)

        # Login Page Buttons
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=3)
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=0)
        Button(self.master,text='Master Login',command=self.Master,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=1)
        Button(self.master,text='Driver Login',command=self.Driver,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=2)
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
        
    # Return To 'Home' Screen
    def back(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=Home(root2)
    # Going To Master Login
    def Master(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=MasterLogin(root2)
        
    def Driver(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=DriverLogin(root2)
    
########################################################################################################################################################
########################################################################################################################################################

class MasterLogin():
    def __init__(self, master):
        self.master = master
        self.master.title("Master Login")
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
        self.passwordEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.passwordEntry.grid(row=3,column=2,columnspan=2)

        # Login Page Buttons
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=3)
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=0)
        Button(self.master,text='Login',command=self.checkLogin,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=2)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=4)

        Button(self.master,text='temp bypass',command=self.tempbypass,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=5)

    
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
        
    # Return To 'Menu' Screen
    def back(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=loginMenu(root2)
    
    # Connecting To Database To Check Login
    def checkLogin(self):
        email=self.emailEntry.get()
        password=self.passwordEntry.get()
        t = time()
        ct = ctime(t)
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        sql = """SELECT * from MasterLogin WHERE StaffEmail= ? AND StaffPassword = ?"""
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
        muGUI=MasterMenu(root2)
    
    def tempbypass(self):
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
        muGUI=MasterMenu(root2)

class MasterMenu():
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
        muGUI=MasterLogin(root2)
        
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
        Button(self.master,text='Add Driver',command=self.add_driver,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=5)


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
        muGUI=MasterMenu(root2)
        
        
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
        
    def add_driver(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))

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
        Button(self.master,text='Add Customer',command=self.addTo,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
        Button(self.master,text='Add And Continue',command=self.advBooking,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=3)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=4)
    
    # New Customer Label
        Label(self.master,text='Forename',bg='turquoise3',font='Bembo',fg='black').grid(row=1,column=0,pady=10)
        Label(self.master,text='Surname',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=0,pady=10)
        Label(self.master,text='Email',bg='turquoise3',font='Bembo',fg='black').grid(row=3,column=0,pady=10)
        Label(self.master,text='Mobile Number',bg='turquoise3',font='Bembo',fg='black').grid(row=4,column=0,pady=10)

    # New Customer Entry
        self.forenameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.forenameEntry.grid(row=1,column=1,pady=10,columnspan=2)
        
        self.surnameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.surnameEntry.grid(row=2,column=1,pady=10,columnspan=2)
        
        self.emailEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.emailEntry.grid(row=3,column=1,pady=10,columnspan=2)
        
        self.mobileEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.mobileEntry.grid(row=4,column=1,pady=10,columnspan=2)


    
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
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        sql = """INSERT INTO Customer(Forename,Surname,Email,MobileNum)
            VALUES(?,?,?,?)"""
        cursor.execute(sql,[(forename),(surname),(email),(mobile)])
        
        if len(forename) > 0 and len(surname) > 0 and len(email) > 0 and len(mobile):
            db.commit()
            print("\n---------------------------------------------\nNew Customer Committed")
            Label(self.master,text='Addition Added  ',bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3)
        else:
            print("\n---------------------------------------------\n~~New Customer Commit Failed")
            Label(self.master,text='Addition Failed ',bg='turquoise3',font='Bembo',fg='red').grid(row=1,column=3)
            
    def advBooking(self):
        forename=self.forenameEntry.get()
        surname=self.surnameEntry.get()
        email=self.emailEntry.get()
        mobile=self.mobileEntry.get()
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        sql = """INSERT INTO Customer(Forename,Surname,Email,MobileNum)
            VALUES(?,?,?,?)"""
        cursor.execute(sql,[(forename),(surname),(email),(mobile)])
        
        if len(forename) > 0 and len(surname) > 0 and len(email) > 0 and len(mobile):
            db.commit()
            print("\n---------------------------------------------\nNew Customer Committed")
            Label(self.master,text='Addition Added  ',bg='turquoise3',font='Bembo',fg='green').grid(row=1,column=3)
            
            self.master.withdraw()
            root2=Toplevel(self.master)
            root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
            muGUI=CusBooking(root2)
        
        else:
            print("\n---------------------------------------------\n~~New Customer Commit Failed")
            Label(self.master,text='Addition Failed ',bg='turquoise3',font='Bembo',fg='red').grid(row=1,column=3)
class CusBooking():
    def __init__(self, master):
        self.master = master
        self.master.title("Add New Login")
        self.master.configure(background='turquoise3')
        
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
        Button(self.master,text='Find Customer',command=self.find_customer,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=12,column=5)

    
    # New Customer Label
        Label(self.master,text='StartStreetNum',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=0,pady=10)
        Label(self.master,text='StartStreet',bg='turquoise3',font='Bembo',fg='black').grid(row=3,column=0,pady=10)
        Label(self.master,text='StartPostcode',bg='turquoise3',font='Bembo',fg='black').grid(row=4,column=0,pady=10)
        Label(self.master,text='DestinationStreetNum',bg='turquoise3',font='Bembo',fg='black').grid(row=5,column=0,pady=10)
        Label(self.master,text='DestinationStreet',bg='turquoise3',font='Bembo',fg='black').grid(row=6,column=0,pady=10)
        Label(self.master,text='DestinationPostcode',bg='turquoise3',font='Bembo',fg='black').grid(row=7,column=0,pady=10)
        Label(self.master,text='Fufilled',bg='turquoise3',font='Bembo',fg='black').grid(row=8,column=0,pady=10)
        Label(self.master,text='Date',bg='turquoise3',font='Bembo',fg='black').grid(row=9,column=0,pady=10,padx=10)
        Label(self.master,text='Time',bg='turquoise3',font='Bembo',fg='black').grid(row=10,column=0,pady=10,padx=10)
        Label(self.master,text='CustomerID',bg='turquoise3',font='Bembo',fg='black').grid(row=11,column=0,pady=10)
        Label(self.master,text='Forename',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=3,pady=10,padx=10)
        Label(self.master,text='Surname',bg='turquoise3',font='Bembo',fg='black').grid(row=3,column=3,pady=10,padx=10)



    # New Booking Entry
        
        self.StartStreetNumEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.StartStreetNumEntry.grid(row=2,column=1,pady=10,columnspan=2)

        self.StartStreetEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.StartStreetEntry.grid(row=3,column=1,pady=10,columnspan=2)
        
        self.StartPostcodeEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.StartPostcodeEntry.grid(row=4,column=1,pady=10,columnspan=2)

        self.DestinationStreetNumEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.DestinationStreetNumEntry.grid(row=5,column=1,pady=10,columnspan=2)
        
        self.DestinationStreetEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.DestinationStreetEntry.grid(row=6,column=1,pady=10,columnspan=2)
        
        self.DestinationPostcodeEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.DestinationPostcodeEntry.grid(row=7,column=1,pady=10,columnspan=2)
        
        self.FufilledEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.FufilledEntry.grid(row=8,column=1,pady=10,columnspan=2)
        
        self.DateEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.DateEntry.grid(row=9,column=1,pady=10,columnspan=2)
        
        self.TimeEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.TimeEntry.grid(row=10,column=1,pady=10,columnspan=2)
        
        self.CustomerIDEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.CustomerIDEntry.grid(row=11,column=1,pady=10,columnspan=2)
        
        self.ForenameEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.ForenameEntry.grid(row=2,column=4,pady=10,columnspan=2)
        
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
    
    # Find CustomerID
    def find_customer(self):
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        
        Forename=self.ForenameEntry.get()
        Surname=self.SurnameEntry.get()
        
        if len(Forename) >=  1 :
            sql = """SELECT CustomerID FROM CUSTOMER WHERE Forename LIKE ?"""
            cursor.execute(sql,[(Forename)])
            result=cursor.fetchall()
            if result:
                Label(self.master,text='Customer Found',bg='turquoise3',font='Bembo',fg='red').grid(row=12,column=5)
        elif len(Surname) >= 1:
            sql = """SELECT CustomerID FROM CUSTOMER WHERE Surname LIKE ?"""
            cursor.execute(sql,[(Surname)])
            result=cursor.fetchall()
        if result:
            Label(self.master,text='Customer Found',bg='PaleTurquoise1',font='Bembo',fg='red').grid(row=12,column=5)
            #################
            # Turn To DropBox
            print(result)
            Label(self.master,text=result,bg='turquoise3',font='Bembo',fg='black').grid(row=12,column=6,pady=10,padx=10)
            ###############################
            
        customer=result

    # Adding To Database
    def addTo(self):
        StartStreetNum=self.StartStreetNumEntry.get()
        StartStreet=self.StartStreetEntry.get()
        StartPostcode=self.StartPostcodeEntry.get()
        DestinationStreetNum =self.DestinationStreetNumEntry.get()
        DestinationStreet=self.DestinationStreetEntry.get()
        DestinationPostcode=self.DestinationPostcodeEntry.get()
        Fufilled=self.FufilledEntry.get()
        Date=self.DateEntry.get()
        Time=self.TimeEntry.get()
        CustomerID=self.CustomerIDEntry.get()
        if len(CustomerID) == 0:
            CustomerID=self.customer.get()

        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        sql = """INSERT INTO Bookings(CustomerID,StartStreetNum,StartStreet,StartPostcode,DestinationStreetnum,DestinationStreet,DestinationPostcode,Fufilled,Date,Time)
            VALUES(?,?,?,?,?,?,?,?,?,?)"""
        cursor.execute(sql,[(CustomerID),(StartStreetNum),(StartStreet),(StartPostcode),(DestinationStreetNum),(DestinationStreet),(DestinationPostcode),(Fufilled),(Date),(Time)])
        
        if len(CustomerID) >= 0 and len(StartStreetNum) > 0 and len(StartStreet) > 0 and len(StartPostcode) > 0 and len(DestinationStreetNum) > 0 and len(DestinationStreet) > 0 and len(DestinationPostcode) > 0 and len(Fufilled) > 0 and len(Date) > 0 and len(Time):
            db.commit()
            print("\n---------------------------------------------\nNew Booking Committed")
            Label(self.master,text='Addition Added  ',bg='turquoise3',font='Bembo',fg='green').grid(row=9,column=1)
        else:
            print("\n---------------------------------------------\n~~New Booking Commit Failed")
            Label(self.master,text='Addition Failed ',bg='turquoise3',font='Bembo',fg='red').grid(row=9,column=1)


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

#################
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
########################################################################################################################################################
########################################################################################################################################################

class DriverLogin():
    def __init__(self, master):
        self.master = master
        self.master.title("Driver Login")
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
        self.passwordEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.passwordEntry.grid(row=3,column=2,columnspan=2)

        # Login Page Buttons
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=3)
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=0)
        Button(self.master,text='Login',command=self.checkLogin,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=2)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=4)

        Button(self.master,text='temp bypass',command=self.tempbypass,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=5)

    
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
        muGUI=loginMenu(root2)
    
    # Connecting To Database To Check Login
    def checkLogin(self):
        email=self.emailEntry.get()
        password=self.passwordEntry.get()
        t = time()
        ct = ctime(t)
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        sql = """SELECT * from DriverLogin WHERE DriverEmail= ? AND DriverPassword = ?"""
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
    
    def tempbypass(self):
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

########################################################################################################################################################

def main():
    root=Tk()
    myGUIWelcome=Home(root)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.mainloop()
if __name__ == '__main__':
    main()
