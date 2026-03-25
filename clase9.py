#trabajar con archivos/directorios del os
import os
import subprocess


print(os.listdir('/Users/santi'))  # -> Obtener lista de carpetas y archivos

print(os.getcwd())  # -> Obtener el directorio de ejecución

print(os.path.exists('/Users/santi'))  # -> Booleano que muestra si existe la ruta



os.mkdir('/Users/santi/webmetadata/Curso_lunes')  # -> Crear directorio

os.remove('/Users/santi/webmetadata/Curso_lunes/data.txt')  # -> Eliminar archivo

os.rmdir('/Users/santi/webmetadata/Curso_lunes')  # -> Eliminar carpeta vacía

os.rename('/Users/santi/webmetadata/datos.txt', '/Users/santi/webmetadata/resumen.txt')  # -> Renombrar archivo

os.system('clear')  # limpiar terminal
subprocess.run(["clear"])

import shutil

# print(shutil.copy('/Users/santi/webmetadata/resumen.txt', '/Users/santi/webmetadata/backup'))  # -> Copiar archivo

# print(shutil.move('/Users/santi/webmetadata/resumen.txt', '/Users/santi/webmetadata/backup/'))  # -> Mover archivo

# shutil.rmtree('/Users/santi/webmetadata/backup')  # -> Eliminar carpeta con archivos/subcarpetas

import subprocess

subprocess.run(['mkdir', 'carpeta_curso_python'], shell=True)
# Ejecuta el comando "mkdir carpeta_curso_python" en la terminal → crea una carpeta
shell=True #permite ejecutar comandos como si los escribieras en la terminal (más flexible, pero menos seguro)

print("Carpeta creada")
# Muestra un mensaje en pantalla indicando que la carpeta fue creada

p = subprocess.run('hostname', capture_output=True, encoding='cp850')
# Ejecuta el comando "hostname" → devuelve el nombre de la máquina
capture_output=True #guarda la salida en p.stdout en vez de imprimirla directamente
encoding='cp850' #es típico de Windows (en Mac usar 'utf-8')

# print(p.stdout)
# Imprime el nombre de la máquina que devolvió el comando

p = subprocess.run(
    ['python3', '--version'],   # comando que se ejecuta → equivalente a "python3 --version" en terminal
    capture_output=True,        # guarda la salida del comando en vez de mostrarla directamente
    encoding='utf-8'            # convierte la salida a texto legible (en Mac usar utf-8)
)

print(p.stdout)  # imprime la versión de Python



import os
import sys

def buscar_archivos(ruta, extension):
    # Asegurarse de que la extensión empiece con punto
    if not extension.startswith("."):
        extension = "." + extension

    # Verificar que la carpeta existe
    if not os.path.exists(ruta):
        print(f"Error: La carpeta '{ruta}' no existe.")
        return

    if not os.path.isdir(ruta):
        print(f"Error: '{ruta}' no es una carpeta.")
        return

    # Buscar archivos con la extensión dada
    archivos_encontrados = [
        archivo
        for archivo in os.listdir(ruta)
        if os.path.isfile(os.path.join(ruta, archivo)) and archivo.endswith(extension)
    ]

    # Mostrar resultados
    print(f"Archivos con extensión {extension}:")
    if archivos_encontrados:
        for archivo in archivos_encontrados:
            print(f"  - {archivo}")
    else:
        print("  (ninguno encontrado)")


# --- Punto de entrada ---
if len(sys.argv) != 3:
    print("Uso: python buscar_archivos.py <ruta_carpeta> <extensión>")
    print('Ejemplo: python buscar_archivos.py "C:\\ruta\\carpeta" .exe')
    sys.exit(1)

ruta_carpeta = sys.argv[1]
extension_buscada = sys.argv[2]

buscar_archivos(ruta_carpeta, extension_buscada)