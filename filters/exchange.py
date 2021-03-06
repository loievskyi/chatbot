import re

from aiogram.dispatcher.filters import BoundFilter
from aiogram import types


class IsExchange(BoundFilter):
    # start with /exchange
    async def check(self, message: types.Message):
        return message.text.startswith("/exchange")


class IsExchangeCorrectFormat(BoundFilter):
    # Ex.: /exchange 10 USD to CAD
    async def check(self, message: types.Message):
        return bool(re.match(re.compile(r"^/exchange\s+\d+([.,]{1}\d+)?\s+[A-Za-z]{3}\s+to\s+[A-Za-z]{3}$",
                    flags=re.IGNORECASE), message.text))
