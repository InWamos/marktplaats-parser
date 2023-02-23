import asyncio
import logging
import sys

from src.pyro_modules.bot import Bot
from src.marketplace_requests.get_advertisement import send_requests_loop

logging.basicConfig(
    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
    filename='logger.log',
    filemode='w')


bot_client = Bot("main_bot")
send_pyrogram_message = bot_client.send_message_on_update

async def main() -> None:
    try:
        f1 = send_requests_loop(send_update=send_pyrogram_message)
        f2 = bot_client.run_bot()
        tasks = [f1, f2]
        await asyncio.gather(*tasks)

    except:
        logging.exception("Error in the main thread: ", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())