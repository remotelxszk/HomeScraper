# Parameters :)
base_url = "https://www.olx.pl"
category = "d/nieruchomosci/mieszkania/wynajem"
location = "warszawa"
additionalFilters = [
    "?search%5Border%5D=created_at:desc", #order by the newest
    "search%5Bfilter_enum_rooms%5D%5B0%5D=one", #single room flat
    "search%5Bfilter_enum_rooms%5D%5B1%5D=two", #double room flat
    "search%5Bfilter_float_m:from%5D=25", #min square meters
    "search%5Bfilter_float_price:from%5D=1500", #min price
    "search%5Bfilter_float_price:to%5D=2700" #max price
]

neighbourhoods = [
    "Srodmiescie",
    "Ochota",
    "Wola"
]

# Trying to avoid posting too much listings at the same time as it crashes the bot
# Telegram has a limit of 20 so maybe keep it to 15 just to be safe
telegram_message_limit = 15

autorun_delay = 330 # Just a random 5 and a half minutes, probably could lower that

bot_api_key = ""
bot_group_chat_id = 000000 # No longer needed, bot answers to direct /start message
