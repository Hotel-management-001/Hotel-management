from  tkinter import*
from PIL  import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox





class cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital mangement system") 
        self.root.geometry("1295x550+230+220")

        #----------------------------variable-----------------------------------
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_post=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_idproof=StringVar()
        self.var_idnumber=StringVar()
        self.var_address=StringVar()
    

        #--------------------------------title----------------------------------------------------------
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


        #--------------------------------logo-----------------------------------------------------------------
        
        img2=Image.open(r"C:\Users\Vaibhav Gupta\OneDrive\Desktop\hotel management system\image\logo.jpg")
        img2=img2.resize((100,40),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lbling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbling.place(x=0,y=50,width=1295,height=50)
        #------------------------------label frame-------------------
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="CUSTOMER DETAILS",font=("times new roman",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #-------------------------------labels and entry-----------------------------------------------------------------
        label_cust_ref=Label(labelframeleft,text="Customer Ref:",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_cust_ref.grid(row=0,column=0,sticky=W)

        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,font=("times new roman",13,"bold"),width=29,state="readonly")
        entry_ref.grid(row=0,column=1)

        #cust name
        cname=Label(labelframeleft,text="Customer Name:",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1,column=0,sticky=W)
        entry_cname=ttk.Entry(labelframeleft,textvariable=self.var_cust_name,font=("arial",13,"bold"),width=29)
        entry_cname.grid(row=1,column=1)
        #mother  name
        lblmname=Label(labelframeleft,text="Mother Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_mother,font=("arial",13,"bold"),width=29)
        txtmname.grid(row=2,column=1)
        #gender combobox

        lbl_gender=Label(labelframeleft,text="Gender:",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_gender.grid(row=3,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.grid(row=3,column=1)
        combo_gender.current(0)
        #postcode
        lblpostcode=Label(labelframeleft,text="Postcode:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblpostcode.grid(row=4,column=0,sticky=W)
        txtpostcode=ttk.Entry(labelframeleft,textvariable=self.var_post,font=("times new roman",13,"bold"),width=29)
        txtpostcode.grid(row=4,column=1,sticky=W)
        #mobile number
        lblmobile=Label(labelframeleft,text="Mobile:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblmobile.grid(row=5,column=0,sticky=W)
        txtmobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("times new roman",13,"bold"),width=29)
        txtmobile.grid(row=5,column=1)
        #email
        lblemail=Label(labelframeleft,text="Email:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblemail.grid(row=6,column=0,sticky=W)
        txtemail=ttk.Entry(labelframeleft,textvariable=self.var_email,font=("times new roman",13,"bold"),width=29)
        txtemail.grid(row=6,column=1)
        #nationality
        lblnationality=Label(labelframeleft,text="Nationality:",font=("arial",12,"bold"),padx=2,pady=6)
        lblnationality.grid(row=7,column=0,sticky=W)
        combonationality=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")
        combonationality["value"]=("Indian","American","British")
        combonationality.grid(row=7,column=1)
        combonationality.current(0)

        #idproof type cobobox
        lblidproof=Label(labelframeleft,text="ID Proof:",font=("arial",12,"bold"),padx=2,pady=6)
        lblidproof.grid(row=8,column=0,sticky=W)
        combo_idproof=ttk.Combobox(labelframeleft,textvariable=self.var_idproof,font=("arial",12,"bold"),width=27,state="readonly")
        combo_idproof["value"]=("Aadhaar Card","PAN Card","Passport")
        combo_idproof.grid(row=8,column=1)
        combo_idproof.current(0)
        #id number
        lblidnumber=Label(labelframeleft,text="ID Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lblidnumber.grid(row=9,column=0,sticky=W)
        txtidnumber=ttk.Entry(labelframeleft,textvariable=self.var_idnumber,font=("arial",13,"bold"),width=29)
        txtidnumber.grid(row=9,column=1)
        #address
        lbladdress=Label(labelframeleft,text="Address:",font=("arial",12,"bold"),padx=2,pady=6)
        lbladdress.grid(row=10,column=0,sticky=W)
        txtaddress=ttk.Entry(labelframeleft,textvariable=self.var_address,font=("arial",13,"bold"),width=29)
        txtaddress.grid(row=10,column=1)
        #---------------------------btns-----------------------------
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)
        btnadd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width=9)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="Update",command=self.update,font=("arial",11,"bold"),bg="black",fg="gold",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btndelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",11,"bold"),bg="black",fg="gold",width=9)
        btndelete.grid(row=0,column=2,padx=1)

        btnreset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=9)
        btnreset.grid(row=0,column=3,padx=1)

        #-----------------------------table frame------------------------------------
        Table_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="VIew  DETAILS and Serch System",font=("arial",12,"bold"),padx=2)
        Table_frame.place(x=435,y=50,width=860,height=490)
        
        lblserchBy=Label(Table_frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lblserchBy.grid(row=0,column=0,sticky=W,padx=2)

        self.serch_var=StringVar()
        combo_serch=ttk.Combobox(Table_frame,textvariable=self.serch_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_serch["value"]=("Mobile No.","Ref")
        combo_serch.current(0)
        combo_serch.grid(row=0,column=1,padx=2)

        txtSearch=ttk.Entry(Table_frame,textvariable=self.text_serch,font=("arial",13,"bold"),width=24)
        txtSearch.grid(row=0,column=2,padx=2)

        btnSearch=Button(Table_frame,text="Serch",command=self.serch,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnSearch.grid(row=0,column=3,padx=1)

        btnshowAll=Button(Table_frame,text="Show All",command=self.fetch_data,font=("arial",11,"bold"),bg="black",fg="gold",width=10)
        btnshowAll.grid(row=0,column=4,padx=1)

        #--------------------------show date table------------------------------------------------
        details_table=Frame(Table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll__y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,columns=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll__y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll__y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll__y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationlity")
        self.Cust_Details_Table.heading("idproof",text="Id proof")
        self.Cust_Details_Table.heading("idnumber",text="Id number")
        self.Cust_Details_Table.heading("address",text="Address")



        self.Cust_Details_Table["show"]="headings"
       


        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)


    def add_data(self):
        if self.var_mobile.get()==""or self.var_cust_name.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
            return
        try:
        
            conn=mysql.connector.connect(host="localhost",username="root",password="vaibhav@2026",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s"),
                (self.var_ref.get(),
               self.var_cust_name.get(),
               self.var_mother.get(),
               self.var_gender.get(),
               self.var_post.get(),
               self.var_mobile.get(),
               self.var_email.get(),
               self.var_nationality.get(),
               self.var_idproof.get(),
               self.var_idnumber.get(),
               self.var_address.get()
               )
            
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","customer has been added",parent=self.root)
            
        except Exception as es:
            messagebox.showwarning("warning",f"something went wrong:{str()}",parent=self.root)   



    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="vaibhav@2026",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select* from customer") 
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table_get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,value=i)
                
            conn.close()
    def get_cuersor(self,event=""):
                cursor_row=self.cust_Details_Table.focus()
                content=self.cust_Details_table.item(cursor_row) 
                row=content["values"]
                
                if row:
                     self.var_ref.set(row[0]),
                     self.var_cust_name.set(row[1]),
                     self.var_mother.set(row[2]),
                     self.var_gender.set(row[3]),
                     self.var_post.set(row[4]),
                     self.var_mobile.set(row[5]),
                     self.var_email.set(row[6]),
                     self.var_nationality.set(row[7]),
                     self.var_id_proof.set(row[8]),
                     self.var_id_number.set(row[9]),
                     self.var_address.set(row[10]),
    def update(self):
        if self.var_mobile.get()=="":
             messagebox.showerror("Error","please enter mobiloe number ",parent=self.root)
        else:
             conn=mysql.connector.connect(host="localhost",username="root",password="vaibhav@2026",database="management")
             my_cursor=conn.cursor()
             my_cursor.execute("update* from customer set Name=%s,Mother=%s,Gender=%s,Postcode=%s,Mobile=%s,Email=%s,Nationality=%s,idproof=%s,idnumber=%s,Address=%s where Ref=%s",
                               ( 
                               (self.var_ref.get(),                                                                                                                                                                       
                                self.var_cust_name.get(),
                                self.var_mother.get(),
                                self.var_gender.get(),
                                self.var_post.get(),
                                self.var_mobile.get(),
                                self.var_email.get(),
                                self.var_nationality.get(),
                                self.var_idproof.get(),
                                self.var_idnumber.get(),
                                self.var_address.get(),
                                 self.var_ref.get(),
                                ))
            conn.commit()
            self.fetch_data()
            conn. close()
            messagebox.showinfo("update","customer details has been updated successfully")    

    def mDelete(self):
        mDelete=messagebox.askyesno("Hotel Management system","Do you want delete this customer",parents=self.root)
        if mDelete>0:
           conn=mysql.connector.connect(host="localhost",username="root",password=vaibhav@2026,database="management")
           my_cursor=conn.cursor()
           query="delete from customer ref =%s"  
           value=(self.var_ref.get(),)
           my_cursor.execute(query,value)
           else:
               if not mDelete:
                     return 
                conn.commit()
                self.fetch_data()
                conn.close()
    def reset(self):
         self.var_ref.set(row[0]),
                             self.var_cust_name.set(""),
                             self.var_mother.set(""),
                             
                             #self.var_gender.set(""),
                             self.var_post.set(""),
                             self.var_mobile.set(""),
                             self.var_email.set(""),
                            # self.var_nationality.set(""),
                             #self.var_id_proof.set(""),
                             self.var_id_number.set(""),
                             self.var_address.set(""),
                             self.var_ref=StringVar()
                             x=random.randint(1000,9999)
                             self.var_ref.set(str(x)) 
    def serch(self):
         conn=mysql.connector.connect(host="localhost",username="root",password=vaibahv@2026,database="management")
         my_cursor=conn.cursor()

         my_cursor.execute("select * from customer where"+str(self.serch_var.get())+"Like'%"+str(self.txt_serch.get)
         rows=my_cursor.fetchall()
         if len(rows)!=0:
              self.cust_Details_Table.delete(*self.cust_Details_table)
              for i in rows:
                self.cust_Details_table.insert("",END,values=i)
                conn.commit()
                conn.clase()


     rows=my_cursor.fetchall()
        

        


if __name__=="__main__":
    root=Tk()
    app=cust_win(root)
    root.mainloop()
