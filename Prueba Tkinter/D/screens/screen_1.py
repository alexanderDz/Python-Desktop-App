import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl
from screens.screen_master import masterPanel

class app:
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Assistant HAB")
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana,800,500)

        ##Frame para fechas importantes

        frame_fechas = tk.Frame(self.ventana, bd=0, width=100, height=100, relief=tk.SOLID, padx=10, pady=10, bg='red')
        frame_fechas.pack(side="top", expand=tk.NO, fill=tk.BOTH)

        ##Frame Botones Principales

        frame_botonesP = tk.Frame(self.ventana, bd=0, width=500, height=100, relief=tk.SOLID, padx=10, pady=10, bg='blue')
        frame_botonesP.pack(side="left", expand=tk.NO, fill=tk.BOTH)
       
        #Frames botones secundarios

        frame_botonesS = tk.Frame(self.ventana, bd=0, width=300, height=100, relief=tk.SOLID, padx=10, pady=10, bg='green')
        frame_botonesS.pack(side='right', expand=tk.NO, fill=tk.BOTH)



        self.ventana.mainloop()