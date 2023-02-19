import sqlite3
from data.config import *
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, db, bot

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    
    await message.answer(f"Assalomu alaykum, {message.from_user.full_name}!\nImloBotga xush kelibsiz!\n Botga so`z yuboring va imlosini tekshirib oling.")
    
    name = message.from_user.full_name
    try:
        db.add_user(id=message.from_user.id, name = name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo`shildi.\n Bazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)