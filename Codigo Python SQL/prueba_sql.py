import mysql.connector
import tkinter as tk

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysql12345",
            database="multiservicios"
        )
        return conexion
    except mysql.connector.Error as error:
        print("Error de conexión: {}".format(error))

def consultar_datos():
    conexion = conectar()
    cursor = conexion.cursor()

    # Realizar la consulta
    query = ("INSERT INTO `multiservicios`.`area` (`Area_ID`, `Nombre_Area`, `Porcentaje_comision`) VALUES ('1', 'MECANICA', '0.15')")

    cursor.execute(query)
    conexion.commit()

    if cursor.rowcount == 1:
        print("La inserción fue exitosa.")
    else:
        print("La inserción falló.")


    query = ("SELECT * FROM `multiservicios`.`area`")
    cursor.execute(query)

# Imprimir los resultados de la consulta
    print("Tabla actualizada:")
    for fila in cursor:
        print(fila)
    
    cursor.close()
    conexion.close()


conectar()
consultar_datos()
