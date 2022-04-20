from tkinter import *
from tkinter import ttk
from traverse.db.tables.Employee import Employee as emp
class Agent:
    def __init__(self, session):
        self.agent_screen = Tk()
        self.session = session
        self.agent_screen.title("agent Dashboard")
        self.agent_screen.geometry("1090x600")
        self.container_tree = Frame(self.agent_screen, width=100, height=300)
        self.container_tree.grid(row=0, column=0)
        self.container_tree.pack_propagate(0)
        columns = ('name', 'dob', 'phno', 'address', 'email', 'username', 'password', 'age', 'designation', 'doj')
        self.agent_tree = ttk.Treeview(self.container_tree, columns=columns, show='headings')
        self.agent_tree.heading('name', text='name')
        self.agent_tree.heading('dob', text='dob')
        self.agent_tree.heading('phno', text='phno')
        self.agent_tree.heading('address', text='address')
        self.agent_tree.heading('email', text='email')
        self.agent_tree.heading('username', text='username')
        self.agent_tree.heading('password', text='password')
        self.agent_tree.heading('age', text='age')
        self.agent_tree.heading('designation', text='designation')
        self.agent_tree.heading('doj', text='doj')
        self.agent_tree.column("name", width=150)
        self.agent_tree.column("dob", width=80)
        self.agent_tree.column("phno", width=80) 
        self.agent_tree.column("address", width=200)
        self.agent_tree.column("email", width=150)
        self.agent_tree.column("username", width=100)
        self.agent_tree.column("password", width=120) 
        self.agent_tree.column("age", width=30)
        self.agent_tree.column("designation", width=100) 
        self.agent_tree.column("doj", width=80)
        contacts = []
        result = session.query(emp).filter(emp.designation=="agent").all()
        for row in result:
            u = row.user
            contacts.append((u.name, u.dob, u.phno, u.address, u.email, u.username, 
                            u.password, u.age, row.designation, row.doj))
        for contact in contacts:
            self.agent_tree.insert('', END, values=contact)
        self.agent_tree.grid(row=0, column=0, sticky='nsew')
        h = Scrollbar(self.agent_screen, orient = 'horizontal')
        h.configure(command=self.agent_tree.xview)
        h.grid(row=1, column=0, sticky='we', columnspan=3)
        v = Scrollbar(self.agent_screen)
        v.grid(row=0, column=1, sticky='ns')
        self.agent_tree.configure(yscrollcommand=v.set, xscrollcommand=h.set)
        self.agent_screen.mainloop()