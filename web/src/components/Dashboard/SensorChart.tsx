import React from 'react';
import { Line } from 'react-chartjs-2';

const SensorChart = () => {
    const data = {
        labels: ['January', 'February', 'March', 'April', 'May'],
        datasets: [
            {
                label: 'Temperature',
                data: [65, 59, 80, 81, 56],
                fill: false,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1
            }
        ]
    };

    return <Line data={data} />;
};

export default SensorChart;
