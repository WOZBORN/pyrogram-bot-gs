from pyrogram.types import KeyboardButton, InlineKeyboardButton, WebAppInfo

from brawl_stars import brawler_info

# Общие кнопки (клавиатура)
back_button = KeyboardButton(f"◀️Назад")

# Кнопки меню (клавиатура)
date_button = KeyboardButton(f"🗓️Дата")
help_button = KeyboardButton(f"❓Помощь")
settings_button = KeyboardButton(f"⚙️Настройки")

# Кнопки inline
steam_random_button = InlineKeyboardButton("🎮Steam Random", url="https://store.steampowered.com/explore/random/")
snake_button = InlineKeyboardButton("🐍Snake", web_app=WebAppInfo(url="https://snake.io/"))
brawler_button = InlineKeyboardButton("🏹Brawler Shelly", callback_data="shelly")