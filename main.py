import asyncio
import logging
from threading import Thread

from src.pyro_modules.bot import Bot
from src.marketplace_requests.get_advertisement import send_requests_loop, get_links

logging.basicConfig(
    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
    filename='logger.log',
    filemode='w')

async def main() -> None:
    try:
        _bot = Bot()

        loops = [
            send_requests_loop(links=get_links(), client=_bot._bot),
            _bot.run()
        ]
        await asyncio.gather(*loops)

    except:
        logging.exception("Error in the main thread: ", exc_info=True)    

if __name__ == "__main__":
    asyncio.run(main())