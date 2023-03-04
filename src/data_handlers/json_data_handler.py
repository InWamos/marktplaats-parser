import json

from src.classes.car_ad import CarAdvertisement


async def update_json_file(last_offers: list[CarAdvertisement], send_update) -> None:
    """Sends the message to user(user's id defined in bot.py) in case of new advertisement 
       and writes new advertisement to the last_offers.json
    Args:
        last_offers (list[CarAdvertisement]): list of parsed advertisements
        send_update (method): Bot's method: send_message_on_update
    """

    with open('last_offers.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

        for i in last_offers:

            if i.link_to_page not in data:

                data[i.link_to_page] = [i.link_to_item]
                await send_update(i)

            elif i.link_to_page in data:

                if i.link_to_item not in data[i.link_to_page]:

                    data[i.link_to_page].append(i.link_to_item)
                    await send_update(i)
        

    with open('last_offers.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)