from cgitb import text
from tkinter import *


root = Tk()
root.geometry("400x400")
Login_label = LabelFrame(root,text="Payment Portal",padx=150,pady=50).pack(fill="both",expand="yes")
username_label= Label(Login_label, text ="Enter Card Number", )
username_label.place(x = 50, y = 20)
 
Username = Entry(Login_label,width=35)
Username.place(x = 180, y = 20, width = 150)
  
passwprd_label= Label(Login_label, text ="CVC Code")
passwprd_label.place(x = 50, y = 50)
 
password = Entry(Login_label, width = 70)
password.place(x = 180, y = 50, width = 150)

payment_label= Label(Login_label, text ="Payment Amount")
payment_label.place(x = 50, y = 80)
 
payment = Entry(Login_label, width = 70)
payment.place(x = 180, y = 80, width = 150)

 
submitbtn = Button(Login_label, text ="Pay")
submitbtn.place(x = 150, y = 135, width = 155)
 
root.mainloop()