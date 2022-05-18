from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
from data.data import data_questions
from tools.other_func import *


menu_button = ['Играть', 'Выйти']
keyboard_menu = ReplyKeyboardMarkup(resize_keyboard=True).add(*menu_button)
keyboard_return = ReplyKeyboardMarkup(resize_keyboard=True).add('Выйти')
exit = ReplyKeyboardMarkup(resize_keyboard=True).add('Выйти')


keyboard_help = ReplyKeyboardMarkup(resize_keyboard=True).add(*['50/50', 'Помощь бота']).row('Выйти')
kb_without_50 = ReplyKeyboardMarkup(resize_keyboard=True).add('Помощь бота').row('Выйти')
kb_without_help_bot = ReplyKeyboardMarkup(resize_keyboard=True).add('50/50').row('Выйти')


def get_question(data_questions, step=0):
    kb = InlineKeyboardMarkup(row_width=2)
    data = data_questions[step]
    keyboard_answers_button = [InlineKeyboardButton(text=i, callback_data=i) for i in data['answers']]
    return data['questions'], kb.add(*keyboard_answers_button), data['true_answer']

