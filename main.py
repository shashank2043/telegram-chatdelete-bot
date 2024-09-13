import telebot  # Import the telebot library to interact with Telegram API

# Replace with your actual bot token
API_TOKEN = 'enter bot token here'

# Initialize the bot with the provided API token
bot = telebot.TeleBot(API_TOKEN)

# List of words or phrases to filter out from messages
FILTERED_WORDS = ['word1', 'word2', 'word3']

@bot.channel_post_handler(content_types=['text'])
def filter_messages(message):
    """
    Handler function to filter and delete messages containing certain words or phrases.
    
    Args:
    message (telebot.types.Message): The message object received from the channel.
    """
    # Convert the message text to lowercase for case-insensitive comparison
    message_text = message.text.lower()
    
    # Check if any word from FILTERED_WORDS is in the message text
    if any(word in message_text for word in FILTERED_WORDS):
        # Delete the message if it contains any filtered word or phrase
        bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(commands=['start'])
def greet_user(message):
    """
    Handler function to greet users when they start a chat with the bot.
    
    Args:
    message (telebot.types.Message): The message object received when the command is issued.
    """
    bot.reply_to(message, 'Hello!')

# Start polling for messages
bot.infinity_polling()
