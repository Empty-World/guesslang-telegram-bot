from bot import BOT_TOKEN
from .plugins.commands import start_msg
from .plugins.f import text_message
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
