from utils.db_api import db_gino
from aiogram import executor
from filters import dp
from handlers import dp
from loader import db


async def on_startup(dp):
    # connect to db
    await db_gino.on_startup(dp)
    await db.gino.drop_all()
    await db.gino.create_all()


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
