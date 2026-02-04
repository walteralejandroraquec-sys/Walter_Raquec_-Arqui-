dia_sem = int(input("ingrese un numero del 1 al 7 y se le mostrar un dia de la semana: "))

match dia_sem:
    case 1:
        print("Hoy es dia lunes")
    case 2:
        print("Hoy es dia martes")
    case 3:
        print("Hoy es dia miercoles")
    case 4:
        print("Hoy es dia jueves")
    case 5:
        print("Hoy es dia viernes")
    case 6:
        print("Hoy es dia Sabado")
    case 7:
        print("Hoy es dia domingo")
    case _:
        print("Es el limite del programa")
