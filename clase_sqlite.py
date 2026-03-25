import sqlite3




conn = sqlite3.connect("contabilidad.sqlite")



cursor= conn.cursor()

#crear una tabla

# cursor.execute("CREATE TABLE personas (nombre TEXT, edad NUMERIC)")


nombre =  "julian"
edad = 27
#prevenir inyeccion codigo sql

#nombre =  "julian; Delete from personas"

cursor.execute("INSERT INTO personas VALUES(?,?)",(nombre,edad))



personas = (("ana", 50),("marcelo", 48), ("Emilia", 34))

for nombre, edad in personas:
    cursor.execute("INSERT INTO personas VALUES(?,?)", (nombre,edad))
    


#listado

# cursor.execute("SELECT * FROM personas ")
# personasConsulta = cursor.fetchall()


# for nombre, edad in personasConsulta:
#     print(f"nombre: {nombre} - edad: {edad}")


# print(cursor.fetchone())


try:
 cursor.execute("SELECT FROM personas")

except sqlite3.OperationalError:
   print("error al obtener los registros")



conn.close()

