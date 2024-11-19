"""
notifications.py: Module for handling notification settings.
"""

from utils.db_utils import DatabaseUtils

# Initialize database for notifications
db = DatabaseUtils("data/notifications.json")

def toggle_notifications(user_id):
    """
    Toggle notification settings for a user.

    Args:
        user_id (int): The Telegram user ID.

    Returns:
        bool: The updated notification status (True for enabled, False for disabled).
    """
    try:
        # Fetch user notification status
        user_data = db.fetch("notifications", {"user_id": user_id})
        current_status = user_data[0]["enabled"] if user_data else False

        # Toggle the status
        new_status = not current_status
        if user_data:
            db.update("notifications", {"enabled": new_status}, {"user_id": user_id})
        else:
            db.insert("notifications", {"user_id": user_id, "enabled": new_status})

        return new_status
    except Exception as e:
        raise RuntimeError(f"Failed to toggle notifications for user {user_id}: {e}")
