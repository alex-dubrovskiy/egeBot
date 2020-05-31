import telebot #Импорт бибилиотеки
from telebot import types #Подключаем подбиблиотеку для вывода кнопок
bot = telebot.TeleBot('981871882:AAEXvC9lKCTnkZf3UtszrXOrRy2XFSW6QYQ') #токен, для связи с телеграмом

@bot.message_handler(commands = ['help']) #бот реагирует на /help
def help_message(message):
    bot.send_message(message.chat.id, ''' Доступные команды:
    /start - начало работы.
    /help - доступные команды.
    /about - обо мне
    ''')
@bot.message_handler(commands = ['words']) #бот реагирует на /words
def words_message(message):
    bot.send_message(message.chat.id, '''
    Доступные слова, на которые отвечает бот:
    1. Привет
    2. Пока
    3. Как дела?
    4. Помоги
    5. Когда
    6. Экзамен
    7. Экзамены
    8. ЕГЭ
    ''')

@bot.message_handler(commands = ['start']) #бот реагирует на /words и присылает инфомарцию об отправителе
def start_message(message):
    bot.send_message(message.chat.id, '''Добро пожаловать!
    Введи /help для просмотра доступных команд.
    Введи /words чтобы посмотреть, что я понимаю.
    ''')
    print(message.from_user)

@bot.message_handler(commands = ['author']) #бот реагирует на команду /author и присылает имя создателя
def author_message(message):
    bot.send_message(message.chat.id, 'Alexander Dubrovskiy <3')

@bot.message_handler(commands = ['about']) #бот реагирует на команду /about
def about_message(message):
    bot.send_message(message.chat.id, 'Этот бот напоминает тебе даты твоего ЕГЭ, который ты ему скажешь. Также с ним можно немного пообщаться')

@bot.message_handler(content_types=['text']) #бот принимают инфомарцию в виде текста
def send_text(message):

    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Здравствуй, дружище! Введи "когда" или "экзамен", чтобы узнать дату своего ЕГЭ.')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока, удачи на экзамене!')
        bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
    elif message.text.lower() == 'как дела?':
        bot.send_message(message.chat.id, 'Плохо, не хочу экзамены, а ты как?')
    elif message.text.lower() == 'помоги' or message.text.lower() == 'когда' or message.text.lower() == 'егэ' or message.text.lower() == 'экзамены' or message.text.lower() == 'экзамен':
        keyboard = types.InlineKeyboardMarkup()

        key_russ = types.InlineKeyboardButton(text='Русский язык', callback_data='russ')  #вывод кнопок на экран
        keyboard.add(key_russ)

        key_math = types.InlineKeyboardButton(text='Математика', callback_data='math')
        keyboard.add(key_math)

        key_geo = types.InlineKeyboardButton(text='География', callback_data='geo')
        keyboard.add(key_geo)

        key_litra = types.InlineKeyboardButton(text='Литература', callback_data='litra')
        keyboard.add(key_litra)

        key_info = types.InlineKeyboardButton(text='Информатика', callback_data='info')
        keyboard.add(key_info)

        key_ist = types.InlineKeyboardButton(text='История', callback_data='ist')
        keyboard.add(key_ist)

        key_fiz = types.InlineKeyboardButton(text='Физика', callback_data='fiz')
        keyboard.add(key_fiz)

        key_him = types.InlineKeyboardButton(text='Химия', callback_data='him')
        keyboard.add(key_him)

        key_obs = types.InlineKeyboardButton(text='Обществознание', callback_data='obs')
        keyboard.add(key_obs)

        key_bio = types.InlineKeyboardButton(text='Биология', callback_data='bio')
        keyboard.add(key_bio)

        key_ino = types.InlineKeyboardButton(text='Иностранный язык', callback_data='ino')
        keyboard.add(key_ino)

        key_rezerv = types.InlineKeyboardButton(text='Резервные дни',callback_data='rezerv')
        keyboard.add(key_rezerv)

        bot.send_message(message.chat.id, text='Выбери свой экзамен', reply_markup=keyboard)
    else: bot.send_message(message.chat.id, 'Понятно')


@bot.callback_query_handler(func=lambda call: True) #возвращаем инфомацию о датах
def call_worker(call):
    if call.data =='russ':
        bot.send_message(call.message.chat.id, 'Ты сдаешь русский 6 или 7 июля. Смотря в какую группу тебя забросят)')
    elif call.data == 'math':
        bot.send_message(call.message.chat.id, 'Ты сдаешь математику 10 июля.')
    elif call.data == 'geo':
        bot.send_message(call.message.chat.id, 'Ты сдаешь географию 3 июля.')
    elif call.data == 'litra':
        bot.send_message(call.message.chat.id, 'Ты сдаешь литературу 3 июля.')
    elif call.data == 'info':
        bot.send_message(call.message.chat.id, 'Ты сдаешь информатику 3 июля.')
    elif call.data == 'ist':
        bot.send_message(call.message.chat.id, 'Ты сдаешь историю 13 июля.')
    elif call.data == 'fiz':
        bot.send_message(call.message.chat.id, 'Ты сдаешь физику 13 июля.')
    elif call.data == 'him':
        bot.send_message(call.message.chat.id, 'Ты сдаешь химию 16 июля.')
    elif call.data == 'obs':
        bot.send_message(call.message.chat.id, 'Ты сдаешь обществознание 16 июля.')
    elif call.data == 'bio':
        bot.send_message(call.message.chat.id, 'Ты сдаешь биологию 20 июля.')
    elif call.data == 'ino':
        bot.send_message(call.message.chat.id, 'Ты сдаешь иностранный язык 20 июля. \n А устную часть 22 или 23 июля.')
    elif call.data == 'rezerv':
        bot.send_message(call.message.chat.id, 'Резервные дни будут 24 и 25 июля.')


bot.polling(none_stop=True,interval=0)  #бот постоянно проверяет пришла ли новая информация


