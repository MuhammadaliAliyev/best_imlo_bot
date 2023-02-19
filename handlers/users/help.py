from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Botga so`z yuboring va imlosini tekshirib oling\n",
        "Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/about - Bot haqida")
    
    await message.answer("\n".join(text))
