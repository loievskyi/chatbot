import re

from aiogram.dispatcher.filters import BoundFilter
from aiogram import types


class IsHistory(BoundFilter):
    # start with /history
    async def check(self, message: types.Message):
        return message.text.startswith("/history")


class IsHistoryCorrectFormat(BoundFilter):
    # Ex.: /history USD/CAD for 7 days
    async def check(self, message: types.Message):
        return bool(re.match(re.compile(r"^/history\s+[A-Za-z]{3}/+[A-Za-z]{3}\s+for\s+\d+\s+day(s)?$",
                    flags=re.IGNORECASE), message.text))
