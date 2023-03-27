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

def abrir_cliente():
    ventana_cliente = tk.Toplevel(ventana1)
    ventana_cliente.title("Registra cliente")
    ventana_cliente.geometry("400x400")

    #Formulario
    formulario=ttk.Frame(ventana_cliente)
    formulario.grid(padx=20, pady=20)

    #Etiquetas
    ttk.Label(formulario, text="ID Cliente").grid(column=0, row=0, padx=5, pady=5)
    ttk.Label(formulario, text="Nombre").grid(column=0, row=1, padx=5, pady=5)
    ttk.Label(formulario, text="Apellido").grid(column=0, row=2, padx=5, pady=5)
    ttk.Label(formulario, text="Celular").grid(column=0, row=3, padx=5, pady=5)
    ttk.Label(formulario, text="Correo Electronico").grid(column=0, row=4, padx=5, pady=5)
    ttk.Label(formulario, text="Direccion").grid(column=0, row=5, padx=5, pady=5)
    ttk.Label(formulario, text="Documneto de identidad").grid(column=0, row=6, padx=5, pady=5)


    #Entradas de texto
    nombre = tk.StringVar()
    apellido = tk.StringVar()
    celular = tk.StringVar()
    correo = tk.StringVar()
    direccion = tk.StringVar()
    identifiaccion = tk.StringVar()
    
    ttk.Entry(formulario, textvariable=nombre).grid(column=1, row=1, padx=5, pady=5)
    ttk.Entry(formulario, textvariable= apellido).grid(column=1, row=2, padx=5, pady=5)
    ttk.Entry(formulario, textvariable=celular).grid(column=1, row=3, padx=5, pady=5)
    ttk.Entry(formulario, textvariable= correo).grid(column=1, row=4, padx=5, pady=5)
    ttk.Entry(formulario, textvariable=direccion).grid(column=1, row=5, padx=5, pady=5)
    ttk.Entry(formulario, textvariable= identifiaccion).grid(column=1, row=6, padx=5, pady=5)

    #Boton de enviar
    ttk.Button(formulario, text="Enviar").grid(column=1, row=7, padx=5, pady=5)


    # Establecer el foco en el primer campo
    ttk.Entry(formulario, textvariable=nombre).focus()

    ventana_cliente.mainloop()


boton0 = ttk.Button(ventana1, text="Agregar cliente", style="Accent.TButton", width=25, command=abrir_cliente)
boton0.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")



def abrir_orden_trabajo():
    ventana_orden_trabajo = tk.Toplevel(ventana1)
    ventana_orden_trabajo.title("Orden de trabajo")
    ventana_orden_trabajo.geometry("400x400")

    #Formulario
    formulario=ttk.Frame(ventana_orden_trabajo)
    formulario.grid(padx=20, pady=20)

    #Etiquetas
    ttk.Label(formulario, text="Nombre").grid(column=0, row=0, padx=5, pady=5)
    ttk.Label(formulario, text="Placa Auto").grid(column=0, row=1, padx=5, pady=5)


    #Entradas de texto
    nombre = tk.StringVar()
    placa = tk.StringVar()
    ttk.Entry(formulario, textvariable=nombre).grid(column=1, row=0, padx=5, pady=5)
    ttk.Entry(formulario, textvariable= placa).grid(column=1, row=1, padx=5, pady=5)


    #Boton de enviar
    ttk.Button(formulario, text="Enviar").grid(column=1, row=2, padx=5, pady=5)


    # Establecer el foco en el primer campo
    ttk.Entry(formulario, textvariable=nombre).focus()

    ventana_orden_trabajo.mainloop()

boton1 = ttk.Button(ventana1, text="Orden de trabajo", style="Accent.TButton", width=25, command=abrir_orden_trabajo)
boton1.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")


def abrir_nomina():
    ventana_nomina = tk.Toplevel(ventana1)
    ventana_nomina.title("Nomina semanal")
    ventana_nomina.geometry("400x400")
    etiqueta_nomina = ttk.Label(ventana_nomina, text="Esta es la ventana de nomina")
    etiqueta_nomina.pack(padx=20, pady=20)

boton2 = ttk.Button(ventana1, text="Nomina semanal", style="Accent.TButton", width=25, command=abrir_nomina)
boton2.grid(row=0, column=2, padx=5, pady=10, sticky="nsew")


def abrir_inventario():
    ventana_inventario = tk.Toplevel(ventana1)
    ventana_inventario.title("Administracion de inventario")
    ventana_inventario.geometry("400x400")
    etiqueta_inventario = ttk.Label(ventana_inventario, text="Esta es la ventana de inventario")
    etiqueta_inventario.pack(padx=20, pady=20)

boton3 = ttk.Button(ventana1, text="Administracion de inventario", style="Accent.TButton", width=25, command=abrir_inventario)
boton3.grid(row=0, column=3, padx=5, pady=10, sticky="nsew")

boton4 = ttk.Button(ventana1, text="Consultas", style="Accent.TButton", width=25)
boton4.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

#Agregando resposibidad de la app
for i in range(ventana1.grid_size()[0]):
    ventana1.grid_columnconfigure(i, weight=1)

for i in range(ventana1.grid_size()[1]):
    ventana1.grid_rowconfigure(i, weight=1)

boton0.grid(padx=20, pady=20)
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
