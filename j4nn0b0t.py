#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from telegram import ChatAction
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from util import draw, alarm, reminder

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def manage_text(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    msg = update.message.text.lower()

    if msg in ('j4nn0', 'j4nno'):
        update.message.reply_text("H1 f4th3r")
    elif msg == 'gianno':
        update.message.reply_text('Hi father')
    elif msg in ('thanks', 'thank you', 'ty', 'thank you so much'):
        update.message.reply_text("No problem master. I'm at your service")
    else:
        update.message.reply_text("Sorry I can't understand. Press /help for more info")


def manage_command(bot, update):
    update.message.reply_text("Unknown command. Press /help for more info")


def start(bot, update):
    update.message.reply_text("Hi " + update.message.from_user.first_name + " press /help for more info")


def help(bot, update):
    update.message.reply_text("⭕️ /about: info about developer\n"
                              "\n📝 LIST 📝\n"
                              "/addtolist <items>: to add items to the list\n"
                              "/rmfromlist <items>: to remove items from the list\n"
                              "/show_list: to see all items\n"
                              "/clear_list: to reset the list\n"
                              "\n🔀 RANDOM 🔀\n"
                              "/random <number>: will return a random number in range(0, number)\n"
                              "\n⏰ ALARM ⏰ \n"
                              "/set <seconds>: to set alarm\n"
                              "/unset: to unset alarm\n")


def about(bot, update):
    keyboard = [[InlineKeyboardButton("GitHub", callback_data='git'),
                 InlineKeyboardButton("Twitter", callback_data='twitter'),
                 InlineKeyboardButton("Youtube", callback_data='youtube')]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('📌 Developed by @J4NN0.\n', reply_markup=reply_markup)


def about_call_back(bot, update):
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


def error(bot, update, err):
    # Log Errors caused by Updates.
    logger.warning('Error: "%s" caused error "%s"', update, err)


def main():
    # Create the Updater
    updater = Updater("YOUR_TOKEN_HERE")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # On different commands
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(CommandHandler('about', about))
    dp.add_handler(CallbackQueryHandler(about_call_back))

    # SQL Reminders (list.db)
    dp.add_handler(CommandHandler('addtolist', reminder.add_to_list))
    dp.add_handler(CommandHandler('rmfromlist', reminder.remove_from_list))
    dp.add_handler(CommandHandler('show_list', reminder.show_list))
    dp.add_handler(CommandHandler('clear_list', reminder.clear_list))

    # Random
    dp.add_handler(CommandHandler('random', draw.random_var))

    # Alarm
    dp.add_handler(CommandHandler("set", alarm.set_timer, pass_args=True, pass_job_queue=True, pass_chat_data=True))
    dp.add_handler(CommandHandler("unset", alarm.unset, pass_chat_data=True))

    # Easter eggs ...

    # On non-command, i.e just text message
    dp.add_handler(MessageHandler(Filters.text, manage_text))
    dp.add_handler(MessageHandler(Filters.command, manage_command))

    # Log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()
