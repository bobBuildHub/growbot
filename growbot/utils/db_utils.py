"""
db_utils.py: Utility functions for database interaction using TinyDB.
"""

import logging
from tinydb import TinyDB, Query
from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/db_utils.log")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class DatabaseUtils:
    def __init__(self, db_path):
        """
        Initialize TinyDB database.
        """
        try:
            self.db = TinyDB(db_path, storage=CachingMiddleware(JSONStorage))
            logger.info(f"Database initialized at {db_path}")
        except Exception as e:
            logger.error(f"Database initialization failed: {e}")
            raise

    def insert(self, table_name, data):
        """
        Insert data into a specific table.
        """
        try:
            table = self.db.table(table_name)
            record_id = table.insert(data)
            logger.info(f"Inserted record {record_id} into table '{table_name}'")
            return record_id
        except Exception as e:
            logger.error(f"Insert failed for table '{table_name}': {e}")
            raise

    def fetch(self, table_name, query):
        """
        Fetch data from a specific table using a query.
        """
        try:
            table = self.db.table(table_name)
            return table.search(Query().fragment(query))
        except Exception as e:
            logger.error(f"Fetch failed for table '{table_name}': {e}")
            raise

    def update(self, table_name, updates, query):
        """
        Update records in a specific table using a query.
        """
        try:
            table = self.db.table(table_name)
            table.update(updates, Query().fragment(query))
            logger.info(f"Updated records in table '{table_name}'")
        except Exception as e:
            logger.error(f"Update failed for table '{table_name}': {e}")
            raise
