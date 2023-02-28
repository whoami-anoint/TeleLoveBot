import telegram
import random

# Replace YOUR_BOT_TOKEN with your actual bot token obtained from BotFather
bot = telegram.Bot(token='YOUR_BOT_TOKEN')

# Define a list of love quotes to choose from
love_quotes = [
    "You are the sunshine that brightens up my day.",
    "You make me the happiest person in the world.",
    "My love for you grows stronger every day.",
    "You are the missing puzzle piece in my life.",
    "I cannot imagine my life without you."
]

# Define a function to send a random love quote to your girlfriend
def send_love_quote(chat_id):
    quote = random.choice(love_quotes)
    bot.send_message(chat_id=chat_id, text=quote)

# Replace YOUR_GIRLFRIEND_CHAT_ID with your girlfriend's Telegram chat ID
send_love_quote(YOUR_GIRLFRIEND_CHAT_ID)
