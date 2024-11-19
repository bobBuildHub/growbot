"""
visualization.py: Advanced graph generation logic.
"""

import matplotlib.pyplot as plt
from datetime import datetime
import os
from utils.logger import setup_logger

logger = setup_logger("visualization", "logs/growbot.log")

def generate_graph(data, title="Metric Graph", filename="graphs/metric_graph.png"):
    """
    Generate a graph from the provided data and save it.
    """
    try:
        x, y = zip(*data.items())
        plt.figure(figsize=(10, 5))
        plt.plot(x, y, marker="o")
        plt.title(title)
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.grid()
        plt.savefig(filename)
        logger.info(f"Graph saved as {filename}")
        return filename
    except Exception as e:
        logger.error(f"Failed to generate graph: {e}")
        return None
