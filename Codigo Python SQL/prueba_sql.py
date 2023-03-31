import mysql.connector
import tkinter as tk

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysql12345",
            database="test_2"
        )
        return conexion
    except mysql.connector.Error as error:
        print("Error de conexión: {}".format(error))

def crear_ventana():
    ventana = tk.Tk()

    etiqueta_nombre = tk.Label(ventana, text="Nombre:")
    etiqueta_nombre.pack()

    entrada_nombre = tk.Entry(ventana)
    entrada_nombre.pack()

    boton_insertar = tk.Button(
        ventana,
        text="Insertar",
        command=lambda: insertar_datos(entrada_nombre.get())
    )
    boton_insertar.pack()

    return ventana

def insertar_datos(nombre):
    conexion = conectar()
    cursor = conexion.cursor()

    sql = "INSERT INTO usuarios (nombre) VALUES (%s)"
    valores = (nombre,)

    cursor.execute(sql, valores)
    conexion.commit()

    cursor.close()
    conexion.close()

ventana = crear_ventana()
ventana.mainloop()        