import telebot
from telebot import types

bot = telebot.TeleBot('')

# меню для выбора
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Вход")
item2 = types.KeyboardButton("Регистрация")
markup.add(item1, item2)

markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Начать обучение")
markup1.add(item1)

markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
item1 = types.KeyboardButton("Продолжить обучение")
markup2.add(item1)
name = mail = ''
@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard

    bot.send_message(message.chat.id,
                     "Вас приветствует бот по кибербезопасности!\n".format(
                         message.from_user, bot.get_me()), reply_markup=markup,
                     parse_mode='html')


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        global name, mail
        if message.text == 'Регистрация':
            bot.send_message(message.chat.id, "Как я могу к вам обращаться?", reply_markup=types.ReplyKeyboardRemove())
        elif message.text == 'Вход':
            bot.send_message(message.chat.id, "Добрый день, Виктор!", reply_markup=markup2)
        elif message.text == '123':
            bot.send_message(message.chat.id, f"Регистрация успешно пройдена, {name}!", reply_markup=markup1)
        elif message.text and not name:
            name = message.text
            bot.send_message(message.chat.id, f"Рад видеть Вас, {name}!\nУкажите почту или телефон для регистрации", reply_markup=types.ReplyKeyboardRemove())
        elif message.text and not mail:
            mail = message.text
            bot.send_message(message.chat.id, f"Код подтверждения выслан на {mail}\nВведите его пожалуйста", reply_markup=types.ReplyKeyboardRemove())

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Заказ за вами закреплен')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Вам поступит уведомление при новых заказах')
    except Exception as e:
        print(repr(e))
bot.polling(none_stop=True)
