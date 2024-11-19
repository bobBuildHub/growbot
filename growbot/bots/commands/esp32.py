"""
esp32.py: Handles ESP32 integration.
"""

import time
import requests
import json
from utils.logger import setup_logger

logger = setup_logger("esp32", "logs/growbot.log")

class ESP32:
    """
    Class to handle ESP32 operations.
    """

    def __init__(self, config_path="config/esp32_config.json"):
        """
        Initialize ESP32 with configuration.
        """
        try:
            with open(config_path, "r") as config_file:
                self.config = json.load(config_file)
                self.ip = self.config.get("ip", "192.168.1.100")
                logger.info(f"ESP32 initialized with IP: {self.ip}")
        except Exception as e:
            logger.error(f"Failed to load ESP32 configuration: {e}")
            raise

    def check_status(self):
        """
        Check ESP32 connectivity status.
        """
        try:
            response = requests.get(f"http://{self.ip}/status", timeout=5)
            if response.status_code == 200:
                logger.info("ESP32 is online.")
                return response.json()
            else:
                logger.warning("ESP32 responded with an error.")
                return {"status": "error"}
        except Exception as e:
            logger.error(f"ESP32 connectivity check failed: {e}")
            return {"status": "offline"}

    def send_command(self, command):
        """
        Send a command to the ESP32.
        """
        try:
            response = requests.post(f"http://{self.ip}/command", json={"command": command}, timeout=5)
            if response.status_code == 200:
                logger.info(f"Command '{command}' executed successfully on ESP32.")
                return response.json()
            else:
                logger.warning(f"Failed to execute command '{command}' on ESP32.")
                return {"status": "error"}
        except Exception as e:
            logger.error(f"ESP32 command execution failed: {e}")
            return {"status": "offline"}
