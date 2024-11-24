from utils.db_manager import DBManager

async def command(update, context):
    db = DBManager()
    logs = db.fetch_logs(limit=5)
    logs_text = "\n".join([f"{log[2]} - {log[1]}" for log in logs])
    await update.message.reply_text(f"📝 Latest Logs:\n{logs_text}")
        