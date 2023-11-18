const socket = io();

// charts

const ctx = document.getElementById('speedGraph').getContext('2d');
chart = new Chart(ctx, {
    type: 'line',
    data: {
        datasets: [{
            label: 'Vehicle speed',
            borderColor: 'rgba(75, 192, 192, 1)',
            fill: false,
        }]
    },
    options: {
        responsive: true,
        scales: {
            x: {
                reverse: true,
                title: {
                    display: true,
                    text: 'Time',
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Speed'
                }
            }
        }
    }
});

// account



// websockets

socket.on('connect', function(data) {
    console.log('socket.io is connected')
});

socket.on('account_info', function(data) {
    console.log(data);

// car model
    const car_model = document.getElementById('index-car-model');
    car_model.innerHTML = data;
});

socket.on('obd_status', function(data) {
    console.log(data);
    const status = document.getElementById('obd-status');
    status.innerHTML = data;
});

socket.on('obd_speed', function(data) {

    const time = data[0]; // Assuming data[0] is the time value
    const speed = data[1]; // Assuming data[1] is the speed value
    const maxDataPoints = 8; // Adjust this value as needed

    const status = document.getElementById('obd-speed');
    status.innerHTML = speed;

    // Get a reference to the chart's data
    const chartData = chart.data.datasets[0].data;

    // Unshift the new data points to the beginning of the chart dataset
    chartData.unshift({ x: time, y: speed });

    // Remove data points if the number of data points exceeds maxDataPoints
    while (chartData.length > maxDataPoints) {
        chartData.pop(); // Remove the oldest data point from the end
    }

    // Update the chart
    chart.update();

});

socket.on('obd_rpm', function(data) {
    console.log("obd rpm "+data);
    const status = document.getElementById('obd-rpm');
    status.innerHTML = data;
});

socket.on('obd_dtc', function(data) {
    console.log("obd dtc "+data);
    const status = document.getElementById('obd-dtc');
    status.innerHTML = data;
});

socket.on('obd_error', function(data) {
    console.log("obd errors "+data);
    const status = document.getElementById('obd-error');
    status.innerHTML = data;
});

socket.on('rpi_uptime', function(data) {
    const status = document.getElementById('rpi-uptime');
    status.innerHTML = data;
});