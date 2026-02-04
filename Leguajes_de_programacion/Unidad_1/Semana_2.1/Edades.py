edad = int(input("Ingrese su edad: "))

if(edad<=2):
    print("Es un bebe")
elif(edad<=12):
    print("es un niño")
elif(edad<=17):
    print("es un adolecente")
elif(edad<=64):
    print("Es un adulto")
elif(edad>=65):
    print("Es un anciano")
else:
    print("Ese no es un numero")
