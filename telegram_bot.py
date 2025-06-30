
import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'internship_project.settings')
django.setup()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from core.models import TelegramUser

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.from_user.username
    chat_id = update.message.chat_id

    TelegramUser.objects.get_or_create(username=username, chat_id=chat_id)
    await update.message.reply_text(f"Hello @{username}, you're registered!")

def main():
    app = ApplicationBuilder().token('your tel_api').build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()
