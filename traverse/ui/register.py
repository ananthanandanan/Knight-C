from calendar import *
from tkinter import *
# from PIL import Image, ImageTk
import sqlite3
class Register:
    def __init__(self):
        self.register_screen = Tk()
        self.register_screen.title("Register")
        self.register_screen.geometry("500x500")
        self.register_screen.config(bg="pink")
        # bg_image = Image.open("../images/background.png")
        # bg_image_resize = bg_image.resize((500,500))
        # bg_image_test = ImageTk.PhotoImage(bg_image_resize)
        # Label(self.register_screen, image= bg_image_test).place(x=0, y=0, relheight=1, relwidth=1)
        Label(self.register_screen, text="Please enter details below", bg="pink").pack()
        Label(self.register_screen, text="", bg="pink").pack()
        Label(self.register_screen, text="Full name", bg="pink").place(x=120,y=40)
        name = Entry(self.register_screen)
        name.place(x=220,y=40)
        Label(self.register_screen, text="Date of Birth", bg="pink").place(x=120,y=80)
        dob = Entry(self.register_screen)
        dob.place(x=220,y=80)
        Button(self.register_screen, text="cal", width=1,height=1, bg="#fa7a1e", fg="white", activebackground="#f28333", activeforeground="white").place(x=370,y=76)
        Label(self.register_screen, text="Phone No.", bg="pink").place(x=120,y=120)
        phno = Entry(self.register_screen)
        phno.place(x=220,y=120)
        Label(self.register_screen, text="address", bg="pink").place(x=120,y=160)
        address = Entry(self.register_screen)
        address.place(x=220,y=160)
        Label(self.register_screen, text="Email", bg="pink").place(x=120,y=200)
        email = Entry(self.register_screen)
        email.place(x=220,y=200)
        Label(self.register_screen, text="Username", bg="pink").place(x=120,y=240)
        username = Entry(self.register_screen)
        username.place(x=220,y=240)
        Label(self.register_screen, text="Password", bg="pink").place(x=120,y=280)
        password = Entry(self.register_screen, show="*")
        password.place(x=220,y=280)
        Label(self.register_screen, text="Age", bg="pink").place(x=120,y=320)
        age = Entry(self.register_screen)
        age.place(x=220,y=320)
        Button(self.register_screen, text="Back", width=10,height=2, bg="#fa7a1e", fg="white", activebackground="#f28333", activeforeground="white", command= self.register_screen.destroy).place(x=70,y=370)
        Button(self.register_screen, text="Register", width=10,height=2, bg="#fa7a1e", fg="white", activebackground="#f28333", activeforeground="white", command= lambda: print(name.get())).place(x=350,y=370)
        self.register_screen.mainloop()

    def register_user(self):
        pass