from config import token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


#  Предварительный вариант
#  Собираемся использовать Django Rest Framework для того, чтобы создать модель объекта. А также путем пост-запроса собирать данные на каждого юзверя.
#  


bot = Bot(token)
dp = Dispatcher(bot)


def add_value(n):
    interview_data_object[n] = message.text
    return


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Добрый день. Для начала опроса нажмите "Начать опрос".', reply_markup=main_btn())


@dp.message_handler(lambda message: 'Начать опрос' in message.text)
async def get_interview(message: types.Message):
    interview_data_object = {
        'name': '',
        'phone': '',
        'description': ''
    }
    await message.reply('Ответьте на следующие вопросы. Ваше имя?')


@dp.message_handler()
async def get_interview2(message: types.Message):
    await message.reply('Введите ваш номер телефона.')


def main_btn():
    opros = types.KeyboardButton('Начать опрос')
    main_btn = types.ReplyKeyboardMarkup(resize_keyboard=True)
    main_btn.insert(opros)
    return main_btn


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)