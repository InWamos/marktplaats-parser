import aiohttp
import asyncio
import logging

from typing import AsyncIterable

from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from src.data_handlers.json_data_handler import update_json_file
from src.classes.car_ad import CarAdvertisement
  
logging.basicConfig(
    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
    filename='logger.log',
    filemode='w')


def get_links() -> list[str] | None:
    """Parses .txt with links   

    Returns:
        list: list of parsed links from txt
    """

    with open('links.txt', 'r', encoding='utf-8') as file:
        links = file.readlines()
    
    return links if links else None
    
def get_tasks(session: aiohttp.ClientSession, links: list[str]) -> list | None:
    """It is required for asyncio to create a tasks for executing in parallel.
       This function returns a list of tasks to execute concurrently.

    Args:
        session (aiohttp.ClientSession): aiohttp session
        links (list[str]): list of links

    Returns:
        tasks: a list with tasks
        None: if links is empty
    """

    tasks = []

    for i in links:
        tasks.append(get_last_advertisement(i, session=session))

    return tasks

async def ticker(to: int) -> AsyncIterable:

    for i in range(to):

        yield i

async def get_last_advertisement(link: str, session: aiohttp.ClientSession) -> CarAdvertisement | None:

    final_link = ''
    car_name = ''

    async for i in ticker(6):

        try:

            await asyncio.sleep(4)
            print(i)
            res = await session.get(link)
            bs = BeautifulSoup(await res.text(), features="html.parser")


            tag = bs.find_all("ul")
            final_link = f"https://www.marktplaats.nl{tag[4].find_all('a')[0].get('href')}"
            car_name = tag[4].find_all('h3')[0].contents[0]

            if '-' in final_link:

                print(final_link, car_name)
                return CarAdvertisement(link, final_link, car_name)
                    
        except Exception as e:
            continue


async def send_requests(links: list[str] | None) -> list[CarAdvertisement]:

    link_answer = []

    async with aiohttp.ClientSession() as session:

        if links:
            tasks = get_tasks(session, links)

            responses = await asyncio.gather(*tasks)

            for i in responses:
                if i:

                    link_answer.append(i)
        else:
            logging.info(msg="No elements in list. Skipping...")

        return link_answer
    
async def send_requests_loop(send_update: object) -> None:

    while True:
        try:
            await asyncio.sleep(10)
            links = get_links()

            offers_list = await send_requests(links=links)

            await update_json_file(offers_list, send_update)

        except:
            logging.exception(
                msg="Error in get_advertisement.py in send_requests_loop",
                exc_info=True
            )
            await asyncio.sleep(30)