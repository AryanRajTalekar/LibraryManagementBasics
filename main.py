from tkinter import *
from tkinter import ttk


class basics:
    def __init__(self,root):
        self.root=root
        self.root.title("Library management")
        self.root.geometry("1920x1080+0+0")


        lbltitle=Label(self.root,text="Library Management System",bg="light blue",fg="green",bd=20,relief=RIDGE,font=("times new roman",50,"bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=2,pady=6,bg="light blue")
        frame.place(x=0, y=130, width=1530, height=700)

        # ========================DataFrameLeft========================#

        DataFrameLeft=LabelFrame(frame, bd=10, relief=RIDGE, padx=20, bg="light blue", font=("times new roman", 12, "bold",'underline'), text="Library Membership Information")
        DataFrameLeft.place(x=10,y=5,width=880,height=330)

        lblMemberType=Label(DataFrameLeft, text="Member Type", bg="light blue", fg="black", font=("times new roman", 12, "bold"))
        lblMemberType.grid(row=0, column=0, padx=2, pady=6, sticky=W)

        cmbMemberType=ttk.Combobox(DataFrameLeft,font=("times new roman", 12, "bold"), width=27)
        cmbMemberType["value"]=("Admin staff","Student","Lecturer")
        cmbMemberType.grid(row=0,column=1)

        lblMemberId=Label(DataFrameLeft, text="Member ID", bg="light blue", fg="black", font=("times new roman", 12, "bold"))
        lblMemberId.grid(row=1, column=0, padx=2, pady=6, sticky=W)

        lblMemberName=Label(DataFrameLeft, text="Member Name", bg="light blue", fg="black", font=("times new roman", 12, "bold"))
        lblMemberName.grid(row=2, column=0, padx=2, pady=6, sticky=W)

        lblMemberAddress=Label(DataFrameLeft, text="Member Address", bg="light blue", fg="black", font=("times new roman", 12, "bold"))
        lblMemberAddress.grid(row=3, column=0, padx=2, pady=6, sticky=W)

        lblMemberContact=Label(DataFrameLeft, text="Member Contact", bg="light blue", fg="black", font=("times new roman", 12,"bold"))
        lblMemberContact.grid(row=3, column=0, padx=2, pady=6, sticky=W)



        DataFrameRight = LabelFrame(frame, bd=10, relief=RIDGE, padx=20, bg="light blue",font=("times new roman", 12, "bold",'underline'), text="Book Details")
        DataFrameRight.place(x=920, y=5, width=550, height=330)

        #========================Buttons Frame========================#

        FrameButton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="light blue")
        FrameButton.place(x=15, y=505, width=1490, height=70)


             #========================Information Frame========================#

        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="light blue")
        FrameDetails.place(x=15, y=578, width=1490, height=120)


if __name__=="__main__":
    root=Tk()
    obj=basics(root)
    root.mainloop()
