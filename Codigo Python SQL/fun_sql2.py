import mysql.connector

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