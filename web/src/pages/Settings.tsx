import React from 'react';
import UserForm from '../components/Settings/UserForm';
import TelegramConfig from '../components/Settings/TelegramConfig';
import SecuritySettings from '../components/Settings/SecuritySettings';

const Settings = () => (
    <div>
        <h1 className="text-2xl font-bold">Settings</h1>
        <UserForm />
        <TelegramConfig />
        <SecuritySettings />
    </div>
);

export default Settings;
