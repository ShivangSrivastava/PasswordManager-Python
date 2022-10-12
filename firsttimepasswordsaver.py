import pickle
import encrypt_decrypt
import tkinter
import tkinter.messagebox


class Window:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Password Saver")
        self.root.geometry("300x400+100+100")
        self.pwd = ""
        self.pin = tkinter.StringVar()

    def layout(self):
        tkinter.Label(self.root, text="Enter 6 digit PIN", font=("TkTextFont", 20, "bold"), fg="red")\
            .grid(columnspan=4)
        tkinter.Entry(self.root, textvariable=self.pin, font=("TkTextFont", 20, "bold"), fg="red",
                      justify=tkinter.CENTER).grid(columnspan=4)

        tkinter.Button(self.root, text="1", font=("TkTextFont", 20, "bold"), fg="red",
                       command=lambda: self.password(1)).grid(row=2, column=0, pady=10)
        tkinter.Button(self.root, text="2", font=("TkTextFont", 20, "bold"), fg="red",
                       command=lambda: self.password(2)).grid(row=2, column=1)
        tkinter.Button(self.root, text="3", font=("TkTextFont", 20, "bold"), fg="red",
                       command=lambda: self.password(3)).grid(row=2, column=2)
        tkinter.Button(self.root, text="4", font=("TkTextFont", 20, "bold"), fg="red",
                       command=lambda: self.password(4)).grid(row=3, column=0, pady=10)
        tkinter.Button(self.root, text="5", font=("TkTextFont", 20, "bold"), fg="red",
                       command=lambda: self.password(5)).grid(row=3, column=1)
        tkinter.Button(self.root, text="6", font=("TkTextFont", 20, "bold"), fg="red",
                       command=lambda: self.password(6)).grid(row=3, column=2)
        tkinter.Button(self.root, text="7", font=("TkTextFont", 20, "bold"), fg="red",
                       command=lambda: self.password(7)).grid(row=4, column=0, pady=10)
        tkinter.Button(self.root, text="8", font=("TkTextFont", 20, "bold"), fg="red",
                       command=lambda: self.password(8)).grid(row=4, column=1)
        tkinter.Button(self.root, text="9", font=("TkTextFont", 20, "bold"), fg="red",
                       command=lambda: self.password(9)).grid(row=4, column=2)
        tkinter.Button(self.root, text="0", font=("TkTextFont", 20, "bold"), fg="red",
                       command=lambda: self.password(0)).grid(row=5, column=1)

    def password(self, pin):
        if len(self.pwd) < 6:
            self.pwd += str(pin)
            self.pin.set(self.pwd)
            
        if len(self.pwd) == 6:
            tkinter.messagebox.showinfo("Password Saved", f"Password Saved Successfully\n"
                                                          f"You password is {self.pwd}\n")
            tkinter.messagebox.showinfo("Tips", "Type your pin then \n"
                                                "press '=' in calculator")
            self.savepassword()

    def start(self):
        self.layout()
        self.root.mainloop()

    def savepassword(self):
        pwd = self.pwd
        if SavePassword().write(pwd):
            self.stop()

    def stop(self):
        self.root.quit()
        self.root.destroy()


class SavePassword:

    def __init__(self):
        self.filename = "password.bin"

    def write(self, password):
        if self.is_password_not_there():
            with open(self.filename, "wb") as f:
                encrypted = encrypt_decrypt.encode(password)
                pickle.dump(encrypted, f)
                f.close()
                return True

    def replace_password(self, new_password):
        with open(self.filename, "wb") as f:
            encrypted = encrypt_decrypt.encode(new_password)
            pickle.dump(encrypted, f)
            f.close()
            return True

    def is_password_not_there(self):
        with open(self.filename, "rb") as f:
            if len(f.read()) == 0:
                return True
            return False


if __name__ == '__main__':
    Window().start()
