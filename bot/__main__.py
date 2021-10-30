from bot import BOT_TOKEN
from .plugins import text_message, start_msg
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters
)


if __name__ == "__main__":

    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_msg))
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, text_message))

    updater.start_polling()
    updater.idle()
