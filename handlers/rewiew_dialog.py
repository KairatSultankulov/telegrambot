from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters.state import State, StatesGroup



class RestourantRewiew(StatesGroup):
    name = State()
    phone_number = State()
    rate = State()
    extra_comments = State()


async def start_dialog(callback: CallbackQuery):
    await RestourantRewiew.name.set()
    await callback.message.answer('Как Вас зовут?')


async def process_name(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await RestourantRewiew.next()
    await message.answer('Введите Ваш номер телефона')


async def process_phone_number(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone_number'] = message.text
    await RestourantRewiew.next()
    await message.answer('Поставьте оценку от 1 до 5')


async def process_rate(message: Message, state: FSMContext):
    if not message.text.isdigit() or not (1 <= int(message.text) <= 5):
        await message.answer('Введите число от 1 до 5')
        return

    async with state.proxy() as data:
        data['rate'] = int(message.text)
    await RestourantRewiew.next()
    await message.answer('Можете оставить дополнительные коментарии')


async def process_extra_comments(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['extra_comments'] = message.text
    await message.answer('Спасибо за отзыв!')
    await state.finish()

def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(start_dialog, lambda c: c.data == 'feedback')
    dp.register_message_handler(process_name, state=RestourantRewiew.name)
    dp.register_message_handler(process_phone_number, state=RestourantRewiew.phone_number)
    dp.register_message_handler(process_rate, state=RestourantRewiew.rate)
    dp.register_message_handler(process_extra_comments, state=RestourantRewiew.extra_comments)