/* 
    Función que validará nuestros campos del formulario a través
    de otras funciones.
*/
function validar(){

    let nombre = document.getElementById('nombre').value;
    let email = document.getElementById('email').value;
    let inicio = document.getElementById('dia-hora-inicio').value;
    let tema = document.getElementById('tema').value;
    let region = document.getElementById('region1').value;
    let comuna = document.getElementById('comuna1').value;
    let archivo = document.getElementById('foto-actividad').value;
    let celular = document.getElementById('celular').value;
    let inputTema = document.getElementById('inputTema').value;

    /* Errors contendrá todos los errores que vayamos encontrando y luego los escribiremos según corresponda*/
    let errors = '';

    if(validarInputTema(inputTema) == true && validarInicio(inicio) ==true && validarRegion(region) ==true && validarTema(tema) ==true && validarComuna(comuna) ==true && validarEmail(email) ==true && validarNombre(nombre) ==true && validarArchivo(archivo) == true){
        return true;
    }

    if (!validarComuna(comuna)){
        document.getElementById('comuna1').style.backgroundColor = "#fcdbe6";
        document.getElementById('comuna1').style.borderColor = "#f15c8e";
        errors += '<p>Ingrese una comuna.</p>'
    } else{
        document.getElementById('comuna1').style.backgroundColor = "#e2fdf4";
        document.getElementById('comuna1').style.borderColor = "#0ebd84";
    }

    if (!validarNombre(nombre)){
        document.getElementById('nombre').style.backgroundColor = "#fcdbe6";
        document.getElementById('nombre').style.borderColor = "#f15c8e";
        errors += '<p>Ingrese un nombre válido.</p>'
    } else{
        document.getElementById('nombre').style.backgroundColor = "#e2fdf4";
        document.getElementById('nombre').style.borderColor = "#0ebd84";
    }

    if (!validarCelular(celular)){
        document.getElementById('celular').style.backgroundColor = "#fcdbe6";
        document.getElementById('celular').style.borderColor = "#f15c8e";
    } else{
        document.getElementById('celular').style.backgroundColor = "#e2fdf4";
        document.getElementById('celular').style.borderColor = "#0ebd84";
    }

    if (!validarEmail(email)){
        document.getElementById('email').style.backgroundColor = "#fcdbe6";
        document.getElementById('email').style.borderColor = "#f15c8e";
        errors += '<p>Ingrese email válidos.</p>'
    } else{
        document.getElementById('email').style.backgroundColor = "#e2fdf4";
        document.getElementById('email').style.borderColor = "#0ebd84";
    }

    if (!validarArchivo(archivo)){
        document.getElementById('foto-actividad').style.backgroundColor = "#fcdbe6";
        document.getElementById('foto-actividad').style.borderColor = "#f15c8e";
        errors += '<p>Ingrese una contraseña de máximo 10 carácteres.</p>'
    } else{
        document.getElementById('foto-actividad').style.backgroundColor = "#e2fdf4";
        document.getElementById('foto-actividad').style.borderColor = "#0ebd84";
    }

    if (!validarTema(tema)){
        document.getElementById('tema').style.backgroundColor = "#fcdbe6";
        document.getElementById('tema').style.borderColor = "#f15c8e";
    } else{
        document.getElementById('tema').style.backgroundColor = "#e2fdf4";
        document.getElementById('tema').style.borderColor = "#0ebd84";
    }

    if (!validarRegion(region)){
        document.getElementById('region1').style.backgroundColor = "#fcdbe6";
        document.getElementById('region1').style.borderColor = "#f15c8e";
        errors += '<p>Contraseña. Ingrese una contraseña de máximo 10 carácteres.</p>'
    } else{
        document.getElementById('region1').style.backgroundColor = "#e2fdf4";
        document.getElementById('region1').style.borderColor = "#0ebd84";
    }

    if (!validarInicio(inicio)){
        document.getElementById('dia-hora-inicio').style.backgroundColor = "#fcdbe6";
        document.getElementById('dia-hora-inicio').style.borderColor = "#f15c8e";
        errors += '<p>Contraseña. Ingrese una contraseña de máximo 10 carácteres.</p>'
    } else{
        document.getElementById('dia-hora-inicio').style.backgroundColor = "#e2fdf4";
        document.getElementById('dia-hora-inicio').style.borderColor = "#0ebd84";
    }

    if (!validarInputTema(inputTema)){
        document.getElementById('inputTema').style.backgroundColor = "#fcdbe6";
        document.getElementById('inputTema').style.borderColor = "#f15c8e";
        errors += '<p>Contraseña. Ingrese una contraseña de máximo 10 carácteres.</p>'
    } else{
        document.getElementById('inputTema').style.backgroundColor = "#e2fdf4";
        document.getElementById('inputTema').style.borderColor = "#0ebd84";
    }

    /*Finalmente si hay errores lo escribimos en el contenedor de errores, en nuestro div al costado del formulario*/
    if(errors != ''){
        return false;
    }

}

