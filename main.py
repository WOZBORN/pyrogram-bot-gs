from datetime import datetime
import operator

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
    await message.reply(
        "О! Привет! Я бот, прикинь?!\n"
        "Напиши /help, чтобы увидеть мой функционал!"
    )


@app.on_message(filters.command("help"))
async def help_command(client: Client, message: Message):
    await message.reply(
        "Я умею:\n"
        "/help - показать команды\n"
        "/date - напоминать дату\n"
        "/calc - калькулятор"
    )


@app.on_message(filters.command("date"))
async def date_command(client: Client, message: Message):
    await message.reply(f"Сегодня {datetime.now().strftime('%d.%m.%Y')}")


@app.on_message(filters.command("calc"))
async def calc_command(client: Client, message: Message):
    content = message.text.split()

    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    if len(content) != 4 or not content[1].isdigit() or not content[3].isdigit() or content[2] not in operators:
        await message.reply(
            "Неправильное написал пример. Попробуй такие:\n"
            "/calc 2 + 2\n"
            "/calc 2 * 2\n"
            "/calc 2 - 2\n"
            "/calc 2 / 2"
        )

    num1 = int(content[1])
    num2 = int(content[3])
    op = content[2]
    try:
        result = operators[op](num1, num2)
    except ZeroDivisionError:
        await message.reply("На ноль делить нельзя!")
        return

    await message.reply(f"{num1} {op} {num2} = {result}")


@app.on_message(filters.text)
async def echo(client: Client, message: Message):
    await message.reply(
        "Ой, такого я не знаю!\n"
        "Напиши /help, чтобы увидеть мой функционал!"
    )

app.run()