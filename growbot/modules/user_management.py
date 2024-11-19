"""
user_management.py: Handles user roles, permissions, and preferences.
"""

import logging

logger = logging.getLogger(__name__)

class UserManagement:
    def __init__(self, db_utils):
        """
        Initialize with a database utility instance.
        """
        self.db = db_utils

    def add_user(self, chat_id, role="viewer"):
        """
        Add a user to the database.
        """
        try:
            self.db.insert("users", {"chat_id": chat_id, "role": role})
            logger.info(f"Added user {chat_id} with role {role}.")
        except Exception as e:
            logger.error(f"Failed to add user {chat_id}: {e}")

    def get_user_role(self, chat_id):
        """
        Retrieve a user's role based on chat ID.
        """
        try:
            users = self.db.fetch_all("users")
            for user in users:
                if user["chat_id"] == chat_id:
                    return user["role"]
            logger.warning(f"User {chat_id} not found.")
            return None
        except Exception as e:
            logger.error(f"Failed to fetch user role: {e}")
            return None

    def update_user_role(self, chat_id, new_role):
        """
        Update a user's role.
        """
        try:
            updated = self.db.update("users", Query().chat_id == chat_id, {"role": new_role})
            if updated:
                logger.info(f"Updated role for user {chat_id} to {new_role}.")
            else:
                logger.warning(f"No user {chat_id} found to update.")
        except Exception as e:
            logger.error(f"Failed to update user role: {e}")
