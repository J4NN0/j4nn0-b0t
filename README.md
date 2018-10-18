# j4nn0-b0t
This is a python telegram bot hosted on [Heroku](https://www.heroku.com/)

You can find it on telegram [J4NN0_Bot](http://telegram.me/J4NN0_Bot)

# How to host BOT on Heroku

1. Register on [Heroku](https://www.heroku.com/)
2. Download and install [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up) and [git](https://git-scm.com/downloads)
3. Create a folder and put inside it
        
       script.py
       Procfile
       runtime.txt
       requirements.txt
       
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
