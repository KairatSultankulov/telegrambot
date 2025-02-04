import asyncio
from aiogram import Bot, Dispatcher


token = '8121863686:AAGqVoTNE69D8Xh2DCQ1HY5EEZe88HVeVDw'
bot = Bot(token=token)
dp = Dispatcher(bot)


async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())


