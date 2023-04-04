import mysql.connector

#LISTADO DE QUERIES PARA LAS FUNCIONES DE LAS VENTANAS

#VENTANA AREA:
nueva_Area = "INSERT INTO `multiservicios`.`area` (`Nombre_Area`, `Porcentaje_comision`) VALUES (%s, %s)"
def actualizar_Area(Porcentaje_comision, Nombre_Area):
    return "UPDATE `multiservicios`.`area` SET `Porcentaje_comision` = %s WHERE (`Nombre_Area` = %s)"

#FUNCION PARA REALIZAR LA CONEXION DE LA BASE DE DATOS------------------------------------------------------------
def conectarDB():
    try:
        cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mysql12345",
            database="multiservicios"
        )
    except mysql.connector.Error as err:
        print(f"Error al conectarse a la base de datos: {err}")
        return None

    return cnx
#FUNCION PARA EJECUTAR LAS QUERIES ------------------------------------------------------------
def ejecutar_query(cnx, query, params=None, query_type="SELECT"):
    try:
        cursor = cnx.cursor()
        cursor.execute(query, params)

        if query_type == "SELECT":
            result = cursor.fetchall()
            cursor.close()
            return result
        elif query_type in ["INSERT", "UPDATE", "DELETE"]:
            cnx.commit()
            return cursor.lastrowid
        else:
            raise ValueError("Tipo de consulta SQL no válido")

    except mysql.connector.Error as err:
        print(f"Error al ejecutar la consulta: {err}")
        cnx.rollback()
        return None