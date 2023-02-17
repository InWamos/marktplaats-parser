from pyrogram import filters
from pyrogram.sync import idle
from pyrogram.client import Client
from pyrogram.handlers.message_handler import MessageHandler

from src.pyro_modules.bot_utils.handlers import write_new_link, delete_last_row

class Bot:

    def __init__(self, session_name: str) -> None:

        self._bot = Client(
            name=session_name,
            bot_token="6290018241:AAFm1gdY7RGzF7X60YSvINrfZMJy-k4YJio"
            )
        
    
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

    async def run(self) -> None:
        await self._bot.start()
        await idle()

    def get_bot(self) -> Client:
        return self._bot
    
    async def stop(self) -> Client:
        return await self._bot.stop()