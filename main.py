import asyncio
import logging

from bot_config import dp, database
from handlers import (
    start,
    myinfo,
    names,
    branches,
    delivery,
    review_dialog
)


async def main():
    start.register_handlers(dp)
    review_dialog.register_handlers(dp)
    myinfo.register_handlers(dp)
    names.register_handlers(dp)
    branches.register_handlers(dp)
    delivery.register_handlers(dp)
    database.create_tables()
    await dp.start_polling()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
