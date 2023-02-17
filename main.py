import asyncio
import logging
from threading import Thread
from src.pyro_modules.bot import Bot
from src.data_handlers.json_data_handler import update_json_file
from src.marketplace_requests.get_advertisement import send_requests, get_links

logging.basicConfig(
    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
    filename='logger.log',
    filemode='w')

async def main() -> None:
    try:
        _bot = Bot()
        lo = await send_requests(get_links())
        await update_json_file(lo, _bot._bot)

    except:
        logging.exception("Error in the main thread: ", exc_info=True)    

if __name__ == "__main__":
    asyncio.run(main())