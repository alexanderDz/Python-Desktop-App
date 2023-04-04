import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl


def abrir_orden_trabajo():
    ventana_orden_trabajo = tk.Toplevel()
    ventana_orden_trabajo.title("Orden de trabajo")
    ventana_orden_trabajo.geometry("450x450")
    ventana_orden_trabajo.config(bg='#fcfcfc')
    ventana_orden_trabajo.resizable(width=0, height=0)
    utl.centrar_ventana(ventana_orden_trabajo,450,450)

    #Formulario
    formulario=ttk.Frame(ventana_orden_trabajo)
    formulario.grid(padx = 20, pady = 20)

    #Etiquetas
    ttk.Label(formulario, text="ID Orden").grid(column=0, row=0, padx=5, pady=5)
    ttk.Label(formulario, text="ID Cliente").grid(column=0, row=1, padx=5, pady=5)
    ttk.Label(formulario, text="ID Empleado").grid(column=0, row=2, padx=5, pady=5)
    ttk.Label(formulario, text="ID Servicio").grid(column=0, row=3, padx=5, pady=5)
    ttk.Label(formulario, text="ID Factura").grid(column=0, row=4, padx=5, pady=5)
    ttk.Label(formulario, text="ID Remision").grid(column=0, row=5, padx=5, pady=5)
    ttk.Label(formulario, text="Estado").grid(column=0, row=6, padx=5, pady=5)
    ttk.Label(formulario, text="Fecha").grid(column=0, row=7, padx=5, pady=5)
    ttk.Label(formulario, text="Marca del Vehiculo").grid(column=0, row=8, padx=5, pady=5)
    ttk.Label(formulario, text="Diagnostico").grid(column=0, row=9, padx=5, pady=5)
    ttk.Label(formulario, text="Area").grid(column=0, row=10, padx=5, pady=5)


    #Entradas de texto
    idOrden = tk.StringVar()
    idCliente = tk.StringVar()
    idEmpleado = tk.StringVar()
    idServicio = tk.StringVar()
    idFactura = tk.StringVar()
    idRemision = tk.StringVar()
    estado = tk.StringVar()
    fecha = tk.StringVar()
    marca = tk.StringVar()
    diagnostico = tk.StringVar()
    area = tk.StringVar()


    ttk.Entry(formulario, textvariable = marca).grid(column=1, row=8, padx=5, pady=5)
    ttk.Entry(formulario, textvariable = diagnostico).grid(column=1, row=9, padx=5, pady=5)
    ttk.Entry(formulario, textvariable = area).grid(column=1, row=10, padx=5, pady=5)


    #Boton de enviar
    ttk.Button(formulario, text = "Enviar").grid(column=1, row=12, padx=5, pady=5)


    # Establecer el foco en el primer campo
    return ventana_orden_trabajo.mainloop()