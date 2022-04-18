from tkinter import *
from tkinter import ttk

class Package:
    def __init__(self):
        self.package_screen = Tk()
        self.package_screen.title("package Dashboard")
        self.package_screen.geometry("570x600")
        self.container_tree = Frame(self.package_screen, width=100, height=300)
        self.container_tree.grid(row=0, column=0)
        self.container_tree.pack_propagate(0)
        columns = ('package_name', 'start', 'end', 'type', 'cost')
        self.package_tree = ttk.Treeview(self.container_tree, columns=columns, show='headings')
        self.package_tree.heading('package_name', text='package_name')
        self.package_tree.heading('start', text='start')
        self.package_tree.heading('end', text='end')
        self.package_tree.heading('type', text='type')
        self.package_tree.heading('cost', text='cost')
    
        self.package_tree.column("package_name", width=250)
        self.package_tree.column("start", width=80)
        self.package_tree.column("end", width=80) 
        self.package_tree.column("type", width=80)
        self.package_tree.column("cost", width=80)

        contacts = []
        for n in range(1, 30):
            contacts.append(('super delux tour to srilanka', '13-02-1994','14-02-2022', 'cheap', '0.5'))
        for contact in contacts:
            self.package_tree.insert('', END, values=contact)
        self.package_tree.grid(row=0, column=0, sticky='nsew')
        h = Scrollbar(self.package_screen, orient = 'horizontal')
        h.configure(command=self.package_tree.xview)
        h.grid(row=1, column=0, sticky='we', columnspan=3)
        v = Scrollbar(self.package_screen)
        v.grid(row=0, column=1, sticky='ns')
        self.package_tree.configure(yscrollcommand=v.set, xscrollcommand=h.set)
        self.package_screen.mainloop()