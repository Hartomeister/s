#chat member guy

import telebot
from telebot import types
import time
from telebot import apihelper
global user_id
global admin
global chat_id
chat_id = 5206676272
user_id =  -1001247725053
admin = [5206676272, 5058141288]
abusers = []
requests = []
bot = telebot.TeleBot('5405495922:AAEVW3KzY4AWxLWKknQ158zdSJdBEs3hw1Y')

@bot.message_handler(commands=['start'])
def handle_text(message):
    cid = message.chat.id
    bot.send_message(cid, 'BOT IS NOT FINISHED\n\n I have just a few functions: \n\n • /start - this command \n • /rules - announce rules for all group members \n • /admin - calls admin\n\nAdmin commands:\nreset - clear requests\n/ban - ban user\n/mute - mute user')

@bot.chat_member_handler()
def chat_m(message: types.ChatMemberUpdated):
    old = message.old_chat_member
    new = message.new_chat_member
    if new.status == "member":
        bot.send_message(message.chat.id,"Hello {name}!".format(name=new.user.first_name)) # Welcome message

#if bot is added to group, this handler will work
@bot.my_chat_member_handler()
def my_chat_m(message: types.ChatMemberUpdated):
    old = message.old_chat_member
    new = message.new_chat_member
    if new.status == "member":
        bot.send_message(message.chat.id,"Somebody added me to group") # Welcome message, if bot was added to group
        bot.leave_chat(message.chat.id)


@bot.message_handler(commands=['reset'])
def handle_text(message):
    cid = message.chat.id
    user = message.from_user.id
    if user not in admin:
    	bot.send_message(cid, 'Sorry, this command is for admins')
    else:
     	requests.clear()
     	bot.send_message(cid, 'OK, requests cleared ')
@bot.message_handler(commands=['rules'])
def handle_text(message):
    cid = message.chat.id
    user = message.from_user.id
    bot.send_message(cid, 'Rules: \n • No swearing and abusing \n • No discussing any illegal themes \n • No links and advertisement ')

@bot.message_handler(commands=['admin'])
def handle_text(message):
    cid = message.chat.id
    user = message.from_user.id
    if user not in requests:
    	appealer = message.from_user.id
    	admin1 = 5206676272
    	admin2 = 5058141288
    	bot.send_message(admin1, f'User #{appealer} called admins 👮‍♂️')
    	requests.append(appealer)
    	bot.send_message(cid, 'Admins were notified 👮‍♂️\n\n • Please note, that fake calls or spam may lead to ban')
    	if appealer in abusers:
    		bot.send_message(admin1, f'⚠️⚠️⚠️ CAREFUL, user #{appealer} is in suspicious list! ')
    		bot.send_message(admin2, f'⚠️⚠️⚠️ CAREFUL, user #{appealer} is in suspicious list! ')
    	else:
    		bot.send_message(admin1, f'User #{appealer} is not in a suspicious list ')
    else:
    	bot.send_message(cid, 'You already reported️')


@bot.message_handler(commands=["ban"])
def ban(message):
	user = message.from_user.id
	cid = message.chat.id
	if user not in admin:
	  	bot.send_message(cid, 'Sorry, only admins can ban users ⚠️')
	else:
		 cid = message.chat.id
		 age = message.text
		 chat = message.chat.id
		 target = age.split()
		 numy = target[1]
		 bot.ban_chat_member(message.chat.id, numy)
		 bot.send_message(cid, 'User was banned :-| \n\nIf you want to appeal the decision, write to @kjual')

@bot.message_handler(commands=["unban"])
def ban(message):
	user = message.from_user.id
	cid = message.chat.id
	if user not in admin:
	  	bot.send_message(cid, 'Sorry, only admins can unban users ⚠️')
	else:
		 cid = message.chat.id
		 age = message.text
		 chat = message.chat.id
		 target = age.split()
		 numy = target[1]
		 bot.unban_chat_member(message.chat.id, numy)
		 bot.send_message(cid, 'User was unbanned. Welcome back 🚀\n\nIf you want to appeal the decision, write to @kjual')

@bot.message_handler(commands=["mute"])
def mute(message):
	user = message.from_user.id
	cid = message.chat.id
	if user not in admin:
	  	bot.send_message(cid, 'Sorry, only admins can mute users ⚠️')
	else:
		 cid = message.chat.id
		 age = message.text
		 chat = message.chat.id
		 target = age.split()
		 numy = target[1]
		 bot.restrict_chat_member(message.chat.id, numy)
		 bot.send_message(cid, 'User was muted . 🤫')

@bot.message_handler(content_types=[
    "new_chat_members"
])
def foo(message):
    bot.reply_to(message, "Welcome to our debug group")

#thislist.append("orange")
while 1 == 1:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception:
        pass
