import mysql.connector

# Función para establecer la conexión a la base de datos
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

# Función para ejecutar una consulta SQL en la base de datos
def ejecutar_query(query, params=None, query_type="SELECT"):
    cnx = conectarDB()
    if not cnx:
        return None

    try:
        cursor = cnx.cursor()
        cursor.execute(query, params)

        if query_type == "SELECT":
            result = cursor.fetchall()
            cursor.close()
            cnx.commit()
            cnx.close()
            return result
        elif query_type in ["INSERT", "UPDATE", "DELETE"]:
            cnx.commit()
            cnx.close()
            return cursor.lastrowid
        else:
            raise ValueError("Tipo de consulta SQL no válido")

    except mysql.connector.Error as err:
        print(f"Error al ejecutar la consulta: {err}")
        cnx.rollback()
        cnx.close()
        return None