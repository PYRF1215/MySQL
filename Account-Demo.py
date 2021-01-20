#1

from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pymysql

#2

class ConnectorDB:
    
    def __init__(self,root):
        self.root = root
        titlespace = " "
        self.root.title(102 *titlespace + "MySQL Connector")
        self.root.geometry("800x700+300+0")
        self.root.resizable(width=False,height=False)
        
        
            
        MainFrame = Frame(self.root,bd=10,width=770,relief=RIDGE,bg='cadet blue')
        MainFrame.grid()
        
        TitleFrame = Frame(MainFrame,bd=7,width=770,height=100,relief=RIDGE)
        TitleFrame.grid(row = 0,column = 0)
        RF = Frame(MainFrame,bd=5,width=770,height=500,relief=RIDGE)
        RF.grid(row = 1,column = 0)
        
        LF = Frame(RF,bd=5,width=770,height=400,padx=2,bg="cadet blue",relief=RIDGE)
        LF.pack(side=LEFT)
        LF1 = Frame(LF,bd=5,width=600,height=180,padx=12,pady=9,relief=RIDGE)
        LF1.pack(side=TOP)
        
        RF1 = Frame(RF,bd=5,width=100,height=400,padx=2,bg="cadet blue",relief=RIDGE)
        RF1.pack(side=RIGHT)
        RF1a = Frame(RF1,bd=5,width =90,height=300,padx=2,pady=2,relief=RIDGE)
        RF1a.pack(side=TOP)
        
#3
        
        itemname = StringVar()
        account = StringVar()
        pd = StringVar()
        email = StringVar()
        category = StringVar()
        remarks = StringVar()
        
