import logging
import asyncio
import re
from aiogram import Bot, Dispatcher
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram import types, filters
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text

import data.Question_db as question_db
from bot.Token import TgToken as Token
import bot.bot_functions as bot_func
import bot.Alphabet_conv as abc_converter

logging.basicConfig(level=logging.INFO)

bot = Bot(token=Token.TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
keylib = None


def start_bot(kLib):
    global keylib
    keylib = kLib
    executor.start_polling(dp, skip_updates=True)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot_func.start(question_db, bot, message.chat.id, keylib, "Привіт, вибери тест або опитання")


@dp.message_handler(lambda message: 'question' in message.text.lower())
async def handle_question(message: types.Message):
    pass


@dp.message_handler(lambda message: message.text)
async def handle_test(message: types.Message):
    if "Тест" in message.text:
        test = bot_func.extract_number_from_button(message.text)
        print(f"test: {test}")
        user_id = message.chat.id
        if question_db.is_passing_test_now(user_id) is False:
            mess = await bot_func.set_question(bot, user_id, question_db, abc_converter, keylib, 0, int(test))




@dp.callback_query_handler(Text(startswith='question_'))
async def handle_test_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    user = question_db.get_user(user_id)

    answer = callback_query.data.split('_')[1]

    result = abc_converter.convert(int(answer))

    test_id = int(user["test_id"])
    # print(f"Test_id: {test_id}")
    test = question_db.get_test_by_id(test_id)
    # print(callback_query.from_user.id)
    que_answers = user['question_answers']
    que_answers.append(result)
    question_db.update_user_value(user_id, "question_answers", que_answers)
    question_progres = user['question_answered'] + 1
    question_db.update_user_value(user_id, "question_answered", question_progres)

    print(f"{len(test['questions'])}: {user['question_answered'] + 1}")
    if len(test['questions']) > user['question_answered'] + 1:
        await bot_func.set_question(bot, user_id, question_db, abc_converter, keylib, user["question_answered"] + 1,
                                    int(user["test_id"]))
    else:
        question_db.update_user_value(user_id, "is_done", True)

        await bot_func.start(question_db, bot, user_id, keylib, "Дякуємо за проходження тесту")

    # print(f"test: {test}")
