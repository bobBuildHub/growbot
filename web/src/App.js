import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Alerts from './pages/Alerts';
import Settings from './pages/Settings';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/alerts" element={<Alerts />} />
                <Route path="/settings" element={<Settings />} />
            </Routes>
        </Router>
    );
}

export default App;
