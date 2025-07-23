from telethon.tl.types import InputInvoiceStarGift
from telethon import functions

from config.manager import load_config
from config.logger import logger
from asyncio import Queue, sleep


class Buyer:
    def __init__(self, client, queue: Queue):
        self.client = client
        self.queue = queue
        self.config = load_config()

    async def try_buy(self, gift, receiver, hide):

        try:
            invoice = InputInvoiceStarGift(
                peer=receiver,
                gift_id=gift.id,
                hide_name=hide
            )

            form = await self.client(functions.payments.GetPaymentFormRequest(invoice=invoice))

            await self.client(functions.payments.SendStarsFormRequest(
                form_id=form.form_id,
                invoice=invoice)
            )

            logger.info(f"GIFT {gift.id} SUCCESSFULLY BOUGHT TO {self.config["receiver"]}")

            return True

        except Exception as e:
            logger.error(f"FAILED TO BUY GIFT {gift.id}: {e}")

            return False

    async def run(self):
        logger.info("BUYER STARTED")
        receiver = await self.client.get_input_entity(self.config["receiver"])

        while True:
            gifts = await self.queue.get()
            logger.info(f"RECEIVED {len(gifts)} GIFTS FROM CHECKER QUEUE")

            for cycle in range(self.config["cycles"]):
                bought = 0

                for gift in gifts:
                    success = await self.try_buy(
                        gift,
                        receiver,
                        self.config["hide"]
                    )

                    if success:
                        bought += 1
                        entity = await self.client.get_entity(receiver)
                        stars = await self.client(functions.payments.GetStarsStatusRequest(peer=entity))
                        logger.info(f"CYCLE {cycle + 1}: BOUGHT {bought} of gift {gift.id}")
                        logger.info(f"STARS REMAINING: {stars.balance.amount}")

                    await sleep(0.5)
