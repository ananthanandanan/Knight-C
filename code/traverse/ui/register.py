from calendar import *
from tkinter import *
from unicodedata import name
# from app import dbms
from ..db.tables import User
# from PIL import Image, ImageTk
class Register:
    def __init__(self, session):
        self.register_screen = Tk()
        self.session = session
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
        
        self.name = Entry(self.register_screen)
        self.name.place(x=220,y=40)
        
        Label(self.register_screen, text="Date of Birth", bg="pink").place(x=120,y=80)
        self.dob = Entry(self.register_screen)
        self.dob.place(x=220,y=80)
        
        Button(self.register_screen, text="cal", width=1,height=1, bg="#fa7a1e", fg="white", activebackground="#f28333", activeforeground="white").place(x=370,y=76)
        Label(self.register_screen, text="Phone No.", bg="pink").place(x=120,y=120)
        self.phno = Entry(self.register_screen)
        self.phno.place(x=220,y=120)
        
        Label(self.register_screen, text="address", bg="pink").place(x=120,y=160)
        self.address = Entry(self.register_screen)
        self.address.place(x=220,y=160)
        
        Label(self.register_screen, text="Email", bg="pink").place(x=120,y=200)
        self.email = Entry(self.register_screen)
        self.email.place(x=220,y=200)
        
        Label(self.register_screen, text="Username", bg="pink").place(x=120,y=240)
        self.username = Entry(self.register_screen)
        self.username.place(x=220,y=240)
        
        Label(self.register_screen, text="Password", bg="pink").place(x=120,y=280)
        self.password = Entry(self.register_screen, show="*")
        self.password.place(x=220,y=280)
        
        Label(self.register_screen, text="Age", bg="pink").place(x=120,y=320)
        self.age = Entry(self.register_screen)
        self.age.place(x=220,y=320)

        Label(self.register_screen, text="Role", bg="pink").place(x=120,y=350)
        self.role = StringVar(self.register_screen)
        customer = Radiobutton(self.register_screen,text="Customer", variable=self.role, value="customer", background = "pink")
        customer.place(x=220,y=350)
        manager = Radiobutton(self.register_screen,text="Manager", variable=self.role, value="manager", background = "pink")
        manager.place(x=300,y=350)
        agent = Radiobutton(self.register_screen,text="Agent", variable=self.role, value="agent", background = "pink")
        agent.place(x=370,y=350)

        Button(self.register_screen, text="Back", width=10,height=2, bg="#fa7a1e", fg="white", activebackground="#f28333", activeforeground="white", command= self.register_screen.destroy).place(x=70,y=390)
        Button(self.register_screen, text="Register", width=10,height=2, bg="#fa7a1e", fg="white", activebackground="#f28333", activeforeground="white", command= self.register_user).place(x=350,y=390)
        self.register_screen.mainloop()

    def register_user(self):
        u = User.User(name=self.name.get(), dob=self.dob.get(), phno=self.phno.get(), address=self.address.get(),
                email=self.email.get(), username=self.username.get(), password=self.password.get(),
                age=self.age.get())
        self.session.add(u)
        self.session.commit()