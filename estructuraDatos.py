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

def agregar_contacto(nombre, telefono):
    if telefono.isdigit() and len(telefono) > 0 and len(telefono) < 12:
        agenda_contactos[nombre] = telefono
        print(agenda_contactos) 
    else: 
        print("Debes de ingresar un numero de telefono menor a 12 digitos")

def buscar_contacto(nombre):
    if nombre in agenda_contactos:
        print(f"El numero de telefono de {nombre} es: {agenda_contactos[nombre]}")
    else:
        print("El contacto no existe dentro de la agenda")    

def mostrar_contactos():
    print(agenda_contactos)
    
def actualizar_contacto(name, new_phone):
    if name in agenda_contactos:
        validacion_telefono(name, new_phone)
    else: 
        print("Debes de ingresar un numero de telefono menor a 12 digitos")
    
def eliminar_contacto(name: str) -> dict:
    if name in agenda_contactos:
        del agenda_contactos[name]
        print(agenda_contactos)
    else:
        print("El contacto no esta registrado en la agenda")
        
def validacion_telefono(name, phone):
    if phone.isdigit() and len(phone) > 0 and len(phone) <= 12:
        agenda_contactos[name] = phone
        print(agenda_contactos)
        
    

menu_opcion = 0
agenda_contactos: dict = {}


while menu_opcion !=6:
    
    print("\n--- MENÚ DE OPERACIONES ---")
    print("\n--- Agenda de contactos ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Actualizar contacto")
    print("5. Mostrar contactos")
    print("6. Salir")
    
    menu_opcion = int(input("Selecciona una opcion: "))
    
    if menu_opcion == 1:
        
        print("Has seleccionado la opcion de agregar contacto")
        nombre = input("Ingresa el nombre del nuevo contacto: ")
        telefono = input("Ingresa el telefono del nuevo contacto: ")
        agregar_contacto(nombre, telefono)
        
    elif menu_opcion == 2:
        
        print("Has seleccionado la opcion de buscar contacto")
        search_name = input("Ingresa el nombre del contacto a buscar:")
        buscar_contacto(search_name)
    
    elif menu_opcion == 3:
        
        print("Has seleccionado la opcion de eliminar contacto")
        delete_name = input("Ingresa el nombre del contacto a eliminar: ")
        eliminar_contacto(delete_name)
        
    elif menu_opcion == 4:
        
        print("Has seleccionado la opcion de actualizar contacto")
        new_name = input("Ingresa el nombre del contacto a actualizar: ")
        new_phone = input("Ingresa el nuevo telefono del contacto:")
        actualizar_contacto(new_name, new_phone)
        
    elif menu_opcion == 5:
        
        print("Has seleccionado la opcion de mostrar contactos")
        mostrar_contactos()
        
    elif menu_opcion == 6:
        print("Cerrando agenda....")
        break
    else:
        print("Opcion no valida, intenta de nuevo")
    