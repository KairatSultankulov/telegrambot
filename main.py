import asyncio
import random
from aiogram import Bot, Dispatcher
from dotenv import dotenv_values

token = dotenv_values('.env')['BOT_TOKEN']
bot = Bot(token=token)
dp = Dispatcher(bot)

names = ('James', 'Morgan', 'Rachel', 'Mike', 'Benedict', 'Gabriel')

@dp.message_handler(commands=['start'])
async def start_handler(message):
    await message.answer(f'Hello, {message.from_user.first_name}!')

@dp.message_handler(commands=['myinfo'])
async def myinfo_handler(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    await message.answer(f'Ваше имя: {first_name}, \nВаш ник: @{username}, \nВаш id: {user_id}.')

@dp.message_handler(commands=['random'])
async def random_handler(message):
    random_name = random.choice(names)
    await message.answer(f'Random name: {random_name}')

async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())





