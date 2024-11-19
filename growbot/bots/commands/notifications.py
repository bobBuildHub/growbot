from utils.db_utils import DatabaseUtils

db = DatabaseUtils("data/notifications.json")

def toggle_notifications(user_id):
    """Toggle notifications for a user."""
    current_status = db.get(user_id, "notifications")
    new_status = not current_status
    db.set(user_id, "notifications", new_status)
    return new_status
