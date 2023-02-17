import asyncio
import logging

from src.pyro_modules.bot import Bot
from src.marketplace_requests.get_advertisement import send_requests_loop, get_links

logging.basicConfig(
    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
    filename='logger.log',
    filemode='w')

bot_client = Bot("main_bot")

async def main() -> None:
    try:
        f1 = send_requests_loop(links=get_links(), client=bot_client.get_bot())
        f2 = bot_client.run_bot()
        tasks = [f1, f2]
        await asyncio.gather(*tasks)

    except:
        logging.exception("Error in the main thread: ", exc_info=True)    

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())