import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import user_handlers, other_handlers

async def main() -> None:
    config: Config = load_config()

    bot = Bot(config.tg_bot.token)
    dp = Dispatcher()

    dp.include_router(user_handlers.rout)
    dp.include_router(other_handlers.rout)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main()) 