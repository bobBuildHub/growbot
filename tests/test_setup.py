
import unittest
import os

class TestSetup(unittest.TestCase):
    def test_directories(self):
        directories = ["logs", "database", "config", "bots", "utils", "tests"]
        for directory in directories:
            self.assertTrue(os.path.exists(directory), f"Directory missing: {directory}")

    def test_files(self):
        files = [
            "config/token.env",
            "config/config.json",
            "database/growbot.db",
            "database/telegram.json",
            "logs/system.log",
            "logs/admin_bot.log",
            "logs/customer_bot.log",
            "bots/admin_bot.py",
            "bots/customer_bot.py",
            "bots/shared_logic.py",
        ]
        for file in files:
            self.assertTrue(os.path.exists(file), f"File missing: {file}")

if __name__ == "__main__":
    unittest.main()
