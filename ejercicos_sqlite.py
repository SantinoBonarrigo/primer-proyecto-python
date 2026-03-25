import sqlite3

conn = sqlite3.connect("productos.sqlite")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY,
    nombre TEXT,
    precio NUMERIC
)
""")

productos = (("Teclado",25), ("Mouse",18), ("Monitor",300), ("Parlantes",100))

for producto in productos:
    cursor.execute(
        "INSERT INTO productos (nombre, precio) VALUES (?, ?)",
        producto
    )

conn.commit()


while True:
    print("1 - Agregar")
    print("2 - Ver")
    print("3 - Salir")

    opcion1 = input("elige un numero: ")

    if opcion1 == "1":

        id_producto = int(input("marque el id: "))
        nombre = input("marque el nombre del producto: ")
        precio = int(input("marque el precio del producto:"))
    
        try:
            cursor.execute(
                "INSERT INTO productos (id, nombre, precio) VALUES (?, ?, ?)",
                (id_producto, nombre, precio)
            )
            conn.commit()
            print("Producto agregado correctamente")

        except sqlite3.IntegrityError:
            print("❌ Error: ese ID ya existe")

    
    elif opcion1 == "2":
        try:
            cursor.execute("SELECT * FROM productos")
            productos_consultas = cursor.fetchall()

            for id_producto, nombre, precio in productos_consultas:
                print(f"id: {id_producto} | producto: {nombre} | precio: {precio}")

        except sqlite3.OperationalError:
            print("error al obtener los registros")


    elif opcion1 == "3":
        break

    else:
        print("Opción inválida")


conn.close()