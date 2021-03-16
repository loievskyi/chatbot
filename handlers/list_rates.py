from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from helpers import list_rates


@dp.message_handler(Command(["list", "lst"]))
async def bot_list(message: types.Message):
    try:
        currency = message.text.split()[1].upper()
    except Exception as ex:
        currency = "USD"
    courses = await list_rates.get_exchange_rates(currency)
    text = list_rates.format_output_from_db(courses)
    await message.answer(text)
