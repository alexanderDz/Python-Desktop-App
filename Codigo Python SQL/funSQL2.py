import mysql.connector

def conectarDB():
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

def ejecutar_query():
            

def nueva_area(area_id, nombre_area, porcentaje):
    conexion = conectarDB()
    cursor = conexion.cursor()

    # Realizar la consulta
    query = "INSERT INTO `multiservicios`.`area` (`Area_ID`, `Nombre_Area`, `Porcentaje_comision`) VALUES ('{}', '{}', '{}')".format(area_id,nombre_area,porcentaje)

    cursor.execute(query)

    conexion.commit()

def cerrarDB():
    cursor.close()
    conexion.close()