#4
        def iExit():
            iExit = tkinter.messagebox.askyesno("MySql Connection","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        
        
        def Reset():
            self.entitemname.delete(0,END)
            self.entaccount.delete(0,END)
            self.entpd.delete(0,END)
            self.entemail.delete(0,END)
            category.set("")
            self.entremarks.delete(0,END)
            
            
     
        def addData():
             if itemname.get() == "" or account.get() == "" or pd.get()=="":
                 tkinter.messagebox.showerror("Mysql Connection","Enter Correct Details")            
             else:
                 sqlCon=pymysql.connect(host="localhost",user="root",password="mysql123",database="ycaccount")
                 cur = sqlCon.cursor()
                 cur.execute("insert into account_tab values(%s,%s,%s,%s,%s,%s)",(
                     
                 itemname.get(),
                 account.get(),
                 pd.get(),
                 email.get(),
                 category.get(),
                 remarks.get(),        
                 ))
                 sqlCon.commit()
                 sqlCon.close()
                 tkinter.messagebox.showinfo("MySql Connection","Record Updated Successfully")
                     

        def DisplayData():
            sqlCon=pymysql.connect(host="localhost",user="root",password="mysql123",database="ycaccount")
            cur = sqlCon.cursor()
            cur.execute("select * from account_tab")        
            result = cur.fetchall()
            if len(result) !=0:
                self.records.delete(*self.records.get_children())
                for row in result:
                        self.records.insert('',END,values = row)
                sqlCon.commit()
            sqlCon.close()
                     
         
        def ycaccountInfo(ev):
            viewInfo = self.records.focus()
            learnerData = self.records.item(viewInfo)
            row = learnerData['values']
            itemname.set(row[0])
            account.set(row[1])
            pd.set(row[2])
            email.set(row[3])
            category.set(row[4])
            remarks.set(row[5])   
            
        def update():
             sqlCon=pymysql.connect(host="localhost",user="root",password="mysql123",database="ycaccount")
             cur = sqlCon.cursor()
             

             cur.execute("update account_tab set account=%s,password=%s,email=%s,category=%s,remarks=%s where itemname=%s",(
                    
             account.get(),
             pd.get(),
             email.get(),
             category.get(),
             remarks.get(),        
             itemname.get()
             ))
             sqlCon.commit()
             sqlCon.close()
             tkinter.messagebox.showinfo("Data Entry Form","Record Updated Successfully")
                     
            
        def deleteDB():
            sqlCon = pymysql.connect(host="localhost",user="root",password="mysql123",database="ycaccount")
            cur = sqlCon.cursor()
            cur.execute("delete from account_tab where itemname=%s",itemname.get())
            
            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry From","Record Successfully Deleted")
            Reset()    
            
        def searchDB():
            try:
                sqlCon = pymysql.connect(host="localhost",user="root",password="mysql123",database="ycaccount")
                cur = sqlCon.cursor()
                cur.execute("select * from account_tab where itemname='%s'"%itemname.get())
                
                row = cur.fetchone()
                
                itemname.set(row[0])
                account.set(row[1])
                pd.set(row[2])
                email.set(row[3])
                category.set(row[4])
                remarks.set(row[5])
                
                sqlCon.commit()
                
            except:
                tkinter.messagebox.showinfo("Data Entry From","No such Record Found")
                Reset()
            sqlCon.close()
                
#5
        
        self.lbltitle=Label(TitleFrame,font=('arial',40,'bold'),text="MySQL Connection",bd=7)
        self.lbltitle.grid(row=0,column=0,padx=132)


        self.lblitemname=Label(LF1, font=('arial',12,'bold'),text="ItemName",bd=7)
        self.lblitemname.grid(row=1,column=0,sticky=W,padx=5)
        self.entitemname=Entry(LF1,font=('arial',12,'bold'),bd=5,width=44,justify='left',textvariable=itemname)
        self.entitemname.grid(row=1,column=1,sticky=W,padx=5)
        
        self.lblaccount=Label(LF1, font=('arial',12,'bold'),text="Account",bd=7)
        self.lblaccount.grid(row=2,column=0,sticky=W,padx=5)
        self.entaccount=Entry(LF1, font=('arial',12,'bold'),bd=5,width=44,justify='left',textvariable=account)
        self.entaccount.grid(row=2,column=1,sticky=W, padx=5)
        
        self.lblpd=Label(LF1,font=('arial',12,'bold'),text="Password",bd=7)
        self.lblpd.grid(row=3,column=0,sticky=W ,padx=5)
        self.entpd=Entry(LF1,font=('arial',12,'bold'),bd=5,width=44,justify='left',textvariable=pd)
        self.entpd.grid(row=3,column=1,sticky=W,padx=5)
        
        self.lblemail = Label(LF1,font=('arial',12,'bold'),text="Email",bd=7,)
        self.lblemail.grid(row=4,column=0,sticky=W,padx=5)
        self.entemail = Entry(LF1,font=('arial',12,'bold'),bd=5,width=44,justify='left',textvariable=email)
        self.entemail.grid(row=4,column=1)
        
        self.lblcategory = Label(LF1,font=('arial',12,'bold'),text="Category",bd=5,)
        self.lblcategory.grid(row=5,column=0,sticky=W,padx=5)
        self.cbocategory =ttk.Combobox(LF1,font=('arial',12,'bold'),width=43,state='readonly',textvariable=category)
        self.cbocategory['values']=('','Female','Male')
        self.cbocategory.current(0)
        self.cbocategory.grid(row=5,column=1)
        
        self.lblremarks = Label(LF1, font=('arial',12,'bold'),text="Remarks",bd=5)
        self.lblremarks.grid(row=6,column=0,sticky=W,padx=5)
        self.entremarks = Entry(LF1,font=('arial',12,'bold'),bd=5,width=44,textvariable=remarks)
        self.entremarks.grid(row=6,column=1,sticky=W,padx=5)


#6
        scroll_y=Scrollbar(LF,orient=VERTICAL)
        
        self.records = ttk.Treeview(LF,height=12,columns=("itemname","account","password","email","category","remarks"),yscrollcommand=scroll_y.set)
        
        scroll_y.pack(side = RIGHT, fill=Y)
        

        self.records.heading("itemname",text="ItemName")
        self.records.heading("account",text="Account")
        self.records.heading("password",text="Password")
        self.records.heading("email",text="Email")
        self.records.heading("category",text="Category")
        self.records.heading("remarks",text="Remarks")
        
        self.records['show']='headings'
        
        self.records.column("itemname",width=70)
        self.records.column("account",width=100)
        self.records.column("password",width=100)
        self.records.column("email",width=100)
        self.records.column("category",width=70)
        self.records.column("remarks",width=70)
        
        self.records.pack(fill =BOTH, expand=1)
        # DisplayData()
        self.records.bind("<ButtonRelease-1>",ycaccountInfo)
        
#7
        
        
        
        self.btnAddNew=Button(RF1a,font=('arial',16,'bold'),text="Add New",bd=4,pady=1,padx=24,
                       width=8,height=2, command=addData).grid(row=0, column=0,padx=1)

        self.btnDisplay=Button(RF1a,font=('arial',16,'bold'),text="Display",bd=4,pady=1,padx=24,
                       width=8,height=2,command=DisplayData).grid(row=1, column=0,padx=1)

        self.btnUpdate=Button(RF1a,font=('arial',16,'bold'),text="Update",bd=4,pady=1,padx=24,
                       width=8,height=2,command=update).grid(row=2, column=0,padx=1)

        self.btnDelete=Button(RF1a,font=('arial',16,'bold'),text="Delete",bd=4,pady=1,padx=24,
                       width=8,height=2,command=deleteDB).grid(row=3, column=0,padx=1)

        self.btnSearch=Button(RF1a,font=('arial',16,'bold'),text="Search",bd=4,pady=1,padx=24,
                       width=8,height=2,command=searchDB).grid(row=4, column=0,padx=1)

        self.btnReset=Button(RF1a,font=('arial',16,'bold'),text="Reset",bd=4,pady=1,padx=24,
                       width=8,height=2,command=Reset).grid(row=5, column=0,padx=1)

        self.btnExit=Button(RF1a,font=('arial',16,'bold'),text="Exit",bd=4,pady=1,padx=24,
                       width=8,height=2,command=iExit).grid(row=6, column=0,padx=1)
        
        
        
#8
        
if __name__ =="__main__":
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()



