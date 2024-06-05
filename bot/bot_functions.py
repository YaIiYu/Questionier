import re
from aiogram.types import ReplyKeyboardRemove

def extract_number_from_button(text):
    match = re.search(r'\d+', text)
    if match:
        return match.group()
    return None

async def start(question_db, bot, user_id, keylib, message_text):
    test_arr = question_db.get_all_tests()
    await bot.send_message(user_id, message_text,
                           reply_markup=await keylib.set_start_reply_keyboard(test_arr))
async def set_question(bot, user_id, question_db, abc_converter, keylib, question_num, test):
    test_data = question_db.get_test_by_id(test)
    print(f"test_data: {test_data}")

    question = question_db.get_question(test_data['questions'][question_num])
    question_db.user_reg(user_id, test)
    question_text = question["text"]
    answers = question["answers"]
    answers_variants = f""
    for i in range(len(answers)):
        answers_variants = answers_variants + f"{abc_converter.convert(i + 1)}. {answers[i]} \n"

    keyboard = await keylib.set_inline_keyboard(len(answers), answers)
    mess = await bot.send_message(user_id, f"Питання {question_num + 1}: \n", reply_markup=ReplyKeyboardRemove())

    mess = await bot.send_message(user_id,
                                            f"{question_text}:\n"
                                            f"{answers_variants}", reply_markup=keyboard)

