import time

from config import autorun_delay
import main

autorun_enabled = True

def func(bot_chat_id):
    main.main(bot_chat_id)

def start(bot_chat_id):
    while autorun_enabled:
        func(bot_chat_id)
        time.sleep(autorun_delay)