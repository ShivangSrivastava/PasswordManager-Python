import tkinter
from tkinter import ttk
import tkinter.messagebox
import tkinter.font
import encrypt_decrypt
import firsttimepasswordsaver
import pickle
import theme
from datetime import datetime
import os
import webbrowser


FONT = "Bradley Hand ITC"


class Record:
    def __init__(self, master: tkinter.Tk):
        self.master=master
        self.canvas = tkinter.Canvas(master)
        self.tree = ttk.Treeview(self.canvas, columns=(
            "0", "1", "2", "3"), show="headings")

        self.tree.heading("0", text="Site")
        self.tree.heading("1", text="Password")
        self.tree.heading("2", text="Comment")
        self.tree.heading("3", text="Creation Date")

    def tree_setup(self):
        self.canvas.place(x=0, y=120, relwidth=1, relheight=1)
        self.tree.place(x=0, y=0, relwidth=1, relheight=1)
        self.tree.bind("<Double-1>", self.copy_text)
        self.tree.bind("<Key>", self.keypress)
    
    def keypress(self, event):
        try:
            item = self.tree.selection()[0]
        except IndexError:
            pass
        value=self.tree.item(item)['values']
        all_record = []
        with open("userdata.bin","rb") as f:
            while 1:
                try:
                    bin_data = pickle.load(f)
                    decoded_ = list(eval(encrypt_decrypt.decode(bin_data)))
                    if decoded_ != value:
                        all_record.append(decoded_)
                except EOFError:
                    break
        if event.keysym == "Delete":
            yn = tkinter.messagebox.askyesno("Delete Password", "Are you sure want to\ndelete seleted record?")
            if yn:
                with open("userdata.bin", "wb") as file:
                    for rec in all_record:
                        encoded_data = encrypt_decrypt.encode(str(rec))
                        pickle.dump(encoded_data, file)
                    file.close()
                a = tkinter.messagebox.showinfo(
                    "Delete", "Record Deleted...")
                if a:
                    self.canvas.destroy()
                    self.master.destroy()
                    Window().run()
        

    def insert(self):
        with open("userdata.bin", "rb") as f:
            while True:
                try:
                    encrypted_data = pickle.load(f)
                except EOFError:
                    break
                value = eval(encrypt_decrypt.decode(encrypted_data))
                self.tree.insert('', tkinter.END, value=value)
            f.close()

    def copy_text(self, event):
        try:
            item = self.tree.selection()[0]
            text = self.tree.item(item, "value")[1]
            command = 'echo ' + text.strip() + '| clip'
            os.system(command)
            tkinter.messagebox.showinfo(
                "Copied", "Record copied to clipboard...")
        except IndexError:
            pass
        

    def run(self):
        self.insert()
        self.tree_setup()

class AddNewPassword:       
    def __init__(self, master:tkinter.Tk):
        self.master = master
        self.root = tkinter.Toplevel(master)
        self.root.title("Add New Password")
        tkinter.Label(self.root, text="Please enter password details").pack()

        tkinter.Label(self.root, text="").pack()
        tkinter.Label(self.root, text="Site Name").pack()
        self.site_entry = tkinter.Entry(
            self.root, textvariable="site")
        self.site_entry.pack()

        tkinter.Label(self.root, text="").pack()
        tkinter.Label(self.root, text="Password").pack()
        self.password_entry = tkinter.Entry(
            self.root, textvariable="password", show='*')
        self.password_entry.pack()

        tkinter.Label(self.root, text="").pack()
        tkinter.Label(self.root, text="Comment").pack()
        self.comment_entry = tkinter.Entry(
            self.root, textvariable="comment")
        self.comment_entry.pack()

        tkinter.Label(self.root, text="").pack()
        tkinter.Button(self.root, text="Save", width=10, height=1, command=lambda:self.save()).pack()
        self.root.mainloop()

    def save(self):
        site = str(self.site_entry.get())
        password = str(self.password_entry.get())
        comment = str(self.comment_entry.get())
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        data = [site, password, comment, dt_string]
        encoded_data = encrypt_decrypt.encode(str(data))
        with open("userdata.bin", "ab") as file:
            pickle.dump(encoded_data, file)
            file.close()
        a=tkinter.messagebox.showinfo("Saved", "Record saved...\nDouble Click to copy password")
        if a:
            self.root.destroy()
            self.master.destroy()
            Window().run()
            
class Font:
    def __init__(self):
        self.root = ""
        tkinter.font.families(self.root)


class Settings:
    pass

class ChangeFTP:
    def __init__(self, window):
        open("password.bin", "w").close()
        window.destroy()
        import main        

class Window:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("900x600+50+50")
        self.root.resizable(False, False)

        self.change_theme_button = tkinter.Button(self.root)
        self.setting_button = tkinter.Button(self.root)
        self.password_manager_label = tkinter.Label(self.root)
        self.add_new_password_button = tkinter.Button(self.root)

        self.theme_mode = "dark"
        self.theme = theme.Theme(self.theme_mode)

        self.sun_emoji = "\u2600"
        self.moon_emoji = "\u263d"

        self.theme_text = self.moon_emoji

    def coloring(self):
        self.change_theme_button["text"] = self.theme_text

        self.change_theme_button['bg'] = self.theme.button1color()
        self.change_theme_button['fg'] = self.theme.normal_text_color()

        self.setting_button['bg'] = self.theme.button2color()
        self.setting_button['fg'] = self.theme.normal_text_color()

        self.password_manager_label['bg'] = self.theme.bg()
        self.password_manager_label['fg'] = "red"

        self.add_new_password_button['bg'] = self.theme.button3color()
        self.add_new_password_button['fg'] = self.theme.normal_text_color()
        self.add_new_password_button['command'] = lambda:AddNewPassword(self.root)
        

        self.root["bg"] = self.theme.bg()
        
    def add_commands(self):
        self.change_theme_button['command'] = lambda: self.mode()
        self.change_theme_button["font"] = (FONT, 15, "bold")

        self.setting_button['command'] = lambda: Settings()
        self.setting_button['text'] = "Settings"
        self.setting_button['font'] = (FONT, 15, "bold")

        self.password_manager_label['text'] = "Password Manager"
        self.password_manager_label['font'] = (FONT, 50, "bold")

        self.add_new_password_button['text'] = "Add New password"
        self.add_new_password_button['font'] = (FONT, 15, "bold")

    def placing(self):
        self.change_theme_button.place(x=850, y=0)
        self.setting_button.place(x=740, y=0)
        self.password_manager_label.place(x=100, y=10)
        self.add_new_password_button.place(x=700, y=60)

    def mode(self):
        if self.theme_mode == "light":
            self.theme_mode = "dark"
            self.theme_text = self.moon_emoji
        else:
            self.theme_mode = "light"
            self.theme_text = self.sun_emoji
        
        self.theme = theme.Theme(self.theme_mode)
        self.coloring()

    def setup(self):
        self.add_commands()
        self.coloring()
        self.placing()
        Record(self.root).run()
        self.root.bind("<Button-1>", self.fun)
        self.root.bind("<F1>", self.help)
        self.root.bind("<F5>", self.refresh)
    @staticmethod
    def fun(event):
        print(event)

    @staticmethod
    def help(event):
        webbrowser.open(
            "https://github.com/ShivangSrivastava/PasswordManager-Python"
            )
    
    def refresh(self, event):
        self.root.destroy()
        self.__init__()
        self.run()
        
    def run(self):
        self.setup()
        self.root.mainloop()

if __name__ == '__main__':
    Window().run()

