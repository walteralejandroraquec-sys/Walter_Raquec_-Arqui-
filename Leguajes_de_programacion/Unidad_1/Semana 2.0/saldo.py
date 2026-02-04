#saldo=int(input("ingrese su saldo inicial "))
#producto=100

#if(total_pro>=Producto):
 #   vuelto=saldo-producto
  #  print(f"Compra exiotosa, tu vuelto es de:{vuelto}")
#else:
 #print("No te alcanza ")

#Solicitar al usuario con cuanto desea iniciar su saldo, tome en cuenta que debe asignar un producto con valor de 200
#Quetzales, pregunte al ususatio si si desea realizar la compra confirmando con una "s", si acepta realizar la compra
#calcule si al usuario le alcanza para comprar el producto y si le alcanza mostrar: compra exitosa, su vuelto es: 
#(moatrar su vuelto)

saldo=int(input("Ingrese su saldo inicial: "))
respuesta=input("Deseas realizar la compra s/n: ")

mause=200
if(respuesta=="s"):
    if(saldo<mause):
        print("No le alcanza")
    else:
         saldo=saldo-mause
    print(f"Compra exitosa, SU VUELTO ES: {saldo}")
else:
    print("Vuelve pronto") 



