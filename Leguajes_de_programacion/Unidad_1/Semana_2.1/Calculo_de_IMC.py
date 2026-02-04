
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros:"))
imc = peso / altura ** 2
if imc > 25:
    print(f"Su IMC es {imc}, tu peso me preocupa bro")
else:
    print(f"Su IMC es {imc}, Su peso es estable")