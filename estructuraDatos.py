"""
Estructura de datos
Listas
"""

marcas_cigarros = ["Malboro", "Camel", "Pall Mall", "Lucky Strike", "Chesterfield"]
print(marcas_cigarros)
# agregar elemento
marcas_cigarros.append("Link")
print(marcas_cigarros)
# eliminar elementos
marcas_cigarros.remove("Camel")
print(marcas_cigarros)

print(marcas_cigarros[1])
marcas_cigarros[1] = "Cristal" #Actualizacion
print(marcas_cigarros)

marcas_cigarros.sort() #Ordenacion 
print(marcas_cigarros)

"""
Tuplas de datos
"""

my_tuple = ("Angel", "Rubio", "JR", "25")
print(my_tuple)
print(my_tuple[1])
print(my_tuple[2])

my_tuple = tuple(sorted(my_tuple)) #Ordenacion
print(my_tuple)

"""
Sets
"""
print("----------- Seccion de Sets -----------")
my_set = {"Angel", "Rubio", "JR", "25"}
print(my_set)
my_set.add("Hola que hace") #Insertar elementos 
my_set.add("Hola que hace")
print(my_set)
my_set.remove("JR") # Eliminacion
print(my_set)

my_set = set(sorted(my_set)) #No se puede ordenar
print(type(my_set))

"""
Diccionarios
"""
print("----------- Seccion de diccionarios -----------")
my_dict: dict = {
    "nombre": "Angel", 
    "apellido": "Rubio", 
    "edad": 25
}
my_dict ["email"] = "angel.rubio@example.com" #Insercion
print(my_dict)
del my_dict["apellido"] #Eliminacion
print(my_dict["nombre"]) #Acceso
my_dict["edad"] = 26 #Actualizacion
print(my_dict)
my_dict = dict(sorted(my_dict.items()))
print(my_dict)
print(type(my_dict))


"""
Ejercicio 
"""
print("----------- Seccion del ejercicio -----------")