// script.js

function obtenerDatos() {

    let numero1 = parseFloat(document.getElementById("num1").value);
    let numero2 = parseFloat(document.getElementById("num2").value);

    return [numero1, numero2];
}

function mostrarResultado(resultado){
    document.getElementById("resultado").innerHTML = resultado;
}

function sumar(){

    let [num1, num2] = obtenerDatos();

    let suma = num1 + num2;

    mostrarResultado(suma);
}

function restar(){

    let [num1, num2] = obtenerDatos();

    let resta = num1 - num2;

    mostrarResultado(resta);
}

function multiplicar(){

    let [num1, num2] = obtenerDatos();

    let multiplicacion = num1 * num2;

    mostrarResultado(multiplicacion);
}

function dividir(){

    let [num1, num2] = obtenerDatos();

    if(num2 === 0){
        mostrarResultado("No se puede dividir entre 0");
    }else{
        let division = num1 / num2;
        mostrarResultado(division);
    }
}
function limpiar(){

    document.getElementById("num1").value = "";
    document.getElementById("num2").value = "";

    document.getElementById("resultado").innerHTML = "0";
}