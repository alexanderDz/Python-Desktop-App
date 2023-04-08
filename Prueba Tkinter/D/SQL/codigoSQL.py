import mysql.connector
from funSQL import *

cnx = conectarDB()
id = actualizar_Area(cnx,0.5,"FRENOS Y SUSPENSION")
print(id)
cnx.close()