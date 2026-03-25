import pymysql

conn = pymysql.connect(
    host='localhost',
    user='fabiom',
    passwd='qwerty1234'
)

cursor = conn.cursor()

# Mostrar las bases del motor
cursor.execute('SHOW DATABASES')
lista_bd = cursor.fetchall()

for database in lista_bd:
    print(database)

conn.close()