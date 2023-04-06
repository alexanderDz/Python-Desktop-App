import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl
from SQL.funSQL import *
from tkcalendar import DateEntry

def cotizaciones():

    ventana_coti = tk.Toplevel()
    ventana_coti.title("Cotizaciones")
    ventana_coti.geometry("450x250")
    ventana_coti.config(bg='#fcfcfc')
    ventana_coti.resizable(width=0, height=0)
    utl.centrar_ventana(ventana_coti,650,550)
    ventana_coti.wm_attributes('-topmost', False)

    # Formulario
    formulario = ttk.Frame(ventana_coti)
    formulario.grid(padx=20, pady=20)

    ttk.Label(formulario, text="Fecha").grid(column=2, row=0, padx=15, pady=5)

    fechaContr = DateEntry(formulario, width=12, background="#217346",
                           foreground='white', borderwidth=2)
    fechaContr.grid(column=4, row=0, padx=10, pady=10)

    ttk.Label(formulario, text="Nombre").grid(column=0, row=1, padx=15, pady=5)
    ttk.Label(formulario, text="Identificacion (CC/NIT)").grid(column=0, row=2, padx=15, pady=5)
    ttk.Label(formulario, text="Telefono").grid(column=2, row=1, padx=15, pady=5)
    ttk.Label(formulario, text="Direccion").grid(column=0, row=3, padx=15, pady=5)
    ttk.Label(formulario, text="Ciudad").grid(column=2, row=2, padx=15, pady=5)
    ttk.Label(formulario, text="Placa").grid(column=0, row=6, padx=15, pady=5)
    ttk.Label(formulario, text="Modelo").grid(column=2, row=3, padx=15, pady=5)

    # Entradas de texto
    nombreCot = tk.StringVar()
    identificacion = tk.StringVar()
    telefono = tk.StringVar()
    direccion = tk.StringVar()
    ciudad = tk.StringVar()
    placa = tk.StringVar()
    modelo = tk.StringVar()

    ttk.Entry(formulario, textvariable=nombreCot).grid(column=1, row=1, padx=15, pady=15)
    ttk.Entry(formulario, textvariable=identificacion).grid(column=1, row=2, padx=15, pady=15)
    ttk.Entry(formulario, textvariable=telefono).grid(column=4, row=1, padx=15, pady=15)
    ttk.Entry(formulario, textvariable=direccion).grid(column=1, row=3, padx=15, pady=15)
    ttk.Entry(formulario, textvariable=ciudad).grid(column=4, row=2, padx=15, pady=15)
    ttk.Entry(formulario, textvariable=placa).grid(column=1, row=6, padx=15, pady=15)
    ttk.Entry(formulario, textvariable=modelo).grid(column=4, row=3, padx=15, pady=15)


    ttk.Button(formulario, text="Guardar", style="Accent.TButton").grid(column=4, row=9, padx=5, pady=5)


    return ventana_coti.mainloop()