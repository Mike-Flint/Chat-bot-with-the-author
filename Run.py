import asyncio
import logging
from aiogram import Bot, Dispatcher
import key

bot = Bot(token=key.key1)
dp = Dispatcher()

from handlers.user_handlers import user_handlers_router


dp.include_router(user_handlers_router)



async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("EXIT")


        