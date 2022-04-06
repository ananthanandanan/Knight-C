from cgitb import text
from threading import main_thread
from tkinter import *
from tkinter.font import BOLD
from login import Login
from register import Register
from PIL import Image, ImageTk

class App:
    def __init__(self):
        self.main_screen = Tk()
        self.main_screen.geometry("400x300")
        self.main_screen.title("Traverse")
        self.main_screen.resizable(False,False)
        bg_image = Image.open("../images/background.png")
        bg_image_resize = bg_image.resize((400,300))
        bg_image_test = ImageTk.PhotoImage(bg_image_resize)
        Label(self.main_screen, image= bg_image_test).place(x=0, y=0, relheight=1, relwidth=1)
        Label(self.main_screen, text="Login or Register", height=3, width=100, font=("Calibri",13,BOLD), bg="#ffad61").pack(pady=20)
        Button(self.main_screen, text="Login", height=2, width=10, command=self.login_button, bg="#fa7a1e", fg="white", activebackground="#f28333", activeforeground="white", bd=0).place(x=150, y=120)
        Button(self.main_screen, text="Register", height=2, width=10, command=self.register_button, bg="#fa7a1e", fg="white", activebackground="#f28333", activeforeground="white", bd=0).place(x=150, y=180)
        self.main_screen.mainloop()

    def login_button(self):
        # self.main_screen.destroy()
        Login()
    
    def register_button(self):
        # self.main_screen.destroy()
        Register()

myapp = App()