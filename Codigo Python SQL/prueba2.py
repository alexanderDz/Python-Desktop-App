import mysql.connector
import funSQL

funSQL.conectarDB()
params = (1,"FRENOS Y SUSPENSION",0.15)
query = "INSERT INTO `multiservicios`.`area` (`Area_ID`, `Nombre_Area`, `Porcentaje_comision`) VALUES (%s, %s, %s)"
id = funSQL.ejecutar_query(query,params,"INSERT")
print(id)