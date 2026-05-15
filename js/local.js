// Instanciar  las variables 
// Variable tipo bandera 
let accion = "A";
let indice = -1;
let datos = localStorage.getItem("datos");
//Implementacion JSON
datos = JSON.parse(datos);
if (datos == null) datos = [];

//funcion para listar los registros en JSON
function lista() {
	//Llamar a la tabla donde se encuentran los resultados "listado"
	document.getElementById("listado").innerHTML = "";
	let tabla = "<tr>" +
		"<th>Nombre</th>" +
		"<th>Apellido</th>" +
		"<th>Edad</th>" +
		"<th>Direccion</th>" +
		"<th>Estado Civil</th>" +
		"<th>Borrar</th>" +
		"<th>Editar</th>" +
		"</tr>";
	//Recorrido del arreglo de datos 
	for (let i in datos) {
		let dato = JSON.parse(datos[i]);
		tabla += "<tr><td>" + dato.nombre + "</td>";
		tabla += "<td>" + dato.apellido + "</td>";
		tabla += "<td>" + dato.edad + "</td>";
		tabla += "<td>" + dato.dir + "</td>";
		tabla += "<td>" + dato.estado + "</td>";
		tabla += "<td><input type='button' value='Borrar' onClick='borrar(" + i + ")'></td>";
		tabla += "<td><input type='button' value='Editar' onClick='editar(" + i + ")'></td>";
		tabla += "</tr>";
	}

	document.getElementById("listado").innerHTML = tabla;
}
function guardar() {
	//recuperar datos 
	let nombre = document.getElementById("nombre").value;
	let apellido = document.getElementById("apellido").value;
	let edad = document.getElementById("edad").value;
	let dir = document.getElementById("dir").value;
	let estado = document.getElementById("estado").value;

	//Creamos el objeto en JSON
	let dato = JSON.stringify({
		nombre: nombre,
		apellido:apellido,
		edad:edad,
		dir:dir,
		estado,estado
	});

	//Añadir objeto JSON
	if (accion == "A") {
		//guardarmos los datos
		datos.push(dato);
		localStorage.setItem("datos", JSON.stringify(datos));
		alert("Información guardada con éxito");
	} else {
		//actualizar los datos
		datos[indice] = dato;
		localStorage.setItem("datos", JSON.stringify(datos));
		alert("Información actualizado exitosamente");
	}

	//limpiar cajas de texto
	document.getElementById("nombre").value = "";
	document.getElementById("apellido").value = "";
	document.getElementById("edad").value = "";
	document.getElementById("direccion").value = "";
	document.getElementById("estado").value = "";

	lista();
	return true;
}

//Delete - Borrar

function borrar(i) {
	indice = i;
	let dato = JSON.parse(datos[indice]);
	let nombre = dato.nombre;
	let apellido = dato.apellido;
	let edad = dato.edad;
	let dir = dato.dir;
	let estado = dato.estado;
	if (confirm("¿Desea borrar la información de '" + nombre + apellido + "'?")) {
		datos.splice(indice, 1);
		localStorage.setItem("datos", JSON.stringify(datos));
		alert("La informacion de '" + nombre + apellido  +"' ha sido eliminado");
	}

	lista(); //Actualizar la lista de los datos existentes en el localStorage
}

//Editar los datos encontrados en el LocalStorage
function editar(i) {
	indice = i;
	accion = "E";
	//Carga de los datos  a las cajas de texto
	let dato = JSON.parse(datos[indice]);
	document.getElementById("nombre").value = dato.nombre;
	document.getElementById("apellido").value = dato.apellido;
	document.getElementById("edad").value = dato.edad;
	document.getElementById("dir").value = dato.dir;
	document.getElementById("estado").value = dato.estado;
}

//Arrancar partiendo de la funcion lista
window.onload = function () {
	lista();
}