from pyrogram.client import Client
from pyrogram.types.messages_and_media import Message
from src.classes.car_ad import CarAdvertisement

async def send_update(client: Client, new_offer: CarAdvertisement) -> Message:
    """Outdated method. Used to send the messages to user

    Args:
        client (Client): pyro client
        new_offer (CarAdvertisement): Instance of new advertisement

    Returns:
        Message: bot's sent message
    """
    _chat_id = 5252866509

    async with client:
        return await client.send_message(
            chat_id=_chat_id, text=str(new_offer))