import os
from pyrogram import Client, filters

app = Client(
    "groovenest_bot",
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
    bot_token=os.environ["BOT_TOKEN"]
)

@app.on_message(filters.command("start"))
def start(client, message):
    message.reply_text("🎶 Welcome to GrooveNest Music Bot!")

app.run()
