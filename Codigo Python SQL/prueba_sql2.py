import mysql.connector
import fun_sql2

cnx = fun_sql2.conectarDB()

if cnx is not None:
    # Ejecutar una consulta INSERT
    query = "INSERT INTO `multiservicios`.`area` (`Area_ID`, `Nombre_Area`, `Porcentaje_comision`) VALUES (%s, %s, %s)"
    params = (1,"FRENOS Y SUSPENSION",0.15)
    last_id = fun_sql2.ejecutar_query(cnx, query, params, "INSERT")
    print(f"Último ID insertado: {last_id}")

    # Cerrar la conexión
    cnx.close()
