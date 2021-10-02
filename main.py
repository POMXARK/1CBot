import telebot
import config
#import random
from telebot import types
from expiration_date import expiration_date

### Deploy HEROKU ###
"""
git init
git push heroku master
"""


bot = telebot.TeleBot(config.TOKEN)

keyboard = types.ReplyKeyboardMarkup() # обновить клавиатуру

# keyboard
markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
item1 = types.KeyboardButton("Дата окончания срока годности")
markup.add(item1)

#@bot.message_handler(content_types=['text'])
def welcome(pm):
    sent_msg = bot.send_message(pm.chat.id, "Добрый день, Сэр! Пожалуйства введите количество часов",reply_markup=keyboard)
    bot.register_next_step_handler(sent_msg, number_of_hours_handler)  # Next message will call the name_handler function

#@bot.message_handler(commands=["newkeyboard"])

def number_of_hours_handler(pm):
    try:
        number_of_hours = expiration_date(int(pm.text))
        sent_msg = bot.send_message(pm.chat.id, f"{number_of_hours}")
        welcome(pm)
    except ValueError:
        sent_msg = bot.send_message(pm.chat.id, f"Сэр, вы ввели некоректное число, попробуйте снова")
        welcome(pm)
    #number_of_hours = pm.text

    #bot.register_next_step_handler(sent_msg, age_handler, number_of_hours)  # Next message will call the age_handler function


#def age_handler(pm, name):
#    age = pm.text
#    bot.send_message(pm.chat.id, f"Your name is {name}, and your age is {age}.", reply_markup=keyboard)
"""
@bot.message_handler(commands=["new_keyboard_for_all_users"])
def send_new_keyboard (message):
    keyboard = types.ReplyKeyboardMarkup() # Новая клавиатура
    for user in users_list:
        bot.send_message(user, 'Произвольное сообщение', reply_markup=keyboard)
"""

bot.polling(none_stop=True)

"""
@bot.message_handler(content_types=['text'])
def welcome(pm):
    sent_msg = bot.send_message(pm.chat.id, "Welcome to bot. what's your name?")
    bot.register_next_step_handler(sent_msg, name_handler)  # Next message will call the name_handler function


def name_handler(pm):
    name = pm.text
    sent_msg = bot.send_message(pm.chat.id, f"Your name is {name}. how old are you?")
    bot.register_next_step_handler(sent_msg, age_handler, name)  # Next message will call the age_handler function


def age_handler(pm, name):
    age = pm.text
    bot.send_message(pm.chat.id, f"Your name is {name}, and your age is {age}.")


bot.polling()
"""
"""
@bot.message_handler(commands=['start'])
def welcome(message):
    #sti = open('static/welcome.webp', 'rb')
   # bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
    item1 = types.KeyboardButton("🎲 Рандомное число")
    item2 = types.KeyboardButton("😊 Как дела?")
    item3 = types.KeyboardButton("Дата окончания срока годности")
    markup.add(item1, item2,item3)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))
        elif message.text == 'Дата окончания срока годности':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("24", callback_data='24')
            item2 = types.InlineKeyboardButton("36", callback_data='36')
            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Выбери количество часов', reply_markup=markup)
        elif message.text == '😊 Как дела?':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить  😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Бывает 😢')
            #if call.data == '24':
            #    pass
            # remove inline buttons
            #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
            #                      reply_markup=None)

            # show alert
            #bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
            #                          text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)
"""
