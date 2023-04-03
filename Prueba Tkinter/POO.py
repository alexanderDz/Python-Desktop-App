import tkinter as tk
from tkinter import ttk

class VentanaPrincipal:
    def __init__(self,master):
        self.master = master
        self.ventana = tk.Tk()
        self.ventana.title("Assistant HAB")
        self.ventana1.option_add("*tearOff", False)

        style = ttk.Style(self.ventana1)
        self.ventana1.tk.call("source", "forest-light.tcl")
        style.theme_use("forest-light")

        self.ventana1.geometry("800x500")


        self.crear_widgets()

        

    def crear_widgets(self):
        # Definir los botones principales
        boton1 = ttk.Button(self.ventana, text="Botón 1", width=25)
        boton1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

        boton2 = ttk.Button(self.ventana, text="Botón 2", width=25)
        boton2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

        boton3 = ttk.Button(self.ventana, text="Botón 3", width=25)
        boton3.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")

        boton4 = ttk.Button(self.ventana, text="Botón 4", width=25)
        boton4.grid(row=1, column=1, padx=5, pady=10, sticky="nsew")

        # Definir el frame para los botones horizontales y verticales
        frame = ttk.Frame(self.ventana)
        frame.grid(row=0, column=2, rowspan=2, padx=5, pady=10, sticky="nsew")



        # Crear el nuevo frame para los botones adicionales
        frame2 = ttk.Frame(self.ventana)
        frame2.grid(row=0, column=3, rowspan=2, padx=5, pady=10, sticky="nsew")

        # Crear los botones adicionales en el nuevo frame
        boton5 = ttk.Button(frame2, text="Botón 9", width=25)
        boton5.grid(row=0, column=0, pady=10, sticky="nsew")

        boton6 = ttk.Button(frame2, text="Botón 10", width=25)
        boton6.grid(row=1, column=0, pady=10, sticky="nsew")

        boton7 = ttk.Button(frame2, text="Botón 11", width=25)
        boton7.grid(row=2, column=0, pady=10, sticky="nsew")

        boton8 = ttk.Button(frame2, text="Botón 12", width=25)
        boton8.grid(row=3, column=0, pady=10, sticky="nsew")

        boton9 = ttk.Button(frame2, text="Botón 13", width=25)
        boton9.grid(row=4, column=0, pady=10, sticky="nsew")

        boton10 = ttk.Button(frame2, text="Botón 14", width=25)
        boton10.grid(row=5, column=0, pady=10, sticky="nsew")

        # Correr la ventana
        self.ventana.mainloop()

# Crear una instancia de la ventana principal y correrla
ventana = VentanaPrincipal()
