import mysql.connector
from fun_sql2 import *

cnx = conectarDB()

#id = nueva_Area(cnx,"MECANICA", 0.35)
id = actualizar_Area(cnx,0.05,"MECANICA")
print(id)

cnx.close()
