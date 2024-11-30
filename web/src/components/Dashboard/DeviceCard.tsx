// src/components/Dashboard/DeviceCard.tsx
import React from "react";

interface Device {
  name: string;
  status: string;
}

interface DeviceCardProps {
  device: Device;
}

const DeviceCard: React.FC<DeviceCardProps> = ({ device }) => (
  <div className="border rounded p-4 bg-gray-900 text-gray-100 shadow-md">
    <h2 className="text-lg font-bold">{device.name}</h2>
    <p>Status: <span className="font-semibold">{device.status}</span></p>
    <button className="mt-4 bg-blue-500 hover:bg-blue-600 text-white px-4 py-2 rounded">
      Control
    </button>
  </div>
);

export default DeviceCard;
