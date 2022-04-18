from tkinter import *
from turtle import back, color
from .customer import Customer
from .manager import Manager
from .agent import Agent
from .package import Package
from PIL import ImageTk, Image

class Admin_dash:
    def __init__(self, session):
        self.admin_screen = Tk()
        self.session = session
        self.admin_screen.title("Admin Dashboard")
        self.admin_screen.geometry("800x600")
        top_label = Label(text="Dashboard", background="black", height=3, width=125, fg="#f7e328", font='Verdana 10 bold')
        top_label.place(x=0, y=0)

        self.admin_screen.columnconfigure(1, weight=1, minsize=100)
        self.admin_screen.rowconfigure(1, weight=1, minsize=50)
        frame = Frame( master=self.admin_screen, borderwidth=4,background="#c95353",height=200,width=200)
        frame.bind('<Button-1>', self.customer_button)
        frame.grid(row=1, column=1, padx=5, pady=5)
        frame.pack_propagate(0)
        img = Image.open("../../images/Customer.png")
        customer_image = img.resize((200,200))
        customer_image_test = ImageTk.PhotoImage(customer_image)
        label = Label(frame, image = customer_image_test)
        label.bind('<Button-1>', self.customer_button)
        label.pack()

        self.admin_screen.columnconfigure(1, weight=1, minsize=100)
        self.admin_screen.rowconfigure(1, weight=1, minsize=50)
        frame = Frame( master=self.admin_screen, borderwidth=4,background="#c95353",height=200,width=200)
        frame.bind('<Button-1>', self.manager_button)
        frame.grid(row=1, column=2, padx=5, pady=5)
        frame.pack_propagate(0)
        img = Image.open("../../images/manager.png")
        manager_image = img.resize((200,200))
        manager_image_test = ImageTk.PhotoImage(manager_image)
        label = Label(frame, image = manager_image_test)
        label.bind('<Button-1>', self.manager_button)
        label.pack()

        self.admin_screen.columnconfigure(2, weight=1, minsize=100)
        self.admin_screen.rowconfigure(2, weight=1, minsize=50)
        frame = Frame( master=self.admin_screen, borderwidth=4,background="#c95353",height=200,width=200)
        frame.bind('<Button-1>', self.agent_button)
        frame.grid(row=2, column=1, padx=5, pady=5)
        frame.pack_propagate(0)
        img = Image.open("../../images/agent.png")
        agent_image = img.resize((200,200))
        agent_image_test = ImageTk.PhotoImage(agent_image)
        label = Label(frame, image = agent_image_test)
        label.bind('<Button-1>', self.agent_button)
        label.pack()

        self.admin_screen.columnconfigure(2, weight=1, minsize=100)
        self.admin_screen.rowconfigure(2, weight=1, minsize=50)
        frame = Frame( master=self.admin_screen, borderwidth=4,background="#c95353",height=200,width=200)
        frame.bind('<Button-1>', self.package_button)
        frame.grid(row=2, column=2, padx=5, pady=5)
        frame.pack_propagate(0)
        img = Image.open("../../images/package.png")
        package_image = img.resize((200,200))
        package_image_test = ImageTk.PhotoImage(package_image)
        label = Label(frame, image = package_image_test)
        label.bind('<Button-1>', self.package_button)
        label.pack()

        self.admin_screen.mainloop()

    def customer_button(self,event):
        # self.admin_screen.destroy()
        Customer()
    
    def manager_button(self,event):
        # self.admin_screen.destroy()
        Manager()

    def agent_button(self,event):
        # self.admin_screen.destroy()
        Agent()

    def package_button(self,event):
        # self.admin_screen.destroy()
        Package()

    def package_details(self,package_name):
        self.package_screen = Tk()
        self.package_screen.title(package_name)
        self.package_screen.geometry("400x400")    
        Button(self.package_screen,text="Buy", command=self.payment_details).pack()
        self.package_screen.mainloop()

    def payment_details(self):
        self.payment_screen = Tk()
        self.payment_screen.title("Payment portal")
        self.payment_screen.geometry("300x300")
        self.payment_screen.mainloop()


# admin = Admin_dash()