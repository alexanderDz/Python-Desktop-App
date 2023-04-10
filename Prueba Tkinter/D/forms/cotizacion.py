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
    utl.centrar_ventana(ventana_coti,1050,600)
    ventana_coti.wm_attributes('-topmost', False)


    frame_datos = tk.Frame(ventana_coti, bd=0, width=100, height=100, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
    frame_datos.grid(row=0, column=0, padx=0, pady=0)


    ttk.Label(frame_datos, text="Fecha").grid(column=2, row=0, padx=10, pady=5)

    fechaContr = DateEntry(frame_datos, width=12, background="#217346",
                           foreground='white', borderwidth=2)
    fechaContr.grid(column=4, row=0, padx=10, pady=10)

    ttk.Label(frame_datos, text="Nombre").grid(column=0, row=1, padx=10, pady=2)
    ttk.Label(frame_datos, text="Identificacion (CC/NIT)").grid(column=0, row=2, padx=10, pady=2)
    ttk.Label(frame_datos, text="Telefono").grid(column=2, row=1, padx=10, pady=2)
    ttk.Label(frame_datos, text="Direccion").grid(column=0, row=3, padx=10, pady=2)
    ttk.Label(frame_datos, text="Ciudad").grid(column=2, row=2, padx=10, pady=2)
    ttk.Label(frame_datos, text="Placa").grid(column=0, row=6, padx=10, pady=2)
    ttk.Label(frame_datos, text="Modelo").grid(column=2, row=3, padx=10, pady=2)

    # Entradas de texto
    nombreCot = tk.StringVar()
    identificacion = tk.StringVar()
    telefono = tk.StringVar()
    direccion = tk.StringVar()
    ciudad = tk.StringVar()
    placa = tk.StringVar()
    modelo = tk.StringVar()

    ttk.Entry(frame_datos, textvariable=nombreCot).grid(column=1, row=1, padx=10, pady=2)
    ttk.Entry(frame_datos, textvariable=identificacion).grid(column=1, row=2, padx=10, pady=2)
    ttk.Entry(frame_datos, textvariable=telefono).grid(column=4, row=1, padx=10, pady=2)
    ttk.Entry(frame_datos, textvariable=direccion).grid(column=1, row=3, padx=10, pady=2)
    ttk.Entry(frame_datos, textvariable=ciudad).grid(column=4, row=2, padx=10, pady=2)
    ttk.Entry(frame_datos, textvariable=placa).grid(column=1, row=6, padx=10, pady=2)
    ttk.Entry(frame_datos, textvariable=modelo).grid(column=4, row=3, padx=10, pady=2)


    ttk.Button(frame_datos, text="Guardar Cliente", style="Accent.TButton").grid(column=4, row=9, padx=5, pady=5)

    frame_prod = tk.Frame(ventana_coti, bd=0, width=100, height=165, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
    frame_prod.grid(row=0, column=1, padx=0, pady=0, sticky='nsew')
    ttk.Label(frame_datos, text="Información del cliente").grid(column=0, row=0, padx=10, pady=2)

    ttk.Label(frame_prod, text="Empleados").grid(column=0, row=0, padx=10, pady=2)
    ttk.Label(frame_prod, text="Area").grid(column=1, row=0, padx=10, pady=2)

#################################################################################################

    ##Agregar empleado
    def add_emp(event=None):
        item = lista_empleados.get().strip()
        if item:
            items.append(item)
            listbox.insert(tk.END, item)

    empleados = ["Carlos", "Jose", "Ramiro", "Diego"]

    items = []

    # Crear la entrada de lista
    lista_empleados = ttk.Combobox(frame_prod, values=empleados)
    lista_empleados.grid(column=0, row=1, padx=15, pady=2)

    # Crear el botón para añadir elementos
    button1 = ttk.Button(frame_prod, text="Añadir empleado", style="Accent.TButton", command=add_emp)
    button1.grid(column=0, row=2, padx=15, pady=2)
    # Crear la lista de elementos
    listbox = tk.Listbox(frame_prod, height=5)
    listbox.grid(column=0, row=3, padx=15, pady=2)

    # Configurar el botón y la entrada de lista
    lista_empleados.bind("<Return>", add_emp)
    # button.bind("<Button-1>", add_item)

################################################################################################

    ##Agregar empleado
    def add(event=None):
        item1 = lista_areas.get().strip()
        if item1:
            items1.append(item1)
            listbox1.insert(tk.END, item1)

    area = ["Carlos", "Jose", "Ramiro", "Diego"]

    items1 = []

    # Crear la entrada de lista
    lista_areas = ttk.Combobox(frame_prod, values=area)
    lista_areas.grid(column=1, row=1, padx=15, pady=2)

    # Crear el botón para añadir elementos
    button2 = ttk.Button(frame_prod, text="Añadir area", style="Accent.TButton", command=add)
    button2.grid(column=1, row=2, padx=15, pady=2)
    # Crear la lista de elementos
    listbox1 = tk.Listbox(frame_prod, height=5)
    listbox1.grid(column=1, row=3, padx=15, pady=2)

    # Configurar el botón y la entrada de lista
    lista_areas.bind("<Return>", add)
    #button.bind("<Button-1>", add_item)

    ttk.Label(frame_prod, text="").grid(column=0, row=4, padx=10, pady=2)
    ttk.Label(frame_prod, text="").grid(column=1, row=4, padx=10, pady=2)

    ttk.Label(frame_prod, text="Diagnostico").grid(column=0, row=5, padx=10, pady=2)
    diagnostico = tk.StringVar()

    ttk.Entry(frame_prod, textvariable=diagnostico).grid(column=1, row=5, padx=10, pady=2)

#################################################################################################

    frame_ser = tk.Frame(ventana_coti, bd=0, width=100, height=165, relief=tk.SOLID, padx=10, pady=10, bg='#fcfcfc')
    frame_ser.grid(row=1, column=0, columnspan=2, padx=0, pady=0, sticky='nsew')


    table = ttk.Treeview(frame_ser, columns=("col1", "col2", "col3"), height=5)
    table.grid(column=0, row=17, padx=10, pady=2)
    # Configurar las columnas
    table.column("#0", width=0, stretch=tk.NO)
    table.column("col1", width=50, anchor=tk.CENTER)
    table.column("col2", width=125, anchor=tk.CENTER)
    table.column("col3", width=125, anchor=tk.CENTER)

    # Crear las cabeceras de columna
    table.heading("#0", text="", anchor=tk.CENTER)
    table.heading("col1", text="ID", anchor=tk.CENTER)
    table.heading("col2", text="Repuesto", anchor=tk.CENTER)
    table.heading("col3", text="Precio", anchor=tk.CENTER)

    # Función para agregar una fila a la tabla
    def add_row():
        # Obtener el valor de la entrada de combobox
        val2 = lista_areas.get()

        # Insertar una nueva fila en la tabla con el valor obtenido en la segunda columna
        table.insert("", tk.END, text=f"Fila {table.index('') + 1}", values=("", val2, ""))

        # Limpiar la entrada de combobox
        lista_areas.set("")

    ttk.Label(frame_ser, text="Agrega los repuestos").grid(column=0, row=0, padx=10, pady=2)

    # Crear la entrada de combobox
    repuestos = ["Frenos", "bombombunes", "leche", "pan de yuca"]
    lista_areas = ttk.Combobox(frame_ser, values=repuestos)
    lista_areas.grid(column=0, row=1, padx=10, pady=2)

    # Crear el botón para agregar filas
    button = ttk.Button(frame_ser, text="Agregar", style="Accent.TButton", command=add_row)
    button.grid(column=0, row=2, padx=10, pady=2)

    # Mostrar la tabla
    #table.grid(expand=tk.YES, fill=tk.BOTH)
    table.grid(column=0, row=3,  sticky="nsew")

    ##############################################################################

    table2 = ttk.Treeview(frame_ser, columns=("col1", "col2", "col3"), height=5)
    table2.grid(column=1, row=0, padx=10, pady=2)
    # Configurar las columnas
    table2.column("#0", width=0, stretch=tk.NO)
    table2.column("col1", width=50, anchor=tk.CENTER)
    table2.column("col2", width=125, anchor=tk.CENTER)
    table2.column("col3", width=125, anchor=tk.CENTER)

    # Crear las cabeceras de columna
    table2.heading("#0", text="", anchor=tk.CENTER)
    table2.heading("col1", text="ID", anchor=tk.CENTER)
    table2.heading("col2", text="Servicio", anchor=tk.CENTER)
    table2.heading("col3", text="Precio", anchor=tk.CENTER)

    # Función para agregar una fila a la tabla
    def add_row2():
        # Obtener el valor de la entrada de combobox
        val3 = lista_areas2.get()

        # Insertar una nueva fila en la tabla con el valor obtenido en la segunda columna
        table2.insert("", tk.END, text=f"Fila {table2.index('') + 1}", values=("", val3, ""))

        # Limpiar la entrada de combobox
        lista_areas2.set("")

    ttk.Label(frame_ser, text="Agrega los servicios").grid(column=1, row=0, padx=10, pady=2)


    # Crear la entrada de combobox
    repuestos = ["Frenos", "bombombunes", "leche", "pan de yuca"]
    lista_areas2 = ttk.Combobox(frame_ser, values=repuestos)
    lista_areas2.grid(column=1, row=1, padx=10, pady=2)

    # Crear el botón para agregar filas
    button = ttk.Button(frame_ser, text="Agregar", style="Accent.TButton", command=add_row2)
    button.grid(column=1, row=2, padx=10, pady=2)

    # Mostrar la tabla
    # table.grid(expand=tk.YES, fill=tk.BOTH)
    table2.grid(column=1, row=3, sticky="nsew")

    ttk.Label(frame_ser, text="Estado").grid(column=2, row=1, padx=10, pady=2)

    estados = ["En proceso", "Terminada"]

    estado = ttk.Combobox(frame_ser, values=estados)
    estado.current(0)
    estado.grid(column=2, row=2, padx=5, pady=10, sticky="ew")

    button = ttk.Button(frame_ser, text="Guardar cotizacion", style="Accent.TButton")
    button.grid(column=2, row=3, padx=10, pady=2)

    return ventana_coti.mainloop()