import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl
from SQL.funSQL import *


def area():
    ventana_area = tk.Toplevel()
    ventana_area.title("Orden de trabajo")
    ventana_area.geometry("450x250")
    utl.centrar_ventana(ventana_area,450,250)

    #Formulario
    formulario=ttk.Frame(ventana_area)
    formulario.grid( padx = 30, pady = 20)

    #Etiquetas
    ttk.Label(formulario, text="Nombre").grid(column=0, row=0, padx=15, pady=5)
    ttk.Label(formulario, text="Porcentaje").grid(column=0, row=1, padx=15, pady=5)

    #Entradas de texto
    nombre = tk.StringVar()
    porcentaje = tk.StringVar()

    ttk.Entry(formulario, textvariable = nombre).grid(column=1, row=0, padx=15, pady=15)
    ttk.Entry(formulario, textvariable = porcentaje).grid(column=1, row=1, padx=15, pady=15)


    query = "INSERT INTO `multiservicios`.`area` (`Area_ID`, `Nombre_Area`, `Porcentaje_comision`) VALUES (%s, %s, %s)"

    ttk.Button(formulario, text = "Guardar", command=lambda: ejecutar_query(query, (1, nombre.get(), porcentaje.get()), "INSERT")).grid(column=1, row=2, padx=5, pady=5)

    return ventana_area.mainloop()
