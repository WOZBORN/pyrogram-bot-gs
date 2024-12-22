from pyrogram.types import KeyboardButton
from pyrogram import emoji

# Общие кнопки
back_button = KeyboardButton(f"{emoji.BACK_ARROW}Назад")

# Кнопки меню
date_button = KeyboardButton(f"{emoji.CALENDAR}Дата")
help_button = KeyboardButton(f"{emoji.RED_QUESTION_MARK}Помощь")
settings_button = KeyboardButton(f"{emoji.GEAR}Настройки")
