from tkinter import *
# from PIL import Image, ImageTk
class Login:
    def __init__(self, session):
        self.login_screen = Tk()
        self.session = session
        self.login_screen.title("Login")
        self.login_screen.geometry("400x400")
        self.login_screen.config(bg="pink")
        # bg_image = Image.open("../images/background.png")
        # bg_image_resize = bg_image.resize((400,400))
        # bg_image_test = ImageTk.PhotoImage(bg_image_resize)
        # Label(self.login_screen, image= bg_image_test).place(x=0, y=0, relheight=1, relwidth=1)
        Label(self.login_screen, text="Username", bg="pink").place(x=80,y=100)
        self.username = Entry(self.login_screen)
        self.username.place(x=180,y=100)
        Label(self.login_screen, text="Password", bg="pink").place(x=80,y=140)
        self.password = Entry(self.login_screen, show="*")
        self.password.place(x=180,y=140)
        Button(self.login_screen, text="Back", width=10,height=2, bg="#fa7a1e", fg="white", activebackground="#f28333", activeforeground="white", command= self.login_screen.destroy).place(x=70,y=200)
        Button(self.login_screen, text="Login", width=10,height=2, bg="#fa7a1e", fg="white", activebackground="#f28333", activeforeground="white").place(x=260,y=200)
        self.login_screen.mainloop()
