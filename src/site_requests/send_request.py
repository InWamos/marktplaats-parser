import aiohttp
import asyncio
from bs4 import BeautifulSoup
from dataclasses import dataclass

@dataclass
class LastOffer:
    name: str
    link: str

    def __str__(self) -> str:
        return f"Новый автомобиль!\n🚘 Название: {self.name}\n🔗 Ссылка: {self.link}"
    

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
        tasks.append(session.get(i))

    return tasks if tasks else None


async def get_last_advertisement(link: str, session: aiohttp.ClientSession) -> LastOffer:

    final_link = ''
    car_name = 'Undefined'
    while '-' not in final_link:

        try:
            async with session:
                res = await session.get("https://www.marktplaats.nl/l/auto-s/bmw/f/2-serie/10901/")
                bs = BeautifulSoup(await res.text(), features="html.parser")

                tag = bs.find_all("ul")
                final_link = f"https://www.marktplaats.nl{tag[4].find_all('a')[0].get('href')}"
                car_name = tag[4].find_all('h3')[0].contents[0]
        except:
            break

    return LastOffer(car_name, link)

async def send_requests(links: list[str] | None) -> dict | None:
    """Makes parallel requests to links

    Args:
        links (list): links to be requested

    Returns:
        dict | None: returns a ditionary in format {link_name: server_answer}
    """

    link_answer = {}

    async with aiohttp.ClientSession() as session:

        if links is not None:
            tasks = get_tasks(session, links)

            responses = await asyncio.gather(*tasks)
            for i in responses:
                link_answer[str(i.real_url)] = await i.text()
            
            return link_answer
        
        else:
            return None


asyncio.run(send_requests(links=get_links()))