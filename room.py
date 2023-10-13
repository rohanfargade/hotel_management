
#                                                    video 4/6


from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Room Booking System")
        self.root.geometry("1295x550+230+220")


        #************title***********
        lbl_title=Label(self.root,text="ROOMBOOKING DETAILS", font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1355,height=50)


        #**************logo************
        img2=Image.open(r"E:\Rohan_project\Hotel_management\images\bg_card.jpg")
        img2=img2.resize((100,40), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0, relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)



        #*************LabelFrame*************
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Roombooking Details",font=("arial",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)


        """now go to the hotel.py and add the following below the def cust_detalis
        
    def roombooking(self):
        self.new_window=toplevel(self.root)
        self.app=Roombooking(self.new_window)
            now go to the upper side button ROOM type
            ....."ROOM",command=self.roombooking

        """

        #************labels and entrys************
        #Customer Contact
        lbl_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)

        enty_contact=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=20,)
        enty_contact.grid(row=0,column=1,sticky=W)

        #Fetach data Button
        btnFetchdata=Button(labelframeleft,text="Fetch Data",font=("arial",10,"bold"),bg="black",fg="gold",width=8)
        btnFetchdata.place(x=340,y=4)


        #check in date
        check_in_date=Label(labelframeleft,font=("arial",12,"bold"),text="Check_in Date:",padx=2,pady=6)
        check_in_date.grid(row=1,column=0,sticky=W)
        textcheck_in_date=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        textcheck_in_date.grid(row=1,column=1)

        # check out date
        lbl_Check_out=Label(labelframeleft,font=("arial",12,"bold"),text="Check_out Date:",padx=2,pady=6)
        lbl_Check_out.grid(row=1,column=0,sticky=W)
        text_Check_out=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        text_Check_out.grid(row=1,column=1)

        #Room type
        label_RoomType=Label(labelframeleft,font=("arial",12,"bold"),text="Room Type:",padx=2,pady=6)
        label_RoomType.grid(row=3,column=0,sticky=W)

        combo_RoomType=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=12,state="readonly")
        combo_RoomType["value"]=("Single","Double","Luxury")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)


        #Available Room
        lblRoomAvailable=Label(labelframeleft,font=("arial",12,"bold"),text="Available room:",padx=2,pady=6)
        lblRoomAvailable.grid(row=4,column=0,sticky=W)
        txtRoomAvailable=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtRoomAvailable.grid(row=4,column=1)


        #Meal
        lblMeal=Label(labelframeleft,font=("arial",12,"bold"),text="Meal:",padx=2,pady=6)
        lblMeal.grid(row=5,column=0,sticky=W)
        txtMeal=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtMeal.grid(row=5,column=1)


        # No Of Days
        lblNoOfDays=Label(labelframeleft,font=("arial",12,"bold"),text="No Of Days:",padx=2,pady=6)
        lblNoOfDays.grid(row=6,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=6,column=1)


        # Paid tax
        lblNoOfDays=Label(labelframeleft,font=("arial",12,"bold"),text="Pais tax:",padx=2,pady=6)
        lblNoOfDays.grid(row=7,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=7,column=1)


        # Sub Total
        lblNoOfDays=Label(labelframeleft,font=("arial",12,"bold"),text="Sub Total:",padx=2,pady=6)
        lblNoOfDays.grid(row=8,column=0,sticky=W)
        txtNoOfDays=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtNoOfDays.grid(row=8,column=1)


        # Total Cost
        lblIdNumber=Label(labelframeleft,font=("arial",12,"bold"),text="Total Cost:",padx=2,pady=6)
        lblIdNumber.grid(row=9,column=0,sticky=W)
        txtIdNumber=ttk.Entry(labelframeleft,font=("arial",13,"bold"),width=29)
        txtIdNumber.grid(row=9,column=1)


        #***************Bill Button*************
        btnBill=Button(labelframeleft,text="Bill",font=("arial",13,"bold"),bg="black",fg="gold",width=8)
        btnBill.grid(row=10,column=0,padx=2,sticky=W)


        #=====================buttons====================================
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="ADD",font=("arial",13,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=2)

        btnUpdate=Button(btn_frame,text="Update",font=("arial",13,"bold"),bg="black",fg="gold",width=8)
        btnUpdate.grid(row=0,column=1,padx=8)

        btnDelete=Button(btn_frame,text="Delete",font=("arial",13,"bold"),bg="black",fg="gold",width=8)
        btnDelete.grid(row=0,column=2,padx=8)

        btnReset=Button(btn_frame,text="Reset",font=("arial",13,"bold"),bg="black",fg="gold",width=8)
        btnReset.grid(row=0,column=3,padx=8)


        #*******************Rightside image*****************
        img3=Image.open(r"E:\Rohan_project\Hotel_management\images\bg_card.jpg")
        img3=img3.resize((800,200), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0, relief=RIDGE)
        lblimg.place(x=860,y=55,width=300,height=300)



        #=======================================table frame=======================================
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search system",font=("arial",15,"bold"),padx=2)
        Table_Frame.place(x=435,y=280,width=920,height=260)

        lblSearchBy=Label(Table_Frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lblSearchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",15,"bold"),width=24,state="readonly")
        combo_search["value"]=("Contact","Room")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)


        self.txt_search=StringVar()
        txtSearch=ttk.Entry(Table_Frame,textvariable=self.txt_search,font=("arial",15,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_Frame,text="Seacrh",font=("arial",13,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnShowAll=Button(Table_Frame,text="Show All",font=("arial",13,"bold"),bg="black",fg="gold",width=10)
        btnShowAll.grid(row=0,column=4,padx=1)


        #==============================show data table===========================================
        details_table=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.room_table=ttk.Treeview(details_table,column=("contact","checkinDate","checkoutDate","roomType","roomavailable","meal","NoOfDays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        
        self.room_table.heading("contact", text="Mobile")
        self.room_table.heading("checkinDate", text="Check-in")  # Corrected the column name
        self.room_table.heading("checkoutDate", text="Check-out")  # Corrected the column name
        self.room_table.heading("roomType", text="Room Type")
        self.room_table.heading("roomavailable", text="Room no")
        self.room_table.heading("meal", text="Meal")



        self.room_table["show"]="headings"
        
        self.room_table.column("contact", width=100)
        self.room_table.column("checkinDate", width=100)  # Corrected the column name
        self.room_table.column("checkoutDate", width=100)  # Corrected the column name
        self.room_table.column("roomType", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)


        self.room_table.pack(fill=BOTH,expand=1)




if __name__ == "__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()
