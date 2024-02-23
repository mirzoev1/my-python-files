import logging

from aiogram import Bot, Dispatcher, executor

API_TOKEN = '7139109243:AAFeNK8YGhLbzgheNHLg9MvKtOTnAczfA1Y'



# "YOUR_TOKEN" o'rniga BotFather orqali olingan asal bot belgisi kiriting

# Bot va Dispatcher'ni boshlang
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# /start buyrug'i qabul qiluvchi funktsiyani aniqlang
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Salom! Men EchoBotman. Menga istalgan xabarni yuboring va men unga javob qaytaraman.")

# Echo xabarni qaytarish funktsiyasini aniqlang
@dp.message_handler()
async def echo_message(message: types.Message):
    await message.reply(message.text)

# Botni ishga tushiring
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
