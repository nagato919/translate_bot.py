import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from googletrans import Translator

API_TOKEN = os.getenv("API_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
translator = Translator()

@dp.message_handler()
async def translate_message(message: types.Message):
    text = message.text
    try:
        result = translator.translate(text, dest='vi')  # Dịch sang tiếng Việt
        reply = f"🌐 Ngôn ngữ gốc: {result.src.upper()}\n🇻🇳 Dịch: {result.text}"
    except Exception as e:
        reply = f"⚠️ Lỗi dịch: {e}"
    await message.reply(reply)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
