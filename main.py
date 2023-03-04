import asyncio
import logging
import sys

from src.pyro_modules.bot import Bot
from src.marketplace_requests.get_advertisement import get_advertisements_from_page_loop

logging.basicConfig(
    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
    filename='logger.log',
    filemode='w')


bot_client = Bot("main_bot")
send_pyrogram_message = bot_client.send_message_on_update

async def main() -> None:
    """The point of entry
    """
    try:
        f1 = bot_client.run_bot()
        f2 = get_advertisements_from_page_loop(send_update=send_pyrogram_message)
        tasks = [f1, f2]
        await asyncio.gather(*tasks)

    except:
        logging.exception("Error in the main thread: ", exc_info=True)
        sys.exit(1)


if __name__ == "__main__":

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())