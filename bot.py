import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo
from aiogram.utils import executor

# 🔹 Укажи свой токен бота
TOKEN = "7789084657:AAGRAEoPXdi0a9Hh3tBvbEkfO6xP7TnsL9E"

# 🔹 Укажи ссылку на миниапп
WEB_APP_URL = "https://madragor13.vercel.app"

# Настройка логов
logging.basicConfig(level=logging.INFO)

# Создаем бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# 📌 Обработчик команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("🚀 Открыть миниапп", web_app=WebAppInfo(url=WEB_APP_URL))
    keyboard.add(button)

    await message.answer("Привет! Нажми кнопку, чтобы открыть миниапп:", reply_markup=keyboard)

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
