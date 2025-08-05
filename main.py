import telebot
from flask import Flask, request
import os

TOKEN = "8231522060:AAGU_xc9C5-_CGemECqCVguSb3xEJ8spcck"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

# Главная страница
@app.route("/", methods=["GET"])
def index():
    return "✅ Бот работает"

# Вебхук: Telegram отправляет сюда обновления
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "ok", 200

# Команда /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    markup.row(
        telebot.types.InlineKeyboardButton("🏷 Тарифные планы", callback_data='tariffs'),
        telebot.types.InlineKeyboardButton("🪪 Моя подписка", callback_data='subscription')
    )
    markup.row(
        telebot.types.InlineKeyboardButton("🔐 Личный кабинет", callback_data='cabinet'),
        telebot.types.InlineKeyboardButton("👨‍💻 Техподдержка", url='https://t.me/gsnxcom')
    )
    bot.send_message(message.chat.id, "👋 Добро пожаловать! Выберите опцию:", reply_markup=markup)

# Кнопки
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'tariffs':
        bot.send_message(call.message.chat.id, "📦 Здесь будут тарифные планы.")
    elif call.data == 'subscription':
        bot.send_message(call.message.chat.id, "🪪 Информация о вашей подписке.")
    elif call.data == 'cabinet':
        bot.send_message(call.message.chat.id, "🔐 Личный кабинет недоступен.")

# Настройка вебхука при запуске
if __name__ == "__main__":
    url = "https://gsnx.onrender.com"  # Твой домен на Render
    bot.remove_webhook()
    bot.set_webhook(url=f"{url}/{TOKEN}")
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)
