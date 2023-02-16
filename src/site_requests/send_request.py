from typing import AsyncIterable
import aiohttp
import asyncio
from bs4 import BeautifulSoup
from dataclasses import dataclass

@dataclass
class LastOffer:
    link_to_page: str
    link_to_advertisement: str
    name: str

    def __str__(self) -> str:
        return f"Новый автомобиль!\n🚘 Название: {self.name}\n🔗 Ссылка: {self.link_to_advertisement}"
    

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

async def get_last_advertisement(link: str, session: aiohttp.ClientSession) -> LastOffer | None:

    final_link = ''
    car_name = ''
    counter = 0

    async for i in ticker(6):

        try:

            await asyncio.sleep(2)
            
            res = await session.get(link)
            bs = BeautifulSoup(await res.text(), features="html.parser")


            tag = bs.find_all("ul")
            final_link = f"https://www.marktplaats.nl{tag[4].find_all('a')[0].get('href')}"
            car_name = tag[4].find_all('h3')[0].contents[0]

            if '-' in final_link:

                print(final_link, car_name)
                return LastOffer(link, final_link, car_name)
                    
        except Exception as e:
            continue


async def send_requests(links: list[str] | None) -> dict:


    link_answer = {}

    async with aiohttp.ClientSession() as session:

        if links:
            tasks = get_tasks(session, links)

            responses = await asyncio.gather(*tasks)

            for i in responses:
                if i:

                    link_answer[i.link_to_page] = i.link_to_advertisement

        return link_answer
