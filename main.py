import asyncio
import logging

from bot_config import dp
from handlers import (
    start,
    myinfo,
    random,
    branches,
    delivery
)


async def main():
    start.register_handlers(dp)
    myinfo.register_handlers(dp)
    random.register_handlers(dp)
    branches.register_handlers(dp)
    delivery.register_handlers(dp)
    await dp.start_polling()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
