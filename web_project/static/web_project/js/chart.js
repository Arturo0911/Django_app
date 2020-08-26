$(document).ready(function(){
    //alert('hola mundo');
    const ctx = document.getElementById('Mychart').getContext('2d');
    var scatterChart = new Chart(ctx, {
        type: 'scatter',
        data: {
            datasets: [{
                label: 'Scatter Dataset',
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: [{
                    x: 3,
                    y: 5
                }, {
                    x: 7,
                    y: 8
                }, {
                    x: 8,
                    y: 8
                },{
                    x: 9,
                    y: 10
                },{
                    x: 4,
                    y: 3
                },{
                    x: 2,
                    y: 2
                },{
                    x: 5,
                    y: 3
                },{
                    x: 10,
                    y: 8
                },{
                    x: 8,
                    y: 9
                },{
                    x: 7,
                    y: 8
                }]
            }]
        },
        options: {
            scales: {
                xAxes: [{
                    type: 'linear',
                    position: 'bottom'
                }]
            }
        }
    });

    //alert('holis')
    $.ajax({
        method:'GET' ,
        url: 'http://127.0.0.1:8000/predictions/api/',
        success: function(response){
            console.log(response);
        },
        error: function(){
            console.log('error while fetching data from Python');
        }
    });

    
});