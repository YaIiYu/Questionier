from aiogram import Bot, Dispatcher, executor, types, filters
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InputFile, InlineKeyboardButton


class KeyboardLibrary():

    async def set_inline_keyboard(self, count, button_message):
        ex_keyboard = InlineKeyboardMarkup(resize_keyboard=True)
        for i in range(count):
            button = InlineKeyboardButton(button_message[i], callback_data=f'question_{i+1}')
            ex_keyboard.add(button)
        return ex_keyboard

    async def set_reply_keyboard(self, count, button_message):
        # print(f"Count: {count}")
        ex_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        for i in range(count):
            button = KeyboardButton(button_message[i])
            ex_keyboard.add(button)
        return ex_keyboard

    async def set_start_reply_keyboard(self, test_ids):
        #print(f"Count: {test_ids}")
        ex_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        for test in test_ids:
            #print(f'Test title: {test}')
            button = KeyboardButton(test["title"], command=f'test_{test["title"]}')
            ex_keyboard.add(button)
        return ex_keyboard

