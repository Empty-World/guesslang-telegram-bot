from telegram import Update
from ..utils.gess_lang import gess_language_name

def text_message(update: Update, _) -> None:
    """
    get from user text
    """
    print(update.message.text)
