import asyncio
import logging

from src.pyro_modules.bot import Bot
from src.marketplace_requests.get_advertisement import send_requests_loop, get_links

logging.basicConfig(
    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
    filename='logger.log',
    filemode='w')

async def main() -> None:
    try:
        bot_client = Bot("main_bot")
        f1 = send_requests_loop(links=get_links(), client=bot_client.get_bot())
        f2 = bot_client.run()
        tasks = [f1, f2]
        await asyncio.gather(*tasks)

    except:
        logging.exception("Error in the main thread: ", exc_info=True)    

if __name__ == "__main__":
    asyncio.run(main())