import requests
from aiogram import types

from loader import dp
from filters import IsExchangeCorrectFormat, IsExchange
from helpers.list_rates import get_exchange_rates, format_to_request_dict


@dp.message_handler(IsExchangeCorrectFormat())
async def bot_exchange_correct_format(message: types.Message):
    amount_of_money = message.text.split()[1]
    base_currency = message.text.split()[2]
    final_currency = message.text.split()[-1]

    rates = format_to_request_dict(await get_exchange_rates(base_currency))
    if final_currency not in rates:
        await message.answer("This currency is not listed.")
    else:
        result_sum = float(amount_of_money) * float(rates[final_currency])
        await message.answer(f"{result_sum:.2f} {final_currency}")


@dp.message_handler(IsExchange())
async def bot_exchange(message: types.Message):
    text = "Wrong format. Correct format ex.: /exchange 10 USD to CAD"
    await message.answer(text)
