from bot import BOT_TOKEN
from .plugins.commands import start_msg
from telegram.ext import Updater, CommandHandler



if __name__ == "__main__":

    updater = Updater(BOT_TOKEN)

    updater.dispatcher.add_handler(CommandHandler('start', start_msg))

    updater.start_polling()
    updater.idle()
