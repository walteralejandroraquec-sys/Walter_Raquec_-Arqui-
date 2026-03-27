cel = parseFloat(prompt("Ingrese la temperatura en grados Celsius:"))
opcion = prompt("Como desea convertirlo\n1. Fahrenheit\n2. Kelvin")


if (opcion == "1") {
    fa = (cel * 9/5) + 32
    alert("La temperatura en Fahrenheit es:  " + fa)
} else if (opcion == "2") {
    kel = cel + 273.15
    alert("La temperatura en Kelvin es:  " + kel)
} else {
    alert("Opcion no invalida")
}
