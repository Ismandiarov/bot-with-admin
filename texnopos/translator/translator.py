import translators
from aiogram import Bot, Dispatcher, types
API_TOKEN = ''
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("с рус на англ")

@dp.message_handler()
async def translate(message: types.Message):
    translator = translators.translate_text(from_language='ru', to_language='en', query_text=message.text)
    await message.answer(translator)

if __name__ == '__main__':
    from aiogram import executor

    executor.start_polling(dp, skip_updates=True)