/*validarNombre recibe un nombre y lo valida según largo y pregunta si sólo contiene letras*/
function validarNombre(nombre){

    let regex = /^[a-zA-Z ]*$/;

    if (nombre.length < 2 | nombre.length > 200 | !regex.test(nombre)){
        return false;
    }

    return true;

}

/*validarEmail recibe un email y lo valida según emailregex*/
function validarEmail(email){
    let emailregex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/

    if (email.match(emailregex)) {
        return true;
    }
    
    return false;

}

/*validarSector recibe un sector y lo valida según largo*/
function validarSector(sector){

    if (sector.length < 8 | sector.length > 100){
        return false;
    }

    return true;

}

/*validarTema recibe un tema y lo valida según largo*/
function validarTema(tema){

    if (tema == 0){
        return false;
    }

    return true;

}

/*validarSector recibe un inputTema y lo valida según largo*/
function validarInputTema(inputTema){

    if (inputTema.length < 3 || inputTema.length > 15){
        return false;
    }
    else{
        return true;
    }
}

/*Validar archivo recibe un archivo y pregunta si es vacío o no*/
function validarArchivo(archivo){

    if(archivo == '') {
        return false;
    }

    return true;

}

/*Validar que se selecciona alguna categoría de la región*/
function validarRegion(region){

    if(region == 0) {
        return false;
    }

    return true;

}

/*Validar que se selecciona alguna categoría de la comuna*/
function validarComuna(comuna){

    if(comuna == "-") {
        return false;
    }

    return true;

}

/*Validar que se comenta algo*/
function validarInicio(inicio){
    let regexfecha = /[0-9]{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1]) (2[0-3]|[01][0-9]):[0-5][0-9]/
    
    if (!inicio.match(regexfecha) | !regexfecha.test(inicio)){
        return false;
    }

    return true;

}

/*Validar que se comenta algo*/
function validarCelular(celular){
    let regexcelular = /^(\+?56)?(\s?)(0?9)(\s?)[9876543]\d{7}$/

    if (!celular.match(regexcelular)){
        return false;
    }

    return true;

}

