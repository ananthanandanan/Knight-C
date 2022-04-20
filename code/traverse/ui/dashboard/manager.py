from tkinter import *
from tkinter import ttk
from traverse.db.tables.Employee import Employee as emp
class Manager:
    def __init__(self, session):
        self.manager_screen = Tk()
        self.session = session
        self.manager_screen.title("manager Dashboard")
        self.manager_screen.geometry("1090x600")
        self.container_tree = Frame(self.manager_screen, width=100, height=100)
        self.container_tree.grid(row=0, column=0)
        self.container_tree.pack_propagate(0)
        columns = ('name', 'dob', 'phno', 'address', 'email', 'username', 'password', 'age', 'designation', 'doj')
        self.manager_tree = ttk.Treeview(self.container_tree, columns=columns, show='headings')
        self.manager_tree.heading('name', text='name')
        self.manager_tree.heading('dob', text='dob')
        self.manager_tree.heading('phno', text='phno')
        self.manager_tree.heading('address', text='address')
        self.manager_tree.heading('email', text='email')
        self.manager_tree.heading('username', text='username')
        self.manager_tree.heading('password', text='password')
        self.manager_tree.heading('age', text='age')
        self.manager_tree.heading('designation', text='designation')
        self.manager_tree.heading('doj', text='doj')
        self.manager_tree.column("name", width=150)
        self.manager_tree.column("dob", width=80)
        self.manager_tree.column("phno", width=80) 
        self.manager_tree.column("address", width=200)
        self.manager_tree.column("email", width=150)
        self.manager_tree.column("username", width=100)
        self.manager_tree.column("password", width=120) 
        self.manager_tree.column("age", width=30)
        self.manager_tree.column("designation", width=100) 
        self.manager_tree.column("doj", width=80)
        contacts = []
        result = session.query(emp).filter(emp.designation=="manager").all()
        for row in result:
            u = row.user
            contacts.append((u.name, u.dob, u.phno, u.address, u.email, u.username, 
                            u.password, u.age, row.designation, row.doj))
        for contact in contacts:
            self.manager_tree.insert('', END, values=contact)
        self.manager_tree.grid(row=0, column=0, sticky='nsew')
        h = Scrollbar(self.manager_screen, orient = 'horizontal')
        h.configure(command=self.manager_tree.xview)
        h.grid(row=1, column=0, sticky='we', columnspan=3)
        v = Scrollbar(self.manager_screen)
        v.grid(row=0, column=1, sticky='ns')
        self.manager_tree.configure(yscrollcommand=v.set, xscrollcommand=h.set)
        self.manager_screen.mainloop()