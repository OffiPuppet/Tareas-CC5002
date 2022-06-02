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
function requestLine(){
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
}
function requestPie() {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var pie = xmlhttp.responseText;
            let pie_div = document.getElementById("pieplot");
            Highcharts.chart(pie_div, create_layout('Porcentaje de eventos por tipo', '', ''));
        }
    }
    xmlhttp.open("GET", "gtorta.py", true);
    xmlhttp.send();
}
function requestBar(){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            var bar = xmlhttp.responseText;
            let bar_div = document.getElementById('barplot');
            let layout = create_layout('N° de eventos según mes y hora del día', 'Mes', 'Cantidad')
            Highcharts.chart(bar_div, layout);
        }
    }
    xmlhttp.open("GET", "gbarra.py", true);
    xmlhttp.send();
}

requestLine();
requestPie();
requestBar();