var comunas_I = new Array("-", "Alto Hospicio", "Camiña", "Colchane", "Huara", "Iquique", "Pica", "Pozo Almonte");
var comunas_II = new Array("-","Antofagasta", "Calama", "María Elena", "Mejillones", "Ollagüe", "San Pedro de Atacama", "Sierra Gorda", "Taltal", "Tocopilla");
var comunas_III = new Array("-","Alto del Carmen", "Caldera", "Chañaral", "Copiapó", "Diego de Almagro", "Freirina", "Huasco", "Tierra Amarilla", "Vallenar");
var comunas_IV = new Array("-", "Andacollo", "Canela", "Combarbalá", "Coquimbo", "Illapel", "La Higuera", "La Serena", "Los Vilos", "Monte Patria", "Ovalle", "Paihuano", "Punitaqui", "Río Hurtado", "Salamanca", "Vicuña");
var comunas_V = new Array("-", "Algarrobo", "Cabildo", "Calle Larga", "Cartagena", "Casablanca", "Catemu", "Concón", "El Quisco", "El Tabo", "Hijuelas", "Isla de Pascua", "Juan Fernández", "La Calera", "La Cruz", "La Ligua", "Limache", "Llay Llay", "Los Andes", "Nogales", "Olmué", "Panquehue", "Papudo", "Petorca", "Puchuncaví", "Putaendo", "Quillota", "Quilpué", "Quintero", "Rinconada", "San Antonio", "San Esteban", "San Felipe", "Santa María", "Santo Domingo", "Valparaíso", "Villa Alemana", "Viña del Mar", "Zapallar");
var comunas_VI = new Array("-", "Chépica", "Chimbarongo", "Codegua", "Coinco", "Coltauco", "Doñihue", "Graneros", "La Estrella", "Las Cabras", "Litueche", "Lolol", "Machalí", "Malloa", "Marchigüe", "Mostazal", "Nancagua", "Navidad", "Olivar", "Palmilla", "Paredones", "Peralillo", "Peumo", "Pichidegua", "Pichilemu", "Placilla", "Pumanque", "Quinta de Tilcoco", "Rancagua", "Rengo", "Requínoa", "San Fernando", "San Vicente de Tagua Tagua", "Santa Cruz");
var comunas_VII = new Array("-", "Cauquenes", "Chanco", "Colbún", "Constitución", "Curepto", "Curicó", "Empedrado", "Hualañé", "Licantén", "Linares", "Longaví", "Maule", "Molina", "Parral", "Pelarco", "Pelluhue", "Pencahue", "Rauco", "Retiro", "Río Claro", "Romeral", "Sagrada Familia", "San Clemente", "San Javier", "San Rafael", "Talca", "Teno", "Vichuquén", "Villa Alegre", "Yerbas Buenas");
var comunas_VIII = new Array("-", "Alto Bío Bío", "Antuco", "Arauco", "Cabrero", "Cañete", "Chiguayante", "Concepción", "Contulmo", "Coronel", "Curanilahue", "Florida", "Hualpén", "Hualqui", "Laja", "Lebu", "Los Ángeles", "Los Álamos", "Lota", "Mulchén", "Nacimiento", "Negrete", "Penco", "Quilaco", "Quilleco", "San Pedro de la Paz", "San Rosendo", "Santa Bárbara", "Santa Juana", "Talcahuano", "Tirúa", "Tomé", "Tucapel", "Yumbel");
var comunas_IX = new Array("-", "Angol", "Carahue", "Chol Chol", "Collipulli", "Cunco", "Curacautín", "Curarrehue", "Ercilla", "Freire", "Galvarino", "Gorbea", "Lautaro", "Loncoche", "Lonquimay", "Los Sauces", "Lumaco", "Melipeuco", "Nueva Imperial", "Padre Las Casas", "Perquenco", "Pitrufquén", "Pucón", "Purén", "Renaico", "Saavedra", "Temuco", "Teodoro Schmidt", "Toltén", "Traiguén", "Victoria", "Vilcún", "Villarrica");
var comunas_X = new Array("-", "Ancud", "Calbuco", "Castro", "Chaitén", "Chonchi", "Cochamó", "Curaco de Vélez", "Dalcahue", "Fresia", "Frutillar", "Futaleufú", "Hualaihué", "Llanquihue", "Los Muermos", "Maullín", "Osorno", "Palena", "Puerto Montt", "Puerto Octay", "Puerto Varas", "Puqueldón", "Purranque", "Puyehue", "Queilén", "Quellón", "Quemchi", "Quinchao", "San Juan de la Costa", "San Pablo");
var comunas_XI = new Array("-", "Aysén", "Chile Chico", "Cisnes", "Cochrane", "Coyhaique", "Guaitecas", "Lago Verde", "O’Higgins", "Río Ibáñez", "Tortel");
var comunas_XII = new Array("-", "Antártica", "Cabo de Hornos", "Laguna Blanca", "Porvenir", "Primavera", "Puerto Natales", "Punta Arenas", "Río Verde", "San Gregorio", "Timaukel", "Torres del Paine");
var comunas_RM = new Array("-", "Alhué", "Buin", "Calera de Tango", "Cerrillos", "Cerro Navia", "Colina", "Conchalí", "Curacaví", "El Bosque", "El Monte", "Estación Central", "Huechuraba", "Independencia", "Isla de Maipo", "La Cisterna", "La Florida", "La Granja", "La Pintana", "La Reina", "Lampa", "Las Condes", "Lo Barnechea", "Lo Espejo", "Lo Prado", "Macul", "Maipú", "María Pinto", "Melipilla", "Ñuñoa", "Padre Hurtado", "Paine", "Pedro Aguirre Cerda", "Peñaflor", "Pañalolen", "Pirque", "Providencia", "Pudahuel", "Puente Alto", "Quilicura", "Quinta Normal", "Recoleta", "Renca", "San Bernardo", "San Joaquín", "San José de Maipo", "San Miguel", "San Pedro", "San Ramón", "Santiago", "Talagante", "Tiltil", "Vitacura");
var comunas_XIV = new Array("-", "Corral", "Futrono", "La Unión", "Lago Ranco", "Lanco", "Los Lagos", "Máfil", "Mariquina", "Paillaco", "Panguipulli", "Río Bueno", "Valdivia");
var comunas_XV = new Array("-", "Arica", "Camarones", "General Lagos", "Putre");
var comunas_XVI = new Array("-", "Bulnes", "Chillán", "Chillán Viejo", "Cobquecura", "Coelemu", "Coihueco", "El Carmen", "Ninhue", "Ñiquén", "Pemuco", "Pinto", "Portezuelo", "Quillón", "Quirihue", "Ránquil", "San Carlos", "San Fabián", "San Ignacio", "San Nicolás", "Trehuaco", "Yungay");

