print("MENU DE OPERACIONES BASICAS")
print("1.Suma, 2.Resta, 3.Multiplicacion, 4.Division ")

valor = int(input("Ingrese su selccion: "))

match valor:
    case 1:
        print("su opcion es suma")
        num1 = int(input("ingrese el primer valor: "))
        num2 = int(input("Ingrese el segundo valor: "))
        total = num1 + num2 
        print(f"El resultado final es: {total}")
    case 2:
        print("su opcion es resta")
        num1 = int(input("ingrese el primer valor: "))
        num2 = int(input("Ingrese el segundo valor: "))
        total = num1 - num2 
        print(f"El resultado final es: {total}")
    case 3:
        print("su opcion es multiplicacion")
        num1 = int(input("ingrese el primer valor: "))
        num2 = int(input("Ingrese el segundo valor: "))
        total = num1 * num2 
        print(f"El resultado final es: {total}")
    case 4:
        print("su opcion es Division ")
        num1 = int(input("ingrese el primer valor: "))
        num2 = int(input("Ingrese el segundo valor: "))
        total = num1 / num2 
        print(f"El resultado final es: {total}")
    case _:
        print("Opcion indisponible")