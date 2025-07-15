import os
from pyrogram import Client, filters
import yt_dlp
from pydub import AudioSegment
import asyncio

app = Client(
    "groovenest_bot",
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
    bot_token=os.environ["BOT_TOKEN"]
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("🎶 Welcome to GrooveNest Music Bot!\n\nSend me a **song name** or **YouTube link**, and I’ll download the audio for you.")

@app.on_message(filters.text & ~filters.command(["start"]))
async def music(client, message):
    msg = await message.reply("🔍 Searching for your song...")

    url = message.text

    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'song.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get("title", "🎵 Downloaded Song")

        audio_file = "song.mp3"
        await msg.edit("📤 Uploading song...")

        await message.reply_audio(audio_file, title=title)
        os.remove(audio_file)
        await msg.delete()

    except Exception as e:
        await msg.edit(f"❌ Error: {e}")

app.run()
