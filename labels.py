from tkinter import Label
from tkinter import font

class MyLabel(Label):

    def __init__(self, root, textvariable, fg="grey", bg="black", highlightthickness=2, width=18, borderwidth=2, relief="groove"):
        font_style = ("Gill Sans MT", 12)
        self.fg = fg
        self.bg = bg
        self.root = root
        self.textvariable = textvariable
        self.font = font
        # self.highlightthickness = highlightthickness
        self.width = width
        self.borderwidth = borderwidth
        self.relief = relief
        super().__init__()
        self["textvariable"] = self.textvariable
        self["font"] = font_style
        # self["highlightthickness"] = 2
        self["width"] = 25
        self["borderwidth"] = 2
        self["relief"] = "groove"
        self["bg"] = "black"
        self["fg"] = "white"


