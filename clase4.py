# paises = {
#     "ar": "Argentina",
#     "es": "España",
#     "us": "Estados Unidos",
#     "fr": "Francia"
# }

# while True:
#     busqueda = input("Ingrese código de país: ")

#     if busqueda == "salir":
#         print("Has salido del programa")
#         break

#     try:
#        print(paises[busqueda])
#     except KeyError:
#         print("El país no existe")


#TRABAJAR CON STR

# texto = "hola mundo!"
# print(texto[0])

# print(texto[0:4])


#caracteres especiales


#salto de linea 

# # texto= "hola\nsoy\nsantino"

# # print(texto.replace("\n", " ")). # para eliminar saltos de lineas 

# #split 

# lenguaje = " programando en Python "

# print(lenguaje.split()) # te convierte en lista  los stringss lo que esta escrito, si no pongo argumentos lo toma el espacio par aseprar


# frutas ="manzanas,peras,bananas"

# print(frutas.split(","))


# frutas ="manzanas-peras-bananas"

# print(frutas.split("-"))


# frutas ="manzanas-peras-bananas-sushi"

# print(frutas.split("-", 2))   # segundo argumento es max split


# #find 

# texto="hola mundo"

# print(texto.find("mundo")) # te retorna a partie de que caracter encuentra esa palabra si noexiste reotrna -1
# # find solo si exsite poscicion, pero si existe una porcion se usa el in para saber si esta el arg en la cadena




# print(texto.upper()) # texto en mayus
# print(texto.lower()) # texto en minuscula


# # otros meotdos: isecimal(). title() capitalize(),  title()


# msg= "vive la vida pq la vida es una mensaje"

# print(msg.count("vida"))



# #formar cadena de caracteres
# nombre= "santino"
# edad= 23
# mensaje = f"hola mi nombre es {nombre} tengo {edad} años"

# print(mensaje)




nombres = ["juan salvo", "henry courtney", "elizabeth bennet", "marge simpson"]
listanueva = []




for nombre in nombres:
    listanueva.append(nombre.title())
    
print(listanueva)


