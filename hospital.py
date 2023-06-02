from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class hospital:
    # window name is root
    def __init__(self,root):
        self.root = root
        # giving title to the window
        self.root.title("Hospital Management System")
        # we have to give height,width,x-axis,y-axis to the window
        self.root.geometry("1540x800+0+0")
    
        #self matlab voh object jispe yeh method call ho rha
        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate =StringVar()
        self.DailyDose = StringVar()
        self.sideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine =StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientId  =StringVar()
        self.nhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()



    # label title
    # border,border-style
        lbltitle = Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="green",bg="powder blue",font=("times new roman",50,"bold")) 
        # we have to pack to show title
        # hume x-axis mai fill krna tha
        lbltitle.pack(side=TOP,fill=X)

        #=======Dataframe==========
        Dataframe = Frame(self.root,bg="powder blue",bd = 20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

        DataframeLeft = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,bg="powder blue",font=("times new roman",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)

        DataframeRight = LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,bg="powder blue",font=("arial",12,"bold"),text="Prescription")
        DataframeRight.place(x=990,y=5,width=460,height=350)

        #================== buttons frame ============
        Buttonframe =Frame(self.root,bd=20,bg="powder blue",relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)

        #=================== details frame ============

        Detailsframe = Frame(self.root,bg="powder blue",bd=10,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)

        #=============dataframe left======================
        lblNameTablet = Label(DataframeLeft,text="Names of tablet",bg="powder blue",font=("times new roman",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNametablet  =ttk.Combobox(DataframeLeft,textvariable=self.Nameoftablets,font=("times new roman",12,"bold"),width=35)
        comNametablet["values"]=("Nice","Corona Vaccine","Acetaminophen","Adderall","Amlodipine","Ativan")
        comNametablet.grid(row=0,column=1)

        lblref = Label(DataframeLeft,font=("Arial",12,"bold"),bg="powder blue",text="Refernce No.",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref= Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.ref,width=33)
        txtref.grid(row=1,column=1)

        lblDose = Label(DataframeLeft,font=("arial",12,"bold"),bg="powder blue",text="Dose",padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Dose,width=33)
        txtDose.grid(row=2,column=1)

        lblNoOftablets = Label(DataframeLeft,font=("arial",12,"bold"),bg="powder blue",text="No of Tablets::",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets = Entry(DataframeLeft,font=("Arial",13,"bold"),textvariable = self.NumberofTablets,width=33)
        txtNoOftablets.grid(row=3,column=1)

        lblLot=Label(DataframeLeft,font=("arial",12,"bold"),bg="powder blue",text="Lot::",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Lot,width=33)
        txtLot.grid(row=4,column=1)

        lblIssueDate = Label(DataframeLeft,font=("arial",12,"bold"),bg="powder blue",text="Issue Date",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtissueDate = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.Issuedate,width=33)
        txtissueDate.grid(row=5,column=1)

        lblExpDate = Label(DataframeLeft,font=("arial",12,"bold"),bg="powder blue",text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate = Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.ExpDate,width=33)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose = Label(DataframeLeft,font=("arial",12,"bold"),bg="powder blue",text="Daily Dose:",padx=2,pady=4)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.DailyDose,width=33)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffect = Label(DataframeLeft,font=("arial",12,"bold"),bg="powder blue",text="Side Effect:",padx=2,pady=4)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.sideEffect,width=33)
        txtSideEffect.grid(row=8,column=1)

        lblFurtherinfo = Label(DataframeLeft,font=("arial",12,"bold"),bg="powder blue",text="Further Information:",padx=2,pady=4)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo= Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.FurtherInformation,width=33)
        txtFurtherinfo.grid(row=0,column=3)

        lblDrivingMachine = Label(DataframeLeft,font=("arial",12,"bold"),bg="powder blue",text="Blood Pressure",padx=2,pady=6)
        lblDrivingMachine.grid(row=1,column=2,sticky=W)
        txtDrivingMachine = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.DrivingUsingMachine,width=33)
        txtDrivingMachine.grid(row=1,column=3)

        lblStorage = Label(DataframeLeft,font=("arial",12,"bold"),bg="powder blue",text="Storage Advice",padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.StorageAdvice,width=33)
        txtStorage.grid(row=2,column=3)

        lblMedicine = Label(DataframeLeft,font=("arial",12,"bold"),bg="powder blue",text="Medication",padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.HowToUseMedication,width=33)
        txtMedicine.grid(row=3,column=3)

        lblPatientId = Label(DataframeLeft,font=("arial",12,"bold"),bg="powder blue",text="Patient Id",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.PatientId,width=33)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber = Label(DataframeLeft,font=("arial",12,"bold"),bg="powder blue",text="NHS Number",padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.nhsNumber,width=33)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientName = Label(DataframeLeft,font=("arial",12,"bold"),bg="powder blue",text="Patient Name",padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.PatientName,width=33)
        txtPatientName.grid(row=6,column=3)

        lblDateofBirth = Label(DataframeLeft,font=("arial",12,"bold"),bg="powder blue",text="Date of Birth",padx=2,pady=6)
        lblDateofBirth.grid(row=7,column=2,sticky=W)
        txtDateofBirth = Entry(DataframeLeft,font=("arial",13,"bold"),textvariable=self.DateOfBirth,width=33)
        txtDateofBirth.grid(row=7,column=3)

        lblPatientAddress = Label(DataframeLeft,font=("arial",12,"bold"),bg="powder blue",text="Patient Address",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress = Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.PatientAddress,width=33)
        txtPatientAddress.grid(row=8,column=3)



        #==============DataFrameRight===============
        self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),bg="powder blue",width=47,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

        #=============Buttons========================
        btnPrescription = Button(Buttonframe,command=self.iPrescription,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=20,pady=6)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData = Button(Buttonframe,command=self.iPrescriptionData,text="Prescription Data",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate = Button(Buttonframe,command=self.update_data,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete = Button(Buttonframe,command=self.idelete,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear = Button(Buttonframe,command=self.clear,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnClear.grid(row=0,column=4)

        btnExit = Button(Buttonframe,command=self.iExit,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnExit.grid(row=0,column=5)


        #=====================table==========================
        #======================scroll bar=====================
        scroll_x = ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe,column=("nameoftable","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand = scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name of Table")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"] = "headings"
        

        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)




        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()



        #===================functionality declaration==============
    def iPrescriptionData(self):
        if(self.Nameoftablets.get()=="" or self.ref.get() ==""):
            messagebox.showerror("Error","All fields are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="#Akshit1093",database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Nameoftablets.get(),
                                                                    self.ref.get(),
                                                                    self.Dose.get(),
                                                                    self.NumberofTablets.get(),
                                                                    self.Lot.get(),
                                                                    self.Issuedate.get(),
                                                                    self.ExpDate.get(),
                                                                    self.DailyDose.get(),
                                                                    self.StorageAdvice.get(),
                                                                    self.nhsNumber.get(),
                                                                    self.PatientName.get(),
                                                                    self.DateOfBirth.get(),
                                                                    self.PatientAddress.get()          
                                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")
    def update_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="#Akshit1093",database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("UPDATE hospital SET Nameoftablets=%s,dose=%s,Numberoftablets=%s,lot=%s,issuedate=%s,expdate=%s,dailydose=%s,storage=%s,nhsnumber=%s,patientname=%s,DOB=%s,patientaddress=%s WHERE Reference_No=%s",(self.Nameoftablets.get(),
                                                                 
                                                                    self.Dose.get(),
                                                                    self.NumberofTablets.get(),
                                                                    self.Lot.get(),
                                                                    self.Issuedate.get(),
                                                                    self.ExpDate.get(),
                                                                    self.DailyDose.get(),
                                                                    self.StorageAdvice.get(),
                                                                    self.nhsNumber.get(),
                                                                    self.PatientName.get(),
                                                                    self.DateOfBirth.get(),
                                                                    self.PatientAddress.get(),
                                                                    self.ref.get()   
                                                                  )
                                                                )

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="#Akshit1093",database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])

    def iPrescription(self):
        self.txtPrescription.insert(END,"Name of Tablets:\t\t\t"+str(self.Nameoftablets.get())+"\n")
        self.txtPrescription.insert(END,"Reference No:\t\t\t"+str(self.ref.get())+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+str(self.Dose.get())+"\n")
        self.txtPrescription.insert(END,"Number of Tablets:\t\t\t"+str(self.NumberofTablets)+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+str(self.Lot.get())+"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t"+str(self.Issuedate.get())+"\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t\t"+str(self.ExpDate.get())+"\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t"+str(self.DailyDose.get())+"\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t"+str(self.sideEffect.get())+"\n")
        self.txtPrescription.insert(END,"Further Information:\t\t\t"+str(self.FurtherInformation.get())+"\n")
        self.txtPrescription.insert(END,"Storage Advice:\t\t\t"+str(self.StorageAdvice.get())+"\n")
        self.txtPrescription.insert(END,"DrivingUsingMachine:\t\t\t"+str(self.DrivingUsingMachine.get())+"\n")
        self.txtPrescription.insert(END,"Patient Id:\t\t\t"+str(self.PatientId.get())+"\n")
        self.txtPrescription.insert(END,"NHS Number:\t\t\t"+str(self.nhsNumber.get())+"\n")
        self.txtPrescription.insert(END,"Patient Name:\t\t\t"+str(self.PatientName.get())+"\n")
        self.txtPrescription.insert(END,"DateofBirth:\t\t\t"+str(self.DateOfBirth.get())+"\n")
        self.txtPrescription.insert(END,"PatientAddress:\t\t\t"+str(self.PatientAddress.get())+"\n")

    def idelete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="#Akshit1093",database="mydata")
        my_cursor = conn.cursor()
        query="delete from hospital where Reference_No=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Patient has been deleted successfully")

    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)

    def iExit(self):
        iExit = messagebox.askyesno("Hospital Management System","Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return





root=Tk()
ob = hospital(root)
root.mainloop()
ob.iPrescriptionData()


