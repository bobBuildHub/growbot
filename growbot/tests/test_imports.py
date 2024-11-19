# growbot/tests/test_imports.py
from utils.db_utils import DatabaseUtils
from modules.notifications import toggle_notifications

db_utils = DatabaseUtils()
print("Imports are working correctly!")
