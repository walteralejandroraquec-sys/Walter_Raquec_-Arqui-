print("Calculado de potencia y raiz ")
print("1.pontecia al cuadrado  2.Raiz ")
selec = int(input("Seleccion que desea: "))

match selec:
    case 1:
        print("Potencia")
        num1 = int(input("Ingrese el numero que quiere potenciar al cuadrado: "))
        total = num1*num1
        print(f"El total de la potencia es: {total}")
    case 2:
        print("Raiz cuadrada")
        num1 = float(input("Ingrese el numero para sacarle la raiz: "))
        import math
        raiz = math.sqrt(num1)
        print(f"la raiz cuadrada es: {raiz}")
    case _:
        print("Limite del programa")