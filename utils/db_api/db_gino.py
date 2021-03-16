from aiogram import Dispatcher
from gino import Gino

from data import config


db = Gino()


async def on_startup(dispatcher: Dispatcher):
    await db.set_bind(config.POSTGRES_URI)
    print("Connected to database")
    # await db.set_bind('sqlite:///:memory:')
