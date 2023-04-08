import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl
from SQL.funSQL import *
from tkcalendar import DateEntry

def remisiones():

    ventana_remi = tk.Toplevel()
    ventana_remi.title("Cotizaciones")
    ventana_remi.geometry("450x250")
    ventana_remi.config(bg='#fcfcfc')
    ventana_remi.resizable(width=0, height=0)
    utl.centrar_ventana(ventana_remi,1050,500)
    ventana_remi.wm_attributes('-topmost', False)

    frame_datos = tk.Frame(ventana_remi, bd=0, width=100, height=255, relief=tk.SOLID, padx=10, pady=10, bg='blue')
    frame_datos.grid(row=0, column=0, padx=0, pady=0)

    ttk.Label(frame_datos, text="Fecha").grid(column=2, row=0, padx=10, pady=5)

    fechaContr = DateEntry(frame_datos, width=12, background="#217346",
                           foreground='white', borderwidth=2)
    fechaContr.grid(column=4, row=0, padx=10, pady=10)

    ttk.Label(frame_datos, text="Nombre").grid(column=0, row=1, padx=10, pady=2)
    ttk.Label(frame_datos, text="Identificacion (CC/NIT)").grid(column=0, row=2, padx=10, pady=2)
    ttk.Label(frame_datos, text="Telefono").grid(column=2, row=1, padx=10, pady=2)
    ttk.Label(frame_datos, text="Direccion").grid(column=0, row=3, padx=10, pady=2)
    ttk.Label(frame_datos, text="Ciudad").grid(column=2, row=2, padx=10, pady=2)
    ttk.Label(frame_datos, text="Placa").grid(column=0, row=6, padx=10, pady=2)
    ttk.Label(frame_datos, text="Modelo").grid(column=2, row=3, padx=10, pady=2)

    # Entradas de texto
    nombreCot = tk.StringVar()
    identificacion = tk.StringVar()
    telefono = tk.StringVar()
    direccion = tk.StringVar()
    ciudad = tk.StringVar()
    placa = tk.StringVar()
    modelo = tk.StringVar()

    ttk.Entry(frame_datos, textvariable=nombreCot).grid(column=1, row=1, padx=10, pady=2)
    ttk.Entry(frame_datos, textvariable=identificacion).grid(column=1, row=2, padx=10, pady=2)
    ttk.Entry(frame_datos, textvariable=telefono).grid(column=4, row=1, padx=10, pady=2)
    ttk.Entry(frame_datos, textvariable=direccion).grid(column=1, row=3, padx=10, pady=2)
    ttk.Entry(frame_datos, textvariable=ciudad).grid(column=4, row=2, padx=10, pady=2)
    ttk.Entry(frame_datos, textvariable=placa).grid(column=1, row=6, padx=10, pady=2)
    ttk.Entry(frame_datos, textvariable=modelo).grid(column=4, row=3, padx=10, pady=2)

    ttk.Button(frame_datos, text="Guardar Cliente", style="Accent.TButton").grid(column=4, row=9, padx=5, pady=5)

    frame_prod = tk.Frame(ventana_remi, bd=0, width=100, height=165, relief=tk.SOLID, padx=10, pady=10, bg='green')
    frame_prod.grid(row=0, column=1, padx=0, pady=0, sticky='nsew')

    frame_ser = tk.Frame(ventana_remi, bd=0, width=100, height=165, relief=tk.SOLID, padx=10, pady=10, bg='yellow')
    frame_ser.grid(row=1, column=0, columnspan=2, padx=0, pady=0, sticky='nsew')