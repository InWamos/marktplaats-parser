import json

from src.classes.last_car_ad import LastCarAdvertisement
from src.pyro_modules.bot import Bot

async def update_json_file(last_offers: list[LastCarAdvertisement], send_update) -> None:


    with open('last_offers.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

        for i in last_offers:

            if i.link_to_page in data:

                if data[i.link_to_page] != i.link_to_advertisement:
                    await send_update(i)

            elif i.link_to_page not in data:
                await send_update(i)

            data[i.link_to_page] = i.link_to_advertisement
        

    with open('last_offers.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)