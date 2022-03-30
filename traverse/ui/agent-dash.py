from tkinter import *
from tkinter import ttk,messagebox

def login():
    messagebox.showinfo(title="login",message="login here!")

dashboard = Tk()
dashboard.title("Agent-board")
dashboard.geometry("700x500")

menubar = Menu(dashboard,tearoff=0)
menubar.add_command(label="home")
menubar.add_command(label="login",command=login)
menubar.add_command(label="signup")
menubar.add_command(label="exit",command=dashboard.quit)
dashboard.config(menu = menubar)
ttk.Label(dashboard, text="This is agent's dashboard!").grid(column=0,row=0)
dashboard.mainloop()