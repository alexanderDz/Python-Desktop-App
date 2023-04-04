import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl
from SQL.funSQL import *


def area():
    cnx = conectarDB()

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


    query = "INSERT INTO `multiservicios`.`area` (`Nombre_Area`, `Porcentaje_comision`) VALUES (%s, %s)"

    ttk.Button(formulario, text = "Guardar", command=lambda: ejecutar_query(cnx, query, (nombre.get(), porcentaje.get()), "INSERT")).grid(column=1, row=2, padx=5, pady=5)

    def on_closing():
        cnx.close()
        if not cnx.is_connected():
            print("La conexión se cerró correctamente.")
        else:
            print("La conexión aún está abierta.")
        ventana_area.destroy()

    ventana_area.protocol("WM_DELETE_WINDOW", on_closing)
    
    return ventana_area.mainloop()
