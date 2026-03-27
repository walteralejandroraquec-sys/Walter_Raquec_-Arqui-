//peticiones del Usuario
/*a = prompt("Digita tu edad")
b = prompt("Escribe tu nombre")

alert("Bienvenido " +b+ " tienes " +a+ " años ")*/

//Operaciones Basicas 
/*a = parseInt(prompt("Ingresa el primer valor: "))
b = parseInt(prompt("Ingresa el segundo valor: "))

//c = a+b
alert("La suma es de: " + (a+b) ) */

//SENTENCIA IF 
/* a=prompt("Ingresa tu edad: ")

if (a>=18) {
    alert("Eres mayor")
}else{
    alert("Eres menor")
} */

// REALIZAR UN MENU CON IF Y VALIDAR QUE DIGITO ESCRIBIO 
//DEL RANDO 1-3

a = prompt("Digita el 1\nDigita el 2\nDigita el 3")
if (a==1) {
    alert("El numero ingresado es 1")
}else if (a==2) {
    alert("El numero ingresado es 2")
}else if (a==3) {
    alert("El numero ingresado es 3")
}else{
    alert("Fuera de Rango")
}