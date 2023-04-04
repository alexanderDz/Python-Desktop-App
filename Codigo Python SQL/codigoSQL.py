import mysql.connector
from funSQL import *

cnx = conectarDB()
params = ("FRENOS Y SUSPENSION",0.15)
id = ejecutar_query(cnx,nueva_Area,params,"INSERT")
print(id)
cnx.close()