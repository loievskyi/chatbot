import requests
from aiogram import types

from loader import dp
from filters import IsExchangeCorrectFormat, IsExchange


@dp.message_handler(IsExchangeCorrectFormat())
async def bot_exchange_correct_format(message: types.Message):
    response = requests.get("https://api.exchangeratesapi.io/latest?base=USD")
    rates = response.json()['rates']
    amount_of_money = message.text.split()[1]
    currency = message.text.split()[-1]
    if currency not in rates:
        await message.answer("This currency is not listed.")
    else:
        result_sum = float(amount_of_money) * float(rates[currency])
        await message.answer(f"{result_sum:.2f} {currency}")


@dp.message_handler(IsExchange())
async def bot_exchange(message: types.Message):
    text = "Wrong format. Correct format ex.: /exchange 10 USD to CAD"
    await message.answer(text)
