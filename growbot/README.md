# growbot
 GrowBot System
├── main.py                                # Entry point for orchestrating bots.
├── bots/                                  # Contains bot-related scripts.
│   ├── __init__.py                        # Initializes bot modules.
│   ├── customer_bot.py                    # Starts Customer Bot.
│   ├── admin_bot.py                       # Starts Admin Bot.
│   ├── commands/                          # Commands for bots.
│       ├── __init__.py                    # Initializes commands.
│       ├── notification_commands.py       # Handles notification toggling.
│       ├── status_commands.py             # Handles status inquiries.
├── modules/                               # Core system modules.
│   ├── __init__.py                        # Initializes system modules.
│   ├── notifications.py                   # Logic for notifications.
│   ├── energy_management.py               # Logic for energy optimization.
├── utils/                                 # Utility scripts.
│   ├── __init__.py                        # Initializes utilities.
│   ├── db_handler.py                      # Centralized TinyDB access.
│   ├── config_loader.py                   # Configuration loader.
├── web/                                   # Flask-based web interface.
│   ├── app.py                             # Main Flask app.
│   ├── templates/                         # HTML templates.
│       ├── index.html                     # Main dashboard page.
├── config/                                # Configuration files.
│   ├── token.env                          # Bot token storage.
├── logs/                                  # Log files.
└── README.md                              # Documentation.

