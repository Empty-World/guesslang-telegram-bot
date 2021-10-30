from telegram import Update
from telegram.ext import CommandHandler

def start_msg(update: Update,_) -> None:
    """
    telegram  start command replay message
    """
    update.message.reply_text("Hello,  World")