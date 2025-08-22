from telethon.tl.types import InputInvoiceStarGift, PeerUser, PeerChannel
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
        try:
            int(self.config["receiver"])

            try:
                receiver = await self.client.get_input_entity(PeerUser(int(self.config["receiver"])))

            except:
                receiver = await self.client.get_input_entity(PeerChannel(int(self.config["receiver"])))

        except:
            receiver = await self.client.get_input_entity(PeerUser(self.config["receiver"]))

        bought = 0

        while True:
            gifts_queue = await self.queue.get()

            if gifts_queue:
                logger.info(f"RECEIVED {len(gifts_queue)} GIFTS FROM CHECKER QUEUE")

            else:
                continue

            for gift in gifts_queue:
                success = await self.try_buy(
                    gift,
                    receiver,
                    self.config["hide"]
                )

                if success:
                    bought += 1
                    entity = await self.client.get_entity("me")
                    stars = await self.client(functions.payments.GetStarsStatusRequest(peer=entity))
                    logger.info(f"BOUGHT: {bought}")
                    logger.info(f"STARS REMAINING: {stars.balance.amount}")

                await sleep(0.1)