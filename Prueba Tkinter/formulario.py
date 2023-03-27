import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi formulario")

# Crear un marco para el formulario
formulario = ttk.Frame(ventana, padding="20 20 20 20")
formulario.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
formulario.columnconfigure(0, weight=1)
formulario.rowconfigure(0, weight=1)

# Crear etiquetas y campos de entrada para el formulario
etiqueta_nombre = ttk.Label(formulario, text="Nombre:")
etiqueta_nombre.grid(column=1, row=1, sticky=tk.W)

campo_nombre = ttk.Entry(formulario)
campo_nombre.grid(column=2, row=1, sticky=(tk.W, tk.E))

etiqueta_correo = ttk.Label(formulario, text="Correo electrónico:")
etiqueta_correo.grid(column=1, row=2, sticky=tk.W)

campo_correo = ttk.Entry(formulario)
campo_correo.grid(column=2, row=2, sticky=(tk.W, tk.E))

# Crear un botón para enviar el formulario
boton_enviar = ttk.Button(formulario, text="Enviar")
boton_enviar.grid(column=2, row=3, sticky=tk.E)

# Agregar espaciado al formulario
for child in formulario.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Mostrar la ventana
ventana.mainloop()
