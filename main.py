import asyncio
from telethon import TelegramClient

from config.logger import logger
from config.manager import load_config
from checker import Checker
from buyer import Buyer


async def main():
    config = load_config()
    client = TelegramClient("session", config["api_id"], config["api_hash"], system_version="4.16.30-vxCUSTOM")
    await client.start()

    queue = asyncio.Queue()
    checker = Checker(client, queue)
    buyer = Buyer(client, queue)

    await asyncio.gather(
        checker.run(),
        buyer.run()
    )

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.warning(f"SCRIPT WAS STOPPED")
    except Exception as e:
        logger.error(f"ERROR: {e}")