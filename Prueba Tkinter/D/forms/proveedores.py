import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl
from SQL.funSQL import *

def proveedor():

    ventana_prove = tk.Toplevel()
    ventana_prove.title("Proveedores")
    ventana_prove.geometry("450x250")
    ventana_prove.config(bg='#fcfcfc')
    ventana_prove.resizable(width=0, height=0)
    utl.centrar_ventana(ventana_prove,450,250)
    ventana_prove.wm_attributes('-topmost', False)

    #Formulario
    formulario=ttk.Frame(ventana_prove)
    formulario.grid( padx = 30, pady = 20)

    # Etiquetas
    ttk.Label(formulario, text="Nombre del proveedor").grid(column=0, row=0, padx=15, pady=5)
    ttk.Label(formulario, text="Telefono").grid(column=0, row=1, padx=15, pady=5)
    ttk.Label(formulario, text="Identificacion").grid(column=0, row=2, padx=15, pady=5)
    ttk.Label(formulario, text="Direccion").grid(column=0, row=3, padx=15, pady=5)

    # Entradas de texto
    nombrePro = tk.StringVar()
    telefono = tk.StringVar()
    identificacion = tk.StringVar()
    direccion = tk.StringVar()

    ttk.Entry(formulario, textvariable=nombrePro).grid(column=1, row=0, padx=15, pady=15)
    ttk.Entry(formulario, textvariable=telefono).grid(column=1, row=1, padx=15, pady=15)
    ttk.Entry(formulario, textvariable=identificacion).grid(column=1, row=0, padx=15, pady=15)
    ttk.Entry(formulario, textvariable=direccion).grid(column=1, row=1, padx=15, pady=15)

