import telebot
import config
import random
from telebot import types
from expiration_date import expiration_date
from decimal import Decimal

# update
### Deploy HEROKU ###
"""
heroku login
git init
git push heroku master
"""
global text_1, info_1, info_3, info_4
key_1 = "Инфо"
key_2 = "Пересорт/Уценка"
key_3 = "ВАЖНО!!!"
key_4 = "НАЧАЛО ДНЯ (НЕТ ВТОРОГО ЧЕЛ)!!!"
info_1 = "Когда принесли телефон (ТСД) Выберите:\nПечать этикеток и ценников -> заполнить из ТСД -> выгружать пустые " \
         "строки -> выводить отчет -> выполнить загрузку из ТСД\n(после удалить задание из устройства ТСД) "
info_2 = "20%\n хлеб: бородинский, зерновой, батон нарезной, хлеб 1 сорт, 2 сорт.\n 30%\n хлеб купеческий"
info_3 = "клб-колбаса(кг) с колбасами заходить в ... (проверять дату),\nпфз - полуфабрикаты,\nдлм-деликатесы"
info_4 = "Терещенко А.Ю (ИП ТАЮ) - торты (ценник с датами, сегодня 8:00), пирожное, салаты. Поставщики(контрагенты) - " \
         "...\nМир " \
         "продуктов "
bot = telebot.TeleBot(config.TOKEN)

keyboard = types.ReplyKeyboardMarkup()  # обновить клавиатуру


@bot.message_handler(commands=['start'])  # новые кнопки * обновление кнопок
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
    item1 = types.KeyboardButton("🎲")
    item2 = types.KeyboardButton(key_1)
    item4 = types.KeyboardButton(key_2)
    item5 = types.KeyboardButton(key_3)
    item6 = types.KeyboardButton(key_4)
    item3 = types.KeyboardButton("Дата окончания срока годности")
    markup.add(item1, item2, item3, item4, item5,item6 )

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть "
                     "подопытным кроликом.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == "text_1":
            # bot.send_message(message.chat.id, str(random.randint(0, 100)))
            sent_msg = bot.send_message(message.chat.id, "Что вы хотите узнать?")
        elif message.text == 'Дата окончания срока годности':

            sent_msg = bot.send_message(message.chat.id, "Добрый день, Сэр! Пожалуйста, введите количество часов",
                                        reply_markup=keyboard)
            bot.register_next_step_handler(sent_msg,
                                           number_of_hours_handler)  # Next message will call the name_handler function
        elif message.text == key_1:

            markup = types.InlineKeyboardMarkup(row_width=4)
            item0 = types.InlineKeyboardButton("ТСД", callback_data='tsd')
            item1 = types.InlineKeyboardButton("Наценка", callback_data='nacens')
            item2 = types.InlineKeyboardButton("Сокращения", callback_data='abbreviations')
            item3 = types.InlineKeyboardButton("Поступления", callback_data='admission')
            markup.add(item0, item1, item2, item3)

            bot.send_message(message.chat.id, 'Что вы хотите узнать?', reply_markup=markup)
        elif message.text == key_2:
            bot.send_message(message.chat.id, 'Складские акты -> Уценка -> понижение сортности -> (на 20% дешевле ( '
                                              'сум. розю прих) , если товар уже уцененный  то его режут на куски ('
                                              'наименование товара с %) 4 шт => 79 руб. Пропикать товар, '
                                              'Ценник горизонтальный')

            sent_msg = bot.send_message(message.chat.id, 'Сэр, введите цену товара')

            bot.register_next_step_handler(sent_msg,
                                           discount)
        elif message.text == key_3:
            bot.send_message(message.chat.id, 'Весы 1, 4- сладости, печенье, торты, крупы, сахар ( то что в мешках '
                                              'кг)\n\nВесы 3,5 - замороженной мясо, рыба, замороженные фруктовые '
                                              'овощные смеси, сыры, творожные массы, ( все что не относится к крупам, '
                                              'и колбасам, ) катлеты, племени)\n\nВесы колбасы - колбасы, длм, '
                                              'мясо копченое\n\nБазу обязательно грузить на весы!!!\n\nНе проходит '
                                              'товар. Номенклатура - зайти в товар (пелимени) - связаные данные - '
                                              'оборудование ( проставить верные галки).После погрузить на '
                                              'оборудование.Дополнительно кинуть на весы терминальные( нужно для '
                                              'ревизии)\n\nСалаты цена за 0.1 кг выбирать ( у салатов может не быть '
                                              'штрихкода, набирают по ячейке)\nВесы колбасы-салаты\n\nТефтели - мир '
                                              'продуктов!!!\n\nБаза - терещенко\nСтудень = холодец\n\nСовственое '
                                              'производство - баранкевич, стебакова, голубенко, терещенко с.и.,'
                                              'жарова ( 1 накладная 7.7)\nБаза перемещение товаров ( основной склад '
                                              'на основной склад)\n\nЕсли есть счёт фактура, то остальные документы в '
                                              'стопку рядом с мфу)\n\nПроверять подпись старшего продовца, '
                                              'и печать!Когда 3 штуки\nСтарший продавец, Аня с короткой '
                                              'стрижкой\n\nВике в долг не давать\n\nМестных поставщиков ( 1 фактура '
                                              '7.7) в папку\n\nЛяпки в долг: печать этикеток и ценников -> выбрать '
                                              'тип цен( если указан неверно, товар будет без цены) делать в 2х '
                                              'экземплярах, один в 16:30 директору Ольге Валерьевне, один отдать на '
                                              'руки берущему)\n\nСоставы на : салаты, печенье, конфеты, котлеты, '
                                              'фарш, ( что то приготовили нужно сделать составы)\n\n( если мы '
                                              'перефасовываем и на товаре был состав указан)\n\nТовар с базы '
                                              'обязательно v3 и оборудование!!!!')
        elif message.text == key_4:
            bot.send_message(message.chat.id, 'Касса. Запуск 1С -> Волчанкова(4212123), робот(111) - отключить '
                                              'автообмен -> прием данных. Волчанкова -> прием данных из POS -> касса '
                                              '2.11( день вчера и сегодня) -> прочитать данные -> загрузить z отчет ( '
                                              'тоже самое с касса 3.9)')

        elif message.text == "Поступления от ИП ТАО":
            bot.send_message(message.chat.id, 'Я не знаю что ответить  😢')
        else:
            pass  # bot.send_message(message.chat.id, 'Я не знаю что ответить')


