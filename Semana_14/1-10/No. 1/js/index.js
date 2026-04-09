var op = Number(prompt("Ingrese un numero y se le mostrara un dia de la semana:"))
if(op>=1 && op<=7){
    switch(op){
        case 1:
            alert("Hoy es lunes")
            break;
        case 2:
            alert("Hoy es martes")
            break;
        case 3:
            alert("Hoy es miercoles")
            break;
        case 4:
            alert("Hoy es jueves")
            break;
        case 5:
            alert("Hoy es viernes")
            break;
        case 6:
            alert("Hoy es Sabado")
            break;
        case 7:
            alert("Hoy es Domingo")
            break;
    }
}else{
    alert("Opcion no valida")
}