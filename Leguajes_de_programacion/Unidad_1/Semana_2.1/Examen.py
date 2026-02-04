Not_1 = int(input("ingrese la nota no.1: "))
Not_2 = int(input("ingrese la nota no.2: "))
Not_3 = int(input("ingrese la nota no.3: "))

promedio = (Not_1  + Not_2 + Not_3)/3

if(promedio>=6):
    print(f"El alumno aprobo con: {promedio}")
else:
    print(f"El alumno reprobo con: {promedio}")