from asyncio import sleep, Queue
from telethon import functions

from config.logger import logger
from config.manager import load_config


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
                filtered = [g for g in gifts.gifts if not g.sold_out
                            and g.limited == True
                            and self.config["start"] <= g.stars <= self.config["end"]
                            and g.availability_total <= self.config["max_supply"]]

                if filtered:
                    logger.info(f"FOUND {len(filtered)} GIFTS MATCHING CRITERIA")
                    for _ in range(self.config["cycles"]):
                        await self.queue.put(filtered)
                    await sleep(3600)

                else:
                    logger.info("NO GIFTS FOUND MATCHING CRITERIA")

            except Exception as e:
                logger.error(f"CHECKER FAILED: {e}")

            await sleep(5)