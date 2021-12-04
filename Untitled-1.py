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
            tstaffid = StringVar() 
            tforename = StringVar()
            tsurname = StringVar()
            temail = StringVar()
            tmobilenum = StringVar()
            tcapabilities = StringVar() 
            tavailability = StringVar()
            tstreetnum = StringVar()
            tstreetname = StringVar()
            tdate = StringVar()
            ttime = StringVar() 
            tforename = StringVar()
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
                sql = "SELECT BookingsID,CustomerID,StartStreetNum,StartStreet,StartPostcode,DestinationStreetNum,DestinationStreet,DestinationPostcode,Fufilled,Date,Time,Forename,Driver FROM Bookings WHERE Forename LIKE '%"+q2+"' OR Driver LIKE '%"+q2+"' OR Date LIKE '%"+q2+"' OR StartPostcode LIKE '%"+q2+"' OR CustomerID LIKE '%"+q2+"' OR Fufilled LIKE '%"+q2+"' OR StartStreet LIKE '%"+q2+"' OR BookingsID LIKE '%"+q2+"' OR DestinationStreet LIKE '%"+q2+"' OR DestinationPostcode LIKE '%"+q2+"'"
                cursor.execute(sql)
                rows = cursor.fetchall()
                update(rows)
                db.close()
                
            # Removes Search
            def clear():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                sql = "SELECT BookingsID,CustomerID,StartStreetNum,StartStreet,StartPostcode,DestinationStreetNum,DestinationStreet,DestinationPostcode,Fufilled,Date,Time,Forename,Driver FROM Bookings"
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
                tdate.set(item['values'][9])
                ttime.set(item['values'][10])
                tforename.set(item['values'][11])
                tpostcode.set(item['values'][12])
                
            # Change an existing entry
            def update_customer():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                bookingid = tstaffid.get()
                customerid = tforename.get()
                startstreetnum = tsurname.get()
                startstreet = temail.get()
                startpost = tmobilenum.get()
                deststreetnum = tcapabilities.get()
                deststreet = tavailability.get()
                destpost = tstreetnum.get()
                fufilled = tstreetname.get()
                date = tdate.get()
                time = ttime.get()
                forename = tforename.get()
                driver = tpostcode.get()
                

                # Confirmation Box
                if messagebox.askyesno("Confirmation","Are you sure you want to update this Booking?"):
                    sql = "UPDATE Bookings SET CustomerID = ? , StartStreetNum = ? , StartStreet = ? , StartPostcode = ? , DestinationStreetNum = ? , DestinationStreet = ? , DestinationPostcode = ? , Fufilled = ? ,Date = ?, Time = ?, Forename = ?, Driver = ? WHERE BookingsID = ?"
                    cursor.execute(sql,(customerid,startstreetnum,startstreet,startpost,deststreetnum,deststreet,destpost,fufilled,date,time,forename,driver,bookingid))

                    db.commit()
                    clear()
                db.commit()
                db.close()
            
            # Adds New Entry
            def add_new():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                customerid = tforename.get()
                startstreetnum = tsurname.get()
                startstreet = temail.get()
                startpost = tmobilenum.get()
                deststreetnum = tcapabilities.get()
                deststreet = tavailability.get()
                destpost = tstreetnum.get()
                fufilled = tstreetname.get()
                date = tdate.get()
                time = ttime.get()
                forename = tforename.get()
                driver = tpostcode.get()
                sql = """INSERT into Bookings (CustomerID, StartStreetNum,StartStreet,StartPostcode,DestinationStreetNum,DestinationStreet,DestinationPostcode,Fufilled,Date,Time,Forename,Driver)
                        VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"""
                cursor.execute(sql,((customerid),(startstreetnum),(startstreet),(startpost),(deststreetnum),(deststreet),(destpost),(fufilled),(date),(time),(forename),(driver)))
                    
                db.commit()
                db.close()
                clear()
                
            # Deletes Entry
            def delete_customer():
                db =sqlite3.connect("main.db")
                cursor = db.cursor()
                bookingid = tstaffid.get()
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
            
            
            trv = ttk.Treeview(wrapper1, columns=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15), show="headings", height="6")
            trv.pack(fill="both", expand="yes",padx=20,pady=10)
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
            trv.heading(13, text="Driver")
            
            trv.bind('<Double 1>', getrow)
            
            db =sqlite3.connect("main.db")
            cursor = db.cursor()
            
            sql = "SELECT BookingsID, CustomerID, StartStreetNum,StartStreet,StartPostcode,DestinationStreetNum,DestinationStreet,DestinationPostcode,Fufilled,Date,Time,Forename,Driver FROM Bookings"
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
            BookIDEntry = Entry(wrapper3, textvariable=tstaffid)
            BookIDEntry.grid(row=0, column=1, padx=5, pady=3)
            
            CustIDLabel = Label(wrapper3, text="Customer ID",bg='turquoise3')
            CustIDLabel.grid(row=1, column=0, padx=5, pady=3)
            CustIDEntry = Entry(wrapper3, textvariable=tforename)
            CustIDEntry.grid(row=1, column=1, padx=5, pady=3)
            
            startstreetnumLabel = Label(wrapper3, text="Start Street Num",bg='turquoise3')
            startstreetnumLabel.grid(row=2, column=0, padx=5, pady=3)
            startstreetnumEntry = Entry(wrapper3, textvariable=tsurname)
            startstreetnumEntry.grid(row=2, column=1, padx=5, pady=3)
            
            startstreetLabel = Label(wrapper3, text="Start Street",bg='turquoise3')
            startstreetLabel.grid(row=3, column=0, padx=5, pady=3)
            startstreetEntry = Entry(wrapper3, textvariable=temail)
            startstreetEntry.grid(row=3, column=1, padx=5, pady=3)
            
            startpostLabel = Label(wrapper3, text="Start Postcode",bg='turquoise3')
            startpostLabel.grid(row=4, column=0, padx=5, pady=3)
            startpostEntry = Entry(wrapper3, textvariable=tmobilenum)
            startpostEntry.grid(row=4, column=1, padx=5, pady=3)
            
            deststreetnumLabel = Label(wrapper3, text="Dest Street Num",bg='turquoise3')
            deststreetnumLabel.grid(row=5, column=0, padx=5, pady=3)
            deststreetnumEntry = Entry(wrapper3, textvariable=tcapabilities)
            deststreetnumEntry.grid(row=5, column=1, padx=5, pady=3)
            
            DestStreetLabel = Label(wrapper3, text="Dest Street",bg='turquoise3')
            DestStreetLabel.grid(row=6, column=0, padx=5, pady=3)
            DestStreetEntry = Entry(wrapper3, textvariable=tavailability)
            DestStreetEntry.grid(row=6, column=1, padx=5, pady=3)
            
            destpostLabel = Label(wrapper3, text="Dest Postcode",bg='turquoise3')
            destpostLabel.grid(row=7, column=0, padx=5, pady=3)
            destpostEntry = Entry(wrapper3, textvariable=tstreetnum)
            destpostEntry.grid(row=7, column=1, padx=5, pady=3)
            
            fufilledLabel = Label(wrapper3, text="Fufilled",bg='turquoise3')
            fufilledLabel.grid(row=8, column=0, padx=5, pady=3)
            fufilledEntry = Entry(wrapper3, textvariable=tstreetname)
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
            
            driverLabel = Label(wrapper3, text="Driver",bg='turquoise3')
            driverLabel.grid(row=12, column=0, padx=5, pady=3)
            driverEntry = Entry(wrapper3, textvariable=tpostcode)
            driverEntry.grid(row=12, column=1, padx=5, pady=3)
            
            # Buttons
            UpdateButton = Button(wrapper3, text="Update", command=update_customer)
            AddButton = Button(wrapper3, text="Add New", command=add_new)
            DeleteButton = Button(wrapper3, text="Delete", command=delete_customer)
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