var todas_las_comunas = [[], comunas_I, comunas_II, comunas_III, comunas_IV, comunas_V, comunas_VI, comunas_VII, comunas_VIII, comunas_IX, comunas_X, comunas_XI, comunas_XII, comunas_RM, comunas_XIV, comunas_XV, comunas_XVI];

function cambiaComuna(){ 
    //tomo el valor del select del pais elegido 
    var region
    region = document.form.region[document.form.region.selectedIndex].value 
    //miro a ver si el pais está definido 
    if (region != 0) { 
       //si estaba definido, entonces coloco las opciones de la provincia correspondiente. 
       //selecciono el array de provincia adecuado 
       mis_comunas = todas_las_comunas[region]
       //calculo el numero de provincias 
       num_comunas = mis_comunas.length 
       //marco el número de provincias en el select 
       document.form.comuna.length = num_comunas 
       //para cada provincia del array, la introduzco en el select 
       for(i = 0; i < num_comunas; i++){ 
          document.form.comuna.options[i].value = mis_comunas[i] 
          document.form.comuna.options[i].text = mis_comunas[i] 
       }	
    }else{ 
       //si no había provincia seleccionada, elimino las provincias del select 
       document.form.comuna.length = 1 
       //coloco un guión en la única opción que he dejado 
       document.form.comuna.options[0].value = "-" 
       document.form.comuna.options[0].text = "-" 
    } 
    //marco como seleccionada la opción primera de provincia 
    document.form.comuna.options[0].selected = true 
}

function cambiaContacto() {
  
    var contactar
    contactar = document.form.contactar[document.form.contactar.selectedIndex].value
    if(contactar != 0 | (contactar.length < 4 && contactar.length > 50)) {
        document.getElementById('inputcontacto').disabled = false
    }
    else {
        document.getElementById('inputcontacto').disabled = true
    }
}

function cambiaTema() {
    var tema
    tema = document.form.tema[document.form.tema.selectedIndex].value
    if(tema == 9) {
        document.getElementById('inputTema').disabled = false
    } 
    else {
        document.getElementById('inputTema').disabled = true
    }
}

let contador = 0;

function AddPhoto(){

    let contenedor = document.getElementById('contenedorObjetos');

    if (contador<4){
        contenedor.innerHTML += '<input type="file" id="foto-actividad" name="foto-actividad">';
        contador++;
    }
}

let contador1 = 0;

