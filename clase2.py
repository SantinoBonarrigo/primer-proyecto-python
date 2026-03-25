def promedio_variable(*args):
    suma = 0
    cantidad = 0

    for numero in args:
        if numero > 0:
            suma = suma + numero
            cantidad = cantidad + 1

    if cantidad == 0:
        return 0

    return suma / cantidad

print(promedio_variable(2, -4, 6))
