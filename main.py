import telebot
from telebot import types
from gen_predict import gen_prediction

token = "5785839066:AAH1hMPdwW52bzSRQPo4vLV-f3iDvFmu_ZY"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
  btn1 = types.KeyboardButton("Общее")
  btn2 = types.KeyboardButton("Здоровье")
  btn3 = types.KeyboardButton("Прошлое, настоящее, будущее")
  btn4 = types.KeyboardButton("Любовь")
  btn5 = types.KeyboardButton("Карьера, деньги")
  markup.add(btn1, btn2, btn3, btn4, btn5)
  bot.send_message(message.chat.id, "Привет, {0.first_name}! Таро подружка приветсвует тебя! Выбери, какой раскладик ты хочешь?".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    prediction = gen_prediction(message.text)
    if prediction.choose_category() is not None:
      prediction.choose_category()
      prediction.random_cards()
      bot.send_message(message.chat.id, text=prediction.write_names())
      bot.send_message(message.chat.id, text=prediction.make_pred())
    else:
      bot.send_message(message.chat.id, "Ты точно хочешь раскладик?")



bot.polling(none_stop=True)
