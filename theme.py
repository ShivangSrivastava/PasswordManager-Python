import tkinter.font

Light_Theme = {
    "bg": "#f2edf3",
    "main_text_color": "#c67bff",
    "normal_text_color": "#ffffff",
    "button1color": "#ffa996",
    "button2color": "#5bacef",
    "button3color": "#54d4c5"
}


Dark_Theme = {
    "bg": "#1c1e2f",
    "main_text_color": "#ffffff",
    "normal_text_color": "#dddddd",
    "button1color": "#6301ed",
    "button2color": "#29c0b1",
    "button3color": "#2c4fed"
}


class Theme:
    def __init__(self, mode):
        self.mode = mode
        if self.mode.lower() == "light":
            self.theme = Light_Theme
        else:
            self.theme = Dark_Theme

    def bg(self): return self.theme.get("bg")

    def main_text_color(self): return self.theme.get("main_text_color")

    def normal_text_color(self): return self.theme.get("normal_text_color")

    def button1color(self): return self.theme.get("button1color")

    def button2color(self): return self.theme.get("button2color")

    def button3color(self): return self.theme.get("button3color")
