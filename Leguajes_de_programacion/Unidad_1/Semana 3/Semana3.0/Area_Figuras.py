print("Area de figuras geometricas")
print("MENU DE FIGURAS")
print("1.cuadrado, 2.triangulo 3.círculo ")
figura = int(input("Ingrese su seleccion: "))

match figura:
    case 1:
        print("Cuadrado")
        lado = int(input("Ingrese el tamaño de los lados del cuadrado "))
        area = lado * lado 
        print(f"el total de el area es: {area}cm²")
    case 2:
        print("Triangulo")
        altu = int(input("Ingrese la altura del triangulo: "))
        base = int(input("Ingrese la base del triangulo: "))
        area = (altu*base)/2
        print(f"El total del area es: {area}cm²")
    case 3:
        print("Círculo")
        radio = int(input("Ingrese el radio del circulo "))
        area = (radio*radio)*3.14
        print(f"El resultado del area es: {area}cm²")
    case _:
        print("limite del programa ") 