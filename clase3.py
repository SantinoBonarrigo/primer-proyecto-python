#funciones de orden superior


def aplicar_operacion(lista, funcion):
    resultados = []
    
    for numero in lista:
        resultado = funcion(numero)
        resultados.append(resultado)
    
    # acá recién devolvés
    return resultados





def cuadrado(num):
    return num * num

print(aplicar_operacion([1, 2, 3], cuadrado))




numeros = [1, 2, 3, 4, 5, 6, 7, 8]

def filtrar_lista(lista,funcion_condicion):
  result=[]
  for numero in lista:
     if funcion_condicion(numero):

        result.append(numero)
  return  result
      






def es_par(num):
 return  num % 2 == 0
    
    # --- USO DE LA FUNCIÓN ---


result2 = filtrar_lista(numeros, es_par)

print(result2)




#excepciones
# numero=input("ingrese un numero: ")

# try:
#  resultado= int(numero) ** 3
#  print(resultado)

# except ValueError:
#    print("debe ingresar un numero")


# try:
#    int([2,3,5])

# except TypeError:
#    print("el argumento no es permitido")


# tratar distintas excepcones en un mismo try 
# try:
   
#    resultado= int("a")+10
#    print(resultado)

# except (ValueError,TypeError):
#    print("hubo un error al realizar la operacion")

# else: 
#    print("Operacion excitosa")



cliente= {"nombre": "emilia", "edad": 23}

try:
  print(cliente["direccion"])

except KeyError:
   
   print("no existe esa clave")


#excpeciones genericas

# try:
   
#    int("2a")
   
# except Exception:
   
#    "hubo un error"




try:
   
  int("2a")
   
except:
   
  print("hubo un error")




#practico calculadora



while True:
    try:
        numero = float(input("ingrese un numero: "))
        break
    except ValueError:
        print("entrada inválida, intente de nuevo")

while True:
    try:
        numero2 = float(input("ingrese otro numero: "))
        break
    except ValueError:
        print("entrada inválida, intente de nuevo")


suma = numero + numero2
resta = numero - numero2
multiplicacion = numero * numero2

print("suma:", suma)
print("resta:", resta)
print("multiplicación:", multiplicacion)

try:
    division = numero / numero2
    print("división:", division)
except ZeroDivisionError:
    print("no se puede dividir por 0")
   
   
   




print("suma:", suma)
print("resta:", resta)
print("multiplicación:", multiplicacion)


