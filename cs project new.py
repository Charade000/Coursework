from tkinter import *
import tkinter as tk
from tkinter import ttk
import sqlite3
from time import time,ctime
from tkinter import messagebox


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
        self.master.attributes("-fullscreen", False)
        

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
                    List INTEGER PRIMARY KEY AUTOINCREMENT,
                    StaffEmail TEXT NOT NULL,
                    StaffPassword TEXT NOT NULL,
                    Type TEXT NOT NULL)"""
                cursor.execute(sql)
                db.commit()
                print("Master Login Table Created")
                # Adding Fake Data For Testing
                sql ="""INSERT into MasterLogin(StaffEmail,StaffPassword,Type)
                    VALUES("test@example.com","Bean","Driver")"""
                cursor.execute(sql)
                db.commit()
                sql ="""INSERT into MasterLogin(StaffEmail,StaffPassword,Type)
                    VALUES("staff@hypothetical.com","password","Staff")"""
                cursor.execute(sql)
                db.commit()
                print("~~Test Master Logins Created~~")

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
                    StaffID Integer NOT NULL)"""
                cursor.execute(sql)
                db.commit()
                print("Bookings Table Created")
                # Adding Fake Data For Testing
                sql ="""INSERT into Bookings(CustomerID,StartStreetNum,StartStreet,StartPostcode,DestinationStreetNum,DestinationStreet,DestinationPostcode,Fufilled,Date,Time,Forename,StaffID)
                    VALUES(1,10,"Downing Street","SW1A 2AA",6,"Jameswick Avenue","BB9 5RE","True","16 August 2020","06:30","Dummy","1")"""
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
                print("---------------------------------------------\nTime Table Created")

class loginMenu(Home):
    def __init__(self,master):
        self.master = master
        super().toggle_fullscreen
        super().end
        
        # self.master = master
        self.master.title("Login")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", False)

        # Login Page Buttons#]#]
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=3)
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=0)
        Button(self.master,text='Master Login',command=self.Master,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=1)
        Button(self.master,text='Driver Login',command=self.Driver,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=2)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=4)

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

class MasterLogin(Home):
    def __init__(self, master):
        self.master = master
        super().toggle_fullscreen
        super().end
        self.master.title("Master Login")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", False)
        
        
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

        Button(self.master,text='temp bypass',command=self.menu,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=5)

    
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
        type = "Staff"
        t = time()
        ct = ctime(t)
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        sql = """SELECT * from MasterLogin WHERE StaffEmail= ? AND StaffPassword = ? AND Type = ?"""
        cursor.execute(sql,[(email),(password),(type)])
        result=cursor.fetchall()
        if result:
            print("--------------------------------")
            print(ct + "\n" + email + " has logged in")
            print("--------------------------------")
            sql = """INSERT INTO Time(Email,LogIn,LogOut)
                VALUES(?,?,?)"""
            cursor.execute(sql,[(email),(ct),('NULL')])
            db.commit()
            db.close()
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

