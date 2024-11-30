import logging
import os

# Initialize logging
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/growbot.log",
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger("GrowBotLogger")
