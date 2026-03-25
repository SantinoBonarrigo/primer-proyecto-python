#tipado dinamico

#int, enteros, float, con decimal, stings, boolean, complex, none 
numero = 5
# print(type(numero))
numero = "5"
# print(type(numero))

#asignaciones multiples

# numero1= None
# print(numero1 is None)

# a, b, c = 20, "python", -3.14


# print(b)

# resultado = None

# numero = 10

# if numero > 5 :
#     resultado = numero **2


# if resultado is not None:
#     print("el resultado es: ", resultado)

# else: 

#     print("no se pudo calcular un resultado")


# Casting

# Implicita

num1= 1
num2= 2.5

num1= num1 + num2

# print(num1) # aca num1 paso de de int a float


#explicita

num1= 10.5

num1= int(num1)

# print(num1) # aca pase de float a int




#colecciones


#LISTAS []

numeros = [20, 5, -5]

varios =[20, True, "Servidor", ["Php", "JS"]] 

numeros.append(100) # aca va al ultimo
# print(numeros)

numeros.insert(2,4) # primeor el indice desp el numero

numeros[0] = 200

# print(numeros)

del  numeros[1]

# print(numeros)


# print(numeros[-1])


string= varios[2] + " Encendido"

# print(string)

total = numeros + varios # suma de listas

# print(total)

#tuplas(). inmutables

articulos = ("montior", "heladera", 5)

# print(articulos[1])

variosNum=(20)


print(type(variosNum))

variosNum1=(20,) #le agrego la coma la final para que sea una tupla 

print(type(variosNum1))





#litas indexacion


bichoszoo= ["gato","Perro", "Gallo", "Caballo", "Tiburon", "Pajaro"]


#slices

# print(bichoszoo[2:5])

# print(bichoszoo[0:5:2])
# print(bichoszoo[2:])


#diccionarios


cliente_1={"nombre":"Pedro","edad":40, (10,20):True, "nombre":"Sofia"}


print(cliente_1)

#desempacetamiento

numeors = (10,20,30)

num1, num2, num3 = numeors


print(num2)



#is(identidad) #sirve pregunta laboral


num1=10

num2=10

#print(num1 is num2)


#num 1 es num 2 pq tienen el mismo id del objeto y la misma expresion si le asignas la misma expresion el identificador es el mismo


#if


#operadores ternarios

esta_activo= False

estado= "servidr encendido" if esta_activo else "servidor apagado"





 



