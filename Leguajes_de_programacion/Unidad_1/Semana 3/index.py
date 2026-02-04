#Pedir al usuario 3 numero y halla el mayor de ellos 

#Pedir el usuario 3 numero y hallar mayor, menor de ellos

#pedir al usuario 3 numeros y verificar si alguno de ellos se repite 

num1=float(input("Ingrese su primer numero"))
num2=float(input("Ingrese su segundo numero"))
num3=float(input("Ingrese su tercer numero"))

if(num1>num2 or num3):
    print(f"el numero mayor es: {num1}")
elif(num2 > num1 or num3):
        print(f"el numero mayor es: {num2}")
elif(num3 > num1 or num2):
    print(f"el numero mayor es: {num3}")
