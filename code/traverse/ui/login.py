from tkinter import *
from traverse.ui.dashboard.admin_dash import Admin_dash
from traverse.db.tables.User import User
from tkinter import messagebox
# from PIL import Image, ImageTk
class Login:
    def __init__(self, session):
        self.login_screen = Tk()
        self.session = session
        self.login_screen.title("Login")
        self.login_screen.geometry("400x400")
        self.login_screen.config(bg="#f7e328")
        # bg_image = Image.open("../images/background.png")
        # bg_image_resize = bg_image.resize((400,400))
        # bg_image_test = ImageTk.PhotoImage(bg_image_resize)
        # Label(self.login_screen, image= bg_image_test).place(x=0, y=0, relheight=1, relwidth=1)
        Label(self.login_screen, text="Username", bg="#f7e328").place(x=80,y=100)
        self.username = Entry(self.login_screen)
        self.username.place(x=180,y=100)
        Label(self.login_screen, text="Password", bg="#f7e328").place(x=80,y=140)
        self.password = Entry(self.login_screen, show="*")
        self.password.place(x=180,y=140)
        Button(self.login_screen, text="Back", width=10,height=2, bg="#f7e328", activebackground="#f7e328", fg="black", activeforeground="black", command= self.back, font='Verdana 10 bold').place(x=70,y=200)
        Button(self.login_screen, text="Login", width=10,height=2, bg="#f7e328", activebackground="#f7e328", fg="black", activeforeground="black", command=self.login_user, font='Verdana 10 bold').place(x=260,y=200)
        self.login_screen.mainloop()
        
    def login_user(self):
        result = self.session.query(User).filter_by(username=self.username.get(),
                                                    password=self.password.get()).one_or_none()
        if result is not None:
            self.login_screen.destroy()
            Admin_dash(self.session)
        else:
            messagebox.showwarning("Warning", "No such user!")
        
    def back(self):
        self.login_screen.destroy()
        # exec(open('/home/akshay/Knight-C/code/traverse/ui/app.py').read())

            
        