def discount(pm):  # pm - введенное сообщение
    try:
        x = (float(pm.text))
        discount_20 = 0.2
        number_of_hours = x - (x * discount_20)
        sent_msg = bot.send_message(pm.chat.id, f"Цена при 20% скидке:\n{(round(number_of_hours,2))} руб.")
    except ValueError:
        sent_msg = bot.send_message(pm.chat.id, f"Сэр, вы ввели некорректное число, попробуйте снова")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'tsd':
                bot.send_message(call.message.chat.id, info_1)
            elif call.data == 'nacens':
                bot.send_message(call.message.chat.id, info_2)
            elif call.data == 'abbreviations':
                bot.send_message(call.message.chat.id, info_3)
            elif call.data == 'admission':
                bot.send_message(call.message.chat.id, info_4)

    except Exception as e:
        print(repr(e))


####


# @bot.message_handler(content_types=['text'])
def welcome(pm):
    sent_msg = bot.send_message(pm.chat.id, "Добрый день, Сэр! Пожалуйста, введите количество часов",
                                reply_markup=keyboard)
    bot.register_next_step_handler(sent_msg,
                                   number_of_hours_handler)  # Next message will call the name_handler function


# @bot.message_handler(commands=["newkeyboard"])

def number_of_hours_handler(pm):
    try:
        number_of_hours = expiration_date(int(pm.text))
        sent_msg = bot.send_message(pm.chat.id, f"{number_of_hours}")
        # welcome(pm)
    except ValueError:
        sent_msg = bot.send_message(pm.chat.id, f"Сэр, вы ввели некоректное число, попробуйте снова")
        # welcome(pm)
    # number_of_hours = pm.text

    # bot.register_next_step_handler(sent_msg, age_handler, number_of_hours)  # Next message will call the age_handler function


# def age_handler(pm, name):
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
