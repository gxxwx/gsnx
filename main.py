from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "8231522060:AAGU_xc9C5-_CGemECqCVguSb3xEJ8spcck"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    
    btn_tariffs = types.InlineKeyboardButton(text="🏷 Тарифные планы", callback_data="tariffs")
    btn_subscription = types.InlineKeyboardButton(text="🪪 Моя подписка", callback_data="subscription")
    btn_account = types.InlineKeyboardButton(text="🔐 Личный кабинет", callback_data="account")
    btn_support = types.InlineKeyboardButton(text="👨‍💻 Техподдержка", callback_data="support")

    keyboard.add(btn_tariffs, btn_subscription, btn_account, btn_support)

    await message.answer("Выберите пункт меню:", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data)
async def callback_handler(callback_query: types.CallbackQuery):
    data = callback_query.data

    responses = {
        "tariffs": "Здесь информация о тарифных планах.",
        "subscription": "Информация о вашей подписке.",
        "account": "Добро пожаловать в личный кабинет.",
        "support": "Свяжитесь с техподдержкой через этот канал."
    }

    answer = responses.get(data, "Неизвестная команда.")
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, answer)

if __name__ == "__main__":
    executor.start_polling(dp)
