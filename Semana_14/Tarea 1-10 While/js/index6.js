var s = 0
var a = Number(prompt("ingresa un numero\nn0.salir"))
while(a != 0){
    s = s +a
    a = Number(prompt("ingresa un numero\nn0.salir"))
}
alert("la suma de los numeros dados es: " + s)