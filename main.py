from tkinter import *
from tkinter import messagebox
from twilio.rest import Client
import random

class otp_verification:
    def __init__(self,root):
        self.root=root
        self.root.title("OTP Verification System")
        self.root.geometry("600x500+300+70")
        self.root.resizable(False,False)

        self.can=Canvas(self.root,bg='white',width=400,height=280)
        self.can.place(x=100,y=60)

        self.title=Label(self.root,text='OTP Verification',font=('arial',20,'bold'),bg='white',fg='black')
        self.title.place(x=190,y=90)

        self.entry=Text(self.root,borderwidth=2,wrap='word',width=30,height=2)
        self.entry.place(x=180,y=160)

        self.btn_submit=Button(self.root,text='Submit',font=('times new roman',17,'bold'),bg='#ffebcd',fg='black')
        self.btn_submit.place(x=245,y=220)

        self.btn_resend=Button(self.root,text='Resend OTP',font=('times new roman',17,'bold'),bg='#e3cf57',fg='black')
        self.btn_resend.place(x=217,y=400)


root=Tk()
obj=otp_verification(root)
root.mainloop()