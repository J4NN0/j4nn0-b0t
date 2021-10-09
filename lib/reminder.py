import sqlite3
from telegram import ChatAction


def add_to_list(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    strings = update.message.text.lower().split()

    if len(strings) >= 2:
        strings.remove('/addtolist')

        # Connecting to the SQL database
        conn = sqlite3.connect('../database/list.db')
        c = conn.cursor()

        chat_id = update.message.chat_id
        chat_id = str(chat_id)
        username = update.message.from_user.username

        for s in strings:
            c.execute("INSERT INTO REMINDERS VALUES('" + chat_id + "','" + s + "','" + username + "')")

        conn.commit()
        conn.close()

        update.message.reply_text("All items are added to your list")
    else:
        update.message.reply_text("Syntax error. Press /help for more info")


def remove_from_list(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    strings = update.message.text.lower().split()

    if len(strings) >= 2:
        strings.remove('/rmfromlist')

        # Connecting to the SQL database
        conn = sqlite3.connect('../database/list.db')
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
    bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    # Connecting to the SQL database
    conn = sqlite3.connect('../database/list.db')
    c = conn.cursor()

    chat_id = update.message.chat_id
    chat_id = str(chat_id)

    c.execute("SELECT ITEM FROM REMINDERS WHERE CHATID='" + chat_id + "'")
    rows = c.fetchall()
    conn.close()
    if len(rows) > 0:
        items = ""
        for row in rows:
            items += row[0] + "\n"

        username = update.message.from_user.username
        update.message.reply_text("📄 " + username + "'s list:\n" + items)
    else:
        update.message.reply_text("No items in your list")


def clear_list(bot, update):
    bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)

    # Connecting to the SQL database
    conn = sqlite3.connect('../database/list.db')
    c = conn.cursor()

    chat_id = update.message.chat_id
    chat_id = str(chat_id)

    if c.execute("DELETE FROM REMINDERS WHERE CHATID='" + chat_id + "'").rowcount > 0:
        conn.commit()
        update.message.reply_text("List delete successfully")
    else:
        update.message.reply_text("Nothing to delete")

    conn.close()