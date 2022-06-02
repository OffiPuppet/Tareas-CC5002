function create_layout(title, xlabel, ylabel){
    let layout = {
        title: {
            text: title,
            font: {
                family: 'Courier New, monospace',
                size: 24
            },
            xref: 'paper',
            x: 0.05,
        },
        xaxis: {
            title: {
                text: xlabel,
                font: {
                    family: 'Courier New, monospace',
                    size: 18,
                    color: '#7f7f7f'
                }
            },
        },
        yaxis: {
            title: {
                text: ylabel,
                font: {
                    family: 'Courier New, monospace',
                    size: 18,
                    color: '#7f7f7f'
                }
            }
        }
    };
    return layout;
}

//GRAFICO 1
//Gráfico de líneas que informa la cantidad de actividades por día.
//En el eje X muestra los días y en el eje Y muestra la cantidad de actividades. 
document.addEventListener('DOMContentLoaded', function () {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var line = xmlhttp.responseText;
            let line_div = document.getElementById('lineplot');
            let line_layout = create_layout('N° de eventos por día', 'Fecha', 'Número de eventos');
            Highcharts.chart(line_div, line_layout);
        }
    }
    xmlhttp.open("GET", "glinea.py", true);
    xmlhttp.send();
});

//GRAFICO 2
//Gráfico de torta que muestra el total de actividades por tipo.
document.addEventListener('DOMContentLoaded', function () {
    let chart = Highcharts.chart("pieplot", {
        chart: {
            type: 'pie'
        },
        title: {
            text: 'Cantidad de Actividades por Tipo'
        },
        xAxis: {
            categories: ['tipo1', 'tipo2', 'tipo3','tipo4','tipo5']
        },
        series: [{
            data: [22,55,3,20,0]
        }],
    });
});

//GRAFICO 3
//Gráfico de barras que muestra tres barras por cada punto del eje X.
//El eje X son los meses y para cada mes muestra una barra con la cantidad de actividades que se inician en la
//mañana (antes de las 11:00), la cantidad de actividades que se inician al mediodía (entre las 11:00 y 14:59)
//y la cantidad de actividades que se inician en la tarde (desde las 15:00).
//El eje Y indica la cantidad.

document.addEventListener('DOMContentLoaded', function () {
    const chart = Highcharts.chart("barplot", {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Actividades por mes '
        },
        xAxis: {
            categories: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        },
        yAxis: {
            title: {
                text: 'Cantidad Actividades'
            }
        },
        series: [{
            name: 'Mañana',
            data: [12,11,45,22,22,1, 0, 4,55,65,34,12,3]
        }, {
            name: 'Mediodía',
            data: [12,11,45,22,22,1, 0, 4,55,65,34,12,3]
        },{
            name:'Tarde',
            data:[12,11,45,22,22,1, 0, 4,55,65,34,12,3]
        }]
    });
});