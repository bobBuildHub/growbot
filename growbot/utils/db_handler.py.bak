from tinydb import TinyDB, Query
from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware

class DatabaseHandler:
    """
    Centralized handler for TinyDB interactions.
    Provides methods for managing thresholds, logs, metrics, and preferences.
    """

    def __init__(self, db_path="db/growbot.json"):
        """
        Initialize the database with caching to improve performance.
        :param db_path: Path to the TinyDB file.
        """
        self.db = TinyDB(db_path, storage=CachingMiddleware(JSONStorage))
        self.thresholds = self.db.table("thresholds")
        self.preferences = self.db.table("preferences")
        self.logs = self.db.table("logs")
        self.metrics = self.db.table("metrics")

    def get_threshold(self, name):
        """
        Retrieve a threshold value by its name.
        :param name: Name of the threshold to retrieve.
        :return: Threshold value or None if not found.
        """
        result = self.thresholds.get(Query().name == name)
        return result["value"] if result else None

    def set_threshold(self, name, value):
        """
        Update or insert a threshold.
        :param name: Name of the threshold.
        :param value: Value to set for the threshold.
        """
        self.thresholds.upsert({"name": name, "value": value}, Query().name == name)

    def log_event(self, event_type, message):
        """
        Add an event log.
        :param event_type: Type of event (info, warning, error).
        :param message: Event message to log.
        """
        self.logs.insert({"type": event_type, "message": message})

    def add_metric(self, name, value):
        """
        Add a metric to the database.
        :param name: Name of the metric.
        :param value: Metric value.
        """
        self.metrics.insert({"name": name, "value": value})

    def get_metrics(self, name):
        """
        Retrieve all metrics of a given name.
        :param name: Metric name to search.
        :return: List of metrics matching the name.
        """
        return self.metrics.search(Query().name == name)
