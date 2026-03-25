# Pedido (request) - cliente (Navegador, Python)
# Respuesta (response) - Servidor
# JSON (Formato de intercambio de datos)

# Arquitectura RestFull (recursos)
# https://universidad.com/alumnos
# https://universidad.com/materias
# https://universidad.com/profesores

# GET /alumno (Obtener info del recurso) - 200
# POST /materia (Grabar un nuevo recurso) - 201
# PUT /materia/10 (Modificar un recurso)- 204
# DELETE /materia/100 (Eliminar un recurso) - 204


import requests  # Importamos la librería para hacer requests HTTP (GET, POST, etc.)

# -----------------------------
# Cargar un dato en el servidor
# -----------------------------

# Datos que queremos enviar al backend
nombre = 'Mateo'
cursos = 4

# Hacemos una petición POST (sirve para CREAR datos en el servidor)
# URL: endpoint donde escucha tu backend
# json: se convierte automáticamente a JSON y se envía en el body
r = requests.post(
    'http://localhost:7001/student',
    json={
        "name": nombre,     # clave "name" con valor de la variable nombre
        "courses": cursos   # clave "courses" con valor de la variable cursos
    }
)

# r es la respuesta del servidor (response)

# Código de estado HTTP:
# 200 = OK
# 201 = creado correctamente
# 400 = error del cliente
# 500 = error del servidor
print("Código:", r.status_code)

# r.json() convierte la respuesta del servidor (que viene en JSON)
# a un diccionario de Python
print("Contenido:", r.json())


# -----------------------------
# IDEAS CLAVE (MUY IMPORTANTE)
# -----------------------------

# - requests.post() → enviar datos (crear)
# - requests.get() → obtener datos
# - json={} → lo manda como JSON automáticamente
# - r.status_code → te dice si salió bien o mal
# - r.json() → convierte la respuesta a algo usable en Python

# Pensalo así:
# Tu Python = cliente
# localhost:7001 = servidor (tu API)
# POST = "che, guardá esto"