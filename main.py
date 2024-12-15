from pyrogram import Client, filters
from pyrogram.types import Message

import config as cfg


app = Client(
    "gs_super_bot",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)


@app.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    await message.reply("О! Привет! Я бот, прикинь?!\nНапиши /help, чтобы увидеть мой функционал!")


@app.on_message(filters.command("help"))
async def help_command(client: Client, message: Message):
    await message.reply("Я умею:\n/help - показать команды\n/date - напоминать дату")


@app.on_message(filters.text)
async def echo(client: Client, message: Message):
    await message.reply("Ой, такого я не знаю!\nНапиши /help, чтобы увидеть мой функционал!")

app.run()