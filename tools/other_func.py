from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
import re
from data.data import data_questions


def true_answer(data: list, step=0):
    return data[step]['true_answer']


def points_result(text):
    points = int(re.findall(r"\d+", text)[0])
    if points == 1000:
        return 0
    return points // 2


def answer(question):
    for i in data_questions:
        if i['questions'] == question:
            return i['true_answer']


def get_question_help(data):
    kb = InlineKeyboardMarkup(row_width=2)
    keyboard_answers_button = [InlineKeyboardButton(text=i, callback_data=i) for i in data]
    kb.add(*keyboard_answers_button)
    return kb