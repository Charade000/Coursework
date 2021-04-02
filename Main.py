from tkinter import *
import sqlite3

class Home():
    def __init__(self, master):
        self.master = master
        self.master.title("Taxi And Minibus")
        self.master.configure(background='turquoise3')
        
        # Creating Database
        self.createCustomerTable("Customers.db")
        self.createLoginTable("Login.db")
        self.createBookingsTable("Bookings.db")
        self.createVehicleTable("Vehicle.db")
        self.createStaffTable("Staff.db")

        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = False
        self.master.attributes("-fullscreen", False)
        

        # 'Home' Page Buttons
        self.Full_B=Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=3,padx=20)
        self.Login_B=Button(self.master,text='Login',command=self.login,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=0)
        self.SignUp_B=Button(self.master,text='Sign Up',command=self.sign_up,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=1)
        self.About_B=Button(self.master,text='About Us',command=self.about,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=2)

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

    def sign_up(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=signupWindow(root2)
    
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

    # Creating All The Databases Or Checking If They Exist
    def createCustomerTable(self,dbName):
        if 'Customer' in self.getTables(dbName):
            print ("\nVet Table Already Exists")
        else:
            with sqlite3.connect(dbName) as db:
                cursor=db.cursor()
                sql ="""CREATE TABLE Customer(
                    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Forename TEXT NOT NULL,
                    Surname TEXT NOT NULL,
                    TelephoneNo TEXT NOT NULL)"""
                cursor.execute(sql)
                db.commit()
    def createLoginTable(self,dbName):
        if 'Login' in self.getTables(dbName):
            print ("\nLogin Table Already Exists")
        else:
            with sqlite3.connect(dbName) as db:
                cursor=db.cursor()
                sql ="""CREATE TABLE Login(
                    LoginID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Forename TEXT NOT NULL,
                    Surname TEXT NOT NULL,
                    TelephoneNo TEXT NOT NULL)"""
                cursor.execute(sql)
                db.commit()
    def createBookingsTable(self,dbName):
        if 'Bookings' in self.getTables(dbName):
            print ("\nBookings Table Already Exists")
        else:
            with sqlite3.connect(dbName) as db:
                cursor=db.cursor()
                sql ="""CREATE TABLE Bookings(
                    BookingsID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Forename TEXT NOT NULL,
                    Surname TEXT NOT NULL,
                    TelephoneNo TEXT NOT NULL)"""
                cursor.execute(sql)
                db.commit()
    def createVehicleTable(self,dbName):
        if 'Vehicle' in self.getTables(dbName):
            print ("\nVehicle Table Already Exists")
        else:
            with sqlite3.connect(dbName) as db:
                cursor=db.cursor()
                sql ="""CREATE TABLE Vehicle(
                    VehicleID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Forename TEXT NOT NULL,
                    Surname TEXT NOT NULL,
                    TelephoneNo TEXT NOT NULL)"""
                cursor.execute(sql)
                db.commit()
    def createStaffTable(self,dbName):
        if 'Staff' in self.getTables(dbName):
            print ("\nStaff Table Already Exists")
        else:
            with sqlite3.connect(dbName) as db:
                cursor=db.cursor()
                sql ="""CREATE TABLE Staff(
                    StaffID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Forename TEXT NOT NULL,
                    Surname TEXT NOT NULL,
                    TelephoneNo TEXT NOT NULL)"""
                cursor.execute(sql)
                db.commit()


class loginWindow():
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = False
        self.master.attributes("-fullscreen", False)
        

        # Login Page Buttons
        self.Full_B=Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=3,padx=20)
        self.Back_B=Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=0)
        self.LoginButton=Button(self.master,text='Login',command=self.checkLogin,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=2)
        
        # Login Page Labels
        self.emailLabel=Label(self.master,text='Email',bg='turquoise3',font='Bembo',fg='black').grid(row=2,column=0,pady=5)
        self.passwordLabel=Label(self.master,text='Password',bg='turquoise3',font='Bembo',fg='black').grid(row=3,column=0,pady=5)
        
        # Entry Page Entry
        self.emailEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=15).grid(row=2,column=2,pady=5)
        self.passwordEntry=Entry(self.master,bg='PaleTurquoise1',bd=0,font='Bembo',fg='black',width=15).grid(row=3,column=2,pady=5)


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
        
        pass
        # db =sqlite3.connect("vet.db")
        # cursor = db.cursor()
        # sql = "SELECT COUNT(*) FROM Pet"
        # cursor.execute(sql)
        # noOfPetRecords = cursor.fetchone()[0]
        
        

class signupWindow():
    def __init__(self, master):
        self.master = master
        self.master.title("Sign Up")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = False
        self.master.attributes("-fullscreen", False)
        
        # Sign Up Page Buttons
        self.Full_B=Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=3,padx=20)
        self.Back_B=Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=0)

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
        

class aboutWindow():
    def __init__(self, master):
        self.master = master
        self.master.title("About Us")
        self.master.configure(background='turquoise3')
        
        # Binding F11 and ESCAPE keys to full screen
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)
        self.state = False
        self.master.attributes("-fullscreen", False)
        
        # About Window Buttons
        self.Full_B=Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=3,padx=20)
        self.Back_B=Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=0)

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
        # root2.geometry("200x{1}+0+0".format(root2.winfo_screenheight()))
        root2.geometry("{0}x{1}+0+0".format(root2.winfo_screenwidth(), root2.winfo_screenheight()))
        muGUI=Home(root2)




def main():
    root=Tk()
    myGUIWelcome=Home(root)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.mainloop()

if __name__ == '__main__':
    main()
