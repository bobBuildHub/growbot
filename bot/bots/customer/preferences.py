from utils.db_manager import DBManager

async def command(update, context):
    user_id = update.effective_user.id
    db = DBManager()

    if context.args:
        preference = " ".join(context.args)
        db.update_preference(user_id, preference)
        await update.message.reply_text(f"✅ Your preference has been updated to: {preference}")
    else:
        preference = db.fetch_preference(user_id)
        if preference:
            await update.message.reply_text(f"🔧 Your current preference is: {preference[0]}")
        else:
            await update.message.reply_text("ℹ️ You have no preferences set.")
        