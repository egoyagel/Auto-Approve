from pyrogram import Client, filters
from pyrogram.types import *
import os

CHAT_ID = os.getenv("-1001842902572")
API_ID = os.getenv("23776178")
API_HASH = os.getenv("b69598ab1d4021eb968d2db5b8bed30a")
BOT_TOKEN = os.getenv("6323849431:AAHX8uFm54ZkJcSD2hmnoLlxO1lvLaunP3A")

app = Client(
    session_name="session_name.session",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

TEXT = "Hello {}, Welcome To {}"
APPROVED = True  # set to True by default

# auto approve members 
@app.on_chat_join_request((filters.group | filters.channel) & filters.chat(CHAT_ID) if CHAT_ID else (filters.group | filters.channel))
async def autoapprove(client: Client, message: ChatJoinRequest):
    chat = message.chat
    user = message.from_user
    print(f"{user.first_name} Joined")
    if APPROVED:
        await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
        await client.send_message(chat_id=chat.id, text=TEXT.format(user.mention, chat.title))

# enable/disable auto approve feature
@app.on_message(filters.command("autoapprove") & filters.private)
async def toggle_autoapprove(client: Client, message: Message):
    chat = message.chat
    user_id = message.from_user.id
    member = await client.get_chat_member(chat_id=chat.id, user_id=user_id)
    if member.can_manage_chat:
        if len(message.command) > 1:
            action = message.command[1].lower()
            if action == "on":
                global APPROVED
                APPROVED = True
                await message.reply("Auto approve is now enabled.")
            elif action == "off":
                global APPROVED
                APPROVED = False
                await message.reply("Auto approve is now disabled.")
            else:
                await message.reply("Invalid argument. Use 'on' or 'off'.")
        else:
            await message.reply(f"Auto approve is currently {'enabled' if APPROVED else 'disabled'}. Use 'on' or 'off' to toggle.")
    else:
        await message.reply("Only group admins can enable or disable auto approve.")

app.run()
