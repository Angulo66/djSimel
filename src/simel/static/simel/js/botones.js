
function mensaje(){
    alert("Guardando");
}

function Cancelar(){
    alert("Cancelando.. Volvera a la pagina anterior");
    location.href='index-estudiante.html'
}
function MateriasMovilidad(){
    alert("Direccionando.. Materias De Movilidad");
    location.href='Academia-MateriasMovilidad.html'
}
function MateriasCursadas(){
    alert("Direccionando.. Materias De Cursadas");
    location.href='Academia-MateriasCursadas.html'
}


function Alerta(){
    var mensaje;
    var opcion = confirm("Esta Seguro? una vez confirmado no podra deshacerlo");
    if (opcion == true) {
        mensaje = "Has clickado OK";
	} else {
	    mensaje = "Has clickado Cancelar";
	}
	document.getElementById("ejemplo").innerHTML = mensaje;
}



var cont=0;
function agregar(){
var valor= $('#imputMaterias').find('option:selected').val();
<th scope="row" id="fila"></th>
var fila=' <tr>th scope="row">'+cont+'</th><td>'+valor+'</td></tr>';
cont++;
}
