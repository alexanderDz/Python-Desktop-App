import tkinter as tk
from tkinter.font import BOLD
import util.generic as itl

class masterPanel:
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Assistant HAB")
        w,h = self.ventana.winfo_screenwidth(), self.ventana.winfo_screenheight()
        self.ventana.geometry("%dx%d+0+0" % (w, h))
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)


        self.ventana.mainloop()