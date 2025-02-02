from datetime import datetime
import operator

from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery

import brawl_stars
import config as cfg
import database
import keyboards



app = Client(
    "gs_super_bot",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)


database.create_user_table()


@app.on_callback_query()
async def inline_callback(client: Client, callback_query: CallbackQuery):
    tg_user = callback_query.from_user
    user = database.get_user_name(tg_user.id)
    if user == None:
        database.add_user(tg_user.id, tg_user.first_name)
    battle_tag = database.get_battletag(tg_user.id)[0]
    if callback_query.data == "cat":
        await callback_query.message.delete()
        await callback_query.message.reply_photo("https://cataas.com/cat", reply_markup=keyboards.cat_keyboard)
        return
    if callback_query.data == "shelly":
        if battle_tag is None:
            await callback_query.message.edit(
                "Не знаю твой battletag. Задай его так:\n /battletag #ТВОЙ-БАТТЛ-ТЭГ")
            return
        brawler_info = brawl_stars.brawler_info(battle_tag, "shelly")
        await callback_query.message.edit(brawler_info)
        return


@app.on_message(filters.command("start") | filters.regex("◀️Назад"))
async def start_command(client: Client, message: Message):
    await message.reply(
        "О! Привет! Я бот, прикинь?!\n",
        reply_markup=keyboards.main_keyboard
    )


@app.on_message(filters.command("help") | filters.regex("❓Помощь"))
async def help_command(client: Client, message: Message):
    await message.reply(
        "Я умею:\n"
        "/help - показать команды\n"
        "/date - напоминать дату\n"
        "/calc - калькулятор"
        "/cat - котик"
    )


@app.on_message(filters.command("cat") | filters.regex("🐈Котик"))
async def cat_command(client: Client, message: Message):
    url = "https://cataas.com/cat"
    await message.reply_photo(photo=url, reply_markup=keyboards.cat_keyboard)


@app.on_message(filters.command("inline"))
async def inline_send_command(client: Client, message: Message):
    await message.reply(
        "Вот окно для теста inline-кнопок!",
        reply_markup=keyboards.inline_test_keyboard
    )



@app.on_message(filters.command("battletag"))
async def battletag_command(client: Client, message: Message):
    content = message.text.split()
    if len(content) != 2:
        await message.reply(
            "Неправильно написал. Попробуй так:\n"
            "/battletag #ТВОЙ-БАТТЛ-ТЭГ"
        )
        return
    tg_user = message.from_user
    user = database.get_user_name(tg_user.id)
    if user == None:
        database.add_user(tg_user.id, tg_user.first_name)
    database.set_battletag(tg_user.id, content[1])
    await message.reply(f"Твой баттлтэг: {content[1]}")


@app.on_message(filters.command("brawler"))
async def brawler_command(client: Client, message: Message):
    content = message.text.split()
    tg_user = message.from_user
    user = database.get_user_name(tg_user.id)
    if user == None:
        database.add_user(tg_user.id, tg_user.first_name)
    battle_tag = database.get_battletag(tg_user.id)[0]
    if len(content) != 2:
        await message.reply(
            "Неправильно написал. Попробуй так:\n"
            "/brawler Shelly"
        )
        return
    if battle_tag is None:
        await message.reply(
            "Не знаю твой battletag. Задай его так:\n"
            "/battletag #ТВОЙ-БАТТЛ-ТЭГ"
        )
        return
    brawler_info = brawl_stars.brawler_info(battle_tag, content[1])
    await message.reply(brawler_info)


@app.on_message(filters.command("settings") | filters.regex("⚙️Настройки"))
async def settings_command(client: Client, message: Message):
    await message.reply(
        "Меню настроек. Выберите кнопку.",
        reply_markup=keyboards.settings_keyboard
    )


@app.on_message(filters.command("date") | filters.regex("🗓️Дата"))
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