class MasterMenu(Home):
    def __init__(self, master):
        self.master = master
        super().toggle_fullscreen
        super().end
        self.master.title("Logged In")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", False)
        
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
        
        db.close()
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=MasterLogin(root2)
        
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
        self.master.attributes("-fullscreen", False)
        
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
        self.master.attributes("-fullscreen", False)
        
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
        
        tree_scrollx = Scrollbar(wrapper1, orient ="horizontal")
        tree_scrollx.pack(side=BOTTOM, fill="x")
            
        tree_scrolly = Scrollbar(wrapper1, orient ="vertical")
        tree_scrolly.pack(side=RIGHT, fill="y")
        
        trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5), xscrollcommand = tree_scrollx.set, yscrollcommand = tree_scrolly.set, show="headings", height="6")
        trv.pack(fill="both", expand="yes",padx=20,pady=10)
        tree_scrollx.config(command = trv.xview)
        tree_scrolly.config(command = trv.yview)
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
            self.master.attributes("-fullscreen", False)
            
            # Initialising Strings
            q=StringVar()
            tlist=  StringVar()
            temail = StringVar() 
            tpass = StringVar()
            ttype= StringVar()
            
            # Button
            Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black').pack(padx=20,pady=20)

            # db =sqlite3.connect("main.db")
            # cursor = db.cursor()

            # Reloads the Database
            def update(rows):
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                trv.delete(*trv.get_children())
                for i in rows:
                    trv.insert('', 'end', values=i)
                db.close()
            
            # Finds Row using SQL
            def search():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                q2 = q.get()
                sql = "SELECT List,StaffEmail,StaffPassword,Type FROM MasterLogin WHERE List LIKE '%"+q2+"' OR StaffEmail LIKE '%"+q2+"' OR StaffPassword LIKE '%"+q2+"' OR Type LIKE '%"+q2+"'"
                cursor.execute(sql)
                rows = cursor.fetchall()
                update(rows)
                db.close()
                
            # Removes Search
            def clear():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                sql = "SELECT List,StaffEmail,StaffPassword,Type FROM MasterLogin"
                cursor.execute(sql)
                rows = cursor.fetchall()
                update(rows)
                db.close()
            
            # Double Click Auto Imports Data Into Entry
            def getrow(event):
                rowid = trv.identify_row(event.y)
                
                item = trv.item(trv.focus())
                tlist.set(item['values'][0])
                temail.set(item['values'][1])
                tpass.set(item['values'][2])
                ttype.set(item['values'][3])
                
            # Change an existing entry
            def update_login():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                
                staffemail = temail.get()
                stafflist = tlist.get()
                staffpass = tpass.get()
                type = ttype.get()
                

                # Confirmation Box
                if messagebox.askyesno("Confirmation","Are you sure you want to update this Login?"):
                    sql = "UPDATE MasterLogin SET StaffEmail = ?, StaffPassword = ?, Type = ? WHERE List = ? "
                    cursor.execute(sql,(staffemail,staffpass,type,stafflist))

                    db.commit()
                    clear()
                db.commit()
                db.close()
            
            # Adds New Entry
            def add_new():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                staffemail = temail.get()
                staffpass = tpass.get()
                type = ttype.get()
                
                sql = """INSERT into MasterLogin (StaffEmail, StaffPassword, Type)
                        VALUES(?,?,?)"""
                cursor.execute(sql,((staffemail),(staffpass),(type)))
                    
                db.commit()
                db.close()
                clear()
                
            # Deletes Entry
            def delete_login():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                list = tlist.get()
                if messagebox.askyesno("Warning","This will delete all Logins which have this Email and Password!"):
                    sql = "DELETE FROM Masterlogin WHERE List = ?"
                    cursor.execute(sql,((list)))
                    db.commit()
                    db.close()
                    clear()
                else:
                    db.close()
                    return True
                
            wrapper1 = LabelFrame(master, text="Login List",bg='turquoise3')
            wrapper2 = LabelFrame(master, text="Search",bg='turquoise3')
            wrapper3 = LabelFrame(master, text="Login Data",bg='turquoise3')
            wrapper1.pack(fill="both", expand="yes",padx=20,pady=10)
            wrapper2.pack(fill="both", expand="yes",padx=20,pady=10)
            wrapper3.pack(fill="both", expand="yes",padx=20,pady=10)
            
            tree_scrollx = Scrollbar(wrapper1, orient ="horizontal")
            tree_scrollx.pack(side=BOTTOM, fill="x")
            
            tree_scrolly = Scrollbar(wrapper1, orient ="vertical")
            tree_scrolly.pack(side=RIGHT, fill="y")
            
            trv = ttk.Treeview(wrapper1, columns=(1,2,3,4), xscrollcommand = tree_scrollx.set, yscrollcommand = tree_scrolly.set, show="headings", height="6")
            trv.pack(fill="both", expand="yes",padx=20,pady=10)
            tree_scrollx.config(command = trv.xview)
            tree_scrolly.config(command = trv.yview)
            trv.heading(1, text="List")
            trv.heading(2, text="StaffEmail")
            trv.heading(3, text="StaffPassword")
            trv.heading(4, text="Type")

            
            trv.bind('<Double 1>', getrow)
            
            db =sqlite3.connect("main.db")
            cursor = db.cursor()
            
            sql = "SELECT List, StaffEmail, StaffPassword, Type FROM MasterLogin"
            cursor.execute(sql)
            rows = cursor.fetchall()
            update(rows)
            db.close()
            
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
            StaffEmailLabel = Label(wrapper3, text="Staff Email",bg='turquoise3') ############////////////////''
            StaffEmailLabel.grid(row=0, column=0, padx=5, pady=3)
            StaffEmailEntry = Entry(wrapper3, textvariable=temail)
            StaffEmailEntry.grid(row=0, column=1, padx=5, pady=3)
            
            StaffPasswordLabel = Label(wrapper3, text="Staff Password",bg='turquoise3')
            StaffPasswordLabel.grid(row=1, column=0, padx=5, pady=3)
            StaffPasswordEntry = Entry(wrapper3, textvariable=tpass)
            StaffPasswordEntry.grid(row=1, column=1, padx=5, pady=3)
            
            StaffListLabel = Label(wrapper3, text="List",bg='turquoise3')
            StaffListLabel.grid(row=2, column=0, padx=5, pady=3)
            StaffListEntry = Entry(wrapper3, textvariable=tlist)
            StaffListEntry.grid(row=2, column=1, padx=5, pady=3)
            
            TypeLabel = Label(wrapper3, text="Type",bg='turquoise3')
            TypeLabel.grid(row=2, column=0, padx=5, pady=3)
            TypeEntry = Entry(wrapper3, textvariable=ttype)
            TypeEntry.grid(row=2, column=1, padx=5, pady=3)
            
            # Buttons
            UpdateButton = Button(wrapper3, text="Update", command=update_login)
            AddButton = Button(wrapper3, text="Add New", command=add_new)
            DeleteButton = Button(wrapper3, text="Delete", command=delete_login)
            UpdateButton.grid(row=13, column=1,padx=5,pady=3)
            AddButton.grid(row=13, column=0,padx=5,pady=3)
            DeleteButton.grid(row=13, column=2,padx=5,pady=3)
            
            
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
            self.master.attributes("-fullscreen", False)
            
            # Initialising Strings
            q=StringVar()
            tbookingid = StringVar() 
            tcustid = StringVar()
            tstartstreetnum = StringVar()
            tstartstreet = StringVar()
            tstartpost = StringVar()
            tdeststreetnum = StringVar() 
            tdeststreet = StringVar()
            tdestpost = StringVar()
            tfufilled = StringVar()
            tdate = StringVar()
            ttime = StringVar() 
            tforename = StringVar()
            tdriver = StringVar()
            
            # Button
            Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black').pack(padx=20,pady=20)

            # db =sqlite3.connect("main.db")
            # cursor = db.cursor()

            # Reloads the Database
            def update(rows):
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                trv.delete(*trv.get_children())
                for i in rows:
                    trv.insert('', 'end', values=i)
                db.close()
            
            # Finds Row using SQL
            def search():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                q2 = q.get()
                sql = "SELECT BookingsID,CustomerID,StartStreetNum,StartStreet,StartPostcode,DestinationStreetNum,DestinationStreet,DestinationPostcode,Fufilled,Date,Time,Forename,StaffID FROM Bookings WHERE Forename LIKE '%"+q2+"' OR Driver LIKE '%"+q2+"' OR Date LIKE '%"+q2+"' OR StartPostcode LIKE '%"+q2+"' OR CustomerID LIKE '%"+q2+"' OR Fufilled LIKE '%"+q2+"' OR StartStreet LIKE '%"+q2+"' OR BookingsID LIKE '%"+q2+"' OR DestinationStreet LIKE '%"+q2+"' OR DestinationPostcode LIKE '%"+q2+"' ORDER BY Time ASC"
                cursor.execute(sql)
                rows = cursor.fetchall()
                update(rows)
                db.close()
                
            # Removes Search
            def clear():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                sql = "SELECT BookingsID,CustomerID,StartStreetNum,StartStreet,StartPostcode,DestinationStreetNum,DestinationStreet,DestinationPostcode,Fufilled,Date,Time,Forename,StaffID FROM Bookings ORDER BY Time ASC"
                cursor.execute(sql)
                rows = cursor.fetchall()
                update(rows)
                db.close()
            
            # Double Click Auto Imports Data Into Entry
            def getrow(event):
                rowid = trv.identify_row(event.y)
                
                item = trv.item(trv.focus())
                tbookingid.set(item['values'][0])
                tcustid.set(item['values'][1])
                tstartstreetnum.set(item['values'][2])
                tstartstreet.set(item['values'][3])
                tstartpost.set(item['values'][4])
                tdeststreetnum.set(item['values'][5])
                tdeststreet.set(item['values'][6])
                tdestpost.set(item['values'][7])
                tfufilled.set(item['values'][8])
                tdate.set(item['values'][9])
                ttime.set(item['values'][10])
                tforename.set(item['values'][11])
                tdriver.set(item['values'][12])
                
            # Change an existing entry
            def update_booking():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                bookingid = tbookingid.get()
                customerid = tcustid.get()
                startstreetnum = tstartstreetnum.get()
                startstreet = tstartstreet.get()
                startpost = tstartpost.get()
                deststreetnum = tdeststreetnum.get()
                deststreet = tdeststreet.get()
                destpost = tdestpost.get()
                fufilled = tfufilled.get()
                date = tdate.get()
                time = ttime.get()
                forename = tforename.get()
                driver = tdriver.get()
                

                # Confirmation Box
                if messagebox.askyesno("Confirmation","Are you sure you want to update this Booking?"):
                    sql = "UPDATE Bookings SET CustomerID = ? , StartStreetNum = ? , StartStreet = ? , StartPostcode = ? , DestinationStreetNum = ? , DestinationStreet = ? , DestinationPostcode = ? , Fufilled = ? ,Date = ?, Time = ?, Forename = ?, StaffID = ? WHERE BookingsID = ?"
                    cursor.execute(sql,(customerid,startstreetnum,startstreet,startpost,deststreetnum,deststreet,destpost,fufilled,date,time,forename,driver,bookingid))

                    db.commit()
                    clear()
                db.commit()
                db.close()
            
            # Adds New Entry
            def add_new():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                customerid = tcustid.get()
                startstreetnum = tstartstreetnum.get()
                startstreet = tstartstreet.get()
                startpost = tstartpost.get()
                deststreetnum = tdeststreetnum.get()
                deststreet = tdeststreet.get()
                destpost = tdestpost.get()
                fufilled = tfufilled.get()
                date = tdate.get()
                time = ttime.get()
                forename = tforename.get()
                driver = tdriver.get()
                sql = """INSERT into Bookings (CustomerID, StartStreetNum,StartStreet,StartPostcode,DestinationStreetNum,DestinationStreet,DestinationPostcode,Fufilled,Date,Time,Forename,StaffID)
                        VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"""
                cursor.execute(sql,((customerid),(startstreetnum),(startstreet),(startpost),(deststreetnum),(deststreet),(destpost),(fufilled),(date),(time),(forename),(driver)))
                    
                db.commit()
                db.close()
                clear()
                
            # Deletes Entry
            def delete_booking():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                bookingid = tbookingid.get()
                if messagebox.askyesno("Confirmation","Are you sure you want to delete this Booking?"):
                    sql = "DELETE FROM Bookings WHERE BookingsID = "+bookingid
                    cursor.execute(sql)
                    db.commit()
                    db.close()
                    clear()
                else:
                    db.close()
                    return True
                
            wrapper1 = LabelFrame(master, text="Bookings List",bg='turquoise3')
            wrapper2 = LabelFrame(master, text="Search",bg='turquoise3')
            wrapper3 = LabelFrame(master, text="Booking Data",bg='turquoise3')
            wrapper1.pack(fill="both", expand="yes",padx=20,pady=10)
            wrapper2.pack(fill="both", expand="yes",padx=20,pady=10)
            wrapper3.pack(fill="both", expand="yes",padx=20,pady=10)
            
            tree_scrollx = Scrollbar(wrapper1, orient ="horizontal")
            tree_scrollx.pack(side=BOTTOM, fill="x")
            
            tree_scrolly = Scrollbar(wrapper1, orient ="vertical")
            tree_scrolly.pack(side=RIGHT, fill="y")
            
            trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15), xscrollcommand = tree_scrollx.set, yscrollcommand = tree_scrolly.set, show="headings", height="6")
            trv.pack(fill="both", expand="yes",padx=20,pady=10)
            tree_scrollx.config(command = trv.xview)
            tree_scrolly.config(command = trv.yview)
            trv.heading(1, text="BookingID")
            trv.heading(2, text="CustomerID")
            trv.heading(3, text="StartStreetNum")
            trv.heading(4, text="StartStreet")
            trv.heading(5, text="StartStreetPostcode")
            trv.heading(6, text="DestinationStreetNum")
            trv.heading(7, text="DestinationStreet")
            trv.heading(8, text="DestinationStreetPostcode")
            trv.heading(9, text="Fufilled")
            trv.heading(10, text="Date")
            trv.heading(11, text="Time")
            trv.heading(12, text="Forename")
            trv.heading(13, text="StaffID")
            
            trv.bind('<Double 1>', getrow)
            
            db =sqlite3.connect("main.db")
            cursor = db.cursor()
            
            sql = "SELECT BookingsID, CustomerID, StartStreetNum,StartStreet,StartPostcode,DestinationStreetNum,DestinationStreet,DestinationPostcode,Fufilled,Date,Time,Forename,StaffID FROM Bookings ORDER BY Time ASC"
            cursor.execute(sql)
            rows = cursor.fetchall()
            update(rows)
            db.close()
            
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
            BookIDLabel = Label(wrapper3, text="Booking ID",bg='turquoise3') ############////////////////''
            BookIDLabel.grid(row=0, column=0, padx=5, pady=3)
            BookIDEntry = Entry(wrapper3, textvariable=tbookingid)
            BookIDEntry.grid(row=0, column=1, padx=5, pady=3)
            
            CustIDLabel = Label(wrapper3, text="Customer ID",bg='turquoise3')
            CustIDLabel.grid(row=1, column=0, padx=5, pady=3)
            CustIDEntry = Entry(wrapper3, textvariable=tcustid)
            CustIDEntry.grid(row=1, column=1, padx=5, pady=3)
            
            startstreetnumLabel = Label(wrapper3, text="Start Street Num",bg='turquoise3')
            startstreetnumLabel.grid(row=2, column=0, padx=5, pady=3)
            startstreetnumEntry = Entry(wrapper3, textvariable=tstartstreetnum)
            startstreetnumEntry.grid(row=2, column=1, padx=5, pady=3)
            
            startstreetLabel = Label(wrapper3, text="Start Street",bg='turquoise3')
            startstreetLabel.grid(row=3, column=0, padx=5, pady=3)
            startstreetEntry = Entry(wrapper3, textvariable=tstartstreet)
            startstreetEntry.grid(row=3, column=1, padx=5, pady=3)
            
            startpostLabel = Label(wrapper3, text="Start Postcode",bg='turquoise3')
            startpostLabel.grid(row=4, column=0, padx=5, pady=3)
            startpostEntry = Entry(wrapper3, textvariable=tstartpost)
            startpostEntry.grid(row=4, column=1, padx=5, pady=3)
            
            deststreetnumLabel = Label(wrapper3, text="Dest Street Num",bg='turquoise3')
            deststreetnumLabel.grid(row=5, column=0, padx=5, pady=3)
            deststreetnumEntry = Entry(wrapper3, textvariable=tdeststreetnum)
            deststreetnumEntry.grid(row=5, column=1, padx=5, pady=3)
            
            DestStreetLabel = Label(wrapper3, text="Dest Street",bg='turquoise3')
            DestStreetLabel.grid(row=6, column=0, padx=5, pady=3)
            DestStreetEntry = Entry(wrapper3, textvariable=tdeststreet)
            DestStreetEntry.grid(row=6, column=1, padx=5, pady=3)
            
            destpostLabel = Label(wrapper3, text="Dest Postcode",bg='turquoise3')
            destpostLabel.grid(row=7, column=0, padx=5, pady=3)
            destpostEntry = Entry(wrapper3, textvariable=tdestpost)
            destpostEntry.grid(row=7, column=1, padx=5, pady=3)
            
            fufilledLabel = Label(wrapper3, text="Fufilled",bg='turquoise3')
            fufilledLabel.grid(row=8, column=0, padx=5, pady=3)
            fufilledEntry = Entry(wrapper3, textvariable=tfufilled)
            fufilledEntry.grid(row=8, column=1, padx=5, pady=3)
            
            dateLabel = Label(wrapper3, text="Date",bg='turquoise3')
            dateLabel.grid(row=9, column=0, padx=5, pady=3)
            dateEntry = Entry(wrapper3, textvariable=tdate)
            dateEntry.grid(row=9, column=1, padx=5, pady=3)
            
            timeLabel = Label(wrapper3, text="Time",bg='turquoise3')
            timeLabel.grid(row=10, column=0, padx=5, pady=3)
            timeEntry = Entry(wrapper3, textvariable=ttime)
            timeEntry.grid(row=10, column=1, padx=5, pady=3)
            
            forenameLabel = Label(wrapper3, text="Forename",bg='turquoise3')
            forenameLabel.grid(row=11, column=0, padx=5, pady=3)
            forenameEntry = Entry(wrapper3, textvariable=tforename)
            forenameEntry.grid(row=11, column=1, padx=5, pady=3)
            
            driverLabel = Label(wrapper3, text="StaffID",bg='turquoise3')
            driverLabel.grid(row=12, column=0, padx=5, pady=3)
            driverEntry = Entry(wrapper3, textvariable=tdriver)
            driverEntry.grid(row=12, column=1, padx=5, pady=3)
            
            # Buttons
            UpdateButton = Button(wrapper3, text="Update", command=update_booking)
            AddButton = Button(wrapper3, text="Add New", command=add_new)
            DeleteButton = Button(wrapper3, text="Delete", command=delete_booking)
            UpdateButton.grid(row=13, column=1,padx=5,pady=3)
            AddButton.grid(row=13, column=0,padx=5,pady=3)
            DeleteButton.grid(row=13, column=2,padx=5,pady=3)
            
            
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
class display_vehicle():
    def __init__(self, master):
        
            self.master = master
            self.master.title("Display Vehicle")
            self.master.configure(background='turquoise3')
            
            # Binding F11 and ESCAPE keys to full screen
            self.master.bind("<F11>", self.toggle_fullscreen)
            self.master.bind("<Escape>", self.end_fullscreen)
            self.state = True
            self.master.attributes("-fullscreen", False)
            
            # Initialising Strings
            q=StringVar()
            tvehicleid = StringVar() 
            tmot = StringVar()
            tmileage = StringVar()
            tseats = StringVar()
            tmake = StringVar()
            tavailability = StringVar() 
            tstaffid = StringVar()
            
            # Button
            Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black').pack(padx=20,pady=20)

            # db =sqlite3.connect("main.db")
            # cursor = db.cursor()

            # Reloads the Database
            def update(rows):
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                trv.delete(*trv.get_children())
                for i in rows:
                    trv.insert('', 'end', values=i)
                db.close()
            
            # Finds Row using SQL
            def search():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                q2 = q.get()
                sql = "SELECT VehicleID,MOT,Mileage,Seats,Make,Availability,StaffID FROM Vehicle WHERE VehicleID LIKE '%"+q2+"' OR MOT LIKE '%"+q2+"' OR Mileage LIKE '%"+q2+"' OR Seats LIKE '%"+q2+"' OR Make LIKE '%"+q2+"' OR Availability LIKE '%"+q2+"' OR StaffID LIKE '%"+q2+"'"
                cursor.execute(sql)
                rows = cursor.fetchall()
                update(rows)
                db.close()
                
            # Removes Search
            def clear():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                sql = "SELECT VehicleID,MOT,Mileage,Seats,Make,Availability,StaffID FROM Vehicle"
                cursor.execute(sql)
                rows = cursor.fetchall()
                update(rows)
                db.close()
            
            # Double Click Auto Imports Data Into Entry
            def getrow(event):
                rowid = trv.identify_row(event.y)
                
                item = trv.item(trv.focus())
                tvehicleid.set(item['values'][0])
                tmot.set(item['values'][1])
                tmileage.set(item['values'][2])
                tseats.set(item['values'][3])
                tmake.set(item['values'][4])
                tavailability.set(item['values'][5])
                tstaffid.set(item['values'][6])
                
            # Change an existing entry
            def update_vehicle():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                vehicleid = tvehicleid.get()
                mot = tmot.get()
                mileage = tmileage.get()
                seats = tseats.get()
                make = tmake.get()
                availability = tavailability.get()
                staff = tstaffid.get()
                

                # Confirmation Box
                if messagebox.askyesno("Confirmation","Are you sure you want to update this Vehicle?"):
                    sql = "UPDATE Vehicle SET MOT = ? , Mileage = ? , Seats = ? , Make = ? , Availability = ? , StaffID = ? WHERE VehicleID = ?"
                    cursor.execute(sql,(mot,mileage,seats,make,availability,staff,vehicleid))

                    db.commit()
                    clear()
                db.commit()
                db.close()
            
            # Adds New Entry
            def add_new():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                vehicleid = tvehicleid.get()
                mot = tmot.get()
                mileage = tmileage.get()
                seats = tseats.get()
                make = tmake.get()
                availability = tavailability.get()
                staff = tstaffid.get()
                
                
                sql = """INSERT into Vehicle (MOT,Mileage,Seats,Make,Availability,StaffID)
                        VALUES(?,?,?,?,?,?)"""
                cursor.execute(sql,((mot),(mileage),(seats),(make),(availability),(staff)))
                    
                db.commit()
                db.close()
                clear()
                
            # Deletes Entry
            def delete_vehicle():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                vehicleid = tvehicleid.get()
                if messagebox.askyesno("Confirmation","Are you sure you want to delete this Vehicle?"):
                    sql = "DELETE FROM vehicle WHERE VehicleID = "+vehicleid
                    cursor.execute(sql)
                    db.commit()
                    db.close()
                    clear()
                else:
                    db.close()
                    return True
                
            wrapper1 = LabelFrame(master, text="Vehicle List",bg='turquoise3')
            wrapper2 = LabelFrame(master, text="Search",bg='turquoise3')
            wrapper3 = LabelFrame(master, text="Vehicle Data",bg='turquoise3')
            wrapper1.pack(fill="both", expand="yes",padx=20,pady=10)
            wrapper2.pack(fill="both", expand="yes",padx=20,pady=10)
            wrapper3.pack(fill="both", expand="yes",padx=20,pady=10)
            
            tree_scrollx = Scrollbar(wrapper1, orient ="horizontal")
            tree_scrollx.pack(side=BOTTOM, fill="x")
            
            tree_scrolly = Scrollbar(wrapper1, orient ="vertical")
            tree_scrolly.pack(side=RIGHT, fill="y")
            

            trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6,7), xscrollcommand = tree_scrollx.set, yscrollcommand = tree_scrolly.set, show="headings", height="6")
            trv.pack(fill="both", expand="yes",padx=20,pady=10)
            tree_scrollx.config(command = trv.xview)
            tree_scrolly.config(command = trv.yview)
            trv.heading(1, text="VehicleID")
            trv.heading(2, text="MOT")
            trv.heading(3, text="Mileage")
            trv.heading(4, text="Seats")
            trv.heading(5, text="Make")
            trv.heading(6, text="Availability")
            trv.heading(7, text="StaffID")
            
            trv.bind('<Double 1>', getrow)
            
            db =sqlite3.connect("main.db")
            cursor = db.cursor()
            
            sql = "SELECT VehicleID,MOT,Mileage,Seats,Make,Availability,StaffID FROM Vehicle"
            cursor.execute(sql)
            rows = cursor.fetchall()
            update(rows)
            db.close()
            
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
            vehicleidLabel = Label(wrapper3, text="Vehicle ID",bg='turquoise3') ############////////////////''
            vehicleidLabel.grid(row=0, column=0, padx=5, pady=3)
            vehicleidEntry = Entry(wrapper3, textvariable=tvehicleid)
            vehicleidEntry.grid(row=0, column=1, padx=5, pady=3)
            
            motLabel = Label(wrapper3, text="MOT",bg='turquoise3')
            motLabel.grid(row=1, column=0, padx=5, pady=3)
            motEntry = Entry(wrapper3, textvariable=tmot)
            motEntry.grid(row=1, column=1, padx=5, pady=3)
            
            mileageLabel = Label(wrapper3, text="Mileage",bg='turquoise3')
            mileageLabel.grid(row=2, column=0, padx=5, pady=3)
            mileageEntry = Entry(wrapper3, textvariable=tmileage)
            mileageEntry.grid(row=2, column=1, padx=5, pady=3)
            
            seatsLabel = Label(wrapper3, text="Seats",bg='turquoise3')
            seatsLabel.grid(row=3, column=0, padx=5, pady=3)
            seatsEntry = Entry(wrapper3, textvariable=tseats)
            seatsEntry.grid(row=3, column=1, padx=5, pady=3)
            
            makeLabel = Label(wrapper3, text="Make",bg='turquoise3')
            makeLabel.grid(row=4, column=0, padx=5, pady=3)
            makeEntry = Entry(wrapper3, textvariable=tmake)
            makeEntry.grid(row=4, column=1, padx=5, pady=3)
            
            availabilityLabel = Label(wrapper3, text="Availability",bg='turquoise3')
            availabilityLabel.grid(row=5, column=0, padx=5, pady=3)
            availabilityEntry = Entry(wrapper3, textvariable=tavailability)
            availabilityEntry.grid(row=5, column=1, padx=5, pady=3)
            
            staffLabel = Label(wrapper3, text="Staff ID",bg='turquoise3')
            staffLabel.grid(row=6, column=0, padx=5, pady=3)
            staffEntry = Entry(wrapper3, textvariable=tstaffid)
            staffEntry.grid(row=6, column=1, padx=5, pady=3)
            
            
            # Buttons
            UpdateButton = Button(wrapper3, text="Update", command=update_vehicle)
            AddButton = Button(wrapper3, text="Add New", command=add_new)
            DeleteButton = Button(wrapper3, text="Delete", command=delete_vehicle)
            UpdateButton.grid(row=13, column=1,padx=5,pady=3)
            AddButton.grid(row=13, column=0,padx=5,pady=3)
            DeleteButton.grid(row=13, column=2,padx=5,pady=3)
            
            
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
class display_staff():
    def __init__(self, master):
            self.master = master
            self.master.title("Display Staff")
            self.master.configure(background='turquoise3')
            
            # Binding F11 and ESCAPE keys to full screen
            self.master.bind("<F11>", self.toggle_fullscreen)
            self.master.bind("<Escape>", self.end_fullscreen)
            self.state = True
            self.master.attributes("-fullscreen", False)
            
            # Initialising Strings
            q=StringVar()
            tstaffid = StringVar() 
            tforename = StringVar()
            tsurname = StringVar()
            temail = StringVar()
            tmobilenum = StringVar()
            tcapabilities = StringVar() 
            tavailability = StringVar()
            tstreetnum = StringVar()
            tstreetname = StringVar()
            ttown = StringVar()
            tpostcode = StringVar() 
            
            
            # Button
            Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black').pack(padx=20,pady=20)

            # db =sqlite3.connect("main.db")
            # cursor = db.cursor()

            # Reloads the Database
            def update(rows):
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                trv.delete(*trv.get_children())
                for i in rows:
                    trv.insert('', 'end', values=i)
                db.close()
            
            # Finds Row using SQL
            def search():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                q2 = q.get()
                sql = "SELECT StaffID,Forename,Surname,Email,MobileNum,Capabilities,Availability,StreetNum,StreetName,Town,Postcode FROM Staff WHERE StaffID LIKE '%"+q2+"' OR Forename LIKE '%"+q2+"' OR Surname LIKE '%"+q2+"' OR Email LIKE '%"+q2+"' OR MobileNum LIKE '%"+q2+"' OR Capabilities LIKE '%"+q2+"' OR Availability LIKE '%"+q2+"' OR StreetNum LIKE '%"+q2+"' OR StreetName LIKE '%"+q2+"' OR Town LIKE '%"+q2+"' OR Postcode LIKE '%"+q2+"'"
                cursor.execute(sql)
                rows = cursor.fetchall()
                update(rows)
                db.close()
                
            # Removes Search
            def clear():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                sql = "SELECT  StaffID,Forename,Surname,Email,MobileNum,Capabilities,Availability,StreetNum,StreetName,Town,Postcode FROM Staff"
                cursor.execute(sql)
                rows = cursor.fetchall()
                update(rows)
                db.close()
            
            # Double Click Auto Imports Data Into Entry
            def getrow(event):
                rowid = trv.identify_row(event.y)
                
                item = trv.item(trv.focus())
                tstaffid.set(item['values'][0])
                tforename.set(item['values'][1])
                tsurname.set(item['values'][2])
                temail.set(item['values'][3])
                tmobilenum.set(item['values'][4])
                tcapabilities.set(item['values'][5])
                tavailability.set(item['values'][6])
                tstreetnum.set(item['values'][7])
                tstreetname.set(item['values'][8])
                ttown.set(item['values'][9])
                tpostcode.set(item['values'][10])
                
            # Change an existing entry
            def update_staff():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                staffid = tstaffid.get()
                forename = tforename.get()
                surname = tsurname.get()
                email = temail.get()
                mobilenum = tmobilenum.get()
                capabilities = tcapabilities.get()
                availability = tavailability.get()
                streetnum = tstreetnum.get()
                streetname = tstreetname.get()
                town = ttown.get()
                postcode = tpostcode.get()

                # Confirmation Box
                if messagebox.askyesno("Confirmation","Are you sure you want to update this Staff?"):
                    sql = "UPDATE Staff SET Forename = ? , Surname = ? , Email = ? , MobileNum = ? , Capabilities = ? , Availability = ? , StreetNum = ? , StreetName = ?, Town = ?, Postcode = ? WHERE StaffID = ?"
                    cursor.execute(sql,(forename,surname,email,mobilenum,capabilities,availability,streetnum,streetname,town,postcode,staffid))
                    db.commit()
                    clear()
                db.commit()
                db.close()
            
            # Adds New Entry
            def add_new():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                staffid = tstaffid.get()
                forename = tforename.get()
                surname = tsurname.get()
                email = temail.get()
                mobilenum = tmobilenum.get()
                capabilities = tcapabilities.get()
                availability = tavailability.get()
                streetnum = tstreetnum.get()
                streetname = tstreetname.get()
                town = ttown.get()
                postcode = tpostcode.get()
                
                sql = """INSERT into Staff (Forename,Surname,Email,MobileNum,Capabilities,Availability,StreetNum,StreetName,Town,Postcode)
                        VALUES(?,?,?,?,?,?,?,?,?,?)"""
                cursor.execute(sql,((forename),(surname),(email),(mobilenum),(capabilities),(availability),(streetnum),(streetname),(town),(postcode)))
                db.commit()
                db.close()
                clear()
                
            # Deletes Entry
            def delete_staff():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                staffid = tstaffid.get()
                if messagebox.askyesno("Confirmation","Are you sure you want to delete this Staff?"):
                    sql = "DELETE FROM Staff WHERE StaffID = "+staffid
                    cursor.execute(sql)
                    db.commit()
                    db.close()
                    clear()
                else:
                    db.close()
                    return True
                
            wrapper1 = LabelFrame(master, text="Staff List",bg='turquoise3')
            wrapper2 = LabelFrame(master, text="Search",bg='turquoise3')
            wrapper3 = LabelFrame(master, text="Staff Data",bg='turquoise3')
            wrapper1.pack(fill="both", expand="yes",padx=20,pady=10)
            wrapper2.pack(fill="both", expand="yes",padx=20,pady=10)
            wrapper3.pack(fill="both", expand="yes",padx=20,pady=10)
            
            tree_scrollx = Scrollbar(wrapper1, orient ="horizontal")
            tree_scrollx.pack(side=BOTTOM, fill="x")
            
            tree_scrolly = Scrollbar(wrapper1, orient ="vertical")
            tree_scrolly.pack(side=RIGHT, fill="y")
            
            
            trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6,7,8,9,10,11), xscrollcommand = tree_scrollx.set, yscrollcommand = tree_scrolly.set, show="headings", height="6")
            trv.pack(fill="both", expand="yes",padx=20,pady=10)
            tree_scrollx.config(command = trv.xview)
            tree_scrolly.config(command = trv.yview)
            trv.heading(1, text="StaffID")
            trv.heading(2, text="Forename")
            trv.heading(3, text="Surname")
            trv.heading(4, text="Email")
            trv.heading(5, text="Mobile")
            trv.heading(6, text="Capabilities")
            trv.heading(7, text="Availability")
            trv.heading(8, text="StreetNum")
            trv.heading(9, text="StreetName")
            trv.heading(10, text="Town")
            trv.heading(11, text="Postcode")
            
            trv.bind('<Double 1>', getrow)
            
            db =sqlite3.connect("main.db")
            cursor = db.cursor()
            
            sql = "SELECT StaffID,Forename,Surname,Email,MobileNum,Capabilities,Availability,StreetNum,StreetName,Town,Postcode FROM Staff"
            cursor.execute(sql)
            rows = cursor.fetchall()
            update(rows)
            db.close()
            
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
            StaffIDLabel = Label(wrapper3, text="Staff ID",bg='turquoise3') 
            StaffIDLabel.grid(row=0, column=0, padx=5, pady=3)
            StaffIDEntry = Entry(wrapper3, textvariable=tstaffid)
            StaffIDEntry.grid(row=0, column=1, padx=5, pady=3)
            
            ForenameLabel = Label(wrapper3, text="Forename",bg='turquoise3')
            ForenameLabel.grid(row=1, column=0, padx=5, pady=3)
            ForenameEntry = Entry(wrapper3, textvariable=tforename)
            ForenameEntry.grid(row=1, column=1, padx=5, pady=3)
            
            SurnameLabel = Label(wrapper3, text="Surname",bg='turquoise3')
            SurnameLabel.grid(row=2, column=0, padx=5, pady=3)
            SurnameEntry = Entry(wrapper3, textvariable=tsurname)
            SurnameEntry.grid(row=2, column=1, padx=5, pady=3)
            
            EmailLabel = Label(wrapper3, text="Email",bg='turquoise3')
            EmailLabel.grid(row=3, column=0, padx=5, pady=3)
            EmailEntry = Entry(wrapper3, textvariable=temail)
            EmailEntry.grid(row=3, column=1, padx=5, pady=3)
            
            MobileNumLabel = Label(wrapper3, text="Mobile Num",bg='turquoise3')
            MobileNumLabel.grid(row=4, column=0, padx=5, pady=3)
            MobileNumEntry = Entry(wrapper3, textvariable=tmobilenum)
            MobileNumEntry.grid(row=4, column=1, padx=5, pady=3)
            
            CapabilitiesLabel = Label(wrapper3, text="Capabilities",bg='turquoise3')
            CapabilitiesLabel.grid(row=5, column=0, padx=5, pady=3)
            CapabilitiesEntry = Entry(wrapper3, textvariable=tcapabilities)
            CapabilitiesEntry.grid(row=5, column=1, padx=5, pady=3)
            
            AvailabilityLabel = Label(wrapper3, text="Availability",bg='turquoise3')
            AvailabilityLabel.grid(row=6, column=0, padx=5, pady=3)
            AvailabilityEntry = Entry(wrapper3, textvariable=tavailability)
            AvailabilityEntry.grid(row=6, column=1, padx=5, pady=3)

            StreetNumLabel = Label(wrapper3, text="Street Num",bg='turquoise3')
            StreetNumLabel.grid(row=7, column=0, padx=5, pady=3)
            StreetNumEntry = Entry(wrapper3, textvariable=tstreetnum)
            StreetNumEntry.grid(row=7, column=1, padx=5, pady=3)
            
            StreetNameLabel = Label(wrapper3, text="Street Name",bg='turquoise3')
            StreetNameLabel.grid(row=8, column=0, padx=5, pady=3)
            StreetNameEntry = Entry(wrapper3, textvariable=tstreetname)
            StreetNameEntry.grid(row=8, column=1, padx=5, pady=3)
            
            TownLabel = Label(wrapper3, text="Town",bg='turquoise3')
            TownLabel.grid(row=9, column=0, padx=5, pady=3)
            TownEntry = Entry(wrapper3, textvariable=ttown)
            TownEntry.grid(row=9, column=1, padx=5, pady=3)
            
            PostcodeLabel = Label(wrapper3, text="Postcode",bg='turquoise3')
            PostcodeLabel.grid(row=10, column=0, padx=5, pady=3)
            PostcodeEntry = Entry(wrapper3, textvariable=tpostcode)
            PostcodeEntry.grid(row=10, column=1, padx=5, pady=3)
            
            # Buttons
            UpdateButton = Button(wrapper3, text="Update", command=update_staff)
            AddButton = Button(wrapper3, text="Add New", command=add_new)
            DeleteButton = Button(wrapper3, text="Delete", command=delete_staff)
            UpdateButton.grid(row=13, column=1,padx=5,pady=3)
            AddButton.grid(row=13, column=0,padx=5,pady=3)
            DeleteButton.grid(row=13, column=2,padx=5,pady=3)
            
            
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
class display_logs():
    def __init__(self, master):
            self.master = master
            self.master.title("Display Logs")
            self.master.configure(background='turquoise3')
            
            # Binding F11 and ESCAPE keys to full screen
            self.master.bind("<F11>", self.toggle_fullscreen)
            self.master.bind("<Escape>", self.end_fullscreen)
            self.state = True
            self.master.attributes("-fullscreen", False)
            
            # Initialising Strings
            q=StringVar()
            ttimeid = StringVar() 
            temail = StringVar()
            tlogin = StringVar()
            tlogout = StringVar()

            
            # Button
            Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black').pack(padx=20,pady=20)


            # Reloads the Database
            def update(rows):
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                trv.delete(*trv.get_children())
                for i in rows:
                    trv.insert('', 'end', values=i)
                db.close()
            
            # Finds Row using SQL
            def search():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                q2 = q.get()
                sql = "SELECT TimeID,Email,LogIn,LogOut FROM Time WHERE TimeID LIKE '%"+q2+"' OR Email LIKE '%"+q2+"' OR LogIn LIKE '%"+q2+"' OR LogOut LIKE '%"+q2+"' "
                cursor.execute(sql)
                rows = cursor.fetchall()
                update(rows)
                db.close()
                
            # Removes Search
            def clear():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                sql = "SELECT TimeID,Email,LogIn,LogOut FROM Time"
                cursor.execute(sql)
                rows = cursor.fetchall()
                update(rows)
                db.close()
            
            # Double Click Auto Imports Data Into Entry
            def getrow(event):
                rowid = trv.identify_row(event.y)
                
                item = trv.item(trv.focus())
                ttimeid.set(item['values'][0])
                temail.set(item['values'][1])
                tlogin.set(item['values'][2])
                tlogout.set(item['values'][3])
                
            # Change an existing entry
            def update_logs():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                timeid = ttimeid.get()
                email = temail.get()
                login = tlogin.get()
                logout = tlogin.get()

                # Confirmation Box
                if messagebox.askyesno("Confirmation","Are you sure you want to update this Time?"):
                    sql = "UPDATE Time SET TimeID = ?,Email = ?,LogIn = ?,LogOut = ?"
                    cursor.execute(sql,(timeid,email,login,logout))
                    db.commit()
                    clear()
                db.commit()
                db.close()
            
            # Adds New Entry
            def add_new():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                timeid = ttimeid.get()
                email = temail.get()
                login = tlogin.get()
                logout = tlogout.get()
                
                sql = """INSERT into Time (Email,LogIn,LogOut)
                        VALUES(?,?,?)"""
                cursor.execute(sql, ((email),(login),(logout)))
                db.commit()
                db.close()
                clear()
                
            # Deletes Entry
            def delete_logs():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                timeid = ttimeid.get()
                if messagebox.askyesno("Confirmation","Are you sure you want to delete this Time?"):
                    sql = "DELETE FROM Time WHERE TimeID = "+timeid
                    cursor.execute(sql)
                    db.commit()
                    db.close()
                    clear()
                else:
                    db.close()
                    return True
                
            wrapper1 = LabelFrame(master, text="Time List",bg='turquoise3')
            wrapper2 = LabelFrame(master, text="Search",bg='turquoise3')
            wrapper3 = LabelFrame(master, text="Time Data",bg='turquoise3')
            wrapper1.pack(fill="both", expand="yes",padx=20,pady=10)
            wrapper2.pack(fill="both", expand="yes",padx=20,pady=10)
            wrapper3.pack(fill="both", expand="yes",padx=20,pady=10)
            
            tree_scrollx = Scrollbar(wrapper1, orient ="horizontal")
            tree_scrollx.pack(side=BOTTOM, fill="x")
            
            tree_scrolly = Scrollbar(wrapper1, orient ="vertical")
            tree_scrolly.pack(side=RIGHT, fill="y")
            
            trv = ttk.Treeview(wrapper1, columns=(1,2,3,4), xscrollcommand = tree_scrollx.set, yscrollcommand = tree_scrolly.set, show="headings", height="6")
            trv.pack(fill="both", expand="yes",padx=20,pady=10)
            tree_scrollx.config(command = trv.xview)
            tree_scrolly.config(command = trv.yview)
            trv.heading(1, text="TimeID")
            trv.heading(2, text="Email")
            trv.heading(3, text="Login")
            trv.heading(4, text="LogOut")
            
            trv.bind('<Double 1>', getrow)
            
            db =sqlite3.connect("main.db")
            cursor = db.cursor()
            
            sql = "SELECT TimeID,Email,LogIn,LogOut FROM Time"
            cursor.execute(sql)
            rows = cursor.fetchall()
            update(rows)
            db.close()
            
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
            TimeIDLabel = Label(wrapper3, text="Time ID",bg='turquoise3') 
            TimeIDLabel.grid(row=0, column=0, padx=5, pady=3)
            TimeIDEntry = Entry(wrapper3, textvariable=ttimeid)
            TimeIDEntry.grid(row=0, column=1, padx=5, pady=3)
            
            EmailLabel = Label(wrapper3, text="Email",bg='turquoise3')
            EmailLabel.grid(row=1, column=0, padx=5, pady=3)
            EmailEntry = Entry(wrapper3, textvariable=temail)
            EmailEntry.grid(row=1, column=1, padx=5, pady=3)
            
            LoginLabel = Label(wrapper3, text="LogIn",bg='turquoise3')
            LoginLabel.grid(row=2, column=0, padx=5, pady=3)
            LoginEntry = Entry(wrapper3, textvariable=tlogin)
            LoginEntry.grid(row=2, column=1, padx=5, pady=3)
            
            LogOutLabel = Label(wrapper3, text="LogOut",bg='turquoise3')
            LogOutLabel.grid(row=3, column=0, padx=5, pady=3)
            LogOutEntry = Entry(wrapper3, textvariable=tlogout)
            LogOutEntry.grid(row=3, column=1, padx=5, pady=3)
            
            # Buttons
            UpdateButton = Button(wrapper3, text="Update", command=update_logs)
            AddButton = Button(wrapper3, text="Add New", command=add_new)
            DeleteButton = Button(wrapper3, text="Delete", command=delete_logs)
            UpdateButton.grid(row=13, column=1,padx=5,pady=3)
            AddButton.grid(row=13, column=0,padx=5,pady=3)
            DeleteButton.grid(row=13, column=2,padx=5,pady=3)
            
            
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
        self.master.attributes("-fullscreen", False)
        
        type=StringVar()
        self.a=StringVar()
        
        # Login Page Labels
        Label(self.master,text='Email',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=0,pady=10)
        Label(self.master,text='Password',bg='turquoise3',font='Bembo',fg='black').grid(row=3,column=0)
        
        # Entry Page Entry
        self.emailEntry=Entry(self.master,textvariable=self.a,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35)
        self.emailEntry.grid(row=2,column=2,pady=10,columnspan=2)
        self.passwordEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=35,show = "*")
        self.passwordEntry.grid(row=3,column=2,columnspan=2)

        # Login Page Buttons
        Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=3)
        Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=0)
        Button(self.master,text='Login',command=self.checkLogin,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=2)
        Button(self.master,text='Quit',command=self.end,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=4)

        Button(self.master,text='temp bypass',command=self.menu,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=5)

    
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
        type = "Driver"
        t = time()
        ct = ctime(t)
        
        db =sqlite3.connect("main.db")
        cursor = db.cursor()
        sql = """SELECT * from MasterLogin WHERE StaffEmail= ? AND StaffPassword = ? AND Type = ?"""
        cursor.execute(sql,[(email),(password),(type)])
        result=cursor.fetchall()
        if result:
            print("--------------------------------")
            print(ct + "\n" + email + " has logged in")
            print("--------------------------------")
            sql = """INSERT INTO Time(Email,LogIn,LogOut)
                VALUES(?,?,?)"""
            cursor.execute(sql,[(email),(ct),('NULL')])
            db.commit()
            db.close()
            self.menu()
        else:
            print("Login Failed")
            Label(self.master,text='Login Failed',bg='turquoise3',font='Bembo',fg='red').grid(row=2,column=4)
        db.close()

    # Redirecting After Login Page
    def menu(self):
        self.email=self.a.get()
        self.master.withdraw()
        root2=Toplevel(self.master)
        #root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=DriverMenu(root2)
