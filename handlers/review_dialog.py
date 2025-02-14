from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters.state import State, StatesGroup
from bot_config import database


class RestaurantReview(StatesGroup):
    name = State()
    phone_number = State()
    rate = State()
    extra_comments = State()


async def start_dialog(callback: CallbackQuery):
    await RestaurantReview.name.set()
    await callback.message.answer('Как Вас зовут?')


async def stop_dialog(message: Message, state: FSMContext):
    await state.finish()
    await message.answer('Спасибо за потраченное время!')


async def process_name(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await RestaurantReview.next()
    await message.answer('Введите Ваш номер телефона')


async def process_phone_number(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text
    await RestaurantReview.next()
    await message.answer('Поставьте оценку от 1 до 5')


async def process_rate(message: Message, state: FSMContext):
    rate = message.text
    if not rate.isdigit():
        await message.answer('Введите число')
        return
    rate = int(rate)
    if rate < 1 or rate > 5:
        await message.answer('Неподходящая оценка!')
        return
    async with state.proxy() as data:
        data['rate'] = int(message.text)
    await RestaurantReview.next()
    await message.answer('Можете оставить дополнительные коментарии')


async def process_extra_comments(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['extra_comments'] = message.text
    data = await state.get_data()
    database.add_review(data)
    await message.answer('Спасибо за отзыв!')
    await state.finish()

def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_dialog, lambda c: c.data == 'feedback')
    dp.register_message_handler(stop_dialog, Text(equals=('stop', 'стоп'), ignore_case=True), state='*')
    dp.register_message_handler(process_name, state=RestaurantReview.name)
    dp.register_message_handler(process_phone_number, state=RestaurantReview.phone_number)
    dp.register_message_handler(process_rate, state=RestaurantReview.rate)
    dp.register_message_handler(process_extra_comments, state=RestaurantReview.extra_comments)
