from telegram import ChatAction


def set_timer(bot, update, args, job_queue, chat_data):
    """Add a job to the queue."""

    bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)

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

    bot.send_chat_action(chat_id=update.message.chat_id, action=ChatAction.TYPING)

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