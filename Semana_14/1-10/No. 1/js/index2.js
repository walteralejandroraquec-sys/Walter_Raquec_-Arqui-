var op = Number(prompt("Ingrese un numero y se le mostrara un mes:"))
if(op>=1 && op<=12){
    switch(op){
        case 1:
            alert("Es Enero")
            break;
        case 2:
            alert("Es Febrero")
            break;
        case 3:
            alert("Es Marzo")
            break;
        case 4:
            alert("Es Abril")
            break;
        case 5:
            alert("Es Mayo")
            break;
        case 6:
            alert("Es Junio")
            break;
        case 7:
            alert("Es Julio")
            break;
    }
}else{
    alert("Opcion no valida")
}