from cgitb import text
from tkinter import *

root = Tk()
root.title("Traverse")
root.geometry("400x400")
Login_label = LabelFrame(root,text="Register",padx=150,pady=50).pack(fill="both",expand="yes")

full_label= Label(Login_label, text ="Fullname  ", )
full_label.place(x = 50, y = 20)
 
fullname = Entry(Login_label,width=35)
fullname.place(x = 150, y = 20, width = 200)

email_label= Label(Login_label, text ="Email  ", )
email_label.place(x = 50, y = 60)
 
email = Entry(Login_label,width=35)
email.place(x = 150, y = 60, width = 200)

username_label= Label(Login_label, text ="Username  ", )
username_label.place(x = 50, y = 100)
 
Username = Entry(Login_label,width=35)
Username.place(x = 150, y = 100, width = 200)
  
passwprd_label= Label(Login_label, text ="Password  ")
passwprd_label.place(x = 50, y = 140)
 
password = Entry(Login_label, width = 70)
password.place(x = 150, y = 140, width = 200)
 
submitbtn = Button(Login_label, text ="Register",)
submitbtn.place(x = 150, y = 180, width = 155)
 
root.mainloop()