from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text

from config import BOT_TOKEN, TELEGRAM_ID_UMKA

from string import ascii_letters
from strings import HELP_COMMANDS, DESCRIPTION

from inlineKeyboard import ikb_currency
from keyboard import kb

import random
from random import randrange

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

count = 0


async def start(dp: Dispatcher):
    print('Bot Activated!')
    await dp.bot.send_message(TELEGRAM_ID_UMKA, text='Started!')
    await dp.bot.send_sticker(TELEGRAM_ID_UMKA,
                              sticker='CAACAgIAAxkBAAEF3N9jJZmbPGrP0uK9wupfh9XJ-dHCNgACDhQAAqVx2UvprdG3Cj-5YykE')


@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await message.answer(text='<b>Добро пожаловать, @' + message.from_user.username + '.\nВведите /help для получения '
                                                                                      'списка доступных команд.</b>',
                         parse_mode='HTML', reply_markup=kb)
    await message.delete()


@dp.message_handler(Text(equals='❤️'))
async def reply_black_heart(message: types.Message):
    await bot.send_sticker(message.chat.id,
                           sticker='CAACAgIAAxkBAAEF6YZjLbA_WW9KQKePWjGPi-wfhSdgSgACHRYAAklQ0EvKQhoRA3Mx7ykE')


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMANDS, parse_mode='HTML')
    await message.delete()


@dp.message_handler(Text(equals='Random letter'))
async def random_letter(message: types.Message):
    letter = random.choice(ascii_letters)
    await message.answer(letter)


@dp.message_handler(commands=['description'])
async def get_description(message: types.Message):
    await message.answer(DESCRIPTION)


# @dp.message_handler()
# async def check_for_confirmation_emoji(message: types.Message):
#     if '✅' in message.text:
#         await message.reply(text=str(message.text.count('✅')))
#     else:
#         await message.reply('0')

@dp.message_handler(content_types=['sticker'])
async def get_sticker_id(message: types.Message):
    await message.reply(text='ID этого стикера: ' + message.sticker.file_id)


@dp.message_handler(Text(equals='Random location'))
async def send_random_place(message: types.Message):
    await bot.send_location(message.chat.id, latitude=randrange(1, 100), longitude=randrange(1, 100))


@dp.message_handler(commands=['count'])
async def count_calls(message: types.Message):
    global count
    await message.answer(text=f'Count: {count}')
    count += 1
    await message.delete()


@dp.message_handler()
async def no_clue_message(message: types.Message):
    await message.reply(text='Не понимаю 🤔')


# @dp.message_handler()
# async def upRegister(message: types.Message):
#     id = message.chat.id
#     if message.text.count(' ') >= 1:
#         await message.answer(text=message.text.upper())
#     else:
#         await bot.send_message(id, text='Required two or more words')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=start)
