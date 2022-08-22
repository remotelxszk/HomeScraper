import telegram
from telegram.ext import Updater, CallbackContext, CommandHandler
import logging
import autorun

from config import bot_api_key, autorun_delay

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

updater = Updater(token=bot_api_key, use_context=True)
dispatcher = updater.dispatcher

def start(update: telegram.Update, context: CallbackContext):
    bot_chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=bot_chat_id, text=("Starting refresh every" + str(autorun_delay) + " second/s."))
    autorun.autorun_enabled = True
    autorun.start(bot_chat_id)

def stop(update: telegram.Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Refresh stopped.")
    autorun.autorun_enabled = False


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

stop_handler = CommandHandler('stop', stop)
dispatcher.add_handler(stop_handler)

def send_message_to_telegram_group(message, bot_chat_id):
    bot = telegram.Bot(bot_api_key)
    bot.send_message(text=message, chat_id=bot_chat_id)

def telegram_bot_setup(bot_api_key):
    bot = telegram.Bot(bot_api_key)
    print(bot.get_me())
    print(bot.get_updates())

if __name__ == "__main__":
    telegram_bot_setup(bot_api_key)
    updater.start_polling() # answer messages from telegram
