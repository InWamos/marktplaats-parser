from pyrogram import filters
from pyrogram.sync import idle
from pyrogram.client import Client
from pyrogram.types import Message
from pyrogram.handlers.message_handler import MessageHandler

from src.pyro_modules.bot_utils.handlers import write_new_link, delete_last_row
from src.classes.car_ad import CarAdvertisement

class Bot:
    """Class, has all functionality to run and handle bot;
       Also allows to send messages to user
    """
    def __init__(self, session_name: str) -> None:

        self._bot = Client(
            name=session_name,
            bot_token='6054328632:AAFXZMgMcHmDuNuSjoBsdqEG1wkrCUgvKiM',
            api_id=23001853,
            api_hash='ab37512e9f8af726a669ceb19bce06f3',
            )
        
    def add_handlers(self) -> None:

        self._bot.add_handler(
            MessageHandler(
                callback=write_new_link,
                filters=filters.command(["add"])
            )
        )

        self._bot.add_handler(
            MessageHandler(
                callback=delete_last_row,
                filters=filters.command(["cancel"])
            )
        )
 
    async def send_message_on_update(self, new_offer: CarAdvertisement) -> Message:
        """Sends message to chat id 

        Args:
            new_offer (CarAdvertisement): New item offer

        Returns:
            Message: bot's sent message
        """
        _chat_id = 5252866509

        return await self._bot.send_message(
            chat_id=_chat_id, text=str(new_offer)
            )
    
    async def run_bot(self) -> None:
        """Starts the bot
        """
        await self._bot.start()
        self.add_handlers()
        await idle()
        await self._bot.stop()

    def get_bot(self) -> Client:
        """Getter of the bot

        Returns:
            Client: bot's instance
        """                 
        return self._bot
    
    async def stop(self) -> Client:
        """stops polling

        Returns:
            Client: bot's instance
        """
        return await self._bot.stop()