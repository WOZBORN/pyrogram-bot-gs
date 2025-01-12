from pyrogram.types import ReplyKeyboardMarkup

import buttons as b

main_keyboard = ReplyKeyboardMarkup([
    [b.date_button, b.help_button],
    [b.settings_button]
], resize_keyboard=True)

settings_keyboard = ReplyKeyboardMarkup([
    [b.back_button]
], resize_keyboard=True)

