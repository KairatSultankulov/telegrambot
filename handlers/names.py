import random
from aiogram import types, Dispatcher

names = ('James', 'Morgan', 'Rachel', 'Mike', 'Benedict', 'Gabriel')


async def random_handler(message: types.Message):
    random_name = random.choice(names)
    await message.answer(f'Random name: {random_name}')

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(random_handler, commands=['random'])
