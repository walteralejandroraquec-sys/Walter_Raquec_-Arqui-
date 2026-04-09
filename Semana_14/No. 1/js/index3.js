var op = Number(prompt("Ingrese un numero del 1-10\n y se le mostrara su valor en romano"))

if (op >= 1 && op <= 10) {
  switch (op) {
    case 1:
      alert("El valor en romano es I")
      break;
    case 2:
      alert("El valor en romano es II")
      break;
    case 3:
      alert("El valor en romano es III")
      break;
    case 4:
      alert("El valor en romano es IV")
      break;
    case 5:
      alert("El valor en romano es V")
      break;
    case 6:
      alert("El valor en romano es VI")
      break;
    case 7:
      alert("El valor en romano es VII")
      break;
    case 8:
      alert("El valor en romano es VIII")
      break;
    case 9:
      alert("El valor en romano es XI")
      break;
    case 10:
      alert("El valor en romano es X")
      break;
  }
}else{
    alert("Fuera de rango")
}
