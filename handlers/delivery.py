from aiogram import types, Dispatcher


async def delivery_handler(message: types.Message):
    await message.answer('Бесплатная доставка еды работает круглосуточно 24/7. Доставим в любую точку Бишкека')

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(delivery_handler, commands=['delivery'])