from pyrogram import filters
from pyrogram.client import Client
from pyrogram.handlers.message_handler import MessageHandler
from src.pyro_modules.bot_utils.handlers import write_new_link, delete_last_row

class Bot:

    def __init__(self) -> None:

        self._bot = Client("test_connection")

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

    def run(self) -> None:
        self._bot.run()


    async def stop(self) -> None:
        await self._bot.stop()