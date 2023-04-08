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
    utl.centrar_ventana(ventana_coti,750,600)
    ventana_coti.wm_attributes('-topmost', False)

    # Formulario
    formulario = ttk.Frame(ventana_coti)
    formulario.grid(padx=20, pady=20)

    ttk.Label(formulario, text="Fecha").grid(column=2, row=0, padx=10, pady=5)

    fechaContr = DateEntry(formulario, width=12, background="#217346",
                           foreground='white', borderwidth=2)
    fechaContr.grid(column=4, row=0, padx=10, pady=10)

    ttk.Label(formulario, text="Nombre").grid(column=0, row=1, padx=10, pady=2)
    ttk.Label(formulario, text="Identificacion (CC/NIT)").grid(column=0, row=2, padx=10, pady=2)
    ttk.Label(formulario, text="Telefono").grid(column=2, row=1, padx=10, pady=2)
    ttk.Label(formulario, text="Direccion").grid(column=0, row=3, padx=10, pady=2)
    ttk.Label(formulario, text="Ciudad").grid(column=2, row=2, padx=10, pady=2)
    ttk.Label(formulario, text="Placa").grid(column=0, row=6, padx=10, pady=2)
    ttk.Label(formulario, text="Modelo").grid(column=2, row=3, padx=10, pady=2)

    # Entradas de texto
    nombreCot = tk.StringVar()
    identificacion = tk.StringVar()
    telefono = tk.StringVar()
    direccion = tk.StringVar()
    ciudad = tk.StringVar()
    placa = tk.StringVar()
    modelo = tk.StringVar()

    ttk.Entry(formulario, textvariable=nombreCot).grid(column=1, row=1, padx=10, pady=2)
    ttk.Entry(formulario, textvariable=identificacion).grid(column=1, row=2, padx=10, pady=2)
    ttk.Entry(formulario, textvariable=telefono).grid(column=4, row=1, padx=10, pady=2)
    ttk.Entry(formulario, textvariable=direccion).grid(column=1, row=3, padx=10, pady=2)
    ttk.Entry(formulario, textvariable=ciudad).grid(column=4, row=2, padx=10, pady=2)
    ttk.Entry(formulario, textvariable=placa).grid(column=1, row=6, padx=10, pady=2)
    ttk.Entry(formulario, textvariable=modelo).grid(column=4, row=3, padx=10, pady=2)


    ttk.Button(formulario, text="Guardar Cliente", style="Accent.TButton").grid(column=4, row=9, padx=5, pady=5)


    ##Agregar empleado
    def add_item(event=None):
        item = lista_areas.get().strip()
        if item:
            items.append(item)
            listbox.insert(tk.END, item)

    areas = ["Carlos", "Jose", "Ramiro", "Diego"]

    items = []

    # Crear la entrada de lista
    lista_areas = ttk.Combobox(formulario, values=areas)
    lista_areas.grid(column=0, row=10, padx=15, pady=2)

    # Crear el botón para añadir elementos
    button = ttk.Button(formulario, text="Añadir empleado", style="Accent.TButton", command=add_item)
    button.grid(column=0, row=11, padx=15, pady=2)
    # Crear la lista de elementos
    listbox = tk.Listbox(formulario, height=5)
    listbox.grid(column=0, row=12, padx=15, pady=2)

    # Configurar el botón y la entrada de lista
    lista_areas.bind("<Return>", add_item)
    # button.bind("<Button-1>", add_item)

    def agregar_area(event=None):
        item = lista_areas.get().strip()
        if item:
            items.append(item)
            listbox.insert(tk.END, item)

    areas = ["Mecanica", "Latoneria y pintura", "Frenos y suspencion", "Electricidad"]

    items = []

    # Crear la entrada de lista
    lista_areas = ttk.Combobox(formulario, values=areas)
    lista_areas.grid(column=1, row=10, padx=15, pady=2)

    # Crear el botón para añadir elementos
    button = ttk.Button(formulario, text="Añadir area", style="Accent.TButton", command=agregar_area)
    button.grid(column=1, row=11, padx=15, pady=2)
    # Crear la lista de elementos
    listbox = tk.Listbox(formulario, height=5)
    listbox.grid(column=1, row=12, padx=15, pady=2)

    # Configurar el botón y la entrada de lista
    lista_areas.bind("<Return>", agregar_area)
    # button.bind("<Button-1>", add_item)

    ttk.Label(formulario, text="Diagnostico").grid(column=4, row=10, padx=10, pady=2)
    diagnostico = tk.StringVar()

    ttk.Entry(formulario,  textvariable=diagnostico).grid(column=4, row=11, padx=10, pady=2)



    return ventana_coti.mainloop()