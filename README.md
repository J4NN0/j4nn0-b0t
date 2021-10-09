# j4nn0-b0t

[![https://telegram.me/J4NN0](https://img.shields.io/badge/💬_Telegram-J4NN0-blue.svg)](https://telegram.me/J4NN0) [![https://telegram.me/J4NN0_Bot](https://img.shields.io/badge/💬_Bot_Telegram-J4NN0_Bot-blue.svg)](https://telegram.me/J4NN0_Bot) [![https://pypi.org/project/python-telegram-bot/](https://img.shields.io/pypi/pyversions/python-telegram-bot.svg)](https://pypi.org/project/python-telegram-bot/) [![https://www.gnu.org/licenses/lgpl-3.0.html](https://img.shields.io/pypi/l/python-telegram-bot.svg)](https://www.gnu.org/licenses/lgpl-3.0.html)

The BOT is hosted on [Heroku](https://www.heroku.com/) and it has been tested using Python `v3.6.6`. Also, [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) API and [sqlite3](https://docs.python.org/2/library/sqlite3.html) are needed.  

J4NN0 BOT main features:
1. Store and retrieve data from a database: you can save/delete/show items on your personal list. 
2. Set an alarm: when time is up the BOT will remind you what you asked for.

Check it out on telegram: [@J4NN0_Bot](http://telegram.me/J4NN0_Bot)

### Demo
[![Watch the video](https://img.youtube.com/vi/2pSjPOuMDhk/maxresdefault.jpg)](https://youtu.be/2pSjPOuMDhk)

# Table of Contents
- [Database](https://github.com/J4NN0/j4nn0-b0t#database)
- [BOT usage](https://github.com/J4NN0/j4nn0-b0t#bot-usage)
- [How to host BOT on Heroku](https://github.com/J4NN0/j4nn0-b0t#how-to-host-bot-on-heroku)
- [Utility](https://github.com/J4NN0/j4nn0-b0t#utility)

# Database

You need to 

    import sqlite3
    
I also suggest you to download [DB Browser for SQLite](https://sqlitebrowser.org) to easily manage (create, read, delete, modify, etc.) the database(s). 

# BOT usage

- ⭕ Developer
    - `/about`: to see info about developer
    
- 📝 List
    - `/addtolist <item>`: to add one or several items to your personal list.
    - `/rmfromlist <item>`: to remove  one or several items from your personal list.
    - `/show_list`: it shows all items in your personal list.
    - `/clear_list`: to delete all items from your personal list.

- 🔀 Random value
    - `/random <number>`: it will return a random number between 0 and <number>

- ⏰ Alarm
    - `/timer <seconds>`: to set a timer and wait for your message
    
- Info about bot
    - `/help`:  to have info about all commands
    
#### Easter egg

*There are also a lot of Easter eggs (you can't find it in this code) that i wrote to have fun with my friends. Try to find them and enjoy!*

# How to host BOT on Heroku

1. Register on [Heroku](https://www.heroku.com/)
2. Download and install [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) and [git](https://git-scm.com/downloads)
3. Create a folder and put inside it
        
       bot.py
       Procfile
       runtime.txt
       requirements.txt
       
   You can also have a "app.json" schema useful to declare environment variables, add-ons, and other information required to run an app on Heroku. More info [here](https://devcenter.heroku.com/articles/app-json-schema)

4. Put inside "Procfile"

       worker: python script.py
   
5. Check your python version with

       python --version
        
   And put it in "runtime.txt". 
   For example, if the Python version is 3.6.6 just put inside the file:
   
       python-3.6.6

6. Specify explicit dependency versions inside "requirements.txt"
   
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
           
    Or clone this repo
    
       git clone https://github.com/J4NN0/j4nn0-b0t.git
   
   Create heroku app
   
       heroku create
   
   Push your code (or deploy changes) into heroku app
   
       git add .
       git commit -m 'message'
       git push heroku master

8. Run your worker

       heroku ps:scale worker=1

9. Check logs with

       heroku logs --tail
        
10. Enjoy your bot

#### Official Heroku Guide

Checkout also the offical heroku guide: [Getting Started on Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)

# Utility

- [First steps](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot)
- [Telegram Bot’s documentation](https://python-telegram-bot.readthedocs.io/en/stable/index.html)
- [Telegram Bot API](https://core.telegram.org/bots/api#forcereply)
- [Code snippets](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Code-snippets#general-code-snippets)
