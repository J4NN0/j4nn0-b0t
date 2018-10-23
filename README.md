# j4nn0-b0t
This is a python telegram bot hosted on [Heroku](https://www.heroku.com/).

I used [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) API and [sqlite3](https://docs.python.org/2/library/sqlite3.html).

You can find it on telegram: [J4NN0_Bot](http://telegram.me/J4NN0_Bot)

# Database

You need to 

    import sqlite3
    
and I aslo suggest you to download [DB Browser for SQLite](https://sqlitebrowser.org) to easly manage (create, delete, modify and much more) the database. 

# BOT usage

- ⭕ Developer
    - /about: to see info about developer
    
- 📝 List
    - /addtolist \<items>: to add one or several items to your personal list (to do list, reminders or what you want)
    - /rmfromlist \<items>: to remove  one or several itmes from your personal list
    - /show_list: it shows items that you added to your personal list
    - /clear_list: to delete all items from your pesonal list

- ❓Message from strangers
    - /topic: to see topic that contains at least one message from a stranger
    - /msg [-user] \<topic> \<text>: to sent a message that everyone can read; -user is optional, if inserted your username will be showed with the message you sent
    - /showmsg \<topic>: to see message about a specific topic
    - /delmsg \<topic>: to delete a your message that you posted in that topic
    - /tagmsg: to check if someone tag you in a topic or message (tag in telegram: @username)
    - /personalmsg: to see all messages you sent
  
- ⚠ Data store ⚠
    - Work in progress ...

- 🔀 Random value
    - /random \<number>: it will return a random number in range(0, number)

- ⏰ Alarm
    - /timer \<seconds>: to set a timer and wait for your message
    
- Info about bot
    - /help:  to have info about all commands
    
##### Easter egg

*There are also a lot of easter eggs (you can't find it in this code) that i wrote to have fun with my friends. Try to find them and enjoy!*

# How to host BOT on Heroku

1. Register on [Heroku](https://www.heroku.com/)
2. Download and install [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) and [git](https://git-scm.com/downloads)
3. Create a folder and put inside it
        
       script.py
       Procfile
       runtime.txt
       requirements.txt
       
    Or clone the project
    
        git clone https://github.com/J4NN0/j4nn0-b0t.git
       
   You can also have a "app.json" schema useful to declare environment variables, add-ons, and other information required to run an app on Heroku. More info [here](https://devcenter.heroku.com/articles/app-json-schema)

4. Put inside "Procfile"

       worker: python script.py
   
5. You may select your python version and put it in "runtime.txt"

       python --version
        
   For example if the Python version is 3.6.6 just put inside the file:
   
       python-3.6.6

6. Specify explicit dependency versions inside "requirements.txt"
    
       python-3.6.6
   
   For example i'm using [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) API.
   So my file "requirements.txt" will contain 
   
       python-telegram-bot==8.1.1
       
   To update this file, you can use the pip freeze command in your active virtual environment:
   
       pip freeze > requirements.txt
       
   More info [here](https://devcenter.heroku.com/articles/python-runtimes#selecting-a-runtime) 
   
7. Now in terminal 
   If you haven't already, log in to your Heroku account and follow the prompts to create a new SSH public key
   
       heroku login
   
   Create git repository   

       git init
   
   Create heroku app
   
       heroku create
   
   Push your code (or deploy changes) into heroku app
   
       git add .
       git commit -m "message"
       git push heroku master

8. Run your worker

       heroku ps:scale worker=1

9. Check logs with

       heroku logs --tail
        
10. Enjoy your bot

# Official Heroku Guide

- [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)
