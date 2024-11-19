"""
config_loader.py: Handles configuration loading and validation.
"""

import json
import logging

class ConfigLoader:
    def __init__(self, config_path):
        self.config_path = config_path
        self.config = None

    def load_config(self):
        """
        Load and validate the configuration file.
        """
        try:
            with open(self.config_path, "r") as file:
                self.config = json.load(file)
                self.validate_config()
            return self.config
        except FileNotFoundError:
            raise RuntimeError(f"Config file not found at {self.config_path}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Invalid JSON format in config file: {e}")

    def validate_config(self):
        """
        Validate the required keys in the configuration.
        """
        required_keys = ["tokens", "logging", "database", "thresholds"]
        for key in required_keys:
            if key not in self.config:
                raise ValueError(f"Missing required config key: {key}")

    def get_config(self):
        """
        Return the loaded configuration.
        """
        if not self.config:
            return self.load_config()
        return self.config
