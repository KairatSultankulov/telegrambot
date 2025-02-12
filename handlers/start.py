from aiogram import Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


async def start_handler(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Контакты', callback_data='contacts'),
            InlineKeyboardButton(text='Наши вакансии', callback_data='vacancies'),
        ],
        [
            InlineKeyboardButton(text='Наш сайт', url='https://navat.kg/'),
            InlineKeyboardButton(text='Инстаграм', url='https://www.instagram.com/navat_kg/?hl=ru')
        ],
        [
            InlineKeyboardButton(text='Меню', callback_data='menu'),
            InlineKeyboardButton(text='Филиалы', callback_data='branches')
        ],
        [
            InlineKeyboardButton(text='Доставка', callback_data='delivery'),
            InlineKeyboardButton(text='Оставить отзыв', callback_data='feedback'),
        ]
    ])
    await message.answer(f'Здравствуйте, {message.from_user.first_name}! Вас приветсвует бот Navat.kg', reply_markup=kb)



async def contacts_handler(callback: CallbackQuery):
    await callback.message.answer('+996 709 12 55 27 \n+996 505 44 55 66 \n+996 777 53 54 55')


async def vacancies_handler(callback: CallbackQuery):
    await callback.message.answer(
        'У нас есть открытые вакансии! Напишите на email: navatkg@gmail.com для подробной информации.')


async def menu_handler(callback: CallbackQuery):
    await callback.message.answer('Наше меню:\n1. Бешбармак\n2. Манты\n3. Лагман\n4. Боорсоки')

async def branches_handler(callback: CallbackQuery):
    await callback.message.answer('Наши филиалы в Бишкеке: \nИбраимова 111 \nКиевская 24 \nФучика 54'
'\nТокомбаева 12б \nКурманджан Датка 3 \nБайтик Баатыра 132 \nBishkekPark 56'
'\nТурусбекова 34 \nЦУМ 5 этаж \nAsiaMall 3 этаж \nDordoi Plaza 3 этаж \nТехнопарк 2 этаж \nАхунбаева 42')

async def delivery_handler(callback: CallbackQuery):
    await callback.message.answer('Бесплатная доставка еды работает круглосуточно 24/7. Доставим в любую точку Бишкека.')


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_callback_query_handler(contacts_handler, lambda c: c.data == 'contacts')
    dp.register_callback_query_handler(vacancies_handler, lambda c: c.data == 'vacancies')
    dp.register_callback_query_handler(menu_handler, lambda c: c.data == 'menu')
    dp.register_callback_query_handler(delivery_handler, lambda c: c.data == 'delivery')
    dp.register_callback_query_handler(branches_handler, lambda c: c.data == 'branches')