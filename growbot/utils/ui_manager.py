"""
ui_manager.py: Inline keyboards for bot interaction.
"""

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

class UIManager:
    @staticmethod
    def main_menu():
        """
        Create the main menu inline keyboard.
        """
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("📊 Status", callback_data="status")],
            [InlineKeyboardButton("⚙️ Preferences", callback_data="preferences")],
            [InlineKeyboardButton("🔔 Notifications", callback_data="notifications")]
        ])
