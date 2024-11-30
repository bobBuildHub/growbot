import unittest
from utils.db_manager import DBManager
from utils.tinydb_manager import TinyDBManager
import os

class TestDatabases(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Setup databases for testing.
        """
        cls.sqlite_db = DBManager(db_path="test_database/test_growbot.db", encryption_key=b'sample_encryption_key_32bytes')
        cls.tinydb = TinyDBManager(db_path="test_database/test_telegram.json")

    def test_sqlite_interactions(self):
        """
        Test SQLite user interaction logging.
        """
        self.sqlite_db.cursor.execute("INSERT INTO user_interactions (username, command) VALUES ('test_user', 'start')")
        self.sqlite_db.conn.commit()
        result = self.sqlite_db.cursor.execute("SELECT * FROM user_interactions WHERE username = 'test_user'").fetchone()
        self.assertIsNotNone(result, "SQLite failed to log interaction.")

    def test_tinydb_insert(self):
        """
        Test TinyDB data insertion.
        """
        self.tinydb.insert_data("telegram", {"user_id": 1, "command": "start"})
        result = self.tinydb.fetch_data("telegram", lambda q: q.user_id == 1)
        self.assertGreater(len(result), 0, "TinyDB failed to insert or fetch data.")

    @classmethod
    def tearDownClass(cls):
        """
        Clean up test databases.
        """
        cls.sqlite_db.close()
        cls.tinydb.close()
        os.remove("test_database/test_growbot.db")
        os.remove("test_database/test_telegram.json")
        os.rmdir("test_database")

if __name__ == "__main__":
    unittest.main()
