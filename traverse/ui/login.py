
from cgitb import text
from tkinter import *


root = Tk()
root.geometry("400x400")
Login_label = LabelFrame(root,text="Log In",padx=150,pady=50).pack(fill="both",expand="yes")
username_label= Label(Login_label, text ="Username -", )
username_label.place(x = 50, y = 20)
 
Username = Entry(Login_label,width=35)
Username.place(x = 150, y = 20, width = 200)
  
passwprd_label= Label(Login_label, text ="Password -")
passwprd_label.place(x = 50, y = 50)
 
password = Entry(Login_label, width = 70)
password.place(x = 150, y = 50, width = 200)
 
submitbtn = Button(Login_label, text ="Log In")
submitbtn.place(x = 150, y = 135, width = 155)
 
root.mainloop()