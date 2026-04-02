import calculos  

menu_opcion = 0

while menu_opcion != 3:
    
    print("\n--- MENÚ DE OPERACIONES ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")
    menu_opcion = int(input("Selecciona una opción: "))
    
    if menu_opcion == 1:
        print("Has seleccionado la opcion de sumar")
        num1 = int(input("Ingesa el primer numero:"))
        num2 = int(input("Ingesa el primer segundo numero:"))
        resultado = calculos.sumar(num1, num2)
        if resultado == 0 or resultado == None:
            print("No se pudo realizar la suma")
        else:
            print(f"El resultado de la suma es: {resultado}")
            
    elif menu_opcion == 2:
        print("Has seleccionado la opcion de restar")
        num1 = int(input("Ingesa el primer numero:"))
        num2 = int(input("Ingesa el primer segundo numero:"))
        resultado = calculos.operacion_restar(num1, num2)
        if resultado == 0 or resultado == None:
            print("No se pudo realizar la resta")
        else:
            print(f"El resultado de la resta es: {resultado}")
    
    elif menu_opcion == 3:
        print("Saliendo del ciclo")
        break
    else:
        print("Opcion no valida, por favor selecciona una opcion del menu")
        exit()

