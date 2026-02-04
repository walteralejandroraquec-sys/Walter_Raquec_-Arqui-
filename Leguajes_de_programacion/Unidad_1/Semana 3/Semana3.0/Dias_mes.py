print("Ingrese un numero del uno al doce y se le mostran los dias que tinen ")
mes = int(input("mes: "))

match mes:
    case 1:
        print("el primer mes es enero, y los dias son 31 ")
    case 2:
        print("El segundo mes es febrero, y los dias son 28")
    case 3:
        print("El tercer mes es marzo, y los dias son 31")
    case 4:
        print("El cuarto mes es abril, y los dias son 30")
    case 5:
        print("El quinto mes es mayo, y los dias son 31")
    case 6:
        print("El sexto mes es junio, y los dias son 30 ")
    case 7:
        print("El septimo mes es julio, y los dias son 31 ")
    case 8:
        print("El octavo mes es agosto, y los dias son 30")
    case 9:
        print("El noveno mes es septiembre, y los dias son 31")
    case 10:
        print("El decimo mes es octubre, y los dias son 30 ")
    case 11:
        print("El onceabo mes es noviembre, y los dias son 31")
    case 12:
        print("El doceabo mes es diciembre, y los dias son 31")
    case _:
        print("Limite del programa ")