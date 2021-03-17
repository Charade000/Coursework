from tkinter import *

class Home():
    def __init__(self, master):
        self.master = master
        self.master.geometry('610x780')
        self.master.title("Taxi And Minibus")
        self.master.configure(background='turquoise3')
        self.master.attributes("-fullscreen", True)
        self.master.bind("<F11>", self.toggle_fullscreen)
        self.master.bind("<Escape>", self.end_fullscreen)

        self.Full_B=Button(self.master,text='Full Screen',command=self.toggle_fullscreen,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=3,padx=20)
        self.Login_B=Button(self.master,text='Login',command=self.login,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=0)
        self.SignUp_B=Button(self.master,text='Sign Up',command=self.sign_up,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=1)
        self.About_B=Button(self.master,text='About',command=self.about,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=2)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state   # Just toggling the boolean
        self.master.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.master.attributes("-fullscreen", False)
        return "break"
    
    def login(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.resizable(width=False, height=False)
        muGUI=loginWindow(root2)

    def sign_up(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.resizable(width=False, height=False)
        muGUI=signupWindow(root2)
    
    def about(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.resizable(width=False, height=False)
        muGUI=aboutWindow(root2)


class loginWindow():
    def __init__(self, master):
        self.master = master
        self.master.geometry('610x780')
        self.master.title("Login")
        self.master.configure(background='turquoise3')
        
        self.Back_B=Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=0)
        self.adminButton=Button(self.master,text='Admin',command=self.adminlogin,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=1)
        self.LoginButton=Button(self.master,text='Login',command=self.adminlogin,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=2)

        
    def back(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.resizable(width=False, height=False)
        muGUI=Home(root2)
    
    def adminlogin(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.resizable(width=False, height=False)
        muGUI=Admin_Window(root2)
        
class Admin_Window():
    def __init__(self, master):
        self.master = master
        self.master.geometry('610x780')
        self.master.title("Admin Login")
        self.master.configure(background='turquoise3')

class signupWindow():
    def __init__(self, master):
        self.master = master
        self.master.geometry('610x780')
        self.master.title("Sign Up")
        self.master.configure(background='turquoise3')
        
        self.Back_B=Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=0)
    
    def back(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.resizable(width=False, height=False)
        muGUI=Home(root2)
        

class aboutWindow():
    def __init__(self, master):
        self.master = master
        self.master.geometry('610x780')
        self.master.title("About")
        self.master.configure(background='turquoise3')
        
        self.Back_B=Button(self.master,text='Back',command=self.back,bg='PaleTurquoise1',activebackground='turquoise3',bd=0,font='Bembo',fg='black',height=7,width=18).grid(row=1,column=0)
    
    def back(self):
        self.master.withdraw()
        root2=Toplevel(self.master)
        root2.resizable(width=False, height=False)
        muGUI=Home(root2)




def main():
    root=Tk()
    myGUIWelcome=Home(root)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.mainloop()

if __name__ == '__main__':
    main()
