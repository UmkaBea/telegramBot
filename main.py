from aiogram import Bot, Dispatcher, types, executor
from strings import HELP_COMMANDS, DESCRIPTION
from config import BOT_TOKEN
import random
from string import ascii_letters

bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot)

# count = 0


@dp.message_handler(commands=['start'])
async def help_command(message: types.Message):
    await message.answer(text='Добро пожаловать, @' + message.from_user.username)
    await message.delete()


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMANDS)


@dp.message_handler(commands=['random'])
async def random_letter(message: types.Message):
    letter = random.choice(ascii_letters)
    await message.answer(letter)


@dp.message_handler(commands=['description'])
async def get_description(message: types.Message):
    await message.answer(DESCRIPTION)


@dp.message_handler()
async def checkForNull(message: types.Message):
    if '0' in message.text:
        await message.answer('Yes')
    else:
        await message.answer('No')

# @dp.message_handler(commands=['count'])
# async def count_calls(message: types.Message):
#     global count
#     await message.answer(text=f'Count: {count}')
#     count += 1

# @dp.message_handler()
# async def upRegister(message: types.Message):
#     id = message.chat.id
#     if message.text.count(' ') >= 1:
#         await message.answer(text=message.text.upper())
#     else:
#         await bot.send_message(id, text='Required two or more words')


if __name__ == '__main__':
    executor.start_polling(dp)
