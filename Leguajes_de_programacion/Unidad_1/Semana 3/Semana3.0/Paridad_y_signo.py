print("Paridad y signo ")
print("Opciones 1. verificar si es par 2.verificar si es positivo o negativo ")
opcion = int(input("Ingrese el valor:"))

match opcion:
    case 1:
        print("verificar si es par")
        num1 = int(input("ingrese su valor: "))
        calculo = num1 % 2
        if(calculo==0):
            print("El numero es par")
        else:
            print("El numero es impar")
    case 2:
        print("verificar si es positivo o negativo")
        num1 = int(input("ingrese su valor: "))
        if(num1>0):
            print("El numero es positivo")
        else:
            print("El numero es negativo")
    case _:
        print("limite del programa")
