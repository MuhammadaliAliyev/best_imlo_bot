from aiogram import types
from loader import dp

@dp.message_handler(text = '/about')
async def about_bot(message: types.Message):
  haqida = "\t📒 Ushbu bot orqali oʻzbek tilidagi 30 000 dan ortiq soʻzlarning imlosini tekshirib olishingiz mumkin.\n\n🔴🟢🔵Botimizning qulay tomoni shundaki, agar siz notoʻgʻri soʻz kiritsangiz, notoʻgʻriligini koʻrsatibgina qolmay, shunga yaqin soʻzlarni taklif etadi.\n    Bundan tashqari ushbu bot <i><b>lotin</b></i> alifbosida ham, <i><b>kirill</b></i> alifbosida ham ishlayveradi!\n\n❗️❗️❗️<b>Eslatma</b>\n\tBotda hozircha  feʼllarning faqat noaniq shaklini tekshirish mumkin. Masalan: bormoq, yashamoq,..."
  await message.answer(haqida)