import unittest
import os
from utils.config_loader import ConfigLoader

class TestGrowBot(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Load configuration before running tests.
        """
        cls.config_loader = ConfigLoader("config/config.json", "config/token.env")
        cls.config = cls.config_loader.get_config()

    def test_env_file(self):
        """
        Ensure the .env file loads correctly.
        """
        self.assertTrue(os.getenv("ADMIN_BOT_TOKEN"), "Admin bot token not loaded")
        self.assertTrue(os.getenv("CUSTOMER_BOT_TOKEN"), "Customer bot token not loaded")

    def test_config_file(self):
        """
        Validate the structure of the configuration file.
        """
        required_keys = ["tokens", "logging", "database", "thresholds", "notifications"]
        for key in required_keys:
            self.assertIn(key, self.config, f"Missing key: {key}")

    def test_token_validity(self):
        """
        Verify tokens are correctly set and not placeholders.
        """
        admin_token = self.config["tokens"]["admin_bot"]
        customer_token = self.config["tokens"]["customer_bot"]
        self.assertNotEqual(admin_token, "YOUR_ADMIN_BOT_TOKEN", "Invalid Admin Bot Token")
        self.assertNotEqual(customer_token, "YOUR_CUSTOMER_BOT_TOKEN", "Invalid Customer Bot Token")

    def test_logging_setup(self):
        """
        Ensure logging configuration is valid.
        """
        logging_config = self.config["logging"]
        self.assertIn("level", logging_config)
        self.assertIn("file", logging_config)
        self.assertIn("format", logging_config)

if __name__ == "__main__":
    unittest.main()
