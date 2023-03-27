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
ventana1.title("Mi aplicación")

# Definir las dimensiones de la ventana
ventana1.geometry("800x500")

#Botones principales
def abrir_orden_trabajo():
    ventana_orden_trabajo = tk.Toplevel(ventana1)
    ventana_orden_trabajo.title("Orden de trabajo")
    ventana_orden_trabajo.geometry("400x400")
    etiqueta_orden_trabajo = ttk.Label(ventana_orden_trabajo, text="Esta es la ventana de orden de trabajo")
    etiqueta_orden_trabajo.pack(padx=20, pady=20)

boton1 = ttk.Button(ventana1, text="Orden de trabajo", style="Accent.TButton", width=25, command=abrir_orden_trabajo)
boton1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")


def abrir_nomina():
    ventana_nomina = tk.Toplevel(ventana1)
    ventana_nomina.title("Nomina semanal")
    ventana_nomina.geometry("400x400")
    etiqueta_nomina = ttk.Label(ventana_nomina, text="Esta es la ventana de nomina")
    etiqueta_nomina.pack(padx=20, pady=20)

boton2 = ttk.Button(ventana1, text="Nomina semanal", style="Accent.TButton", width=25, command=abrir_nomina)
boton2.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")


def abrir_inventario():
    ventana_inventario = tk.Toplevel(ventana1)
    ventana_inventario.title("Administracion de inventario")
    ventana_inventario.geometry("400x400")
    etiqueta_inventario = ttk.Label(ventana_inventario, text="Esta es la ventana de inventario")
    etiqueta_inventario.pack(padx=20, pady=20)

boton3 = ttk.Button(ventana1, text="Administracion de inventario", style="Accent.TButton", width=25, command=abrir_inventario)
boton3.grid(row=0, column=2, padx=5, pady=10, sticky="nsew")

boton4 = ttk.Button(ventana1, text="Consultas", style="Accent.TButton", width=25)
boton4.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

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
