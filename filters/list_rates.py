from aiogram.dispatcher.filters import BoundFilter
from aiogram import types


class IsListRates(BoundFilter):
    # start with /list or /lst
    async def check(self, message: types.Message):
        return bool(message.text == "/list" or message.text == "/lst")
