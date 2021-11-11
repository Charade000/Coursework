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
            sql = "SELECT CustomerID,StartStreetNum,StartStreet,StartPostcode,DestinationStreetNum,DestinationStreet,DestinationPostcode,Fufilled,Date,Time,Forename,Driver FROM Bookings WHERE Forename LIKE '%"+q2+"' OR Driver LIKE '%"+q2+"' OR Date LIKE '%"+q2+"'"
            cursor.execute(sql)
            rows = cursor.fetchall()
            update(rows)
            
        # Removes Search
        def clear():
            sql = "SELECT CustomerID,StartStreetNum,StartStreet,StartPostcode,DestinationStreetNum,DestinationStreet,DestinationPostcode,Fufilled,Date,Time,Forename,Driver FROM Bookings"
            cursor.execute(sql)
            rows = cursor.fetchall()
            update(rows)
        
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
        def update_customer():
            bookingid = tbookingid.get()
            customerid = tcustid.get()
            startstreetnum = tstartstreetnum.get()
            startstreet = tstartstreet.get()
            startpost = tstartpost.get()
            deststreetnum = tdeststreetnum.get() ////////////////////####################################
            tdeststreet.get()
            tdestpost.get()
            tfufilled.get()
            tdate.get()
            ttime.get()
            tforename.get()
            tdriver.get()
            
            # Confirmation Box
            if messagebox.askyesno("Confirmation","Are you sure you want to update this customer?"):
                sql = "UPDATE Customer SET Forename = ?, Surname = ?, Email = ?,  MobileNum = ? WHERE CustomerID = ?"
                cursor.execute(sql,(fname,lname,email,num,custid))
                db.commit()
                clear()
        
        # Adds New Entry
        def add_new():
            fname = tcustid.get()
            lname = tstartstreetnum.get()
            num= tstartpost.get()
            email = tstartstreet.get()
            sql = """INSERT into Customer(Forename,Surname,Email,MobileNum)
                    VALUES(?,?,?,?)"""
            cursor.execute(sql,((fname),(lname),(email),(num)))
            db.commit()
            clear()
            
        # Deletes Entry
        def delete_customer():
            customer_id = tbookingid.get()
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
        IDEntry = Entry(wrapper3, textvariable=tbookingid)
        IDEntry.grid(row=0, column=1, padx=5, pady=3)
        
        ForenameLabel = Label(wrapper3, text="Forename",bg='turquoise3')
        ForenameLabel.grid(row=1, column=0, padx=5, pady=3)
        ForenameEntry = Entry(wrapper3, textvariable=tcustid)
        ForenameEntry.grid(row=1, column=1, padx=5, pady=3)
        
        SurnameLabel = Label(wrapper3, text="Surname",bg='turquoise3')
        SurnameLabel.grid(row=2, column=0, padx=5, pady=3)
        SurnameEntry = Entry(wrapper3, textvariable=tstartstreetnum)
        SurnameEntry.grid(row=2, column=1, padx=5, pady=3)
        
        EmailLabel = Label(wrapper3, text="Email",bg='turquoise3')
        EmailLabel.grid(row=3, column=0, padx=5, pady=3)
        EmailEntry = Entry(wrapper3, textvariable=tstartstreet)
        EmailEntry.grid(row=3, column=1, padx=5, pady=3)
        
        NumLabel = Label(wrapper3, text="Mobile Number",bg='turquoise3')
        NumLabel.grid(row=4, column=0, padx=5, pady=3)
        NumEntry = Entry(wrapper3, textvariable=tstartpost)
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