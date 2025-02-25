import logging
from aiogram import executor
from bot_config import dp, database, ADMINS, bot
from handlers import start, myinfo, names, branches,delivery,review_dialog, store_fsm, send_products
from db.main_db import create_tables


async def on_startup(_):
    for admin in ADMINS:
        await bot.send_message(chat_id=admin ,text='Бот включен!')
    await create_tables()


async def on_shutdown(_):
    for admin in ADMINS:
        await bot.send_message(chat_id=admin ,text='Бот выключен!')


start.register_handlers(dp)
review_dialog.register_handlers(dp)
myinfo.register_handlers(dp)
names.register_handlers(dp)
branches.register_handlers(dp)
delivery.register_handlers(dp)
database.create_tables()
store_fsm.register_handlers(dp)

send_products.register_handlers(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)