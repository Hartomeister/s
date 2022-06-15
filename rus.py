import random
import telebot
bot = telebot.TeleBot('5398461739:AAGWYC0XLSuj--7UQdu0uA96Hepj4AkEdlQ')

@bot.message_handler(commands=['start'])
def handle_text(message):
    act = ['Расстрел','Налог', 'Штраф', 'Срок', 'Арест', 'Исправительные работы', 'Обязательные работы', 'Пожизненное лишение свободы']
    za = ['бедность', 'слишком высокий доход', 'желто-синюю одежду', 'пользование кислородом', 'пользование общественным транспортом', 'отсутствие денег', 'зеленые кепки', 'плохие оценки', 'превышение скорости', 'поддержку украины', 'оскорбление чувств верующих', 'хорошую жизнь']

    mess = random.choice(act) + ' за '+ random.choice(za) + '. И '+ random.choice(act) + ' за '+ random.choice(za)
    bot.reply_to(message, f"{mess}!")





while 1 == 1:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception:
        pass
