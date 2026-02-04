print("Ingrese un numero del 1 al 12 y se le mostrar la estacion del año que corresponde")
mes = int(input("Mes: "))

match mes:
    case 1:
        print("el primer mes es enero, y su estacion es invierno")
    case 2:
        print("El segundo mes es febrero, y su estacion es invierno")
    case 3:
        print("El tercer mes es marzo, y su estacion es verano")
    case 4:
        print("El cuarto mes es abril, y su estacion es verano")
    case 5:
        print("El quinto mes es mayo, y su estaciones otoño")
    case 6:
        print("El sexto mes es junio, y su estacion es otoño ")
    case 7:
        print("El septimo mes es julio, y su estacion es primavera ")
    case 8:
        print("El octavo mes es agosto, y su estacion del año es primavera")
    case 9:
        print("El noveno mes es septiembre, y su estacion deñ año es otoño")
    case 10:
        print("El decimo mes es octubre, y su estacion es primavera ")
    case 11:
        print("El onceabo mes es noviembre, y su estacion es invierno ")
    case 12:
        print("El doceabo mes es diciembre, y su estacion es invierno ")
    case _:
        print("Limite del programa ")

