#Simple
def my_first_function():
    print("Esta es mi primera funcion sin parametros")
#argumento    
def funcion_con_parametros(name):
    print(f'Hola ! {name} esta es mi primera funcion con parametros')
#retorno    
def funcion_con_retorno(a= 5,b = 10):
    return a + b
# con argumento por defecto o predeterminado
def args_defaults_greet(name="Python"):
    print(f"Hola {name}!")
    
# con retorno de varios valores
def multiple_return_values():
    a = 5
    b = 10
    c = 15  
    suma = a + b + c
    resta = a - b - c
    
    return suma, resta

# con numero variable de argumentos

def variable_arguments(*names):
    for name in names:
        print(f"Hola {name}")
    
# con numero variable de argumentos pero con palabra clave

def variable_key_arguments(**names):
    for key, value in names.items():
        print(f"{key}, tu nombre es {value}")        

name = input("Ingresa tu nombre: ")
print('------------------------------------')
funcion_con_parametros(name)
print('------------------------------------')
my_first_function()
print('------------------------------------')
print(f"El resultado de la suma es: {funcion_con_retorno()}")
print('------------------------------------')
args_defaults_greet()
print('------------------------------------')
sum, rest = multiple_return_values()
print(f"El resultado de la suma es: {sum}")
print(f"El resultado de la resta es: {rest}")
print(f"Los valores retornados son: {multiple_return_values()}")
print('------------------------------------')
print("Funcion con numero variable de argumentos")
variable_arguments("Alan", "Roeque", "Luis")
print('------------------------------------')

variable_key_arguments(
    lenguaje = "Python",
    name = "Angel",
    alias = "Rubio",
    age = 22
)
print('------------------------------------')
""" 
Funciones dentro de funciones
"""

def first_function():
    def second_function():
        print("Esto es una funcion dentro de otra funcion")
    #return second_function()
    second_function()

first_function()

print('------------------------------------')

""" 
Funciones propias del lenguaje
"""

print(len("Angel Martinez"))
print(type(22))
print("Angel Rubio".upper())
print("Angel Rubio".lower())
print('------------------------------------')
""" 
Manejo de local y global
"""

global_variable = "Angel"

def manipulate_variables():
    local_variable = "Martinez"
    print(f"Mi nombre de pila es: {global_variable}")
    print(f"Mi apellido es: {local_variable}")
    
manipulate_variables()
print('------------------------------------')

""" 
Fizz Buzz
"""

def print_numbers(text1, text2) -> int:
    count = 0
    for numbers in range(1, 101):
        if numbers % 3 == 0 and numbers % 5 == 0:
            print(text1 + text2)
        elif numbers % 3 == 0:
            print(text1)
        elif numbers % 5 == 0:
            print(text2)
        else:
            print(numbers)
            count += 1
    return count
            
print(print_numbers("Fizz", " Buzz"))