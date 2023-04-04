import mysql.connector
import funSQL

cnx = funSQL.conectarDB()
params = ("FRENOS Y SUSPENSION",0.15)
query = "INSERT INTO `multiservicios`.`area` (`Nombre_Area`, `Porcentaje_comision`) VALUES (%s, %s)"
id = funSQL.ejecutar_query(cnx,query,params,"INSERT")
print(id)
cnx.close()