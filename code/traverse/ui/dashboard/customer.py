from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from turtle import st

from traverse.db.tables.User import User
from traverse.db.tables.Customer import Customer as cus

class Customer:
    def __init__(self, session):
        self.customer_screen = Tk()
        self.session = session
        self.customer_screen.title("Customer List")
        self.customer_screen.geometry("915x600")
        self.top_frame = Frame(self.customer_screen, background="black", height=25, width=915)
        self.top_frame.pack_propagate(0)
        self.top_frame.grid(row=0, column=0)
        self.top_label = Label(self.top_frame, text="Customers",background="black", fg="#f7e328", font='Verdana 10 bold')
        self.top_label.pack()
        # self.button_frame = Frame(self.customer_screen, height=25, width=915)
        # self.button_frame.pack_propagate(0)
        # self.button_frame.grid(row=1, column=2)
        # self.add = Label(self.button_frame, text="Add", height=10, width=40, background="yellow")
        # self.add.pack()
        self.container_tree = Frame(self.customer_screen)
        self.container_tree.grid(row=2, column=0)
        self.container_tree.pack_propagate(0)
        columns = ('name', 'dob', 'phno', 'address', 'email', 'username', 'password', 'age')
        self.customer_tree = ttk.Treeview(self.container_tree, columns=columns, show='headings')
        self.style = ttk.Style()
        self.customer_tree.heading('name', text='name')
        self.customer_tree.heading('dob', text='dob')
        self.customer_tree.heading('phno', text='phno')
        self.customer_tree.heading('address', text='address')
        self.customer_tree.heading('email', text='email')
        self.customer_tree.heading('username', text='username')
        self.customer_tree.heading('password', text='password')
        self.customer_tree.heading('age', text='age')
        self.customer_tree.column("name", width=150)
        self.customer_tree.column("dob", width=80)
        self.customer_tree.column("phno", width=80) 
        self.customer_tree.column("address", width=200)
        self.customer_tree.column("email", width=150)
        self.customer_tree.column("username", width=100)
        self.customer_tree.column("password", width=120) 
        self.customer_tree.column("age", width=30)
        self.customer_tree.bind("<Double-1>", self.edit_item)
        self.customer_tree.bind("<Button-1>", self.delete_item)
        contacts = []
        result = session.query(cus).join(User).all()
        for row in result:
            u = row.user
            contacts.append((u.name, u.dob, u.phno, u.address, u.email, u.username, u.password, u.age))
        for contact in contacts:
            self.customer_tree.insert('', END, values=contact)
        self.customer_tree.grid(row=0, column=0, sticky='nsew')
        # h = Scrollbar(self.customer_screen, orient = 'horizontal')
        # h.configure(command=self.customer_tree.xview)
        # h.grid(row=1, column=0, sticky='we', columnspan=3)
        # v = Scrollbar(self.customer_screen)
        # v.grid(row=0, column=1, sticky='ns')
        # self.customer_tree.configure(yscrollcommand=v.set, xscrollcommand=h.set)

        self.button_frame = Frame(self.customer_screen, height=30, width=915)
        self.button_frame.pack_propagate(0)
        self.button_frame.grid(row=3, column=0)
        self.add = Button(self.button_frame, text="Add", height=50, width=8, background="#f7e328", activebackground="#f7e328", font='Verdana 10 bold', command=self.add_item)
        self.add.pack(side=LEFT)
        self.delete = Button(self.button_frame, text="Delete", height=50, width=8, background="#f7e328", activebackground="#f7e328", font='Verdana 10 bold', command=self.delete_item)
        self.delete.pack(side=RIGHT)
        self.customer_screen.mainloop()
    
    def delete_item(self, event):
        selected_item = self.customer_tree.focus()
        # res = messagebox.askquestion("Delete item", "are you sure you wanna delete this item?")
        x = self.customer_tree(selected_item, 'values')
        print("herere",x )
        # if res=='yes':
        #     self.clear_all()

            
    def edit_item(self, event):
        self.edit_screen = Tk()
        self.edit_screen.title("Customer List")
        self.edit_screen.geometry("500x500")
        self.edit_screen.config(bg="#f7e328")

        Label(self.edit_screen, text="Please update the details below", bg="#f7e328", width=100, height=2, font='Verdana 11 bold').pack()
        Label(self.edit_screen, text="", bg="#f7e328").pack()

        Label(self.edit_screen, text="Full name", bg="#f7e328").place(x=120,y=40) 
        self.name = Entry(self.edit_screen)
        self.name.place(x=220,y=40)
        
        Label(self.edit_screen, text="Date of Birth", bg="#f7e328").place(x=120,y=80)
        self.dob = Entry(self.edit_screen)
        self.dob.place(x=220,y=80)
        
        Label(self.edit_screen, text="Phone No.", bg="#f7e328").place(x=120,y=120)
        self.phno = Entry(self.edit_screen)
        self.phno.place(x=220,y=120)
        
        Label(self.edit_screen, text="address", bg="#f7e328").place(x=120,y=160)
        self.address = Entry(self.edit_screen)
        self.address.place(x=220,y=160)
        
        Label(self.edit_screen, text="Email", bg="#f7e328").place(x=120,y=200)
        self.email = Entry(self.edit_screen)
        self.email.place(x=220,y=200)
        
        Label(self.edit_screen, text="Username", bg="#f7e328").place(x=120,y=240)
        self.username = Entry(self.edit_screen)
        self.username.place(x=220,y=240)
        
        Label(self.edit_screen, text="Password", bg="#f7e328").place(x=120,y=280)
        self.password = Entry(self.edit_screen, show="*")
        self.password.place(x=220,y=280)
        
        Label(self.edit_screen, text="Age", bg="#f7e328").place(x=120,y=320)
        self.age = Entry(self.edit_screen)
        self.age.place(x=220,y=320)

        Button(self.edit_screen, text="Back", width=10,height=2, bg="#f7e328", activebackground="#f7e328", command= self.edit_screen.destroy, font='Verdana 10 bold').place(x=70,y=350)
        Button(self.edit_screen, text="Save", width=10,height=2, bg="#f7e328", activebackground="#f7e328", command= self.update_user, font='Verdana 10 bold').place(x=350,y=350)
        self.edit_screen.mainloop()

    def update_user(self):
        selected_item = self.customer_tree.selection()[0]
        self.customer_tree.item(selected_item, values=(self.name.get(), self.dob.get(), self.phno.get(), self.address.get(), self.email.get(), self.username.get(), self.password.get(), self.age.get()))
        self.edit_screen.destroy()

    def add_item(self):
        self.add_screen = Tk()
        self.add_screen.title("Customer List")
        self.add_screen.geometry("500x500")
        self.add_screen.config(bg="#f7e328")

        Label(self.add_screen, text="Please update the details below", bg="#f7e328", width=100, height=2, font='Verdana 11 bold').pack()
        Label(self.add_screen, text="", bg="#f7e328").pack()

        Label(self.add_screen, text="Full name", bg="#f7e328").place(x=120,y=40) 
        self.name = Entry(self.add_screen)
        self.name.place(x=220,y=40)
        
        Label(self.add_screen, text="Date of Birth", bg="#f7e328").place(x=120,y=80)
        self.dob = Entry(self.add_screen)
        self.dob.place(x=220,y=80)
        
        Label(self.add_screen, text="Phone No.", bg="#f7e328").place(x=120,y=120)
        self.phno = Entry(self.add_screen)
        self.phno.place(x=220,y=120)
        
        Label(self.add_screen, text="address", bg="#f7e328").place(x=120,y=160)
        self.address = Entry(self.add_screen)
        self.address.place(x=220,y=160)
        
        Label(self.add_screen, text="Email", bg="#f7e328").place(x=120,y=200)
        self.email = Entry(self.add_screen)
        self.email.place(x=220,y=200)
        
        Label(self.add_screen, text="Username", bg="#f7e328").place(x=120,y=240)
        self.username = Entry(self.add_screen)
        self.username.place(x=220,y=240)
        
        Label(self.add_screen, text="Password", bg="#f7e328").place(x=120,y=280)
        self.password = Entry(self.add_screen, show="*")
        self.password.place(x=220,y=280)
        
        Label(self.add_screen, text="Age", bg="#f7e328").place(x=120,y=320)
        self.age = Entry(self.add_screen)
        self.age.place(x=220,y=320)

        Button(self.add_screen, text="Back", width=10,height=2, bg="#f7e328", activebackground="#f7e328", command= self.add_screen.destroy, font='Verdana 10 bold').place(x=70,y=350)
        Button(self.add_screen, text="Add", width=10,height=2, bg="#f7e328", activebackground="#f7e328", command= self.add_user, font='Verdana 10 bold').place(x=350,y=350)
        self.add_screen.mainloop()

    def add_user(self):
        self.customer_tree.insert('', END,values=(self.name.get(), self.dob.get(), self.phno.get(), self.address.get(), self.email.get(), self.username.get(), self.password.get(), self.age.get()))
        self.add_screen.destroy()

    def clear_all(self):
       for item in self.customer_tree.get_children():
            self.customer_tree.delete(item)

