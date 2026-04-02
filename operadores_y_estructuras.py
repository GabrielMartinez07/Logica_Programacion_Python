#Operadores aritmeticos
print(f"Suma: 10 + 6 = {10 + 6}")
print(f"Resta: 10-2 = {10 -2}")
print(f"Multiplicacion: 10*7 = {10*7}")
print(f"Divicion: 10/3 = {10/3}")
print(f"Modulo: 10%3 = {10%3}")
print(f"Potencia: 10**3 = {10**3}")

#operadores de comparacion
print(f"10 > 6: {10 > 6}")
print(f"10 < 6: {10 < 6}")
print(f"10 == 6: {10 == 6}")
print(f"10 != 6: {10 != 6}")

#operadores logicos
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 13 or 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}")
print(f"NOT !: not 10 + 3 == 14 es {not 10 + 3 == 14}")

# Operadores de asignación
my_number = 11  # asignación
print(my_number)
my_number += 1  # suma y asignación
print(my_number)
my_number -= 1  # resta y asignación
print(my_number)
my_number *= 2  # multiplicación y asignación
print(my_number)
my_number /= 2  # división y asignación
print(my_number)
my_number %= 2  # módulo y asignación
print(my_number)
my_number **= 1  # exponente y asignación
print(my_number)
my_number //= 1  # división entera y asignación
print(my_number)

# Operadores de identidad
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(f"my_number is not my_new_number es {my_number is not my_new_number}")

# Operadores de pertenencia
print(f"'u' in 'mouredev' = {'u' in 'mouredev'}")
print(f"'b' not in 'mouredev' = {'b' not in 'mouredev'}")

# Operadores de bit
a = 10  # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 101000

#Condicionales
#EMPEZARE CON LA ESTRUCUTURA DE CONTROL IF
input_number = int(input("Ingrese un numero entero:"))
if input_number < 0:
    x = 0 
    print("Numero negativo o cero")
    
elif input_number == 0:
    print("El numero es cero")
elif input_number == 1:
    print("El numero es uno")
elif input_number > 0:
    print("El numero es entero positivo")
#EL MANEJO DE LA SANGRIA ES IMPORTANTE EN PYTHON, YA QUE NOS INDICA LOS BLOQUES DE CODIGO

#Iterativas
#FOR
words = [ 'gato', 'perro', 'elhdsptmdelyeyo']

for w in words:
    print(w,' ', 'La cantidad de palabras es: ', len(w))
    
users = { 'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active' }

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
    print(users)
#DICCIONARIO
#item() devuelve una lista de parejas clave-valor
#copy() devuelve una copia superficial del diccionario    
active_users = {'Braulio': 'active', 'Pandora': 'inactive', '景太郎': 'inactive'}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
    print(active_users)
    

for i in range(5):
    print(i)
    

a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print(i, a[i])
    
while i <= 10:
    print(i)
    i += 1
    
# Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")
    
for number in range(10, 56):
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)