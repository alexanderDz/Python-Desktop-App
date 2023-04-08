from fun_sql2 import *

cnx = conectarDB()
Nombre_Area = "MECANICA"
id_actual = "SELECT Area_ID FROM `multiservicios`.`area` WHERE Nombre_Area = %s"
busqueda = ejecutar_query(cnx,id_actual,(Nombre_Area,),"SELECT")
area_id = busqueda[0][0]
print(busqueda)
print(area_id)
cnx.close()