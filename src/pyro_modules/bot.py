from pyrogram import filters
from pyrogram.sync import idle
from pyrogram.client import Client
from pyrogram.handlers.message_handler import MessageHandler

from src.pyro_modules.bot_utils.handlers import write_new_link, delete_last_row

class Bot:

    def __init__(self, session_name: str) -> None:

        self._bot = Client(
            name=session_name,
            bot_token='6290018241:AAFm1gdY7RGzF7X60YSvINrfZMJy-k4YJio',
            api_id=23001853,
            api_hash='ab37512e9f8af726a669ceb19bce06f3',
            )
        
    def add_handlers(self, bot: Client) -> None:

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

    async def run_bot(self) -> None:
        await self._bot.start()
        self.add_handlers(self.get_bot())
        await idle()
        await self._bot.stop()

    def get_bot(self) -> Client:
        return self._bot
    
    async def stop(self) -> Client:
        return await self._bot.stop()