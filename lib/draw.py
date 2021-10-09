from random import randint
from telegram import ChatAction


def random_var(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    cmd = update.message.text.lower().split()

    if len(cmd) == 2:
        max_range = int(cmd[1])
        r = randint(0, max_range)
        r = str(r)
        update.message.reply_text("Random value is: " + r)
    else:
        update.message.reply_text("Syntax error. Press /help for more info")
