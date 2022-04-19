from tkinter import *
from tkinter.font import BOLD
from .login import Login
from .register import Register
from PIL import Image, ImageTk

from ..db.tables import (User, Employee, Customer, 
                    Admin, Manager, Agent,
                    Payment, Package,
                    Hotel, Ticket)
from ..db.tables.base import Base
from ..db.Database import Database

dbms = Database("sqlite", dbname='travel.sqlite')
engine = dbms.db_engine
Base.metadata.create_all(engine)
session = dbms.session_manager()
class App:
    def __init__(self, session, main_screen):
        
        self.main_screen = main_screen
        self.session = session
        self.main_screen.geometry("800x600")
        self.main_screen.title("Traverse")
        self.main_screen.resizable(False,False)
        bg_image = Image.open("traverse/images/travel_back.png")
        bg_image_resize = bg_image.resize((800,600))
        bg_image_test = ImageTk.PhotoImage(bg_image_resize)
        Label(self.main_screen, image= bg_image_test).place(x=0, y=0, relheight=1, relwidth=1)
        Label(self.main_screen, text="Login or Register", height=3, width=100, font='Verdana 13 bold', bg="#f7e328").pack(pady=20)
        Button(self.main_screen, text="Login", height=2, width=10, command=self.login_button, bg="#f7e328", activebackground="#f7e328", bd=0, font='Verdana 10 bold').place(x=150, y=170)
        Button(self.main_screen, text="Register", height=2, width=10, command=self.register_button, bg="#f7e328", activebackground="#f7e328", bd=0, font='Verdana 10 bold').place(x=150, y=300)
        self.main_screen.mainloop()

    def login_button(self):
        self.main_screen.destroy()
        Login(self.session)
    
    def register_button(self):
        # self.main_screen.destroy()
        Register(self.session)

main_screen = Tk()        
myapp = App(session, main_screen)
main_screen.mainloop()