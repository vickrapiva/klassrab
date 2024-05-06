import asyncio

from aiogram import Bot, Dispatcher
from handlers import include_routers


bot = Bot(token="7086038652:AAEKbcrL_Mod-9KNUf2jZGNBE_ZYj7ti0jg")
dp = Dispatcher()

async def main():
    include_routers(dp)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
