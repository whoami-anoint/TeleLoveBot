<h1>TeleLoveBot </h1>

TeleLoveBot is a Telegram bot that sends random love quotes to your significant other, making them feel special and loved every day.

## Purpose
- The purpose of TeleLoveBot is to help couples express their love and affection for each other in a unique and memorable way. By sending a daily love quote to their significant other through Telegram, they can show them how much they care and make them feel appreciated and loved.
Features

<b>TeleLoveBot has the following features:</b>

    - Sends a random love quote to your significant other every day at a specific time.
    - Uses the Telegram platform to deliver the message, ensuring that your significant other receives it instantly.
    - Customizable list of love quotes to choose from, allowing you to personalize the messages you send.
    - Easy to set up and use, with clear instructions and sample code provided.
    
    
  ## Requirements
To use TeleLoveBot, you need the following:

   - A Telegram account for both you and your significant other.
   - A Telegram bot token, which you can obtain by following the instructions provided by Telegram at this link: https://core.telegram.org/bots#6-botfather
   - Python 3.x installed on your computer.
   - The python-telegram-bot library installed on your computer. You can do this by running the following command in your terminal:
```
     pip install python-telegram-bot
```
 
### Installation

To install <b>TeleLoveBot </b>, follow these steps:
 
 1. Clone or download the TeleLoveBot project from the Github repository at https://github.com/[username]/telelovebot. Replace [username] with your Github username.
 2. Open the config.py file in a text editor and replace the BOT_TOKEN and CHAT_ID variables with your actual bot token obtained from BotFather and your girlfriend's Telegram chat ID, respectively.
 3. Customize the LOVE_QUOTES list with your own list of love quotes, or use the default list provided.
 4. Save the config.py file and close the text editor.
 5. Run the telelovebot.py file using Python:
 ```
 python telelovebot.py
```
 6. Verify that the bot is working by checking that your girlfriend has received a random love quote from the bot in her Telegram chat.
 
### Usage

To use TeleLoveBot, follow these steps:


   7.  Set up the bot as described in the Installation section.
   8.  Customize the LOVE_QUOTES list in the config.py file with your own list of love quotes, if desired.
   9. Schedule the bot to run every day at a specific time using a task scheduler like cron on Linux or Task Scheduler on Windows. For example, you can use the following command to schedule the bot to run every day at 8:00 AM:
```
   0 8 * * * /usr/bin/python /path/to/telelovebot.py
```
   10. Verify that the bot is running by checking that your girlfriend has received a random love quote from the bot in her Telegram chat at the scheduled time.
   
  ### Conclusion

TeleLoveBot is a simple yet powerful way to express your love and affection for your significant other through a Telegram bot. With its customizable love quotes and easy-to-use interface, it's a great way to make your significant other feel special and loved every day.



 
