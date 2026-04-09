var s = 0
var t = 0
var a = Number(prompt("ingresa un numero\n-1.para terminar"))
while(a != -1){
    t = t + a
    s++
    a = Number(prompt("ingresa un numero\n-1.para terminar"))
}
if(s > 0){
    alert("Promedio: " + (t / s));
}else{
    alert("No ingresaste numeros");
}