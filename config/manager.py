import json
from os import path

CONFIG_PATH = "config.json"

DEFAULT_CONFIG = {
    "api_id": "", # Your api_id from Telegram App Configuration
    "api_hash": "", # Your api_hash from Telegram App Configuration
    "receiver": "", # Your Telegram username/id or channel id to receive gifts
    "hide": True, # True if you want to buy gifts with an anonymous signature or False to not
    "cycles": 5, # Number of gift buying cycles
    "start": 1000, # Start range price
    "end": 10000, # End range price
    "max_supply": 100000 # Maximum supply range
}

def load_config():

    if not path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "w", encoding="utf-8") as fp:
            json.dump(DEFAULT_CONFIG, fp, indent=4)

        return DEFAULT_CONFIG

    with open(CONFIG_PATH, "r", encoding="utf-8") as fp:
        return json.load(fp)
