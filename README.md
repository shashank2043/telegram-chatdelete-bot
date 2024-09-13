# Telegram Chat Deletion Bot

This Python bot automatically deletes messages containing specified words or phrases from a Telegram channel. It also responds with a greeting when a user starts a chat with the bot.

## Features

- **Message Filtering:** Deletes messages that contain specified words or phrases.
- **Greeting Response:** Sends a welcome message when a user starts a chat with the bot.

## Requirements

This bot requires Python to run and utilizes the `pyTelegramBotAPI` and `requests` libraries. 

## How to Use

1. **Clone the Repository**

   To get the latest version of the bot, clone the repository from GitHub using the following command:

  ```bash
  git clone https://github.com/shashank2043/telegram-chatdelete-bot.git
```
  Navigate to the cloned directory:
  ```bash
  cd telegram-chatdelete-bot
```
2. **Install the Requirements**

   Install the required libraries by running:

   ```bash
   pip install -r requirements.txt
   ```
   This will install pyTelegramBotAPI, requests, and any other dependencies listed in requirements.txt.

4. **Configure the Bot**

   Open the script file (main.py) and replace 'enter bot token here' with your actual Telegram bot token:
   ```bash
   API_TOKEN = 'enter bot token here'

6. **Run the Bot**

   Execute the script using the following command:
   ```bash
   python main.py
This will start the bot and begin processing messages according to the defined rules.

##Notes
-Ensure your bot has the necessary permissions to delete messages in the channel.
-Adjust the FILTERED_WORDS list in the script if you want to change the words or phrases that trigger message deletion.
