from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup

import buttons as b

# Обычные клавиатуры
main_keyboard = ReplyKeyboardMarkup([
    [b.date_button, b.help_button],
    [b.settings_button]
], resize_keyboard=True)

settings_keyboard = ReplyKeyboardMarkup([
    [b.back_button]
], resize_keyboard=True)

# Inline-клавиатуры
inline_test_keyboard = InlineKeyboardMarkup([
    [b.steam_random_button],
    [b.snake_button],
    [b.brawler_button]
])