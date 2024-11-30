import React from 'react';
import { Link } from 'react-router-dom';

const Sidebar = () => (
    <nav className="w-64 h-screen bg-gray-800 text-white">
        <ul className="p-4">
            <li><Link to="/">Dashboard</Link></li>
            <li><Link to="/devices">Devices</Link></li>
            <li><Link to="/alerts">Alerts</Link></li>
            <li><Link to="/settings">Settings</Link></li>
        </ul>
    </nav>
);

export default Sidebar;
