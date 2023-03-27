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

# Crear una etiqueta en la ventana
boton1 = ttk.Button(ventana1, text="Orden de trabajo", style="Accent.TButton")
boton1.pack(pady=10, padx=10, fill=tk.BOTH,  side=tk.LEFT)
boton2 = ttk.Button(ventana1, text="Nomina semanal", style="Accent.TButton")
boton2.pack(pady=10, padx=10, fill=tk.BOTH,  side=tk.LEFT)
boton3 = ttk.Button(ventana1, text="Administracion de inventario", style="Accent.TButton")
boton3.pack(pady=10, padx=10, fill=tk.BOTH, side=tk.LEFT)




# Mostrar la ventana
ventana1.mainloop()
