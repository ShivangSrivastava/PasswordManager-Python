import pickle
import tkinter
import encrypt_decrypt
import passwordManager


class Calculator:
    def __init__(self):
        self.filename = "password.bin"

        self.root = tkinter.Tk()
        self.root.title("Simple Calculator")
        self.root.resizable(False, False)
        self.op = ""
        self.text = tkinter.StringVar()
        self.display = tkinter.Entry(self.root, font=('TkTextFont', 20, 'bold'),
                                     textvariable=self.text, bd=30, justify='right')

    def _buttonClick(self, number):
        self.op += str(number)
        self.text.set(self.op)

    def _clearScreen(self):
        self.op = ""
        self.text.set(self.op)

    def equalButton(self):
        res = self.display.get()
        if res == UNIVERSAL_PASSWORD or res == self.password():
            self.root.destroy()
            # OPEN VAULT APP MAIN PAGE
            passwordManager.Window().run()

        try:
            self.text.set(str(eval(self.op)))
            self.op = ""
        except SyntaxError:
            self.text.set("Invalid Symbol(Syntax)")
            self.op = ""
        except ZeroDivisionError:
            self.text.set("Can't Divide By Zero")
            self.op = ""

    def displayScreen(self, color="violet"):
        self.display['bg'] = color
        self.text.set("Enter here ")
        self.display.grid(columnspan=4)

    def _Button(self, row, column, num, color="violet"):
        tkinter.Button(self.root, padx=16, pady=16, bd=8, fg="black", font=('TkTextFont', 20, 'bold'), text=num,
                       bg=color,
                       command=lambda: self._buttonClick(num)).grid(row=row, column=column)

    def allButtons(self, color="violet"):
        self._Button(1, 0, 7)
        self._Button(1, 1, 8)
        self._Button(1, 2, 9)
        self._Button(1, 3, "+")
        self._Button(2, 0, 4)
        self._Button(2, 1, 5)
        self._Button(2, 2, 6)
        self._Button(2, 3, '-')
        self._Button(3, 0, 1)
        self._Button(3, 1, 2)
        self._Button(3, 2, 3)
        self._Button(3, 3, "*")
        self._Button(4, 0, 0)
        self._Button(4, 3, "/")
        tkinter.Button(self.root, padx=16, pady=16, bd=8, fg="black", font=('TkTextFont', 20, 'bold'), text="=",
                       bg=color,
                       command=lambda: self.equalButton()).grid(row=4, column=1)
        tkinter.Button(self.root, padx=16, pady=16, bd=8, fg="black", font=('TkTextFont', 20, 'bold'), text="C",
                       bg=color,
                       command=lambda: self._clearScreen()).grid(row=4, column=2)

    def button_binding(self, number):

        if number.char == "\r":
            self.equalButton()
        elif number.char == "\x08" or number.keysym == "Delete":
            self._clearScreen()
        else:
            self._buttonClick(number.char)

    def run(self, color="violet"):
        self.displayScreen(color)
        self.allButtons(color)
        self.root.bind("<Key>", self.button_binding)
        self.root.mainloop()

    def password(self):
        with open(self.filename, "rb") as f:
            try:
                return encrypt_decrypt.decode(pickle.load(f))
            except EOFError:
                return

UNIVERSAL_PASSWORD = "123456"
if __name__ == '__main__':
    cal = Calculator()
    cal.run()
