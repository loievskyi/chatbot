import requests
from aiogram import types
from loader import dp

from helpers import list_rates


@dp.message_handler(text="/list")
@dp.message_handler(text="/lst")
async def bot_list(message: types.Message):
    response = requests.get("https://api.exchangeratesapi.io/latest?base=USD")
    text = list_rates.format_output(response.json())
    await message.answer(text)
