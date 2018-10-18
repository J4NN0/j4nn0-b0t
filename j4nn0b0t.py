#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import  KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.error import NetworkError, Unauthorized

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# START SHOPPING SECTION

def addtolist(bot, update):
    strings = update.message.text.lower().split

    if len(strings)>2:
        strings.remove('/addtolist')
        fp = open("shopping_list", "a")
        for s in strings:
            fp.write(s + "\n")
        fp.close()
        update.message.reply_text("All items are added to the list")
    else:
        update.message.reply_text("Syntax error. Press /help for more info")

def removefromlist(bot, update):
    strings = update.message.text.lower().split

    if len(strings)>2:
        strings.remove('/removefromlist')
        fp = open("shopping_list", "a")
    else:
        update.message.reply_text("Syntax error. Press /help for more info")

def show_shop(bot, update):
    fp = open("shopping_list", "r")
    data = fp.readlines()
    update.message.reply_text("Shopping list:\n")
    for line in data:
        update.message.reply_text(line)

def clear_shop(bot, update):
    fp = open("shopping_list", "w")
    fp.write('')
    fp.close()
    update.message.reply_text("Reset succefully")

# END SHOPPING SECTION

# START DEBTS SECTION

def set_debts(bot, update):
    string = update.message.text.lower().split()
    
    if len(string)==4:
        fp = open(string[1], "a")
        fp.write(string[2] + " " + string[3] + "\n")
        fp.close()
        update.message.reply_text("%s payed for %s an amount of %s€", string[1], string[2], string[3])
    else:
        update.message.reply_text("Syntax error. Press /help for more info")

def rate_debts(bot, update):
    string = update.message.text.lower().split()
    dic = {}

    if len(string)>2:
        string.remove('/rate_debts')

        for s in string:
            for tmp in string:
                dic[tmp] = 0 #reset dictionary
            fp = open(s, "r")
            data = fp.readlines()
            for line in data:
                words = line.split()
                for name in string:
                    if name == words[0]:
                        dic[name] += int(words[1])
            update.message.reply_text("❗️ " + s + " has to receive:")
            for name in string:
                if name != s:
                    if name in dic:
                        val = dic.get(name)
                        update.message.reply_text("From " + name + " import " + str(val))
            fp.close()

    else:
        update.message.reply_text("Syntax error. Press /help for more info")

def show_debts(bot, update):
    string = update.message.text.lower().split()

    if len(string)>2:
        string.remove('/show_debts')

        for s in string:
            fp = open(s, "r")
            txt = fp.read()
            fp.close()
            update.message.reply_text("▶️ " + s)
            update.message.reply_text(txt)
    else:
        update.message.reply_text("Syntax error. Press /help for more info")

def clear_debts(bot, update):
    string = update.message.text.lower().split()

    if len(string)>2:
        string.remove('/clear_debts')

        for s in string:
            fp = open(s, "w")
            fp.write('')
            fp.close()
            update.message.reply_text("File " + s + " reset succefully")
    else:
        update.message.reply_text("Syntax error. Press /help for more info")

# END DEBTS SECTION

# START ALARM

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

# END ALARM

# START ABOUT DEVELPER

def about(bot, update):
    keyboard = [[InlineKeyboardButton("GitHub", callback_data='git'),
                 InlineKeyboardButton("Twitter", callback_data='twitter')]]

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

#END ABOUT DEVELOPER

def start(bot, update):
    update.message.reply_text("Hi " + update.message.from_user.first_name + "press /help for more info")

def help(bot, update):
    update.message.reply_text("⭕️ /about -> for more info\n"
                              "\n 📝 SHOPPING 📝\n"
                              "/addtolist <item-1> <item-2> ... -> to add items to the list\n"
                              "/removefromlist <item-1> <item-2> ... -> to remove items from the list\n"
                              "/show_shop -> to see all items\n"
                              "/clear_shop -> to reset the shop\n"
                              "\n 💸 DEBTS 💸 \n"
                              "/set_debts <name1> <name2> <cost> -> to save that name1 payed cost for name2\n"
                              "/rate_debts <name-1> <name-2> ... -> to calculate the debts\n"
                              "/show_debts <name-1> <name-2> ... -> to see actual debts\n"
                              "/clear_debts <name-1> <name-2> ... -> to reset all cost to zero\n"
                              "\n ⏰ ALARM ⏰ \n"
                              "/set <seconds> -> to set alarm\n"
                              "/unset -> to unset alarm\n")

def echo(bot, update):
    update.message.reply_text("Press /help for more info")

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

    # Shopping
    dp.add_handler(CommandHandler('addtolist', addtolist))
    dp.add_handler(CommandHandler('removefromlist', removefromlist))
    dp.add_handler(CommandHandler('show_shop', show_shop))
    dp.add_handler(CommandHandler('clear_shop', clear_shop))

    # Debts
    dp.add_handler(CommandHandler('set_debts', set_debts))
    dp.add_handler(CommandHandler('rate_debts', rate_debts))
    dp.add_handler(CommandHandler('show_debts', show_debts))
    dp.add_handler(CommandHandler('clear_debts', clear_debts))
    
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
