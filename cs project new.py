from string import printable
from tkinter import *

import tkinter as tk
from tkinter import ttk
import sqlite3
from time import time,ctime,sleep
import re

from tkinter import messagebox
import mysql.connector


class Home():
    def __init__(self, master):
        self.master = master
        self.master.title("Taxi And Minibus")
        self.master.configure(background='turquoise3')
        
        # Creating Database
        self.createCustomerTable("main.db")
        self.createMasterLoginTable("main.db")
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
        db.close()
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
                db.close()
    
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
                db.close()

    
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
                    Forename TEXT NOT NULL,
                    Driver TEXT NOT NULL)"""
                cursor.execute(sql)
                db.commit()
                print("Bookings Table Created")
                # Adding Fake Data For Testing
                sql ="""INSERT into Bookings(CustomerID,StartStreetNum,StartStreet,StartPostcode,DestinationStreetNum,DestinationStreet,DestinationPostcode,Fufilled,Date,Time,Forename,Driver)
                    VALUES(1,10,"Downing Street","SW1A 2AA",6,"Jameswick Avenue","BB9 5RE","True","16 August 2020","06:30","Dummy","")"""
                cursor.execute(sql)
                
                db.commit()
                print("~~Test Bookings Created~~")
                db.close()
    
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
                db.close()
    
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
                db.close()

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
                db.close()

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
        self.passwordEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35,show = "*")
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
        db.close()

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
        db.close()

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
        Button(self.master,text='Show and Update',command=self.show_data,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
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
        db.close()
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
        db.close()
        
    def show_data(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=showWindow(root2)

#################
class showWindow():
    def __init__(self, master):
        self.master = master
        self.master.title("Show and Update")
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
        db.close()
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

class display_customer():
    def __init__(self, master):
        self.master = master
        self.master.title("Display Customer")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)
        
        # Initialising Strings
        q=StringVar()
        tcustid = StringVar() 
        tfname = StringVar()
        tsname = StringVar()
        temail = StringVar()
        tnum = StringVar()

        # Button
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black').pack(padx=20,pady=20)

        db =sqlite3.connect("main.db")
        cursor = db.cursor()

        # Reloads the Database
        def update(rows):
            trv.delete(*trv.get_children())
            for i in rows:
                trv.insert('', 'end', values=i)
        
        # Finds Row using SQL
        def search():
            q2 = q.get()
            sql = "SELECT CustomerID,Forename,Surname,Email,MobileNum FROM Customer WHERE Forename LIKE '%"+q2+"' OR Surname LIKE '%"+q2+"'"
            cursor.execute(sql)
            rows = cursor.fetchall()
            update(rows)
            
        # Removes Search
        def clear():
            sql = "SELECT CustomerID,Forename,Surname,Email,MobileNum FROM Customer"
            cursor.execute(sql)
            rows = cursor.fetchall()
            update(rows)
        
        # Double Click Auto Imports Data Into Entry
        def getrow(event):
            rowid = trv.identify_row(event.y)
            item = trv.item(trv.focus())
            tcustid.set(item['values'][0])
            tfname.set(item['values'][1])
            tsname.set(item['values'][2])
            temail.set(item['values'][3])
            tnum.set(item['values'][4])

        # Change an existing entry
        def update_customer():
            custid = tcustid.get()
            fname = tfname.get()
            lname = tsname.get()
            email = temail.get()
            num= tnum.get()
            
            # Confirmation Box
            if messagebox.askyesno("Confirmation","Are you sure you want to update this customer?"):
                sql = "UPDATE Customer SET Forename = ?, Surname = ?, Email = ?,  MobileNum = ? WHERE CustomerID = ?"
                cursor.execute(sql,(fname,lname,email,num,custid))
                db.commit()
                clear()
        
        # Adds New Entry
        def add_new():
            fname = tfname.get()
            lname = tsname.get()
            num= tnum.get()
            email = temail.get()
            sql = """INSERT into Customer(Forename,Surname,Email,MobileNum)
                    VALUES(?,?,?,?)"""
            cursor.execute(sql,((fname),(lname),(email),(num)))
            db.commit()
            clear()
            
        # Deletes Entry
        def delete_customer():
            customer_id = tcustid.get()
            if messagebox.askyesno("Confirmation","Are you sure you want to delete this customer?"):
                sql = "DELETE FROM Customer WHERE CustomerID = "+customer_id
                cursor.execute(sql)
                db.commit()
                clear()
            else:
                return True
            
        wrapper1 = LabelFrame(master, text="Customer List",bg='turquoise3')
        wrapper2 = LabelFrame(master, text="Search",bg='turquoise3')
        wrapper3 = LabelFrame(master, text="Customer Data",bg='turquoise3')
        wrapper1.pack(fill="both", expand="yes",padx=20,pady=10)
        wrapper2.pack(fill="both", expand="yes",padx=20,pady=10)
        wrapper3.pack(fill="both", expand="yes",padx=20,pady=10)
        
        trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5), show="headings", height="6")
        trv.pack(fill="both", expand="yes",padx=20,pady=10)
        trv.heading(1, text="CustomerID")
        trv.heading(2, text="Firstname")
        trv.heading(3, text="Lastname")
        trv.heading(4, text="Email")
        trv.heading(5, text="Num")
        
        trv.bind('<Double 1>', getrow)
        
        sql = "SELECT CustomerID,Forename,Surname,Email,MobileNum FROM Customer"
        cursor.execute(sql)
        rows = cursor.fetchall()
        update(rows)
        
        #search section
        SearchLabel = Label(wrapper2, text="Search",bg='turquoise3')
        SearchLabel.pack(side=tk.LEFT, padx=10)
        SearchEntry = Entry(wrapper2, textvariable=q)
        SearchEntry.pack(side=tk.LEFT, padx=6)
        SearchButton = Button(wrapper2, text="Search",command=search)
        SearchButton.pack(side=tk.LEFT, padx=6)
        ClearButton = Button(wrapper2, text="Clear",command=clear)
        ClearButton.pack(side=tk.LEFT, padx=6)
        
        #User Data section
        IDLabel = Label(wrapper3, text="Customer ID",bg='turquoise3')
        IDLabel.grid(row=0, column=0, padx=5, pady=3)
        IDEntry = Entry(wrapper3, textvariable=tcustid)
        IDEntry.grid(row=0, column=1, padx=5, pady=3)
        
        ForenameLabel = Label(wrapper3, text="Forename",bg='turquoise3')
        ForenameLabel.grid(row=1, column=0, padx=5, pady=3)
        ForenameEntry = Entry(wrapper3, textvariable=tfname)
        ForenameEntry.grid(row=1, column=1, padx=5, pady=3)
        
        SurnameLabel = Label(wrapper3, text="Surname",bg='turquoise3')
        SurnameLabel.grid(row=2, column=0, padx=5, pady=3)
        SurnameEntry = Entry(wrapper3, textvariable=tsname)
        SurnameEntry.grid(row=2, column=1, padx=5, pady=3)
        
        EmailLabel = Label(wrapper3, text="Email",bg='turquoise3')
        EmailLabel.grid(row=3, column=0, padx=5, pady=3)
        EmailEntry = Entry(wrapper3, textvariable=temail)
        EmailEntry.grid(row=3, column=1, padx=5, pady=3)
        
        NumLabel = Label(wrapper3, text="Mobile Number",bg='turquoise3')
        NumLabel.grid(row=4, column=0, padx=5, pady=3)
        NumEntry = Entry(wrapper3, textvariable=tnum)
        NumEntry.grid(row=4, column=1, padx=5, pady=3)
        
        # Buttons
        UpdateButton = Button(wrapper3, text="Update", command=update_customer)
        AddButton = Button(wrapper3, text="Add New", command=add_new)
        DeleteButton = Button(wrapper3, text="Delete", command=delete_customer)
        UpdateButton.grid(row=5, column=1,padx=5,pady=3)
        AddButton.grid(row=5, column=0,padx=5,pady=3)
        DeleteButton.grid(row=5, column=2,padx=5,pady=3)
        
    
    # Return To 'Menu' Screen
    def back(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=showWindow(root2)
    # Toggling full screen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state 
        self.master.attributes("-fullscreen", self.state)
        return "break"
    def end_fullscreen(self, event=None):
        self.state = False
        self.master.attributes("-fullscreen", False)
        return "break"    
class display_booking():
    def __init__(self, master):
        self.master = master
        self.master.title("Display Booking")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)
        
        # Initialising Strings
        q=StringVar()
        tcid = StringVar() 
        tfname = StringVar()
        tsname = StringVar()
        temail = StringVar()
        tnum = StringVar()
        tcustid = StringVar() 
        tfname = StringVar()
        tsname = StringVar()
        temail = StringVar()
        tnum = StringVar()
        tcustid = StringVar() 
        tfname = StringVar()
        tsname = StringVar()
        

        # Button
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black').pack(padx=20,pady=20)

        db =sqlite3.connect("main.db")
        cursor = db.cursor()

        # Reloads the Database
        def update(rows):
            trv.delete(*trv.get_children())
            for i in rows:
                trv.insert('', 'end', values=i)
        
        # Finds Row using SQL
        def search():
            q2 = q.get()
            sql = "SELECT CustomerID,Forename,Surname,Email,MobileNum FROM Customer WHERE Forename LIKE '%"+q2+"' OR Surname LIKE '%"+q2+"'"
            cursor.execute(sql)
            rows = cursor.fetchall()
            update(rows)
            
        # Removes Search
        def clear():
            sql = "SELECT CustomerID,Forename,Surname,Email,MobileNum FROM Customer"
            cursor.execute(sql)
            rows = cursor.fetchall()
            update(rows)
        
        # Double Click Auto Imports Data Into Entry
        def getrow(event):
            rowid = trv.identify_row(event.y)
            item = trv.item(trv.focus())
            tcustid.set(item['values'][0])
            tfname.set(item['values'][1])
            tsname.set(item['values'][2])
            temail.set(item['values'][3])
            tnum.set(item['values'][4])

        # Change an existing entry
        def update_customer():
            custid = tcustid.get()
            fname = tfname.get()
            lname = tsname.get()
            email = temail.get()
            num= tnum.get()
            
            # Confirmation Box
            if messagebox.askyesno("Confirmation","Are you sure you want to update this customer?"):
                sql = "UPDATE Customer SET Forename = ?, Surname = ?, Email = ?,  MobileNum = ? WHERE CustomerID = ?"
                cursor.execute(sql,(fname,lname,email,num,custid))
                db.commit()
                clear()
        
        # Adds New Entry
        def add_new():
            fname = tfname.get()
            lname = tsname.get()
            num= tnum.get()
            email = temail.get()
            sql = """INSERT into Customer(Forename,Surname,Email,MobileNum)
                    VALUES(?,?,?,?)"""
            cursor.execute(sql,((fname),(lname),(email),(num)))
            db.commit()
            clear()
            
        # Deletes Entry
        def delete_customer():
            customer_id = tcustid.get()
            if messagebox.askyesno("Confirmation","Are you sure you want to delete this customer?"):
                sql = "DELETE FROM Customer WHERE CustomerID = "+customer_id
                cursor.execute(sql)
                db.commit()
                clear()
            else:
                return True
            
        wrapper1 = LabelFrame(master, text="Customer List",bg='turquoise3')
        wrapper2 = LabelFrame(master, text="Search",bg='turquoise3')
        wrapper3 = LabelFrame(master, text="Customer Data",bg='turquoise3')
        wrapper1.pack(fill="both", expand="yes",padx=20,pady=10)
        wrapper2.pack(fill="both", expand="yes",padx=20,pady=10)
        wrapper3.pack(fill="both", expand="yes",padx=20,pady=10)
        
        trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5), show="headings", height="6")
        trv.pack(fill="both", expand="yes",padx=20,pady=10)
        trv.heading(1, text="CustomerID")
        trv.heading(2, text="Firstname")
        trv.heading(3, text="Lastname")
        trv.heading(4, text="Email")
        trv.heading(5, text="Num")
        
        trv.bind('<Double 1>', getrow)
        
        sql = "SELECT CustomerID,Forename,Surname,Email,MobileNum FROM Customer"
        cursor.execute(sql)
        rows = cursor.fetchall()
        update(rows)
        
        #search section
        SearchLabel = Label(wrapper2, text="Search",bg='turquoise3')
        SearchLabel.pack(side=tk.LEFT, padx=10)
        SearchEntry = Entry(wrapper2, textvariable=q)
        SearchEntry.pack(side=tk.LEFT, padx=6)
        SearchButton = Button(wrapper2, text="Search",command=search)
        SearchButton.pack(side=tk.LEFT, padx=6)
        ClearButton = Button(wrapper2, text="Clear",command=clear)
        ClearButton.pack(side=tk.LEFT, padx=6)
        
        #User Data section
        IDLabel = Label(wrapper3, text="Customer ID",bg='turquoise3')
        IDLabel.grid(row=0, column=0, padx=5, pady=3)
        IDEntry = Entry(wrapper3, textvariable=tcustid)
        IDEntry.grid(row=0, column=1, padx=5, pady=3)
        
        ForenameLabel = Label(wrapper3, text="Forename",bg='turquoise3')
        ForenameLabel.grid(row=1, column=0, padx=5, pady=3)
        ForenameEntry = Entry(wrapper3, textvariable=tfname)
        ForenameEntry.grid(row=1, column=1, padx=5, pady=3)
        
        SurnameLabel = Label(wrapper3, text="Surname",bg='turquoise3')
        SurnameLabel.grid(row=2, column=0, padx=5, pady=3)
        SurnameEntry = Entry(wrapper3, textvariable=tsname)
        SurnameEntry.grid(row=2, column=1, padx=5, pady=3)
        
        EmailLabel = Label(wrapper3, text="Email",bg='turquoise3')
        EmailLabel.grid(row=3, column=0, padx=5, pady=3)
        EmailEntry = Entry(wrapper3, textvariable=temail)
        EmailEntry.grid(row=3, column=1, padx=5, pady=3)
        
        NumLabel = Label(wrapper3, text="Mobile Number",bg='turquoise3')
        NumLabel.grid(row=4, column=0, padx=5, pady=3)
        NumEntry = Entry(wrapper3, textvariable=tnum)
        NumEntry.grid(row=4, column=1, padx=5, pady=3)
        
        # Buttons
        UpdateButton = Button(wrapper3, text="Update", command=update_customer)
        AddButton = Button(wrapper3, text="Add New", command=add_new)
        DeleteButton = Button(wrapper3, text="Delete", command=delete_customer)
        UpdateButton.grid(row=5, column=1,padx=5,pady=3)
        AddButton.grid(row=5, column=0,padx=5,pady=3)
        DeleteButton.grid(row=5, column=2,padx=5,pady=3)
        
    
    # Return To 'Menu' Screen
    def back(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=showWindow(root2)
    # Toggling full screen
    def toggle_fullscreen(self, event=None):
        self.state = not self.state 
        self.master.attributes("-fullscreen", self.state)
        return "break"
    def end_fullscreen(self, event=None):
        self.state = False
        self.master.attributes("-fullscreen", False)
        return "break"    
class display_login():
    def __init__(self, master):
        self.master = master
        self.master.title("Display Login")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)
        
        # New_Customer Window Buttons
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
    
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
        cursor.execute(sql,[ct])
        db.commit()
        db.close()
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
        muGUI=showWindow(root2)
class display_vehicle():
    def __init__(self, master):
        self.master = master
        self.master.title("Display Vehicle")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)
        
        # New_Customer Window Buttons
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
    
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
        cursor.execute(sql,[ct])
        db.commit()
        db.close()
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
        muGUI=showWindow(root2)
class display_staff():
    def __init__(self, master):
        self.master = master
        self.master.title("Display Staff")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)
        
        # New_Customer Window Buttons
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
    
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
        cursor.execute(sql,[ct])
        db.commit()
        db.close()
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
        muGUI=showWindow(root2)
class display_logs():
    def __init__(self, master):
        self.master = master
        self.master.title("Display Logs")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", True)
        
        # New_Customer Window Buttons
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=1)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
    
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
        cursor.execute(sql,[ct])
        db.commit()
        db.close()
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
        muGUI=showWindow(root2)

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
        self.passwordEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35,show = "*")
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
        db.close()

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
        db.close()
        
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
