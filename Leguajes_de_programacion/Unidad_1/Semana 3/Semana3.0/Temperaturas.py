print("Convertidor de medidas ")
print("Menu de grados")
print("1.Fahrenheit 2.kelvin")
grado = int(input("Ingrese su opcion: "))

match grado:
    case 1:
        print("Faherenheit")
        celsius = float(input("ingrese sus grados a convertir, ingreselos en Celsius "))
        faherenheit = (celsius*1.8)+32
        print(f"El resultado {faherenheit} grados Fahrenheit")
    case 2:
        print("kelvin")
        celsius = float(input("ingrese sus grados a convertir, ingreselos en Celsius "))
        kelvin = celsius + 273.15
        print(f"El resultado es: {kelvin} grados kelvin")
    case _:
        print("limite del programa")    

