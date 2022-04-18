from tkinter import *

class Customer_dash:
    def __init__(self):
        self.customer_screen = Tk()
        self.customer_screen.title("Customer Dashboard")
        self.customer_screen.geometry("800x600")
        Label(text="Available Packages",bg="pink", width=800, height=3).pack()
        listbox = Listbox(self.customer_screen, width="800")
        listbox.insert(0,Button(text="Package1", width="800", command=lambda: self.package_details("king pack")).pack(),Label(text="Package2").pack(),Button(text="Package3", width="800").pack(anchor=W),Label(text="Package4").pack())
        listbox.pack()
        c = Canvas(self.customer_screen, height=50, width=50, bg="red")
        c.create_rectangle(50,50,50,50,fill="red")
        c.pack()
        self.customer_screen.mainloop()

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

cus = Customer_dash()