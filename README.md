# Auto Approve Bot
This is a Pyrogram bot that automatically approves join requests for a Telegram group or channel, and can be toggled on or off by group admins.

## Setup
To use this bot, you'll need to have the following:

-A Telegram account
-Python 3.x installed on your computer
-A Telegram bot token obtained from the BotFather
-The pyrogram library installed (you can do this by running `pip install pyrogram`)


To get started, clone this repository and cd into the directory:

```bash
  git clone https://github.com/irymee/Auto-Approve.git
  cd Auto-Approve
  python3 bot.py
```

## Usage
To toggle auto-approval, send a message to the bot with the command `/autoapprove on` or `/autoapprove off`, depending on whether you want to turn auto-approval on or off. Only group admins can toggle this feature.
