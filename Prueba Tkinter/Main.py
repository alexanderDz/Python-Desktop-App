#################################################
######    Aplicación desarrollada por:     ######
######          HAB Solutions              ######
#################################################


import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
ventana1 = tk.Tk()
ventana1.title("Forest")
ventana1.option_add("*tearOff", False) # This is always a good idea

style = ttk.Style(ventana1)
ventana1.tk.call("source", "forest-light.tcl")

# Set the theme with the theme_use method
style.theme_use("forest-light")

# Definir el título de la ventana
ventana1.title("Assistant HAB")

# Definir las dimensiones de la ventana
ventana1.geometry("800x500")

#Botones principales

def abrir_orden_trabajo():
    ventana_orden_trabajo = tk.Toplevel(ventana1)
    ventana_orden_trabajo.title("Orden de trabajo")
    ventana_orden_trabajo.geometry("450x450")

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
    ttk.Entry(formulario, textvariable= nombre).focus()

    ventana_orden_trabajo.mainloop()

boton1 = ttk.Button(ventana1, text="Orden de trabajo", style="Accent.TButton", width=25, command=abrir_orden_trabajo)
boton1.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")


def abrir_nomina():
    ventana_nomina = tk.Toplevel(ventana1)
    ventana_nomina.title("Nomina semanal")
    ventana_nomina.geometry("400x400")
    etiqueta_nomina = ttk.Label(ventana_nomina, text="Esta es la ventana de nomina")
    etiqueta_nomina.pack(padx=20, pady=20)

boton2 = ttk.Button(ventana1, text="Nomina semanal", style="Accent.TButton", width=25, command=abrir_nomina)
boton2.grid(row=1, column=1, padx=5, pady=10, sticky="nsew")


def abrir_inventario():
    ventana_inventario = tk.Toplevel(ventana1)
    ventana_inventario.title("Administracion de inventario")
    ventana_inventario.geometry("400x400")
    etiqueta_inventario = ttk.Label(ventana_inventario, text="Esta es la ventana de inventario")
    etiqueta_inventario.pack(padx=20, pady=20)

boton3 = ttk.Button(ventana1, text="Administracion de inventario", style="Accent.TButton", width=25, command=abrir_inventario)
boton3.grid(row=2, column=1, padx=5, pady=10, sticky="nsew")

def abrir_consultas():
    ventana_inventario = tk.Toplevel(ventana1)
    ventana_inventario.title("Consultas")
    ventana_inventario.geometry("400x400")
    etiqueta_inventario = ttk.Label(ventana_inventario, text="Esta es la ventana de consultas")
    etiqueta_inventario.pack(padx=20, pady=20)

boton4 = ttk.Button(ventana1, text="Consultas", style="Accent.TButton", width=25, command=abrir_consultas)
boton4.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

##########################################################################

frame2 = ttk.Frame(ventana1)
frame2.grid(row=1, column=3, rowspan=2, padx=10, pady=10, sticky="nsew")

# crear los botones adicionales en el nuevo frame
boton5 = ttk.Button(frame2, text="Botón 9", width=25)
boton5.grid(row=1, column=3, pady=10, sticky="nsew")

boton6 = ttk.Button(frame2, text="Botón 10", width=25)
boton6.grid(row=2, column=3, pady=20, sticky="nsew")

boton7 = ttk.Button(frame2, text="Botón 11", width=25)
boton7.grid(row=3, column=3, pady=20, sticky="nsew")

boton8 = ttk.Button(frame2, text="Botón 12", width=25)
boton8.grid(row=4, column=3, pady=20, sticky="nsew")

boton9 = ttk.Button(frame2, text="Botón 13", width=25)
boton9.grid(row=5, column=3, pady=20, sticky="nsew")

boton10 = ttk.Button(frame2, text="Botón 14", width=25)
boton10.grid(row=6, column=3, pady=20, sticky="nsew")


############################################################3



#Agregando resposibidad de la app
for i in range(ventana1.grid_size()[0]):
    ventana1.grid_columnconfigure(i, weight=1)

for i in range(ventana1.grid_size()[1]):
    ventana1.grid_rowconfigure(i, weight=1)


boton1.grid(padx=20, pady=20)
boton2.grid(padx=20, pady=20)
boton3.grid(padx=20, pady=20)
boton4.grid(padx=20, pady=20)


ventana1.update_idletasks()

ancho = ventana1.winfo_width()
alto = ventana1.winfo_height()

x = (ventana1.winfo_screenwidth() // 2) - (ancho // 2)
y = (ventana1.winfo_screenheight() // 2) - (alto // 2)

ventana1.geometry('{}x{}+{}+{}'.format(ancho, alto, x, y))

# Mostrar la ventana
ventana1.mainloop()


