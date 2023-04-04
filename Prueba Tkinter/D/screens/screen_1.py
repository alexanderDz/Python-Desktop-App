import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl
from screens.screen_master import masterPanel
from forms.ordenTrabajo import abrir_orden_trabajo
from forms.area import area
from SQL.funSQL import *


class app:
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Assistant HAB")
        self.ventana.geometry('800x500')
        self.ventana.config(bg='#fcfcfc')
        self.ventana.resizable(width=0, height=0)
        self.ventana.style = ttk.Style()
        self.ventana.tk.call("source", "forest-light.tcl")
        self.ventana.style.theme_use("forest-light")
        utl.centrar_ventana(self.ventana,800,500)

        ##Frame para fechas importantes

        frame_fechas = tk.Frame(self.ventana, bd=0, width=100, height=100, relief=tk.SOLID, padx=10, pady=10, bg='red')
        frame_fechas.pack(side="top", expand=tk.NO, fill=tk.BOTH)

        ##Frame Botones Principales

        frame_botonesP = tk.Frame(self.ventana, bd=0, width=500, height=200, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_botonesP.pack(side="left", expand=tk.NO, fill=tk.BOTH)

        frame_botonesP.grid_columnconfigure(0, weight=1)
        frame_botonesP.grid_columnconfigure(1, weight=1)

        boton1 = ttk.Button(frame_botonesP, text="\n\n\nOrden de trabajo\n\n\n", style="Accent.TButton", width=25, command= abrir_orden_trabajo )
        boton1.grid(row=0, column=0, padx=25, pady=30, sticky="nsew")

        boton2 = ttk.Button(frame_botonesP, text="\n\n\nNomina semanal\n\n\n", style="Accent.TButton", width=25  )
        boton2.grid(row=0, column=1, padx=25, pady=30, sticky="nsew")

        boton3 = ttk.Button(frame_botonesP, text="\n\n\nConsultas\n\n\n", style="Accent.TButton", width=25  )
        boton3.grid(row=1, column=0, padx=25, pady=30, sticky="nsew")

        boton4 = ttk.Button(frame_botonesP, text="\n\n\nInventario\n\n\n", style="Accent.TButton", width=25  )
        boton4.grid(row=1, column=1, padx=25, pady=30, sticky="nsew")
       
        #Frames botones secundarios

        frame_botonesS = tk.Frame(self.ventana, bd=0, width=300, height=100, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
        frame_botonesS.pack(side='right', expand=tk.NO, fill=tk.BOTH)

        frame_botonesS.grid_columnconfigure(0, weight=1)
        frame_botonesS.grid_columnconfigure(1, weight=1)

        boton1 = ttk.Button(frame_botonesS, text="Facturas", style="Accent.TButton", width=25  )
        boton1.grid(row=0, column=0, padx=25, pady=15, sticky="nsew")

        boton2 = ttk.Button(frame_botonesS, text="Remisiones", style="Accent.TButton", width=25  )
        boton2.grid(row=1, column=0, padx=25, pady=15, sticky="nsew")

        boton3 = ttk.Button(frame_botonesS, text="Cotizaciones", style="Accent.TButton", width=25  )
        boton3.grid(row=2, column=0, padx=25, pady=15, sticky="nsew")

        boton4 = ttk.Button(frame_botonesS, text="Empleados", style="Accent.TButton", width=25  )
        boton4.grid(row=3, column=0, padx=25, pady=15, sticky="nsew")

        boton5 = ttk.Button(frame_botonesS, text="Proveedores", style="Accent.TButton", width=25  )
        boton5.grid(row=4, column=0, padx=25, pady=15, sticky="nsew")

        boton6 = ttk.Button(frame_botonesS, text="Areas", style="Accent.TButton", width=25, command=lambda: (area()))
        boton6.grid(row=5, column=0, padx=25, pady=15, sticky="nsew")

        self.ventana.mainloop()