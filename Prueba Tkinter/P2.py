import tkinter as tk
from tkinter import ttk

ventana1 = tk.Tk()

# definir los botones principales
boton1 = ttk.Button(ventana1, text="Botón 1", width=25)
boton1.grid(row=0, column=0, padx=5, pady=10, sticky="nsew")

boton2 = ttk.Button(ventana1, text="Botón 2", width=25)
boton2.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

boton3 = ttk.Button(ventana1, text="Botón 3", width=25)
boton3.grid(row=0, column=1, padx=5, pady=10, sticky="nsew")

boton4 = ttk.Button(ventana1, text="Botón 4", width=25)
boton4.grid(row=1, column=1, padx=5, pady=10, sticky="nsew")

# definir el frame para los botones horizontales y verticales
frame = ttk.Frame(ventana1)
frame.grid(row=0, column=2, rowspan=2, padx=5, pady=10, sticky="nsew")

# definir los botones horizontales


# crear el nuevo frame para los botones adicionales
frame2 = ttk.Frame(ventana1)
frame2.grid(row=0, column=3, rowspan=2, padx=5, pady=10, sticky="nsew")

# crear los botones adicionales en el nuevo frame
boton5 = ttk.Button(frame2, text="Botón 9", width=25)
boton5.grid(row=0, column=0, pady=10, sticky="nsew")

boton6 = ttk.Button(frame2, text="Botón 10", width=25)
boton6.grid(row=1, column=0, pady=10, sticky="nsew")

boton7 = ttk.Button(frame2, text="Botón 11", width=25)
boton7.grid(row=2, column=0, pady=10, sticky="nsew")

boton8 = ttk.Button(frame2, text="Botón 12", width=25)
boton8.grid(row=3, column=0, pady=10, sticky="nsew")

boton9 = ttk.Button(frame2, text="Botón 13", width=25)
boton9.grid(row=4, column=0, pady=10, sticky="nsew")

boton10 = ttk.Button(frame2, text="Botón 14", width=25)
boton10.grid(row=5, column=0, pady=10, sticky="nsew")


ventana1.mainloop()