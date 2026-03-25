## POO
# # los nombres de las clases con mayúscula, buena práctica

# class Automovil:
#     # constructor
#     def __init__(self, marca, modelo, velocidad_max):
#         self.__marca = marca
#         self.__modelo = modelo
#         self.__velocidad = 0
#         self.__velocidad_maxima = velocidad_max
#         self.__color = None  # inicializamos color

#     # métodos
#     def acelerar(self, kms):
#         velocidad_aux = self.__velocidad + kms
#         if velocidad_aux <= self.__velocidad_maxima:
#             self.__velocidad = velocidad_aux
#         else:
#             self.__velocidad = self.__velocidad_maxima

#     # Métodos get / set
#     def get_velocidad(self):
#         return self.__velocidad

#     def set_color(self, color):
#         self.__color = color

#     def get_color(self):
#         return self.__color


# class Persona:
#     def __init__(self, nombre, apellido):
#         self.nombre = nombre
#         self.apellido = apellido


# # Crear un objeto (instanciar una clase)
# auto_1 = Automovil('Ford', 'Ka', 170)

# auto_1.acelerar(100)
# auto_1.acelerar(50)
# print(auto_1.get_velocidad())

# auto_1.acelerar(150)
# print(auto_1.get_velocidad())

# auto_2 = Automovil("Chevrolet", "Cruze", 190)
# persona_a = Persona("Santino", "Bonarrigo")




# class Persona:
#     def __init__(self,nombre,edad):
#         self.__nombre = nombre
#         self.__edad = edad

#     def cumpleaños(self):
#         self.__edad += 1

    
#     def get_nombre(self):
#         return self.__nombre

        
    
#     def get_edad(self):
#             return self.__edad




# p = Persona("Juan", 21)
# p.cumpleaños()
# print(f"{p.get_nombre()} tiene {p.get_edad()} Años")



#herencia

# class Vehiculo:  #superclass
#     def __init__(self, marca, modelo):
#         self.__marca = marca
#         self.__color= "blanco"
#         self.__modelo = modelo



#     def get_marcaModelo(self):
#         return f"{self.__marca} - {self.__modelo}"
    


    
    
    
#     def set_color(self,color):
#          self.__color= color
        
#     def get__color(self):
#         return self.__color
    

# class Automovil(Vehiculo): # subclase
#     def __init__(self, marca, modelo, cantpuertas):
#         super().__init__(marca, modelo)
#         self.__cantpuertas= cantpuertas


    
#     def get_cant_puertas(self):
#         return self.__cantpuertas
    

# auto3= Automovil("citroen","ds3", 5)
# auto3.set_color("azul")
# print(auto3.get_marcaModelo())
# print(auto3.get_cant_puertas())
# print(auto3.get__color())



class Persona:
    def __init__(self,nombre,apellido):
        self.__nombre = nombre
        self.__apellido = apellido
    

    def get_nombre(self):
        return self.__nombre

    
    def get_apellido(self):
        return self.__apellido
    
    def nombre_completo(self):
         return f"{self.__nombre}  {self.__apellido}"
    



class Estudiante(Persona):
    def __init__(self, nombre, apellido,edad,carrera):
        super().__init__(nombre, apellido)
        self.__edad= edad
        self.__carrera= carrera

    
    def get_carrera(self):
      return self.__carrera
    
    def get_edad(self):
      return self.__edad
    

    

e= Estudiante("santino", "Bonarrigo",25,"abogacia") 
print(f"{e.nombre_completo()} {e.get_edad()} {e.get_carrera()}")




        





