print("Ingrese un numero del 1 al 10 y se le mostrara su equivalencia en romano")
num = int(input("numero: "))
match num:
    case 1:
        print("la equivalencia es I ")
    case 2:
        print("La equivalencia es II ")
    case 3:
        print("la equivalencia es III ")
    case 4:
        print("La equivalencia es IV ")
    case 5:
        print("la equivalencia es V ")
    case 6:
        print("La equivalencia es VI ")
    case 7:
        print("la equivalencia es VII ")
    case 8:
        print("La equivalencia es VIII ")
    case 9:
        print("la equivalencia es IX ")
    case 10:
        print("La equivalencia es X ")
    case _:
        print("El limite del programa fue estendido")
        