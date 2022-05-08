import telebot
#words=['id','reddy','+917377379177']
API_TOKEN = '5353018551:AAE7dBbVq9aaok9dCpqQhjzbJeJeM71Nubg'

bot = telebot.TeleBot(API_TOKEN)
@bot.channel_post_handler(content_types=['text'])
def delred(message):
    if 'reddy' in message.text.lower():
        bot.delete_message(message.chat.id, message.message_id)
    elif 'id' in message.text.lower():
        bot.delete_message(message.chat.id, message.message_id)
    elif '+91' in message.text.lower():
        bot.delete_message(message.chat.id, message.message_id)
@bot.message_handler(commands=['start'])
def greetmess(message):
	bot.reply_to(message,'Hello')
bot.infinity_polling()