class DriverMenu():
    def __init__(self, master):
        self.master = master
        self.master.title("Logged In")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = True
        self.master.attributes("-fullscreen", False)
        
        # Menu Up Page Buttons
        Button(self.master,text='Log Out',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=0)
        Button(self.master,text='View Timetable',command=self.viewtable,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=0,column=2)
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
        
        db.close()
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=DriverLogin(root2)
        
    def viewtable(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=indi_table(root2)

class indi_table(Home):
    def __init__(self, master):
            self.master = master
            super().toggle_fullscreen
            self.master.title("Timetable")
            self.master.configure(background='turquoise3')
            
            # Binding F11 and ESCAPE keys to full screen
            self.master.bind("<F11>", self.toggle_fullscreen)
            self.master.bind("<Escape>", self.end_fullscreen)
            self.state = True
            self.master.attributes("-fullscreen", False)
            
            # Initialising Strings
            q=StringVar()
            tbookingid = StringVar() 
            tcustid = StringVar()
            tstartstreetnum = StringVar()
            tstartstreet = StringVar()
            tstartpost = StringVar()
            tdeststreetnum = StringVar() 
            tdeststreet = StringVar()
            tdestpost = StringVar()
            tfufilled = StringVar()
            tdate = StringVar()
            ttime = StringVar() 
            tforename = StringVar()
            tdriver = StringVar()
            
            db =sqlite3.connect("main.db")
            cursor = db.cursor()
            q2 = q.get()
            
            
            sql = "SELECT Email FROM Time ORDER BY TimeID DESC"
            cursor.execute(sql)
            lastlogin = cursor.fetchall()
            lastlogin = str(lastlogin[0])
            lastlogin = (lastlogin[2:-3])
            print(lastlogin)
            sql = "SELECT Staff.StaffID FROM Staff,Time,MasterLogin WHERE Staff.Email = ? AND Staff.Email = MasterLogin.StaffEmail AND MasterLogin.Type = 'Driver'"
            cursor.execute(sql,[(lastlogin)])
            driver = cursor.fetchall()
            driver = ' '.join(map(str, driver))
            driver = driver[1:2]
            print(driver)
            
            db.close()
            
            # Button
            Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black').pack(padx=20,pady=20)

            # Reloads the Database
            def update(rows):
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                trv.delete(*trv.get_children())
                for i in rows:
                    trv.insert('', 'end', values=i)
                db.close()
            
            # Finds Row using SQL
            def search():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                q2 = q.get()
                sql = "SELECT Time,Date,Bookings.CustomerID,StartStreetNum,StartStreet,StartPostcode,DestinationStreetNum,DestinationStreet,DestinationPostcode,Fufilled,Customer.Forename,StaffID,BookingsID FROM Bookings,Customer WHERE Customer.Forename = Bookings.Forename AND Bookings.StaffID = ? AND (Forename LIKE '%"+q2+"' OR Date LIKE '%"+q2+"' OR StartPostcode LIKE '%"+q2+"' OR CustomerID LIKE '%"+q2+"' OR Fufilled LIKE '%"+q2+"' OR StartStreet LIKE '%"+q2+"' OR BookingsID LIKE '%"+q2+"' OR DestinationStreet LIKE '%"+q2+"' OR DestinationPostcode LIKE '%"+q2+"') ORDER BY Time ASC"
                cursor.execute(sql,[(driver)])
                rows = cursor.fetchall()
                update(rows)
                db.close()
                
            # Removes Search
            def clear():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                sql = "SELECT BookingsID,Bookings.CustomerID,StartStreetNum,StartStreet,StartPostcode,DestinationStreetNum,DestinationStreet,DestinationPostcode,Fufilled,Date,Time,Customer.Forename,StaffID FROM Bookings,Customer WHERE Customer.Forename = Bookings.Forename AND Bookings.StaffID = ? ORDER BY Time ASC"
                cursor.execute(sql,[(driver)])
                rows = cursor.fetchall()
                update(rows)
                db.close()

            
            # Double Click Auto Imports Data Into Entry
            def getrow(event):
                rowid = trv.identify_row(event.y)
                
                item = trv.item(trv.focus())
                tbookingid.set(item['values'][0])
                tcustid.set(item['values'][1])
                tstartstreetnum.set(item['values'][2])
                tstartstreet.set(item['values'][3])
                tstartpost.set(item['values'][4])
                tdeststreetnum.set(item['values'][5])
                tdeststreet.set(item['values'][6])
                tdestpost.set(item['values'][7])
                tfufilled.set(item['values'][8])
                tdate.set(item['values'][9])
                ttime.set(item['values'][10])
                tforename.set(item['values'][11])
                tdriver.set(item['values'][12])
                
            # Change an existing entry
            def fulfilled_true():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                booking = tbookingid.get()

                # Confirmation Box
                if messagebox.askyesno("Confirmation","Are you sure you want to change to True?"):
                    sql = "UPDATE Bookings SET Fufilled = 'True' WHERE BookingsID = ?"
                    cursor.execute(sql,(booking))

                    db.commit()
                    clear()
                db.commit()
                db.close()
                
            # Change an existing entry
            def fulfilled_false():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                booking = tbookingid.get()

                # Confirmation Box
                if messagebox.askyesno("Confirmation","Are you sure you want to change to False?"):
                    sql = "UPDATE Bookings SET Fufilled = 'False' WHERE BookingsID = ?"
                    cursor.execute(sql,(booking))

                    db.commit()
                    clear()
                db.commit()
                db.close()
                
                
            wrapper1 = LabelFrame(master, text="Bookings List",bg='turquoise3')
            wrapper2 = LabelFrame(master, text="Search",bg='turquoise3')

            wrapper1.pack(fill="both", expand="yes",padx=20,pady=10)
            wrapper2.pack(fill="both", expand="yes",padx=20,pady=10)

            tree_scrollx = Scrollbar(wrapper1, orient ="horizontal")
            tree_scrollx.pack(side=BOTTOM, fill="x")
            
            tree_scrolly = Scrollbar(wrapper1, orient ="vertical")
            tree_scrolly.pack(side=RIGHT, fill="y")
            
            wrapper3 = LabelFrame(master, text="Booking Data",bg='turquoise3')
            wrapper3.pack(fill="both", expand="yes",padx=20,pady=10)

            
            trv = ttk.Treeview(wrapper1, xscrollcommand = tree_scrollx.set, yscrollcommand = tree_scrolly.set, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15), show="headings", height="6")
            trv.pack(fill="both", expand="yes",padx=20,pady=10)
            tree_scrollx.config(command = trv.xview)
            tree_scrolly.config(command = trv.yview)
            trv.heading(1, text="BookingID")
            trv.heading(2, text="CustomerID")
            trv.heading(3, text="StartStreetNum")
            trv.heading(4, text="StartStreet")
            trv.heading(5, text="StartStreetPostcode")
            trv.heading(6, text="DestinationStreetNum")
            trv.heading(7, text="DestinationStreet")
            trv.heading(8, text="DestinationStreetPostcode")
            trv.heading(9, text="Fufilled")
            trv.heading(10, text="Date")
            trv.heading(11, text="Time")
            trv.heading(12, text="Forename")
            trv.heading(13, text="StaffID")
            
            
            
            trv.bind('<Double 1>', getrow)
            
            db =sqlite3.connect("main.db")
            cursor = db.cursor()
            
            sql = "SELECT BookingsID, Bookings.CustomerID, StartStreetNum,StartStreet,StartPostcode,DestinationStreetNum,DestinationStreet,DestinationPostcode,Fufilled,Date,Time,Customer.Forename,StaffID FROM Bookings,Customer WHERE Customer.Forename = Bookings.Forename AND Bookings.StaffID = ? ORDER BY Time ASC"
            cursor.execute(sql,[(driver)])
            rows = cursor.fetchall()
            update(rows)
            db.close()
            
            
            
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
            BookIDLabel = Label(wrapper3, text="Booking ID",bg='turquoise3') 
            BookIDLabel.grid(row=0, column=0, padx=5, pady=3)
            BookIDEntry = Entry(wrapper3, textvariable=tbookingid)
            BookIDEntry.grid(row=0, column=1, padx=5, pady=3)
            
            CustIDLabel = Label(wrapper3, text="Customer ID",bg='turquoise3')
            CustIDLabel.grid(row=1, column=0, padx=5, pady=3)
            CustIDEntry = Entry(wrapper3, textvariable=tcustid)
            CustIDEntry.grid(row=1, column=1, padx=5, pady=3)
            
            startstreetnumLabel = Label(wrapper3, text="Start Street Num",bg='turquoise3')
            startstreetnumLabel.grid(row=2, column=0, padx=5, pady=3)
            startstreetnumEntry = Entry(wrapper3, textvariable=tstartstreetnum)
            startstreetnumEntry.grid(row=2, column=1, padx=5, pady=3)
            
            startstreetLabel = Label(wrapper3, text="Start Street",bg='turquoise3')
            startstreetLabel.grid(row=3, column=0, padx=5, pady=3)
            startstreetEntry = Entry(wrapper3, textvariable=tstartstreet)
            startstreetEntry.grid(row=3, column=1, padx=5, pady=3)
            
            startpostLabel = Label(wrapper3, text="Start Postcode",bg='turquoise3')
            startpostLabel.grid(row=4, column=0, padx=5, pady=3)
            startpostEntry = Entry(wrapper3, textvariable=tstartpost)
            startpostEntry.grid(row=4, column=1, padx=5, pady=3)
            
            deststreetnumLabel = Label(wrapper3, text="Dest Street Num",bg='turquoise3')
            deststreetnumLabel.grid(row=5, column=0, padx=5, pady=3)
            deststreetnumEntry = Entry(wrapper3, textvariable=tdeststreetnum)
            deststreetnumEntry.grid(row=5, column=1, padx=5, pady=3)
            
            DestStreetLabel = Label(wrapper3, text="Dest Street",bg='turquoise3')
            DestStreetLabel.grid(row=6, column=0, padx=5, pady=3)
            DestStreetEntry = Entry(wrapper3, textvariable=tdeststreet)
            DestStreetEntry.grid(row=6, column=1, padx=5, pady=3)
            
            destpostLabel = Label(wrapper3, text="Dest Postcode",bg='turquoise3')
            destpostLabel.grid(row=7, column=0, padx=5, pady=3)
            destpostEntry = Entry(wrapper3, textvariable=tdestpost)
            destpostEntry.grid(row=7, column=1, padx=5, pady=3)
            
            fufilledLabel = Label(wrapper3, text="Fufilled",bg='turquoise3')
            fufilledLabel.grid(row=8, column=0, padx=5, pady=3)
            fufilledEntry = Entry(wrapper3, textvariable=tfufilled)
            fufilledEntry.grid(row=8, column=1, padx=5, pady=3)
            
            dateLabel = Label(wrapper3, text="Date",bg='turquoise3')
            dateLabel.grid(row=9, column=0, padx=5, pady=3)
            dateEntry = Entry(wrapper3, textvariable=tdate)
            dateEntry.grid(row=9, column=1, padx=5, pady=3)
            
            timeLabel = Label(wrapper3, text="Time",bg='turquoise3')
            timeLabel.grid(row=10, column=0, padx=5, pady=3)
            timeEntry = Entry(wrapper3, textvariable=ttime)
            timeEntry.grid(row=10, column=1, padx=5, pady=3)
            
            forenameLabel = Label(wrapper3, text="Forename",bg='turquoise3')
            forenameLabel.grid(row=11, column=0, padx=5, pady=3)
            forenameEntry = Entry(wrapper3, textvariable=tforename)
            forenameEntry.grid(row=11, column=1, padx=5, pady=3)
            
            driverLabel = Label(wrapper3, text="StaffID",bg='turquoise3')
            driverLabel.grid(row=12, column=0, padx=5, pady=3)
            driverEntry = Entry(wrapper3, textvariable=tdriver)
            driverEntry.grid(row=12, column=1, padx=5, pady=3)
            
            # Buttons
            fulfilledButton = Button(wrapper3, text="Change Availability To True", command=fulfilled_true)
            unfulfilledButton = Button(wrapper3, text="Change Availability To False", command=fulfilled_false)
            fulfilledButton.grid(row=13, column=1,padx=5,pady=3)
            unfulfilledButton.grid(row=13, column=0,padx=5,pady=3)
            
            db =sqlite3.connect("main.db")
            cursor = db.cursor()
            list= []
            sql ="SELECT MIN(Date) FROM Bookings"
            cursor.execute(sql)
            date = cursor.fetchall()
            date = str(date)
            date = date[3:-4]
            list.append(date)
            sql ="SELECT MIN(Time) FROM Bookings WHERE Date = ?"
            cursor.execute(sql,[(date)])
            latest = cursor.fetchall()
            list.insert(0,latest)
            print(latest)
            db.close()
            
            latestLabel = Label(wrapper3, text="Next Booking:",bg='turquoise3', fg = "red")
            latestLabel.grid(row=13, column=2, padx=10, pady=3)
            latestlabelLabel = Label(wrapper3, text=list,bg='turquoise3', fg = "red")
            latestlabelLabel.grid(row=13, column=3, pady=3)
            
            # Return To 'Menu' Screen
    def back(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=DriverMenu(root2)


def main():
    root=Tk()
    myGUIWelcome=Home(root)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.mainloop()
if __name__ == '__main__':
    main()