function AddContacto(){
    if(contador1 < 4){
        contador1++;
        var p = document.getElementById("contactar-g");
        var p_clone = p.cloneNode(true);
        document.getElementById('clones').appendChild(p_clone);
    }
}
const ctx1 = document.getElementById('myChart1').getContext('2d');
const ctx2 = document.getElementById('myChart2').getContext('2d');
const ctx3 = document.getElementById('myChart3').getContext('2d');
const myChart = new Chart(ctx1, {
    type: 'line',
    data: {
        labels: ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'],
        datasets: [{
            label: 'Actividades por día',
            data: [12, 19, 3, 5, 2, 3, 13],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(0, 255, 255, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(54, 162, 235, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
    }
});

const myChart2 = new Chart(ctx2, {
    type: 'pie',
    data: {
        labels: ['Baile', 'Boxeo', 'Zumba', 'Otros'],
        datasets: [{
            label: 'Actividades por día',
            data: [16, 23, 7, 10],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
    }
});

var mañana = {
    label: 'Mañana',
    data: [17, 21, 25, 14, 10, 9, 5, 70, 32, 43, 23, 27],
    backgroundColor: 'rgba(146, 43, 62, 0.6)',
    borderColor: 'rgba(146, 43, 62, 1)',
    yAxisID: "mañana"
};

var mediodia = {
    label: 'Medio Día',
    data: [30, 50, 16, 64, 35, 80, 55, 79, 92, 33, 53, 17],
    backgroundColor: 'rgba(252, 233, 3, 0.6)',
    borderColor: 'rgba(252, 233, 3, 1)',
    yAxisID: "mediodia"
};
var tarde = {
    label: 'Tarde',
    data: [5, 8, 4, 4, 6, 8, 10, 3, 5, 2, 0, 6],
    backgroundColor: 'rgba(0, 0, 205, 0.6)',
    borderColor: 'rgba(0, 0, 205, 1)',
    yAxisID: "tarde"
};

var mesesData = {
    labels: ["Enero", "Fabrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre" , "Diciembre"],
    datasets: [mañana, mediodia, tarde]
};
var chartOptions = {
    responsive: true,
};
   
var barChart = new Chart(ctx3, {
    type: 'bar',
    data: mesesData,
    options: chartOptions
});


// Rellena 'dia hora termino' desdpués de que 'dia hora inicio' es llenado
function refillDate(){
    let y = document.getElementById("dia-hora-inicio").value;
    let container = document.getElementById("dia-hora-termino");
    let new_date = y.split(' ');
    let new_hour = new_date[1].split(':');
    container.value = new_date[0] + " " + ((parseInt(new_hour[0]) + 3)%24).toString() + ":" + new_hour[1];
}
function agrandar(){
    Swal.fire({
        imageUrl: "https://cdn.create.vista.com/api/media/medium/210001626/stock-photo-siberian-husky-dog-lying-autumn?token=",
        imageWidth: 800,
        imageHeight: 600,
        confirmButtonText: 'cerrar'
    })
}

function agrandar1(){
    Swal.fire({
        imageUrl: "https://media.istockphoto.com/photos/woman-zumba-fitness-exercises-dancer-dancing-isolated-silhouette-picture-id817620990",
        imageWidth: 800,
        imageHeight: 600,
        confirmButtonText: 'cerrar'
    })
}
function agrandar2(){
    Swal.fire({
        imageUrl: "https://cdn.pixabay.com/photo/2017/05/29/19/13/fire-and-water-2354583__480.jpg",
        imageWidth: 800,
        imageHeight: 600,
        confirmButtonText: 'cerrar'
    })
}

function agrandar3(){
    Swal.fire({
        imageUrl: "https://cdn.pixabay.com/photo/2017/11/11/21/55/freedom-2940655__480.jpg",
        imageWidth: 800,
        imageHeight: 600,
        confirmButtonText: 'cerrar'
    })
}
// Adds the confirmation section to the document
function confirmation(){
    Swal.fire({
        title: '¿Está seguro que desea agregar esta actividad?',
        showDenyButton: true,
        confirmButtonText: 'Sí, estoy seguro',
        denyButtonText: 'No, no estoy seguro',
      }).then((result) => {
        /* Read more about isConfirmed */
        if (result.isConfirmed && validar() == true) {
            Swal.fire({
                icon: 'success',
                title: '“Hemos recibido su información, muchas gracias y suerte en su actividad',
                confirmButtonText: "Volver al inicio"
            }).then(function() {
                document.getElementById("form").submit();
                window.location = "index.html";
                
            })
        }
        else if(result.isConfirmed && validar() == false){
            Swal.fire({
                icon: 'error',
                title: 'Falta información en el formulario',
                confirmButtonText: "Volver al inicio"
            })
        }
    })
}
