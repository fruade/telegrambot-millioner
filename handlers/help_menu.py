from main import dp, bot
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from tools.other_func import *
from keyboards.keyboard import *


@dp.message_handler(text='Помощь бота', state='*')
async def help_bot(message: Message, state: FSMContext):
    await message.delete()
    await state.update_data(kb2='Помощь бота')
    data = await state.get_data()
    button = []
    answer = data['d'][-1]
    for i in data['d'][1]['inline_keyboard']:
        for j in i:
            button.append(j['text'])
    for i in range(4):
        if button[i] != answer:
            button[i] = "⁠"

    reply_markup = kb_without_help_bot
    if data.get('kb1') == '50/50':
        reply_markup = exit
    await message.answer(text='Помощь бота', reply_markup=reply_markup)
    await message.answer(text=data['d'][0], reply_markup=get_question_help(button))


@dp.message_handler(text='50/50', state='*')
async def help_bot(message: Message, state: FSMContext):
    await message.delete()
    await state.update_data(kb1='50/50')
    data = await state.get_data()
    button = []
    answer = data['d'][-1]
    for i in data['d'][1]['inline_keyboard']:
        for j in i:
            button.append(j['text'])
    stop = 0
    for i in range(4):
        if button[i] != answer and stop != 2:
            button[i] = "⁠"
            stop += 1

    reply_markup = kb_without_50
    if data.get('kb2') == 'Помощь бота':
        reply_markup = exit
    await message.answer(text='50/50', reply_markup=reply_markup)
    await message.answer(text=data['d'][0], reply_markup=get_question_help(button))

@dp.message_handler(text='50/50', state='*')
async def help_bot(message: Message, state: FSMContext):
    await message.delete()
    await state.update_data(kb1='50/50')
    data = await state.get_data()
    button = []
    answer = data['d'][-1]
    for i in data['d'][1]['inline_keyboard']:
        for j in i:
            button.append(j['text'])
    stop = 0
    for i in range(4):
        if button[i] != answer and stop != 2:
            button[i] = "⁠"
            stop += 1

    reply_markup = kb_without_50
    if data.get('kb2') == 'Помощь бота':
        reply_markup = exit
    await message.answer(text='50/50', reply_markup=reply_markup)
    await message.answer(text=data['d'][0], reply_markup=get_question_help(button))