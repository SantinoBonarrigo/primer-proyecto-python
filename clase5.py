#trabajar con archivos externos

#open(archivo,modo)
#archivo:  ruta relativa(el arch s eencuentra en el propio directorio, solo el nombre del archivo)
           # ruta absoluta( cuando el file no esta en la carpeta donde trbaajo. comenzando de la raiz )
#modo r: read. w: write, reemplaza a: append actualizar o escribir al final.

# f = open("config.txt") # relativo



# print(f.read())
# f.close()



# try:
#  f = open("configuracion.txt") # relativo


#  print(f.read())
#  f.close()

# except FileNotFoundError:
#  print("no se encontro el archivo")



# try:
#  f = open("config.txt") # relativo
#  lineas= f.readlines()
#  for linea in lineas:
#    print(linea)


# except FileNotFoundError:
#  print("no se encontro el archivo")

#




 
   # with

# with open("config.txt", "w") as f:
#     f.write("Python avanzado\n miercoles 17.hs")



#append(a)

f= open("config.txt", "a")
f.write("\n utilizaos python" )
f.write("\n ultima version" )
f.close()


#append(a) con with


with open("config.txt","a") as f:
    f.write("\nclase 5")



#ejercicio

# personas = {"Juan":20, "Romina":32, "Tamara":25, "Melanie":19}
# personaslista=[]


# for persona in personas:
#    edad= personas[persona]
#    print(edad)
#    nombres= persona.lower()
#    print(nombres)
#    personaslista.append(f"{nombres}-{edad}")

# with open("listapersona.txt", "w") as f: 

#     texto = "\n".join(personaslista)
#     f.write(texto)

personass = {"Juan":20, "Romina":32, "Tamara":25, "Melanie":19}

with open("listapersona.txt", "w") as f: 
    for nombre, edad in personass.items():
        f.write(f"{nombre.lower()}-{edad}\n")


