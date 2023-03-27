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

boton1 = ttk.Button(ventana1, text="Orden de trabajo", style="Accent.TButton", width=25)
boton1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

boton2 = ttk.Button(ventana1, text="Nomina semanal", style="Accent.TButton", width=25)
boton2.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")

boton3 = ttk.Button(ventana1, text="Administracion de inventario", style="Accent.TButton", width=25)
boton3.grid(row=0, column=2, padx=5, pady=10, sticky="nsew")

boton4 = ttk.Button(ventana1, text="Consultas", style="Accent.TButton", width=25)
boton4.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")


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