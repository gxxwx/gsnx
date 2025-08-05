from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import logging
import asyncio

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Твой токен
TOKEN = "8231522060:AAGU_xc9C5-_CGemECqCVguSb3xEJ8spcck"

# Инициализация бота и диспетчера
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Главное меню (инлайн-кнопки)
main_menu = InlineKeyboardMarkup(row_width=2)
main_menu.add(
    InlineKeyboardButton("📦 Купить доступ", callback_data="buy"),
    InlineKeyboardButton("📜 Правила", callback_data="rules"),
    InlineKeyboardButton("ℹ️ Поддержка", url="https://t.me/gsngsupport")
)

# Обработка команды /start
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("👋 Добро пожаловать в GSNX!\nВыберите действие ниже:", reply_markup=main_menu)

# Обработка кнопок
@dp.callback_query_handler(lambda call: True)
async def handle_buttons(call: types.CallbackQuery):
    if call.data == "buy":
        await call.message.edit_text("💳 Чтобы купить доступ, отправьте сумму на ... (сюда вставьте инструкцию)")
    elif call.data == "rules":
        await call.message.edit_text("📜 Правила:\n1. Не передавайте доступ третьим лицам\n2. ...")
    await call.answer()

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
