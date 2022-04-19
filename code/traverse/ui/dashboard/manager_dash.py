from tkinter import *
from .customer import Customer
from .manager import Manager
from .agent import Agent
from .package import Package
from PIL import ImageTk, Image

class Manager_dash:
    def __init__(self, session):
        self.manager_screen = Tk()
        self.session = session
        self.manager_screen.title("Manager Dashboard")
        self.manager_screen.geometry("800x600")
        top_label = Label(self.manager_screen, text="Dashboard", background="black", height=3, width=125, fg="#f7e328", font='Verdana 10 bold')
        top_label.place(x=0, y=0)

        self.manager_screen.columnconfigure(1, weight=1, minsize=100)
        self.manager_screen.rowconfigure(1, weight=1, minsize=50)
        frame1 = Frame( master=self.manager_screen, borderwidth=4,background="#c95353",height=200,width=200)
        frame1.bind('<Button-1>', self.customer_button)
        frame1.grid(row=1, column=1, padx=5, pady=5)
        frame1.pack_propagate(0)
        img = Image.open("/home/akshay/Knight-C/code/traverse/images/Customer.png")
        customer_image = img.resize((200,200))
        customer_image_test = ImageTk.PhotoImage(customer_image)
        label = Label(frame1, image = customer_image_test)
        label.image = customer_image_test
        label.bind('<Button-1>', self.customer_button)
        label.pack()

        self.manager_screen.columnconfigure(1, weight=1, minsize=100)
        self.manager_screen.rowconfigure(1, weight=1, minsize=50)
        frame3 = Frame( master=self.manager_screen, borderwidth=4,background="#c95353",height=200,width=200)
        frame3.bind('<Button-1>', self.agent_button)
        frame3.grid(row=1, column=2, padx=5, pady=5)
        frame3.pack_propagate(0)
        img = Image.open("/home/akshay/Knight-C/code/traverse/images/agent.png")
        agent_image = img.resize((200,200))
        agent_image_test = ImageTk.PhotoImage(agent_image)
        label = Label(frame3, image = agent_image_test)
        label.image = agent_image_test
        label.bind('<Button-1>', self.agent_button)
        label.pack()

        self.manager_screen.columnconfigure(2, weight=1, minsize=100)
        self.manager_screen.rowconfigure(2, weight=1, minsize=50)
        frame4 = Frame( master=self.manager_screen, borderwidth=4,background="#c95353",height=200,width=200)
        frame4.bind('<Button-1>', self.package_button)
        frame4.grid(row=2, column=1, padx=5, pady=5)
        frame4.pack_propagate(0)
        img = Image.open("/home/akshay/Knight-C/code/traverse/images/package.png")
        package_image = img.resize((200,200))
        package_image_test = ImageTk.PhotoImage(package_image)
        label = Label(frame4, image = package_image_test)
        label.image = package_image_test
        label.bind('<Button-1>', self.package_button)
        label.pack()
        self.manager_screen.mainloop()

    def customer_button(self,event):
        # self.manager_screen.destroy()
        Customer()

    def agent_button(self,event):
        # self.manager_screen.destroy()
        Agent()

    def package_button(self,event):
        # self.manager_screen.destroy()
        Package()


session = 1
ad = Manager_dash(session)