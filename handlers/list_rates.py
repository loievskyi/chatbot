import requests
from aiogram import types

from loader import dp
from filters import IsListRates
from helpers import list_rates


@dp.message_handler(IsListRates())
async def bot_list(message: types.Message):
    response = requests.get("https://api.exchangeratesapi.io/latest?base=USD")
    text = list_rates.format_output(response.json())
    await message.answer(text)
