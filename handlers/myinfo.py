from aiogram import Dispatcher, types


async def myinfo_handler(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    await message.answer(f'Ваше имя: {first_name}, \nВаш ник: @{username}, \nВаш id: {user_id}.')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(myinfo_handler, commands=['myinfo'])
