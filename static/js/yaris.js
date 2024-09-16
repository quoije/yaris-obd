const socket = io();
// map

var map = L.map('map').setView([48.505, -0.09], 13);
            L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            }).addTo(map);
            L.marker([51.5, -0.09]).addTo(map)
            .bindPopup('your car... soon(tm)')
            .openPopup();

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

// websockets

socket.on('connect', function(data) {
    console.log('socket.io is connected')
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

socket.on('obd_error', function(data) {
    console.log("obd errors "+data);
    const status = document.getElementById('obd-error');
    status.innerHTML = data;
});

socket.on('rpi_uptime', function(data) {
    const status = document.getElementById('rpi-uptime');
    status.innerHTML = data;
});

socket.on('gps_location', function(data) {
    console.log("location received")
    const LocationX = document.getElementById('gpsLocationX');
    const LocationY = document.getElementById('gpsLocationY');
    LocationX.innerHTML = data[0];
    LocationY.innerHTML = data[1];

});