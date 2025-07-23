import json
from os import path

CONFIG_PATH = "config.json"

DEFAULT_CONFIG = {
    "api_id": "", # Your api_id from Telegram App Configuration
    "api_hash": "", # Your api_hash from Telegram App Configuration
    "receiver": "", # Your Telegram username/id to receive gifts
    "limited": True, # True if you want to buy limited gifts or False to not
    "blacklist": [], # A list with the id of unwanted gifts
    "hide": False, # True if you want to buy gifts with an anonymous signature or False to not
    "cycles": 10, # Number of gift buying cycles
    "start": 150, # Start range price
    "end": 10000 # End range price
}

def load_config():

    if not path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "w", encoding="utf-8") as fp:
            json.dump(DEFAULT_CONFIG, fp, indent=4)

        return DEFAULT_CONFIG

    with open(CONFIG_PATH, "r", encoding="utf-8") as fp:
        return json.load(fp)
