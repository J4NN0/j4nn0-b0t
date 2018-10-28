# Database

### list.db

It is composed by a single table REMINDERS:

- CHATID: chat id for that user
- USRNAME: username of the user
- ITEM: the item added by the user
    
Every time a user add one or more item, these are added to the db.

### stranger.db

It is composed by a single table MESSAGES:

- CHATID: chat id for that user
- USRNAME: username of the user if the optional command -user is used
- TOPIC: the topic of the message
- MSG: the message that the user sent

# More

Download [DB Browser for SQLite](https://sqlitebrowser.org) to see and modify these databases. 
