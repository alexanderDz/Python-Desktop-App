import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl
from SQL.funSQL import *

def area():

    ventana_area = tk.Toplevel()
    ventana_area.title("Area")
    ventana_area.geometry("450x250")
    ventana_area.config(bg='#fcfcfc')
    ventana_area.resizable(width=0, height=0)
    utl.centrar_ventana(ventana_area,450,250)
    ventana_area.wm_attributes('-topmost', False)

    #Formulario
    formulario=ttk.Frame(ventana_area)
    formulario.grid( padx = 30, pady = 20)

    #Etiquetas

    ttk.Label(formulario, text="Nombre del area").grid(column=0, row=0, padx=15, pady=5)
    ttk.Label(formulario, text="Porcentaje").grid(column=0, row=1, padx=15, pady=5)

    #Entradas de texto
    nombre = tk.StringVar()
    porcentaje = tk.StringVar()

    areas = ["Mecanica", "Latoneria y pintura", "Frenos y suspencion", "Electricidad"]

    nombre = ttk.Combobox(formulario, values=areas)
    nombre.current(0)
    nombre.grid( column=1,row=0, padx=5, pady=10, sticky="ew")

    porcentaje = ttk.Spinbox(formulario, from_=0, to=100)
    porcentaje.insert(0, "Porcentaje")
    porcentaje.grid(column=1, row=1,  padx=5, pady=10, sticky="ew")


    query = "INSERT INTO `multiservicios`.`area` ( `Nombre_Area`, `Porcentaje_comision`) VALUES (%s, %s)"

    def mensaje():

        mensajeDatos = ttk.Label(formulario, text="Datos guardados")
        mensajeDatos.grid(column=1, row=3, padx=15, pady=5)
        nombre.set("")
        porcentaje.set("")


    ttk.Button(formulario, text = "Guardar", style="Accent.TButton", command=lambda: (ejecutar_query(query, (nombre.get(), porcentaje.get()), "INSERT"),mensaje())).grid(column=1, row=2, padx=5, pady=5)
    ttk.Button(formulario, text = "Actualizar", style="Accent.TButton").grid(column=0, row=2, padx=5, pady=5)
    return ventana_area.mainloop()
