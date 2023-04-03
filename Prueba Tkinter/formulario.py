cliente_id=0
def abrir_cliente():

    global cliente_id
    cliente_id += 1

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
    id_cliente = tk.StringVar(value=int(cliente_id))
    nombre = tk.StringVar()
    apellido = tk.StringVar()
    celular = tk.StringVar()
    correo = tk.StringVar()
    direccion = tk.StringVar()
    identifiaccion = tk.StringVar()
    
    ttk.Label(formulario, textvariable=id_cliente).grid(column=1, row=0, padx=5, pady=5)
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