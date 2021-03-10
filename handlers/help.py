from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp, CommandStart

from loader import dp


@dp.message_handler(CommandStart())
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Command list: ',
        '/list or /lst - show list of all available rates',
        '/exchange - converts to the second currency with two ' +
        'decimal precision. Ex.: /exchange 10 USD to CAD',
        '/history USD/CAD for 7 days - show an image graph chart which ' +
        'shows the exchange rate graph/chart of the selected currency ' +
        'for the last 7 days.',
        '/help - show this help',
    ]
    await message.answer('\n'.join(text))
