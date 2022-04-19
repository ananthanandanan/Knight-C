from tkinter import *
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
        self.admin_screen.config(bg="#f7e328")
        top_label = Label(self.admin_screen, text="Dashboard", background="black", height=3, width=125, fg="#f7e328", font='Verdana 10 bold')
        top_label.place(x=0, y=0)

        self.admin_screen.columnconfigure(1, weight=1, minsize=100)
        self.admin_screen.rowconfigure(1, weight=1, minsize=50)
        frame1 = Frame( master=self.admin_screen, relief=RAISED, borderwidth=4,background="#f7e328",height=200,width=200)
        frame1.bind('<Button-1>', self.customer_button)
        frame1.grid(row=1, column=1, padx=5, pady=5)
        frame1.pack_propagate(0)
        img = Image.open("traverse/images/Customer.png")
        customer_image = img.resize((200,200))
        customer_image_test = ImageTk.PhotoImage(customer_image)
        label = Label(frame1, image = customer_image_test)
        label.image = customer_image_test
        label.bind('<Button-1>', self.customer_button)
        label.pack()

        self.admin_screen.columnconfigure(1, weight=1, minsize=100)
        self.admin_screen.rowconfigure(1, weight=1, minsize=50)
        frame2 = Frame( master=self.admin_screen, relief=RAISED, borderwidth=4,background="#f7e328",height=200,width=200)
        frame2.bind('<Button-1>', self.manager_button)
        frame2.grid(row=1, column=2, padx=5, pady=5)
        frame2.pack_propagate(0)
        img = Image.open("traverse/images/manager.png")
        manager_image = img.resize((200,200))
        manager_image_test = ImageTk.PhotoImage(manager_image)
        label = Label(frame2, image = manager_image_test)
        label.image = manager_image_test
        label.bind('<Button-1>', self.manager_button)
        label.pack()

        self.admin_screen.columnconfigure(2, weight=1, minsize=100)
        self.admin_screen.rowconfigure(2, weight=1, minsize=50)
        frame3 = Frame( master=self.admin_screen, relief=RAISED, borderwidth=4,background="#f7e328",height=200,width=200)
        frame3.bind('<Button-1>', self.agent_button)
        frame3.grid(row=2, column=1, padx=5, pady=5)
        frame3.pack_propagate(0)
        img = Image.open("traverse/images/agent.png")
        agent_image = img.resize((200,200))
        agent_image_test = ImageTk.PhotoImage(agent_image)
        label = Label(frame3, image = agent_image_test)
        label.image = agent_image_test
        label.bind('<Button-1>', self.agent_button)
        label.pack()

        self.admin_screen.columnconfigure(2, weight=1, minsize=100)
        self.admin_screen.rowconfigure(2, weight=1, minsize=50)
        frame4 = Frame( master=self.admin_screen, relief=RAISED, borderwidth=4,background="#f7e328",height=200,width=200)
        frame4.bind('<Button-1>', self.package_button)
        frame4.grid(row=2, column=2, padx=5, pady=5)
        frame4.pack_propagate(0)
        img = Image.open("traverse/images/package.png")
        package_image = img.resize((200,200))
        package_image_test = ImageTk.PhotoImage(package_image)
        label = Label(frame4, image = package_image_test)
        label.image = package_image_test
        label.bind('<Button-1>', self.package_button)
        label.pack()
        # self.admin_screen.mainloop()

    def customer_button(self,event):
        # self.admin_screen.destroy()
        Customer(self.session)
    
    def manager_button(self,event):
        # self.admin_screen.destroy()
        Manager(self.session)

    def agent_button(self,event):
        # self.admin_screen.destroy()
        Agent(self.session)

    def package_button(self,event):
        # self.admin_screen.destroy()
        Package(self.session)


# session = 1
# ad = Admin_dash(session)