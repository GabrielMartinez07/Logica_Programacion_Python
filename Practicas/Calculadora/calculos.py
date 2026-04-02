def sumar(num1, num2):
    
    if num1 == 0 or num2 == 0:
        print("Error: No se puede ingresar el numero 0")
    elif num1 is None or num2 is None:
        print("Error: Ambos numeros deben de ser ingresados")
    elif num1 < 0 or num2 < 0:
        print("Error: No se pueden ingresar numeros negativos")
    else:
        return num1 + num2
    
def operacion_restar(num1, num2):
    
    if num1 == 0 or num2 == 0:
        print("Error: No se puede ingresar el numero 0")
    elif num1 is None or num2 is None:
        print("Error: Ambos numeros deben de ser ingresados")
    elif num1 < 0 or num2 < 0:
        print("Error: No se pueden ingresar numeros negativos")
    else:
        return num1 - num2