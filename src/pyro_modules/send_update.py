from pyrogram.client import Client
from pyrogram.types.messages_and_media import Message
from parsers.parser import LastOffer

async def send_update(client: Client, new_offer: LastOffer) -> Message:
    _chat_id = 5252866509

    async with client:
        return await client.send_message(
            chat_id=_chat_id, text=str(new_offer))