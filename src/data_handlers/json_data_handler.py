import json
from pyrogram.client import Client
from src.pyro_modules.send_update import send_update
from src.marketplace_requests.get_advertisement import LastCarAdvertisement

async def update_json_file(last_offers: list[LastCarAdvertisement], client: Client) -> None:


    with open('last_offers.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

        for i in last_offers:

            if i.link_to_page in data:

                if data[i.link_to_page] != i.link_to_advertisement:
                    await send_update(client, i)

            elif i.link_to_page not in data:
                await send_update(client, i)

            data[i.link_to_page] = i.link_to_advertisement
        

    with open('last_offers.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)