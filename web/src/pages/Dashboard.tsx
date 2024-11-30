import React from 'react';
import SensorChart from '../components/Dashboard/SensorChart';
// src/pages/Dashboard.tsx
import React from "react";
import DeviceCard from "../components/Dashboard/DeviceCard";

const sampleDevices = [
  { name: "Soil Moisture Sensor", status: "Active" },
  { name: "Temperature Sensor", status: "Inactive" },
];

const Dashboard: React.FC = () => (
  <div className="p-8">
    <h1 className="text-3xl font-bold text-gray-100 mb-6">GrowBot Dashboard</h1>
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {sampleDevices.map((device, index) => (
        <DeviceCard key={index} device={device} />
      ))}
    </div>
  </div>
);

export default Dashboard;


const Dashboard = () => (
    <div>
        <h1 className="text-2xl font-bold">Welcome to GrowBot Dashboard</h1>
        <SensorChart />
    </div>
);

export default Dashboard;
