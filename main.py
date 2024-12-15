import random

from pyrogram import Client, filters
from pyrogram.types import Message

import config as cfg

app = Client(
    "gs_super_bot",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

@app.on_message(filters.text & filters.private)
async def echo(client: Client, message: Message):
    if random.randint(1,2) == 1:
        await message.reply(message.text)
    else:
        await message.reply(message.text[::-1])

app.run()