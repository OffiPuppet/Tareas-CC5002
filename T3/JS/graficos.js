function create_layout(title, xlabel, ylabel, datos){
    let X_axis = [];
    let info_dia = [];
    for (let i = 0; i < datos.length; i++) {
        X_axis.push(datos[i][0]);
        info_dia.push({
            name: datos[i][0],
            y: datos[i][1]
        })
    }
    console.log(datos);
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
            categories: X_axis
        },
        yaxis: {
            title: {
                text: ylabel,
                font: {
                    family: 'Courier New, monospace',
                    size: 18,
                    color: '#7f7f7f'
                }
            },
        },
        series: [{
            data: info_dia
        }],
        responsive: {
            rules: [{
                condition: {
                    maxWidth: 500
                },
                chartOptions: {
                    legend: {
                        layout: 'horizontal',
                        align: 'center',
                        verticalAlign: 'bottom'
                    }
                }
            }]
        }
    };
    return layout;
}

function create_layout1(title, xlabel, ylabel, datos){
    let layout = {
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: title,
            font: {
                family: 'Courier New, monospace',
                size: 24
            },
            xref: 'paper',
            x: 0.05,
        },
        tooltip: {
            pointFormat: '{series.name}: <br>{point.percentage:.1f} %<br>cantidad: {point.y}'
          },
        plotOptions: {
            pie: {
              dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>:<br>{point.percentage:.1f} %<br>cantidad: {point.y}',
              }
            }
        },
        series: [{
            name: 'Porcentaje',
            colorByPoint: true,
            data: [{
                name: datos["labels"][0],
                y: datos["values"][0],
                sliced: true,
                selected: true
            }, {
                name: datos["labels"][1],
                y: datos["values"][1]
            }, {
                name: datos["labels"][2],
                y: datos["values"][2]
            }, {
                name: datos["labels"][3],
                y: datos["values"][3]
            }, {
                name: datos["labels"][4],
                y: datos["values"][4]
            }, {
                name: datos["labels"][5],
                y: datos["values"][5]
            }, {
                name: datos["labels"][6],
                y: datos["values"][6]
            }, {
                name: datos["labels"][7],
                y: datos["values"][7]
            }, {
                name: datos["labels"][8],
                y: datos["values"][8]
            }, {
                name: datos["labels"][9],
                y: datos["values"][9]
            }]
        }]
    };
    return layout;
}

function create_layout2(title, xlabel, ylabel, datos){
    let X_axis1 = [];
    let info_dia = [];
    for (let i = 0; i < datos.length; i++) {
        X_axis1.push(datos[i][0]);
        info_dia.push({
            name: datos[i][0],
            y: datos[i][1]
        })
    }
    console.log(datos[0]["x"]);
    let layout = {
        chart: {
            type: 'bar'
        },
        title: {
            text: title,
            font: {
                family: 'Courier New, monospace',
                size: 24
            },
            xref: 'paper',
            x: 0.05,
        },
        xAxis: {
            categories: datos[0]["x"],
            title: {
                text: xlabel,
                font: {
                    family: 'Courier New, monospace',
                    size: 18,
                    color: '#7f7f7f'
                }
            }
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
        },
        series: [{
            name: datos[0]["name"],
            data: datos[0]["y"],
        },{
            name: datos[1]["name"],
            data: datos[1]["y"],
        },{
            name: datos[2]["name"],
            data: datos[2]["y"],
        }]

    };
    return layout;
}