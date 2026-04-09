var s = 0
var a = Number(prompt("ingresa un numero\n(negativo para salir)"))
while(a >= 1){
    s++
    a = Number(prompt("ingresa un numero\n(negativo para salir)"))
}
alert("cantidad de numeros ingresados: " + s)