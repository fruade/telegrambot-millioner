from main import dp, bot
from aiogram.types import Message
from keyboards.keyboard import keyboard_menu


@dp.message_handler(commands=['start', 'help'])
async def start_command(message: Message):
    text = "Сыграйте в игру кто хочет стать миллионером!\n/menu - Начинаем"
    #await message.delete()
    await bot.send_message(message.from_user.id, text)


@dp.message_handler(commands=['menu'])
async def menu(message: Message):
    text = 'Меню'
    await bot.send_message(message.from_user.id, text, reply_markup=keyboard_menu)












