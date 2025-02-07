from aiogram import types, Dispatcher


async def branches_handler(message: types.Message):
    await message.answer('Наши филиалы в Бишкеке: \nИбраимова 111 \nКиевская 24 \nФучика 54'
'\nТокомбаева 12б \nКурманджан Датка 3 \nБайтик Баатыра 132 \nBishkekPark 56'
'\nТурусбекова 34 \nЦУМ 5 этаж \nAsiaMall 3 этаж \nDordoi Plaza 3 этаж \nТехнопарк 2 этаж \nАхунбаева 42')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(branches_handler, commands=['branches'])
