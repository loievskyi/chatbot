import datetime
import os
import json

import requests
from aiogram import types

from loader import dp
from filters import IsHistory, IsHistoryCorrectFormat
from helpers.plot import create_graph


@dp.message_handler(IsHistoryCorrectFormat())
async def bot_exchange_correct_format(message: types.Message):
    # Ex.: /history USD/CAD for 7 days
    data = message.text.split()
    base_curency = data[1].split("/")[0]
    final_curency = data[1].split("/")[1]

    curent_day = datetime.date.today()
    start_day = curent_day - datetime.timedelta(days=int(data[3]))

    url = "https://api.exchangeratesapi.io/history?" + \
        f"start_at={start_day:%Y-%m-%d}&end_at={curent_day:%Y-%m-%d}" + \
        f"&base={base_curency}&symbols={final_curency}"
    history = requests.get(url).json()
    with open("result.json", "wt+") as file:
        json.dump(history, file)
    title = message.text[1:]
    file_name = create_graph(history, base_curency, final_curency, title=title)

    with open(file_name, "rb") as photo:
        await message.answer_photo(photo, caption=title)
    os.remove(file_name)


@dp.message_handler(IsHistory())
async def bot_exchange(message: types.Message):
    text = "Wrong format. Correct format ex.: /history USD/CAD for 7 days"
    await message.answer(text)
