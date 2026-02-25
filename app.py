import os
from flask import Flask
from pyrogram import filters
from pyrogram.errors import UserNotParticipant
from config import CHANNEL_ID

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <center>
        <img src="/static/gagan.png" style="border-radius: 2px;"/>/>
    </center>
    <style>
        body {
            background: antiquewhite;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 100vh;
            margin: 0;
        }
        footer {
            text-align: center;
            padding: 10px;
            background: antiquewhite;
            font-size: 1.2em;
        }
    </style>
    <footer>
        Made with 💕 by devgagan.in
    </footer>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
@app.on_message(filters.private & ~filters.command("start"), group=-1)
async def global_force_sub(client, message):
    try:
        await client.get_chat_member(CHANNEL_ID, message.from_user.id)
    except UserNotParticipant:
        await message.reply_text(
            "⚠️ Pehle hamara channel join karo, phir bot use karo."
        )
        return
