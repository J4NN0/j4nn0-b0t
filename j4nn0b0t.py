#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
from random import randint
import logging
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import  KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.error import NetworkError, Unauthorized

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# ABOUT DEVELPER

def about(bot, update):
    keyboard = [[InlineKeyboardButton("GitHub", callback_data='git'),
                 InlineKeyboardButton("Twitter", callback_data='twitter'),
                 InlineKeyboardButton("Youtube", callback_data='youtube')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('📌 Developed by @J4NN0.\n', reply_markup=reply_markup)

def call_back(bot, update):
    query = update.callback_query

    if format(query.data) == 'git':
        bot.edit_message_text(text="https://github.com/J4NN0",
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)

    if format(query.data) == 'twitter':
        bot.edit_message_text(text="https://twitter.com/giannofederico",
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)

    if format(query.data) == 'youtube':
        bot.edit_message_text(text="https://www.youtube.com/channel/UC_lI0Z3CnnWLKCZkOR8Z1oQ",
                              chat_id=query.message.chat_id,
                              message_id=query.message.message_id)

# ABOUT DEVELOPER

# SQL LIST.DB

def addtolist(bot, update):
    strings = update.message.text.lower().split()

    if len(strings) >= 2:
        strings.remove('/addtolist')

        # Connecting to the SQL database
        conn = sqlite3.connect('database/list.db')
        c = conn.cursor()

        chat_id = update.message.chat_id
        chat_id = str(chat_id)
        username = update.message.from_user.username

        for s in strings:
            c.execute("INSERT INTO REMINDERS VALUES('"+chat_id+"','"+s+"','"+username+"')")

        conn.commit()
        conn.close()

        update.message.reply_text("All items are added to your list")
    else:
        update.message.reply_text("Syntax error. Press /help for more info")

def rmfromlist(bot, update):
    strings = update.message.text.lower().split()

    if len(strings) >= 2:
        strings.remove('/rmfromlist')

        # Connecting to the SQL database
        conn = sqlite3.connect('database/list.db')
        c = conn.cursor()

        chat_id = update.message.chat_id
        chat_id = str(chat_id)

        report = "❗Report\n✔️ Items successfully deleted from your list:\n"
        err = "\n✖️No items named:\n"

        for s in strings:
            rc = c.execute("DELETE FROM REMINDERS WHERE CHATID='"+chat_id+"' AND ITEM='"+s+"'").rowcount
            if rc <= 0:
                err += s + "\n"
            else:
                report += s + "\n"

        conn.commit()
        conn.close()

        update.message.reply_text(report + err)
    else:
        update.message.reply_text("Syntax error. Press /help for more info")

def show_list(bot, update):
    # Connecting to the SQL database
    conn = sqlite3.connect('database/list.db')
    c = conn.cursor()

    chat_id = update.message.chat_id
    chat_id = str(chat_id)

    c.execute("SELECT ITEM FROM REMINDERS WHERE CHATID='" + chat_id + "'")
    rows = c.fetchall()
    if len(rows) > 0:
        items = ""
        for row in rows:
            items += row[0] + "\n"

        username = update.message.from_user.username
        update.message.reply_text(username + "'s list:\n" + items)
    else:
        update.message.reply_text("No items in your list")

def clear_list(bot, update):
    # Connecting to the SQL database
    conn = sqlite3.connect('database/list.db')
    c = conn.cursor()

    chat_id = update.message.chat_id
    chat_id = str(chat_id)

    if c.execute("DELETE FROM REMINDERS WHERE CHATID='" + chat_id + "'").rowcount > 0:
        update.message.reply_text("List delete successfully")
    else:
        update.message.reply_text("Nothing to delete")

    conn.commit()
    conn.close()
    
# SQL LIST.DB

# ALARM

def set_timer(bot, update, args, job_queue, chat_data):
    """Add a job to the queue."""
    chat_id = update.message.chat_id
    try:
        # args[0] should contain the time for the timer in seconds
        due = int(args[0])
        if due < 0:
            update.message.reply_text('Sorry we can not go back to future!')
            return

        # Add job to queue
        job = job_queue.run_once(alarm, due, context=chat_id)
        chat_data['job'] = job

        update.message.reply_text('Timer successfully set!')

    except (IndexError, ValueError):
        update.message.reply_text('Usage: /set <seconds>')

def unset(bot, update, chat_data):
    """Remove the job if the user changed their mind."""
    if 'job' not in chat_data:
        update.message.reply_text('You have no active timer')
        return

    job = chat_data['job']
    job.schedule_removal()
    del chat_data['job']

    update.message.reply_text('Timer successfully unset!')

def alarm(bot, job):
    """Send the alarm message."""
    bot.send_message(job.context, text='Beep!')

# ALARM

# RANDOM

def random_var(bot, update):
    cmd = update.message.text.lower().split()

    if len(cmd) == 2:
        max_range = int(cmd[1])
        r = randint(0, max_range)
        r = str(r)
        update.message.reply_text("Random value is: " + r)
    else:
        update.message.reply_text("Syntax error. Press /help for more info")

# RANDOM

# EASTER EGGS
# ...
# ...
# ...
# EASTER EGGS

def echo(bot, update):
    update.message.reply_text("Unknown command. Press /help for more info")

def start(bot, update):
    update.message.reply_text("Hi " + update.message.from_user.first_name + " press /help for more info")

def help(bot, update):
    update.message.reply_text("⭕️ /about -> info about developer\n"
                              "\n 📝 LIST 📝\n"
                              "/addtolist <item-1> <item-2> ... : to add items to the list\n"
                              "/rmfromlist <item-1> <item-2> ... : to remove items from the list\n"
                              "/show_list : to see all items\n"
                              "/clear_list : to reset the list\n"
                              "\n 🔀 RANDOM 🔀\n"
                              "/random <number> : will return a random number in range(0, number)\n"
                              "\n ⏰ ALARM ⏰ \n"
                              "/set <seconds> : to set alarm\n"
                              "/unset : to unset alarm\n")

def error(bot, update, error):
    # Log Errors caused by Updates.
    logger.warning('Error: "%s" caused error "%s"', update, error)

def main():
    # Create the Updater
    updater = Updater("TOKEN")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # On different commands
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('about', about))
    dp.add_handler(CallbackQueryHandler(call_back))

    # SQL list.db
    dp.add_handler(CommandHandler('addtolist', addtolist))
    dp.add_handler(CommandHandler('rmfromlist', rmfromlist))
    dp.add_handler(CommandHandler('show_list', show_list))
    dp.add_handler(CommandHandler('clear_list', clear_list))

    # Random
    dp.add_handler(CommandHandler('random', random_var))

    # Alarm
    dp.add_handler(CommandHandler("set", set_timer, pass_args=True, pass_job_queue=True, pass_chat_data=True))
    dp.add_handler(CommandHandler("unset", unset, pass_chat_data=True))

    # On noncommand i.e message
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

if __name__ == '__main__':
    main()
    
