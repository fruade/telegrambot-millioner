from main import dp, bot, anti_flood
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from tools.other_func import *
from keyboards.keyboard import *
from states.state import Game_state
from .commands import menu
from data.data import data_questions
from aiogram.types import ReplyKeyboardRemove
#shuffle(data_questions)


@dp.message_handler(text='Играть', state=None)
async def game(message: Message, state: FSMContext):
    question = get_question(data_questions, step=0)
    await message.answer(text="Начнем", reply_markup=keyboard_help)
    await message.answer(text=f"Вопрос на 1000 очков:\n{question[0]}", reply_markup=question[1])
    await Game_state.Q1.set()
    await state.update_data(d=question)


@dp.callback_query_handler(text=true_answer(data_questions, 0), state=Game_state.Q1)
async def answer1(message: CallbackQuery, state: FSMContext, points=1000):
    question = get_question(data_questions, step=1)
    await message.message.answer(text=f'Правильный ответ! Вы набрали {points} очков.')
    await message.message.answer(text=f"Вопрос на {points * 2} очков:\n{question[0]}", reply_markup=question[1])
    await state.update_data(d=question)
    await Game_state.next()


@dp.callback_query_handler(text=true_answer(data_questions, 1), state=Game_state.Q2)
async def answer1(message: CallbackQuery, state: FSMContext, points=2000):
    question = get_question(data_questions, step=2)
    await message.message.answer(text=f'Правильный ответ! Вы набрали {points} очков.')
    await message.message.answer(text=f"Вопрос на {points * 2} очков:\n{question[0]}", reply_markup=question[1])
    await state.update_data(d=question)
    await Game_state.next()


@dp.callback_query_handler(text=true_answer(data_questions, 2), state=Game_state.Q3)
async def answer1(message: CallbackQuery, state: FSMContext, points=4000):
    question = get_question(data_questions, step=3)
    await message.message.answer(text=f'Правильный ответ! Вы набрали {points} очков.')
    await message.message.answer(text=f"Вопрос на {points * 2} очков:\n{question[0]}", reply_markup=question[1])
    await state.update_data(d=question)
    await Game_state.next()


@dp.callback_query_handler(text=true_answer(data_questions, 3), state=Game_state.Q4)
async def answer1(message: CallbackQuery, state: FSMContext, points=8000):
    question = get_question(data_questions, step=4)
    await message.message.answer(text=f'Правильный ответ! Вы набрали {points} очков.')
    await message.message.answer(text=f"Вопрос на {points * 2} очков:\n{question[0]}", reply_markup=question[1])
    await state.update_data(d=question)
    await Game_state.next()


@dp.callback_query_handler(text=true_answer(data_questions, 4), state=Game_state.Q5)
async def answer1(message: CallbackQuery, state: FSMContext, points=16000):
    question = get_question(data_questions, step=5)
    await message.message.answer(text=f'Правильный ответ! Вы набрали {points} очков.')
    await message.message.answer(text=f"Вопрос на {points * 2} очков:\n{question[0]}", reply_markup=question[1])
    await state.update_data(d=question)
    await Game_state.next()


@dp.callback_query_handler(text=true_answer(data_questions, 5), state=Game_state.Q6)
async def answer1(message: CallbackQuery, state: FSMContext, points=32000):
    question = get_question(data_questions, step=6)
    await message.message.answer(text=f'Правильный ответ! Вы набрали {points} очков.')
    await message.message.answer(text=f"Вопрос на {points * 2} очков:\n{question[0]}", reply_markup=question[1])
    await state.update_data(d=question)
    await Game_state.next()


@dp.callback_query_handler(text=true_answer(data_questions, 6), state=Game_state.Q7)
async def answer1(message: CallbackQuery, state: FSMContext, points=64000):
    question = get_question(data_questions, step=7)
    await message.message.answer(text=f'Правильный ответ! Вы набрали {points} очков.')
    await message.message.answer(text=f"Вопрос на {points * 2} очков:\n{question[0]}", reply_markup=question[1])
    await state.update_data(d=question)
    await Game_state.next()


@dp.callback_query_handler(text=true_answer(data_questions, 7), state=Game_state.Q8)
async def answer1(message: CallbackQuery, state: FSMContext, points=125000):
    question = get_question(data_questions, step=8)
    await message.message.answer(text=f'Правильный ответ! Вы набрали {points} очков.')
    await message.message.answer(text=f"Вопрос на {points * 2} очков:\n{question[0]}", reply_markup=question[1])
    await state.update_data(d=question)
    await Game_state.next()


@dp.callback_query_handler(text=true_answer(data_questions, 8), state=Game_state.Q9)
async def answer1(message: CallbackQuery, state: FSMContext, points=250000):
    question = get_question(data_questions, step=9)
    await message.message.answer(text=f'Правильный ответ! Вы набрали {points} очков.')
    await message.message.answer(text=f"Вопрос на {points * 2} очков:\n{question[0]}", reply_markup=question[1])
    await state.update_data(d=question)
    await Game_state.next()


@dp.callback_query_handler(text=true_answer(data_questions, 9), state=Game_state.Q10)
async def answer1(message: CallbackQuery, state: FSMContext, points=500000):
    question = get_question(data_questions, step=10)
    await message.message.answer(text=f'Правильный ответ! Вы набрали {points} очков.')
    await message.message.answer(text=f"Вопрос на {points * 2} очков:\n{question[0]}", reply_markup=question[1])
    await state.update_data(d=question)
    await Game_state.next()


@dp.callback_query_handler(text=true_answer(data_questions, 10), state=Game_state.Q11)
async def answer1(message: CallbackQuery, state: FSMContext, points=1000000):
    await message.message.answer(text=f'Вы набрали {points} очков и прошли игру!!!', reply_markup=ReplyKeyboardRemove())
    await message.message.answer(text=f'Поздравляю с победой! ', reply_markup=keyboard_menu)
    return await state.finish()


@dp.message_handler(text='Выйти', state='*')
async def return_menu(message: Message, state: FSMContext):
    await state.finish()
    return await menu(message)


@dp.callback_query_handler(state='*')
async def return_menu(message: CallbackQuery, state: FSMContext):
    question = message.message.text.split('\n')[-1]
    await state.finish()
    await message.message.answer(text=f'Вы не отгадали, правильный ответ "{answer(question)}"', reply_markup=keyboard_menu)
    return await message.message.answer(text=f'Вы набрали {points_result(message.message.text)} очков')



