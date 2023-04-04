import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl
from tkcalendar import DateEntry


def abrir_empleado():
    ventana_empleado = tk.Toplevel()
    ventana_empleado.title("Empleados")
    ventana_empleado.geometry("450x450")
    ventana_empleado.config(bg='#fcfcfc')
    ventana_empleado.resizable(width=0, height=0)
    utl.centrar_ventana(ventana_empleado,450,450)

  #Formulario
    formulario=ttk.Frame(ventana_empleado)
    formulario.grid(padx = 20, pady = 20)

    ttk.Label(formulario, text="Nombre").grid(column=0, row=0, padx=15, pady=5)
    ttk.Label(formulario, text="Apellido").grid(column=0, row=1, padx=15, pady=5)
    ttk.Label(formulario, text="Identificacion").grid(column=0, row=2, padx=15, pady=5)
    ttk.Label(formulario, text="Telefono").grid(column=0, row=3, padx=15, pady=5)
    ttk.Label(formulario, text="Fecha de contratacion").grid(column=0, row=4, padx=15, pady=5)
    ttk.Label(formulario, text="Estado").grid(column=0, row=5, padx=15, pady=5)

    # Entradas de texto
    nombreEmp = tk.StringVar()
    apellidoEmp = tk.StringVar()
    identificacion = tk.StringVar()
    telefono = tk.StringVar()
    fechaContr = tk.StringVar()
    ##estado = tk.getboolean()

    empleadosNombre = ["Jose luis", "el chavo", "Goku", "Juanito alimaña"]

    nombreEmp = ttk.Combobox(formulario, values=empleadosNombre)
    nombreEmp.current(0)
    nombreEmp.grid(column=1, row=0, padx=5, pady=10, sticky="ew")

    empleadosApellido = ["De la hoz", "Del ocho", "Son", "Con mucha maña"]

    apellidoEmp = ttk.Combobox(formulario, values=empleadosApellido)
    apellidoEmp.current(0)
    apellidoEmp.grid(column=1, row=1, padx=5, pady=10, sticky="ew")

    ttk.Entry(formulario, textvariable=identificacion).grid(column=1, row=2, padx=15, pady=15)
    ttk.Entry(formulario, textvariable=telefono).grid(column=1, row=3, padx=15, pady=15)

    fechaContr = DateEntry(formulario, width=12, background="#217346",
                      foreground='white', borderwidth=2)
    fechaContr.grid(column=1, row=4, padx=10, pady=10)

    estado = ttk.Checkbutton(formulario, text="Activo", style="Switch")
    estado.grid(column=1, row=5,  padx=15, pady=15, sticky="nsew")

    ttk.Button(formulario, text="Guardar", style="Accent.TButton").grid(column=1, row=7, padx=5, pady=5)
    ttk.Button(formulario, text="Actualizar", style="Accent.TButton").grid(column=0, row=7, padx=5, pady=5)

    return ventana_empleado.mainloop()