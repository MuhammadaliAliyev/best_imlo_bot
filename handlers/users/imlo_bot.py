from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from utils.imlo.checkWord import checkWords
from utils.imlo.transliterate import to_cyrillic, to_latin
from keyboards.inline.ulashish import ulashish_uchun

from loader import dp


@dp.message_handler()
async def checkImlo(message: types.Message):
    word=message.text
    if word == to_latin(word):
        word=to_cyrillic(word)
        result=checkWords(word)
        if result['available']:
            response=f"✅ {to_latin(word.capitalize())}\n"
        else:
            response=f"❌ {to_latin(word.capitalize())}\n"
            for text in result['matches']:
                response+=f"✅ {to_latin(text.capitalize())}\n"
    else:
        #word=to_cyrillic(word)
        result=checkWords(word)
        if result['available']:
            response=f"✅ {word.capitalize()}\n"
        else:
            response=f"❌ {word.capitalize()}\n"
            for text in result['matches']:
                response+=f"✅ {text.capitalize()}\n"
    await message.answer(response, reply_markup = ulashish_uchun)