from asyncio import sleep, Queue
from config.logger import logger
from config.manager import load_config
from telethon import functions
import random

class Checker:
    def __init__(self, client, queue: Queue):
        self.client = client
        self.queue = queue
        self.config = load_config()

    async def run(self):
        logger.info("CHECKER STARTED")

        while True:

            try:
                gifts = await self.client(functions.payments.GetStarGiftsRequest(hash=0))
                logger.info("FETCHED GIFTS FROM TELEGRAM")
                filtered = [g for g in gifts.gifts if not g.sold_out and g.id not in self.config["blacklist"] and
                            g.limited == self.config["limited"] and self.config["start"] <= g.stars <= self.config["end"]]

                if filtered:
                    logger.info(f"FOUND {len(filtered)} GIFTS MATCHING CRITERIA")
                    for _ in range(self.config["cycles"]):
                        await self.queue.put(filtered)
                    await sleep(3600)

                else:
                    logger.info("NO GIFTS FOUND MATCHING CRITERIA")

            except Exception as e:
                logger.error(f"CHECKER FAILED: {e}")

            await sleep(random.randint(15, 30))