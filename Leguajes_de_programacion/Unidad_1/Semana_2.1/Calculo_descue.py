precio = int(input("Ingrese el precio del producto: "))

if(precio>100):
 total_des = precio * 0.15
 total_pro = precio-total_des
 print(f"su producto tiene un descuento del 15% y el total a pagar es: {total_pro}, su descuento es de {total_des}")
else:
    print(f"Su producto no tiene descuento su total es: {precio}")
    