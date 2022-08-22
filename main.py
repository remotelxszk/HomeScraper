from config import *
from getData import get_data
from telegramBot import send_message_to_telegram_group
import lastRun as lr

from time import sleep
from unidecode import unidecode

def main(bot_chat_id):
    last_run = lr.get_last_run_time_stamp()
    print("Last run: " + last_run.strftime("%H:%M, %d %b, %Y"))
    print("Webscrapping in progress")
    items = get_data(base_url, category, location, additionalFilters)
    print("Webscrapping finished")
    i = 0 
    for item in items:
        if filter_item(item) and i <= telegram_message_limit:
            i += 1
            formatted_string = format_item(item)
            send_message_to_telegram_group(formatted_string, bot_chat_id)
            sleep(0.3)
    lr.save_last_run_time_stamp()

def format_item(item):
    string_without_link = "\n".join([item["listing_title"], item["listing_price"], item['location']]) + "\nDate:" + item['date']
    if "otodom" in item['link']:
        link = "\n" + item['link']
        return string_without_link + link
    else:
        link = "\n" + base_url + item['link']
        return string_without_link + link

def filter_item(item):
    return "Dzisiaj" in item["date"] and lr.check_time_against_last_run(item["date"]) and any(x in unidecode(item["location"]) for x in neighbourhoods)

if __name__ == "__main__":
    main(bot_group_chat_id)