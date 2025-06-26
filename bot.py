from aiogram import Bot, Dispatcher, executor, types
import logging
import os

API_TOKEN = os.getenv("API_TOKEN", "YOUR_BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("🚀 Приступить к заданию", "👤 Личный кабинет")
    keyboard.add("🤝 Реферальная программа", "🆘 Поддержка")
    await message.reply("Добро пожаловать! Выберите действие из меню:", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
