
function mensaje(){
    alert("Guardando");
    location.href='alumno-estado.html'
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

function addMateria(e) {
    e.preventDefault();
    const row = createRow({
      MateriaMovilidad:$('#MateriaMovilidad').val(),
      promedio: $('#promedio').val()
    });
    $('table tbody').append(row);
    clean();
  }
  
  function createRow(data) {
    return (
      `<tr>` +
        `<td>${$('tbody tr').length + 1}</td>` +
        `<td>${data.MateriaMovilidad}</td>` +
        `<td>${data.promedio}</td>` +
      `</tr>`
    );
  }
  
  function clean() {
    $('#imputMateriaMovilidad').val('');
    $('#promedio').val('');
    $('#inputMateriaMovilidad').focus();
  }
  function addMateriaSolicitud(e) {
    e.preventDefault();
    const row = createRow2({
      inputMateria:$('#inputMateria').val()
    });
    $('table tbody').append(row);
    clean2();
  }
  
  function createRow2(data) {
    return (
      `<tr>` +
        `<td>${$('tbody tr').length + 1}</td>` +
        `<td>${data.inputMateria}</td>` +
      `</tr>`
    );
  }
  
  function clean2() {
    $('#inputMateria').val('Elegir ...');
    $('#inputMateria').focus();
  }
  //dependiendo el valor que le des falso o verdadero cargara la imagen esa se la envian cuando de el boton
  //guardar de solicitud
  function EstadoImagen(val){
    var bandera=true;
    bandera=val; 
    if(bandera){
      $("#imagen").attr("src","img/happy.png");
    }else{
      $("#imagen").attr("src","img/sad.png");
    }


  }
  
    
    